/* Filtriranje tabele kandidatov (deluje brez strežnika, brez odvisnosti). */
(function () {
  "use strict";
  var tab = document.getElementById("tab");
  if (!tab) return;

  var q = document.getElementById("q");
  var fLista = document.getElementById("f-lista");
  var fVe = document.getElementById("f-ve");
  var fSvetnik = document.getElementById("f-svetnik");
  var reset = document.getElementById("reset");
  var count = document.getElementById("count");
  var rows = Array.prototype.slice.call(tab.tBodies[0].rows);
  var total = rows.length;

  function normal(s) {
    return (s || "")
      .toString()
      .toLowerCase()
      .replace(/[\u010d\u0107]/g, "c")
      .replace(/\u0161/g, "s")
      .replace(/\u017e/g, "z")
      .replace(/\u0111/g, "d")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  rows.forEach(function (r) {
    var hay = normal(r.dataset.iskalnik + " " + r.textContent);
    r.dataset.hay = " " + hay.replace(/[^a-z0-9]+/g, " ").replace(/\s+/g, " ").trim() + " ";
  });

  function ujemanje(hay, term) {
    // Vsaka beseda iskalnega niza se mora pojaviti na začetku neke besede.
    var besede = term.split(/\s+/).filter(Boolean);
    for (var i = 0; i < besede.length; i++) {
      if (hay.indexOf(" " + besede[i]) === -1) return false;
    }
    return true;
  }

  function apply() {
    var term = normal(q.value.trim()).replace(/[^a-z0-9]+/g, " ").trim();
    var lista = fLista.value;
    var ve = fVe.value;
    var samo = fSvetnik.checked;
    var shown = 0;

    rows.forEach(function (r) {
      var ok = true;
      if (term && !ujemanje(r.dataset.hay, term)) ok = false;
      if (ok && lista && r.dataset.lista !== lista) ok = false;
      if (ok && ve && r.dataset.ve !== ve) ok = false;
      if (ok && samo && r.dataset.svetnik !== "1") ok = false;
      r.hidden = !ok;
      if (ok) shown++;
    });

    count.textContent = shown;
  }

  [q, fLista, fVe].forEach(function (el) {
    el.addEventListener("input", apply);
    el.addEventListener("change", apply);
  });
  fSvetnik.addEventListener("change", apply);

  reset.addEventListener("click", function () {
    q.value = "";
    fLista.value = "";
    fVe.value = "";
    fSvetnik.checked = false;
    apply();
    q.focus();
  });

  apply();
})();
