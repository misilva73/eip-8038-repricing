// Cross-run Trends page: a latest-vs-previous delta table + Δ% diverging-bar
// chart, and one line chart per estimated gas param across every run. All data
// is embedded as JSON in #trends-data by build_site.collect_trends(); Chart.js
// (vendored) draws the charts. Lower = faster, so a negative delta (bar pointing
// left, green) is an improvement and a positive one (right, red) a regression.
(function () {
  "use strict";

  var el = document.getElementById("trends-data");
  if (!el || typeof Chart === "undefined") return;
  var DATA = JSON.parse(el.textContent);

  var RUNS = DATA.runs;                  // chronological (oldest → newest)
  var N = RUNS.length;
  var LABELS = RUNS.map(function (r) { return r.label; });

  var PALETTE = ["#2f6fed", "#e8590c", "#2f9e44", "#ae3ec9", "#1098ad", "#f08c00", "#e03131", "#5c7cfa"];
  var COLOR = {};
  DATA.clients.forEach(function (c, i) { COLOR[c] = PALETTE[i % PALETTE.length]; });

  // ---- shared UI state ----
  var state = {
    param: "all",
    metric: "gas",                       // "gas" | "runtime"
    clients: new Set(DATA.clients),      // active (checked) clients
  };

  // ---- Chart.js global theming (so it reads on a dark background too) ----
  var dark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  Chart.defaults.color = dark ? "#9aa4b2" : "#5b6675";
  Chart.defaults.borderColor = dark ? "#2a313d" : "#e4e7ec";
  Chart.defaults.font.family = getComputedStyle(document.body).fontFamily;

  var GREEN = dark ? "#69db7c" : "#2b8a3e";   // faster / lower (improvement)
  var RED = dark ? "#ff8787" : "#c92a2a";     // slower / higher (regression)
  var GRID = dark ? "#2a313d" : "#e4e7ec";

  // --------------------------------------------------------------------- //
  // Helpers
  // --------------------------------------------------------------------- //
  function seriesStore() { return state.metric === "runtime" ? DATA.runtime : DATA.gas; }

  function seriesFor(param, client) {
    var store = seriesStore();
    return (store[param] && store[param][client]) || null;
  }

  function fmt(v) {
    if (v === null || v === undefined) return "—";
    if (state.metric === "runtime") return Number(v).toPrecision(4).replace(/\.?0+$/, "");
    return Number(v).toLocaleString();
  }

  // Clients that actually have a per-client series for this param.
  function clientsWithSeries(param) {
    return DATA.clients.filter(function (c) { return seriesFor(param, c); });
  }

  // Axis tick label for a percent value: round off float noise, drop trailing
  // zeros (3 decimals covers tiny-range axes), and normalize "-0" → "0".
  function pctTick(v) {
    var s = (Math.round(Number(v) * 1000) / 1000).toFixed(3).replace(/\.?0+$/, "");
    return (s === "-0" ? "0" : s) + "%";
  }

  // --------------------------------------------------------------------- //
  // Section 1 — latest-vs-previous rows (shared by the table and the Δ% chart)
  // --------------------------------------------------------------------- //
  function collectDeltaRows() {
    var prev = N - 2, last = N - 1;
    var rows = [];
    // Estimated params only — derived params have no per-client series.
    DATA.estimated_params.forEach(function (param) {
      if (state.param !== "all" && state.param !== param) return;
      // The binding client is the worst case in the latest run — it sets the proposal.
      var bLast = DATA.binding[param] && DATA.binding[param][last];
      var bindingClient = bLast ? bLast.client : null;

      clientsWithSeries(param).forEach(function (client) {
        if (!state.clients.has(client)) return;

        var s = seriesFor(param, client);
        var pv = s[prev], lv = s[last];
        if (pv == null && lv == null) return;

        var cs = DATA.combo[param] && DATA.combo[param][client];
        var ps = DATA.poor[param] && DATA.poor[param][client];
        var delta = (pv != null && lv != null) ? lv - pv : null;
        var pct = (delta != null && pv) ? (delta / pv) * 100 : null;
        rows.push({
          param: param, client: client, isBinding: client === bindingClient,
          pv: pv, lv: lv, delta: delta, pct: pct,
          comboPrev: cs && cs[prev], comboLast: cs && cs[last],
          poorPrev: !!(ps && ps[prev]), poorLast: !!(ps && ps[last]),
        });
      });
    });
    return rows;
  }

  // --------------------------------------------------------------------- //
  // Section 1 — delta table
  // --------------------------------------------------------------------- //
  var tableBody = document.querySelector("#delta-table tbody");
  var deltaEmpty = document.getElementById("delta-empty");
  var caption = document.getElementById("compare-caption");
  var poorNote = document.getElementById("poor-note");

  function buildTable(rows) {
    if (!tableBody) return;                       // < 2 runs: table not rendered
    caption.textContent = "Comparing " + LABELS[N - 2] + " → " + LABELS[N - 1] +
      " · metric: " + (state.metric === "runtime" ? "runtime (ms)" : "proposed gas") +
      " · highlighted = binding (worst-case) client";

    tableBody.textContent = "";
    var anyPoor = false;
    rows.forEach(function (r) {
      tableBody.appendChild(deltaRow(r));
      anyPoor = anyPoor || r.poorPrev || r.poorLast;
    });
    deltaEmpty.hidden = rows.length > 0;
    if (poorNote) poorNote.hidden = !anyPoor;     // only show the legend when a * is present
  }

  // A "*" on a value whose underlying fit evm-gasfit flagged as poor (its
  // New-gas R²/p-value thresholds). poor_fit is per run, so prev/latest differ.
  function poorMark(isPoor) {
    return isPoor
      ? '<span class="poor-flag" title="Low-confidence fit — flagged as a poor fit (R²/p-value) by the New-gas analysis">*</span>'
      : "";
  }

  function deltaRow(r) {
    var tr = document.createElement("tr");
    if (r.isBinding) tr.className = "binding-row";
    var cls = r.delta == null || r.delta === 0 ? "" : (r.delta < 0 ? "delta-down" : "delta-up");

    var clientCell = "<td>" + r.client;
    if (r.isBinding) {
      clientCell += ' <span class="binding-tag" title="Worst case for this parameter — sets the proposed gas">binding</span>';
    }
    if (r.comboLast) {
      tr.title = "fit: " + r.comboLast;
      if (r.comboPrev && r.comboPrev !== r.comboLast) {
        clientCell += ' <span class="combo-badge" tabindex="0" data-tip="was: ' +
          escapeAttr(r.comboPrev) + '\nnow: ' + escapeAttr(r.comboLast) +
          '">⚠ combo changed</span>';
      }
    }
    clientCell += "</td>";

    tr.innerHTML =
      "<td>" + r.param + "</td>" + clientCell +
      "<td>" + fmt(r.pv) + poorMark(r.poorPrev) + "</td>" +
      "<td>" + fmt(r.lv) + poorMark(r.poorLast) + "</td>" +
      '<td class="' + cls + '">' + (r.delta == null ? "—" : signed(r.delta)) + "</td>" +
      '<td class="' + cls + '">' + (r.pct == null ? "—" : signed(r.pct.toFixed(1)) + "%") + "</td>";
    return tr;
  }

  function signed(v) {
    var n = Number(v);
    if (state.metric === "runtime" && Math.abs(n) < 1000) {
      return (n > 0 ? "+" : "") + (typeof v === "string" ? v : n.toPrecision(4));
    }
    return (n > 0 ? "+" : "") + Math.round(n).toLocaleString();
  }

  function escapeAttr(s) { return String(s).replace(/"/g, "&quot;"); }

  // --------------------------------------------------------------------- //
  // Section 1 — diverging Δ% bars (one bar per row; left = faster, right = slower)
  // --------------------------------------------------------------------- //
  // A two-run line chart is just two dots, so we show the *change* instead. Δ%
  // normalizes across params (gas spans 100→200k), so one axis works whether a
  // single param or "All" is selected — and the bars mirror the table rows.
  var barCanvas = document.getElementById("delta-bar");
  var barHint = document.getElementById("delta-bar-hint");
  var barWrap = document.getElementById("delta-bar-wrap");
  var barChart = null;

  function buildBar(rows) {
    if (!barCanvas) return;                       // < 2 runs
    if (barChart) { barChart.destroy(); barChart = null; }

    // Only rows present in both runs have a % change to draw.
    var drawable = rows.filter(function (r) { return r.pct != null; })
      .sort(function (a, b) { return a.pct - b.pct; });   // biggest improvement first
    var skipped = rows.length - drawable.length;

    barHint.hidden = skipped === 0;
    if (skipped) {
      barHint.textContent = skipped + " row" + (skipped > 1 ? "s" : "") +
        " not shown — the client is missing from one of the two runs, so there's no % change.";
    }
    barCanvas.hidden = drawable.length === 0;
    if (!drawable.length) return;

    // Size the canvas to the row count so bars stay legible as filters change.
    barWrap.style.height = Math.max(150, drawable.length * 30 + 56) + "px";

    barChart = new Chart(barCanvas, {
      type: "bar",
      data: {
        labels: drawable.map(function (r) {
          return state.param === "all" ? r.param + " · " + r.client : r.client;
        }),
        datasets: [{
          data: drawable.map(function (r) { return r.pct; }),
          backgroundColor: drawable.map(function (r) { return r.pct < 0 ? GREEN : RED; }),
          // Outline the binding (worst-case) bar to match the highlighted table row.
          borderColor: drawable.map(function (r) { return r.isBinding ? (dark ? "#e6e9ef" : "#1c2430") : "transparent"; }),
          borderWidth: drawable.map(function (r) { return r.isBinding ? 1.5 : 0; }),
          borderSkipped: false,
        }],
      },
      options: {
        indexAxis: "y",
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            title: { display: true, text: "Δ% vs previous run   (◄ faster · slower ►)" },
            // Round away float noise (e.g. -1.400000000000002 → -1.4) and drop
            // trailing zeros, so small-range axes stay readable.
            ticks: { callback: pctTick },
            grid: { color: GRID },
          },
          y: { ticks: { autoSkip: false }, grid: { display: false } },
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              title: function (items) {
                var r = drawable[items[0].dataIndex];
                return r.param + " · " + r.client;
              },
              label: function (ctx) {
                var r = drawable[ctx.dataIndex];
                return fmt(r.pv) + " → " + fmt(r.lv) +
                  "  (" + (r.pct > 0 ? "+" : "") + r.pct.toFixed(1) + "%)";
              },
              afterLabel: function (ctx) {
                var r = drawable[ctx.dataIndex];
                if (r.comboPrev && r.comboLast && r.comboPrev !== r.comboLast) {
                  return "combo changed: " + r.comboPrev + " → " + r.comboLast;
                }
                return r.comboLast ? "fit: " + r.comboLast : undefined;
              },
            },
          },
        },
      },
    });
  }

  // Recompute the shared rows and redraw both Section 1 views.
  function renderSection1() {
    if (N < 2) return;                            // section not rendered
    var rows = collectDeltaRows();
    buildTable(rows);
    buildBar(rows);
  }

  // --------------------------------------------------------------------- //
  // Section 2 — one line chart per param, across all runs
  // --------------------------------------------------------------------- //
  var chartsHost = document.getElementById("trend-charts");
  var chartsEmpty = document.getElementById("charts-empty");
  var trendCharts = [];                  // {param, chart, section}

  function buildCharts() {
    trendCharts.forEach(function (t) { t.chart.destroy(); });
    trendCharts = [];
    chartsHost.textContent = "";

    // Per-client lines only, and only for estimated params (derived params have
    // no per-client series, so they get no chart here).
    DATA.estimated_params.forEach(function (param) {
      var section = document.createElement("section");
      section.className = "trend-chart";
      section.dataset.param = param;
      section.innerHTML = "<h3>" + param + "</h3>" +
        '<div class="chart-wrap"><canvas></canvas></div>';
      chartsHost.appendChild(section);

      var datasets = clientsWithSeries(param).map(function (client) {
        return lineDataset(client, seriesFor(param, client).slice());
      });

      var chart = new Chart(section.querySelector("canvas"), {
        type: "line",
        data: { labels: LABELS, datasets: datasets },
        options: baseOptions(param),
      });
      trendCharts.push({ param: param, chart: chart, section: section });
    });

    applyClientVisibility();
    applyParamFilter();
  }

  // --------------------------------------------------------------------- //
  // Dataset + options factories
  // --------------------------------------------------------------------- //
  function lineDataset(client, data) {
    return {
      label: client,
      clientName: client,                // used by the client toggle
      data: data,
      borderColor: COLOR[client],
      backgroundColor: COLOR[client],
      borderWidth: 2,
      tension: 0.15,
      spanGaps: true,
      pointRadius: 3,
    };
  }

  function baseOptions(param) {
    return {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: "nearest", intersect: false },
      scales: {
        y: {
          title: { display: true, text: state.metric === "runtime" ? "runtime (ms)" : "proposed gas" },
          beginAtZero: false,
        },
      },
      plugins: {
        legend: { display: true, position: "bottom" },
        tooltip: {
          callbacks: {
            label: function (ctx) {
              return ctx.dataset.label + ": " + fmt(ctx.parsed.y);
            },
            afterLabel: function (ctx) {
              var client = ctx.dataset.clientName;
              if (!client) return undefined;
              var cs = DATA.combo[param] && DATA.combo[param][client];
              return cs && cs[ctx.dataIndex] ? "fit: " + cs[ctx.dataIndex] : undefined;
            },
          },
        },
      },
    };
  }

  // --------------------------------------------------------------------- //
  // Filter application
  // --------------------------------------------------------------------- //
  function applyClientVisibility() {
    trendCharts.forEach(function (t) {
      t.chart.data.datasets.forEach(function (ds, i) {
        if (ds.clientName) t.chart.setDatasetVisibility(i, state.clients.has(ds.clientName));
      });
      t.chart.update();
    });
  }

  function applyParamFilter() {
    var anyShown = false;
    trendCharts.forEach(function (t) {
      var show = state.param === "all" || state.param === t.param;
      t.section.hidden = !show;
      anyShown = anyShown || show;
    });
    if (chartsEmpty) chartsEmpty.hidden = anyShown;
  }

  // --------------------------------------------------------------------- //
  // Wiring
  // --------------------------------------------------------------------- //
  var paramSel = document.getElementById("param-filter");
  paramSel.addEventListener("change", function () {
    state.param = paramSel.value;
    renderSection1();
    applyParamFilter();
  });

  document.querySelectorAll("#client-toggles input").forEach(function (cb) {
    cb.addEventListener("change", function () {
      if (cb.checked) state.clients.add(cb.value); else state.clients.delete(cb.value);
      renderSection1();
      applyClientVisibility();
    });
  });

  document.querySelectorAll("#metric-toggle input").forEach(function (rb) {
    rb.addEventListener("change", function () {
      if (!rb.checked) return;
      state.metric = rb.value;
      renderSection1();
      buildCharts();                     // metric changes the data series → rebuild
    });
  });

  // ---- initial render ----
  renderSection1();
  buildCharts();
})();
