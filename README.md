# Spletna stran o lokalnih volitvah 2026 v občini Logatec

Statična stran (HTML + CSS + malo JavaScripta, brez strežniške logike) s pregledom kandidatov in
občinskih list za lokalne volitve 15. novembra 2026.

## Ogled

V orbu:

```bash
amp orb services ensure
```

Ukaz izpiše javni portal (naslov `https://…onamp.dev/`). Stran lahko odprete tudi lokalno:

```bash
python3 -m http.server 8099
# nato odprite http://localhost:8099/
```

## Struktura

| Pot | Vsebina |
| --- | --- |
| `index.html` | Pregled: volilno leto, ključne številke, kandidati za župana, liste, izid 2022, datumi |
| `zupani.html`, `zupan-<id>.html` | Županski kandidati in njihove predstavitve |
| `liste.html`, `lista-<id>.html` | Občinske liste: program, dosedanje delo, kandidati |
| `kandidati.html` | Vseh 129 kandidatov za občinski svet z iskanjem in filtri |
| `krajevne-skupnosti.html` | Kandidati za svete 10 krajevnih skupnosti (89) |
| `metodologija.html` | Kako so podatki zbrani in označeni, omejitve |
| `viri.html` | Vsi viri s povezavami |
| `assets/` | `style.css` in `app.js` (filtriranje tabele) |
| `build/` | Izvorna koda za generiranje strani in uradni izvoz DVK |
| `.amp/services.yaml` | Deklaracija spletnega strežnika za orbe |

## Ponovno generiranje

Vsebina je v `build/data.py` (ročno povzeti programi, samooocne, biografije) in
`build/viri.py` (viri). Seznam kandidatov se strojno prebere iz `build/dvk-kandidati-064.json`
(uradni izvoz DVK za občino Logatec).

```bash
python3 build/generate.py
```

## Objava na GitHub Pages

Repozitorij vsebuje GitHub Actions potek `.github/workflows/pages.yml`, ki ob vsakem potisku na
vejo `main` objavi statične datoteke (`*.html` in `assets/`) na GitHub Pages.

Nastavitev (enkrat):

1. V repozitoriju odprite **Settings → Pages** in pod **Build and deployment → Source** izberite
   **GitHub Actions**.
2. Potisnite spremembo na vejo `main` ali ročno zaženite potek **Deploy to GitHub Pages** v zavihku
   **Actions**.

Stran je nato dostopna na `https://<uporabnisko-ime>.github.io/<repozitorij>/`.

> Opomba: GitHub Pages za zasebne repozitorije zahteva plačljiv načrt (Pro, Team ali Enterprise).
> Na brezplačnem načrtu mora biti repozitorij javen.

## Viri in označevanje

- Seznam kandidatov je strojno prebran iz uradnega izvoza DVK (`build/dvk-kandidati-064.json`).
- Programi in poročila so povzeti po spletnih straneh list, po občinskem glasilu Logaške novice
  (julij, avgust in oktober 2026) ter po objavah na Facebooku in Instagramu (Demokrati, SDS, NSi).
- Označevanje:
  - **preverjeno** – uradni vir ali javna evidenca (DVK/OVK, občinsko glasilo, uradne objave),
  - **samoocena** – lastna navedba kandidata ali liste, javno objavljena, a ne neodvisno preverjena,
  - **načrt / obljuba** – program za prihodnji mandat,
  - **ni javnega podatka** – v obravnavanih virih podatka ni.

Stran ni povezana z nobeno stranko, listo ali kandidatom in ni volilno propagandno sporočilo.
