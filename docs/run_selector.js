// Run selector dropdown (previous-runs picker), loaded on every page via base.html.
//
// The banner markup is a custom button + listbox (NOT a native <select>) so the
// open popup uses the page font rather than the OS chrome font. Each option is a
// real <a> link, so picking a run is plain navigation — there is no data-swapping
// logic here. If [data-run-dropdown] is absent (single-run pages, or no banner),
// this no-ops cleanly.
(function () {
  "use strict";

  function initRunDropdown() {
    var root = document.querySelector("[data-run-dropdown]");
    if (!root) return;
    var toggle = root.querySelector(".run-dropdown-toggle");
    var list = root.querySelector(".run-dropdown-list");
    var options = Array.prototype.slice.call(root.querySelectorAll(".run-dropdown-option"));
    if (!toggle || !list || !options.length) return;

    function isOpen() { return toggle.getAttribute("aria-expanded") === "true"; }

    function open(focusIndex) {
      list.hidden = false;
      toggle.setAttribute("aria-expanded", "true");
      var i = focusIndex;
      if (i == null) {
        i = options.findIndex(function (o) { return o.classList.contains("is-current"); });
        if (i < 0) i = 0;
      }
      options[i].focus();
    }

    function close(focusToggle) {
      list.hidden = true;
      toggle.setAttribute("aria-expanded", "false");
      if (focusToggle) toggle.focus();
    }

    function focusAt(i) {
      var n = options.length;
      options[((i % n) + n) % n].focus();
    }

    toggle.addEventListener("click", function () { isOpen() ? close(false) : open(); });
    toggle.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown" || e.key === "Enter" || e.key === " ") { e.preventDefault(); open(0); }
      else if (e.key === "ArrowUp") { e.preventDefault(); open(options.length - 1); }
    });

    options.forEach(function (opt, i) {
      opt.addEventListener("keydown", function (e) {
        if (e.key === "ArrowDown") { e.preventDefault(); focusAt(i + 1); }
        else if (e.key === "ArrowUp") { e.preventDefault(); focusAt(i - 1); }
        else if (e.key === "Home") { e.preventDefault(); focusAt(0); }
        else if (e.key === "End") { e.preventDefault(); focusAt(options.length - 1); }
        else if (e.key === "Escape") { e.preventDefault(); close(true); }
      });
    });

    document.addEventListener("click", function (e) {
      if (isOpen() && !root.contains(e.target)) close(false);
    });
  }

  if (document.readyState !== "loading") initRunDropdown();
  else document.addEventListener("DOMContentLoaded", initRunDropdown);
})();
