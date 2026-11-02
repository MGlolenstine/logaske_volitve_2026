# -*- coding: utf-8 -*-
"""Generator statične strani o lokalnih volitvah 2026 v občini Logatec.

Zagon:  python3 build/generate.py
Izhod:  HTML datoteke v korenu projekta + assets/
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import data as D          # noqa: E402
import viri as V          # noqa: E402

DVK = os.path.join(HERE, "dvk-kandidati-064.json")

SITE_TITLE = "Lokalne volitve 2026 v občini Logatec"
SITE_SUB = "Pregled kandidatov in občinskih list"


# ------------------------------------------------------------------ pripomočki
def e(t):
    return html.escape(str(t), quote=True)


def slug(s):
    s = s.lower()
    for a, b in (("č", "c"), ("š", "s"), ("ž", "z"), ("ć", "c"), ("đ", "d")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def letnik_tekst(letnik):
    if not letnik:
        return ""
    return "letnik %s" % letnik


# ------------------------------------------------------- nalaganje podatkov DVK
def nalozi_kandidate():
    with open(DVK, encoding="utf-8") as f:
        rows = json.load(f)

    zupani, svet, ks = [], [], []
    for r in rows:
        rec = {
            "naziv": r["naziv"].strip(),
            "letnik": (r.get("let_roj") or "").strip(),
            "lista": (r.get("lista") or "").strip(),
            "pred": (r.get("pred") or "").strip(),
            "sifra_liste": str(r.get("zap_st_st") or "").strip(),
            "mesto": r.get("zap_st"),
            "ve": str(r.get("ve") or "").strip(),
            "cskv": (r.get("cskv") or "").strip(),
        }
        if r["tip"] == "501":
            zupani.append(rec)
        elif r["tip"] == "502":
            svet.append(rec)
        elif r["tip"] == "508":
            ks.append(rec)
    for coll in (zupani, svet, ks):
        coll.sort(key=lambda x: (x["sifra_liste"] or "", x["ve"] or "", int(x["mesto"] or 0)))
    return zupani, svet, ks


ZUPANI_DVK, SVET_DVK, KS_DVK = nalozi_kandidate()


def prikaz_imena(ime):
    n = D.NASLOVI.get(ime)
    return ("%s %s" % (n, ime)) if n else ime


# --------------------------------------------------------------------- predloga
NAV = [
    ("index.html", "Pregled"),
    ("zupani.html", "Županski kandidati"),
    ("liste.html", "Občinske liste"),
    ("kandidati.html", "Vsi kandidati za svet"),
    ("krajevne-skupnosti.html", "Krajevne skupnosti"),
    ("metodologija.html", "Metodologija"),
    ("viri.html", "Viri"),
]


def page(naziv, body, aktivno="", opis=""):
    nav = "\n".join(
        '        <a href="%s"%s>%s</a>' % (u, ' class="on"' if u == aktivno else "", e(t))
        for u, t in NAV
    )
    return """<!DOCTYPE html>
<html lang="sl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{opis}">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#vsebina">Preskoči na vsebino</a>
<header class="site-head">
  <div class="wrap head-inner">
    <a class="brand" href="index.html">
      <span class="brand-kicker">Občina Logatec · volilno leto 2026</span>
      <span class="brand-title">{sub}</span>
    </a>
    <nav class="mainnav" aria-label="Glavni meni">
{nav}
    </nav>
  </div>
</header>
<main id="vsebina" class="wrap">
{body}
</main>
<footer class="site-foot">
  <div class="wrap">
    <p><strong>Nezavezujoč informativni pregled.</strong> Stran ni povezana z nobeno stranko, listo
    ali kandidatom in ni volilno propagandno sporočilo. Podatki so zbrani iz javnih virov
    {dostop}. Viri so navedeni pri vsakem sklopu in na strani <a href="viri.html">Viri</a>.</p>
    <p class="muted">Podatki o kandidatih: uradni izvoz Državne volilne komisije za lokalne volitve
    2026. Naslovov prebivališča kandidatov ne objavljamo.</p>
  </div>
</footer>
<script src="assets/app.js" defer></script>
</body>
</html>
""".format(title=e(naziv), opis=e(opis or SITE_SUB), nav=nav, body=body,
           sub=e(SITE_SUB), dostop=e(V.DOSTOP))


def badge(kind, text):
    return '<span class="badge b-%s">%s</span>' % (kind, e(text))


def preverjeno_blok(items, naslov="Preverjeni podatki"):
    if not items:
        return ""
    li = "\n".join("      <li>%s</li>" % e(x) for x in items)
    return """
  <section class="panel p-ok">
    <h3>%s %s</h3>
    <ul class="ticks">
%s
    </ul>
  </section>""" % (badge("ok", "preverjeno"), e(naslov), li)


def samoocena_blok(items, vir, naslov="Navedbe liste oz. kandidata"):
    if not items:
        return ""
    li = "\n".join("      <li>%s</li>" % e(x) for x in items)
    v = ('\n    <p class="src">Vir: %s</p>' % e(vir)) if vir else ""
    return """
  <section class="panel p-claim">
    <h3>%s %s</h3>
    <ul class="ticks">
%s
    </ul>%s
  </section>""" % (badge("claim", "samoocena"), e(naslov), li, v)


def program_sklopi(sklopi):
    out = []
    for s in sklopi:
        li = "\n".join("        <li>%s</li>" % e(t) for t in s["tocke"])
        out.append("""    <details class="prog">
      <summary>%s</summary>
      <ul>
%s
      </ul>
    </details>""" % (e(s["naslov"]), li))
    return "\n".join(out)


# ------------------------------------------------------------------------ strani
def stran_index():
    zupan_cards = []
    for z in D.ZUPANI:
        l = next(x for x in D.LISTE if x["id"] == z["lista_id"])
        zupan_cards.append("""
      <article class="card kandidat">
        <div class="card-top"><span class="sifra">%s</span><span class="tag">%s</span></div>
        <h3><a href="zupan-%s.html">%s</a></h3>
        <p class="meta">%s · %s</p>
        <p>%s</p>
        <p class="src">Lista: <a href="lista-%s.html">%s</a></p>
      </article>""" % (
            e(z["sifra"]), e("na glasovnici"),
            e(z["id"]), e(z["ime"]),
            e(z["predlagatelj"]), e(letnik_tekst(z["letnik"])),
            e(z["povzetek"]),
            e(l["id"]), e(l["kratko"]),
        ))

    list_cards = []
    for l in D.LISTE:
        st = sum(1 for r in SVET_DVK if r["sifra_liste"] == l["sifra"])
        zup = ""
        if l.get("zupan"):
            z = next(x for x in D.ZUPANI if x["id"] == l["zupan"])
            zup = '<p class="meta">Županski kandidat: <a href="zupan-%s.html">%s</a></p>' % (
                e(z["id"]), e(z["ime"]))
        elif l.get("podpira_zupana"):
            z = next(x for x in D.ZUPANI if x["id"] == l["podpira_zupana"])
            zup = '<p class="meta">Za župana podpira <a href="zupan-%s.html">%s</a></p>' % (
                e(z["id"]), e(z["ime"]))
        else:
            zup = '<p class="meta">Brez lastnega županskega kandidata</p>'
        list_cards.append("""
      <article class="card lista">
        <div class="card-top"><span class="sifra">%s</span><span class="tag">%s kandidatov</span></div>
        <h3><a href="lista-%s.html">%s</a></h3>
        %s
        <p>%s</p>
      </article>""" % (
            e(l["sifra"]), e(st), e(l["id"]), e(l["naziv"]), zup, e(l["povzetek"]),
        ))

    udelezba = D.IZID_2022
    svet_rows = "\n".join(
        "        <tr><td>%s</td><td>%s</td><td>%s</td><td class=\"num\">%s</td></tr>" % (
            e(n), e(g), e(d), e(m))
        for n, g, d, m in udelezba["svet"])

    body = """
<section class="hero">
  <p class="eyebrow">Lokalne volitve · {dan} · 2. krog {drugi}</p>
  <h1>Kandidati in občinske liste v občini Logatec</h1>
  <p class="lead">Pregled vseh <strong>3 županskih kandidatov</strong>, <strong>7 kandidatnih list</strong>
  s <strong>129 kandidati za občinski svet</strong> in <strong>89 kandidati za svete krajevnih
  skupnosti</strong>. Za vsako listo in vsakega županskega kandidata so zbrani programi, načrti in
  javno dostopni podatki o dosedanjem delu. Kjer podatkov ni, je to izrecno zapisano.</p>
  <div class="facts">
    <div><span>3</span> županski kandidati</div>
    <div><span>7</span> kandidatnih list</div>
    <div><span>129</span> kandidatov za občinski svet</div>
    <div><span>21</span> mandatov v občinskem svetu</div>
    <div><span>10</span> krajevnih skupnosti</div>
  </div>
</section>

<section class="callout">
  <h2>Kako brati te strani</h2>
  <p>Podatki so namenoma ločeni po zanesljivosti, da je jasno, kaj je preverjeno in kaj je trditev
  kandidata ali liste:</p>
  <ul class="legend">
    <li>{bok} podatek iz uradnega vira ali javne evidence (DVK/OVK, občinsko glasilo, uradne objave).</li>
    <li>{bclaim} lastna navedba kandidata ali liste; objavljena je bila javno, vendar je nismo
        neodvisno preverjali.</li>
    <li>{bplan} program, cilj ali obljuba za prihodnji mandat – torej načrt, ne dosežek.</li>
    <li>{bnone} podatka v javnih virih nismo našli.</li>
  </ul>
  <p class="muted">Volilno leto je <strong>2026</strong>; volitve so {dan}, morebitni drugi krog za
  župana pa {drugi}. Volilna kampanja je potekala od {kampanja}.</p>
</section>

<h2 class="sect">Kandidati za župana</h2>
<div class="grid three">
{zk}
</div>

<h2 class="sect">Občinske liste</h2>
<p class="sect-intro">Vrstni red list je vrstni red na glasovnici (številka liste). Vsaka lista
predstavi svoj program in svoje kandidate na svoji strani.</p>
<div class="grid two">
{lk}
</div>

<h2 class="sect">Volitve 2022 za primerjavo</h2>
<div class="panel">
  <p>Občinski svet 2022–2026 je imel 21 mandatov. Volilna udeležba je bila v prvem krogu
  {u1}, v drugem pa {u2}.</p>
  <h3>Župan 2022 – prvi krog</h3>
  <div class="tablewrap"><table>
    <thead><tr><th>Kandidat</th><th>Predlagatelj</th><th class="num">Glasovi</th><th class="num">Delež</th></tr></thead>
    <tbody>
{z1}
    </tbody>
  </table></div>
  <h3>Občinski svet 2022 – deleži in mandati</h3>
  <p class="muted">Deleži glasov so navedeni po volilnih enotah 1 / 2 / 3; mandati so skupni.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Lista</th><th>Glasovi (VE 1 / 2 / 3)</th><th>Delež (VE 1 / 2 / 3)</th><th class="num">Mandati</th></tr></thead>
    <tbody>
{sv}
    </tbody>
  </table></div>
  <p class="src">Vir: uradni izidi DVK/OVK, lokalne volitve 2022 (glej <a href="viri.html">Viri</a>).</p>
</div>

<h2 class="sect">Pomembni datumi</h2>
<div class="panel">
  <ul class="dates">
    <li><span>30. 10. 2026</span> javna objava potrjenih kandidatur</li>
    <li><span>4. 11. 2026</span> zadnji dan za prijavo na glasovanje po pošti</li>
    <li><span>10.–12. 11. 2026</span> predčasno glasovanje</li>
    <li><span>15. 11. 2026</span> volitve, volišča od 7. do 19. ure</li>
    <li><span>29. 11. 2026</span> drugi krog za župana, kjer ni zmagovalca</li>
  </ul>
  <p class="src">Vir: DVK, rokovnik volilnih opravil.</p>
</div>
""".format(
        dan=e(D.DAN_VOLITEV), drugi=e(D.DAN_DRUGEGA_KROGA), kampanja=e(D.OBDOBJE_KAMPANJE),
        bok=badge("ok", "preverjeno"), bclaim=badge("claim", "samoocena"),
        bplan=badge("plan", "načrt / obljuba"), bnone=badge("none", "ni javnega podatka"),
        zk="\n".join(zupan_cards), lk="\n".join(list_cards),
        u1=e(udelezba["udelezba_1"]), u2=e(udelezba["udelezba_2"]),
        z1="\n".join(
            "      <tr><td>%s</td><td>%s</td><td class=\"num\">%s</td><td class=\"num\">%s</td></tr>"
            % (e(a), e(b), e(c), e(d)) for a, b, c, d in udelezba["zupan_1"]),
        sv=svet_rows,
    )
    return page(SITE_TITLE + " – pregled", body, "index.html",
                "Pregled županskih kandidatov, občinskih list in kandidatov za občinski svet "
                "občine Logatec na lokalnih volitvah 2026.")


def stran_zupani():
    cards = []
    for z in D.ZUPANI:
        l = next(x for x in D.LISTE if x["id"] == z["lista_id"])
        cards.append("""
      <article class="card kandidat">
        <div class="card-top"><span class="sifra">%s</span><span class="tag">na glasovnici</span></div>
        <h3><a href="zupan-%s.html">%s</a></h3>
        <p class="meta">%s · %s</p>
        <p>%s</p>
        <p class="src">Lista: <a href="lista-%s.html">%s</a></p>
      </article>""" % (e(z["sifra"]), e(z["id"]), e(z["ime"]), e(z["predlagatelj"]),
                       e(letnik_tekst(z["letnik"])), e(z["povzetek"]),
                       e(l["id"]), e(l["kratko"])))
    body = """
<h1>Kandidati za župana občine Logatec 2026</h1>
<p class="lead">Na glasovnici za župana so {n} kandidati. Vrstni red je vrstni red na glasovnici.
Župana se voli po večinskem sistemu; če v prvem krogu nihče ne dobi večine, sledi drugi krog
{drugi}.</p>
<div class="grid three">
%s
</div>
""".format(n=len(D.ZUPANI), drugi=e(D.DAN_DRUGEGA_KROGA), _=None) % "\n".join(cards)
    return page("Županski kandidati 2026 – Logatec", body, "zupani.html",
                "Trije kandidati za župana občine Logatec na lokalnih volitvah 2026.")


def stran_liste():
    cards = []
    for l in D.LISTE:
        st = sum(1 for r in SVET_DVK if r["sifra_liste"] == l["sifra"])
        po_ve = []
        for ve in ("01", "02", "03"):
            n = sum(1 for r in SVET_DVK if r["sifra_liste"] == l["sifra"] and r["ve"] == ve)
            if n:
                po_ve.append("%s: %d" % (D.VOLILNE_ENOTE[ve]["naziv"], n))
        zup = ""
        if l.get("zupan"):
            z = next(x for x in D.ZUPANI if x["id"] == l["zupan"])
            zup = "Županski kandidat: <strong>%s</strong>" % e(z["ime"])
        elif l.get("podpira_zupana"):
            z = next(x for x in D.ZUPANI if x["id"] == l["podpira_zupana"])
            zup = "Za župana podpira <strong>%s</strong>" % e(z["ime"])
        else:
            zup = "Brez lastnega županskega kandidata"
        cards.append("""
      <article class="card lista">
        <div class="card-top"><span class="sifra">%s</span><span class="tag">%s kandidatov</span></div>
        <h3><a href="lista-%s.html">%s</a></h3>
        <p class="meta">%s</p>
        <p class="meta">%s</p>
        <p>%s</p>
      </article>""" % (e(l["sifra"]), e(st), e(l["id"]), e(l["naziv"]),
                       zup, e(" · ".join(po_ve)), e(l["povzetek"])))
    body = """
<h1>Občinske liste 2026 v občini Logatec</h1>
<p class="lead">Na volitvah za občinski svet občine Logatec nastopa {n} list s skupaj {k} kandidati,
ki se potegujejo za 21 mandatov. Voli se po proporcionalnem sistemu: volivec glasuje za eno listo
in lahko označi enega kandidata z nje (preferenčni glas).</p>
<div class="grid two">
%s
</div>
""".format(n=len(D.LISTE), k=len(SVET_DVK), _=None) % "\n".join(cards)
    return page("Občinske liste 2026 – Logatec", body, "liste.html",
                "Sedem kandidatnih list za občinski svet občine Logatec na volitvah 2026.")


def kandidati_liste(l):
    """Vrne HTML seznam kandidatov liste po volilnih enotah."""
    out = []
    for ve in ("01", "02", "03"):
        rows = [r for r in SVET_DVK if r["sifra_liste"] == l["sifra"] and r["ve"] == ve]
        if not rows:
            continue
        items = []
        for r in rows:
            sv = (' <span class="mini ok" title="Izvoljen/a 2022">2022–2026 svetnik/ca</span>'
                  if r["naziv"] in D.SVETNIKI_2022 else "")
            opis = D.OPISI_KANDIDATOV.get(r["naziv"])
            op = ('<p class="kand-opis">%s</p>' % e(opis)) if opis else ""
            items.append(
                '        <li><span class="kand-num">%s.</span> '
                '<span class="kand-ime">%s</span> <span class="kand-letnik">(%s)</span>%s%s</li>'
                % (e(r["mesto"]), e(prikaz_imena(r["naziv"])), e(r["letnik"]), sv, op))
        out.append("""
    <div class="ve-block">
      <h4>%s <span class="muted">– %s</span></h4>
      <ol class="kand-list">
%s
      </ol>
    </div>""" % (e(D.VOLILNE_ENOTE[ve]["naziv"]), e(D.VOLILNE_ENOTE[ve]["opis"]),
                 "\n".join(items)))
    return "\n".join(out)


def stran_lista(l):
    p = l["program"]
    if p["stanje"] == "da":
        program_html = """
  <p>%s</p>
  %s
  <p class="src">Vir: %s</p>""" % (e(p.get("uvod", "")), program_sklopi(p["sklopi"]), e(p["vir"]))
    elif p["stanje"] == "delno":
        li = "\n".join("      <li>%s</li>" % e(x) for x in p.get("navedki", []))
        program_html = """
  <p>%s</p>
  <ul class="ticks">%s
  </ul>
  <p class="src">Vir: %s</p>""" % (e(p.get("uvod") or p.get("opomba", "")), li, e(p["vir"]))
    else:
        program_html = """
  <div class="empty">%s %s</div>""" % (badge("none", "ni javnega podatka"), e(p["opomba"]))

    m = l["mandat"]
    mandat_parts = []
    mandat_parts.append(preverjeno_blok(m.get("preverjeno", []),
                                        "Preverjeni izidi in sestava 2022"))
    if m["stanje"] == "da":
        mandat_parts.append(samoocena_blok(m.get("samoocena", []), m.get("vir", ""),
                                           "Kaj skupina navaja o svojem delu"))
    else:
        mandat_parts.append("""
  <div class="empty">%s %s</div>""" % (badge("none", "ni javnega podatka"), e(m.get("opomba", ""))))

    mandat_html = "\n".join(x for x in mandat_parts if x)

    zup_html = ""
    if l.get("zupan"):
        z = next(x for x in D.ZUPANI if x["id"] == l["zupan"])
        zup_html = """
  <p>Županski kandidat liste je <a href="zupan-%s.html"><strong>%s</strong></a>.</p>""" % (
            e(z["id"]), e(z["ime"]))
    elif l.get("podpira_zupana"):
        z = next(x for x in D.ZUPANI if x["id"] == l["podpira_zupana"])
        zup_html = """
  <p>Lista nima svojega županskega kandidata, za župana pa podpira
  <a href="zupan-%s.html"><strong>%s</strong></a>.</p>""" % (e(z["id"]), e(z["ime"]))
    else:
        zup_html = """
  <p class="muted">Lista ne kandidira za župana.</p>"""

    st = sum(1 for r in SVET_DVK if r["sifra_liste"] == l["sifra"])

    body = """
<p class="crumbs"><a href="liste.html">Občinske liste</a> ›</p>
<h1>{naziv}</h1>
<p class="lead">{povzetek}</p>
<div class="keyfacts">
  <div><span class="k">Številka na glasovnici</span><span class="v">{sifra}</span></div>
  <div><span class="k">Predlagatelj</span><span class="v">{pred}</span></div>
  <div><span class="k">Število kandidatov</span><span class="v">{st}</span></div>
</div>
{zup}

<h2 class="sect">Program in načrti {planbadge}</h2>
<div class="panel p-plan">
  <h3>{pnaziv}</h3>
{program}
</div>

<h2 class="sect">Dosedanje delo in mandat 2022–2026</h2>
{mandat}

{preverjeno_extra}

<h2 class="sect">Kandidati za občinski svet</h2>
<p class="sect-intro">Vrstni red je vrstni red na glasovnici znotraj liste v posamezni volilni
enoti (vir: uradni izvoz DVK).</p>
{kandidati}
<p class="src">Vir seznama: uradni izvoz DVK za lokalne volitve 2026.</p>
""".format(
        naziv=e(l["naziv"]), povzetek=e(l["povzetek"]), sifra=e(l["sifra"]),
        pred=e(l["predlagatelj"]), st=e(st), zup=zup_html,
        planbadge=badge("plan", "načrt"), pnaziv=e(p["naslov"]), program=program_html,
        mandat=mandat_html,
        preverjeno_extra=preverjeno_blok(l.get("preverjeno", []),
                                         "Druga preverjena dejstva o listi"),
        kandidati=kandidati_liste(l),
    )
    return page("%s – Logatec 2026" % l["naziv"], body, "liste.html",
                "Program, dosedanje delo in kandidati liste %s na volitvah 2026 v občini Logatec."
                % l["naziv"])


def stran_zupan(z):
    l = next(x for x in D.LISTE if x["id"] == z["lista_id"])
    bio = "\n".join("      <li>%s</li>" % e(x) for x in z["biografija"])

    body = """
<p class="crumbs"><a href="zupani.html">Županski kandidati</a> ›</p>
<h1>{ime}</h1>
<p class="lead">Kandidat za župana občine Logatec, volitve {dan}.</p>
<div class="keyfacts">
  <div><span class="k">Številka na glasovnici</span><span class="v">{sifra}</span></div>
  <div><span class="k">Predlagatelj</span><span class="v">{pred}</span></div>
  <div><span class="k">Letnik</span><span class="v">{letnik}</span></div>
  <div><span class="k">Lista</span><span class="v"><a href="lista-{lid}.html">{lime}</a></span></div>
</div>
<p>{povzetek}</p>

<h2 class="sect">Predstavitev kandidata {claimbadge}</h2>
<div class="panel p-claim">
  <p class="hint">Naslednje navedbe so iz predstavitve kandidata in njegove liste; niso neodvisno
  preverjene.</p>
  <ul class="ticks">
{bio}
  </ul>
  <p class="src">Vir: predstavitev kandidata na spletni strani liste in lokalni mediji.</p>
</div>

<h2 class="sect">Preverjeni podatki</h2>
{preverjeno}

{samoocena}

<h2 class="sect">Program, ki ga zagovarja {planbadge}</h2>
<div class="panel p-plan">
  <p>Kandidat nastopa na listi <a href="lista-{lid}.html">{lime}</a>, zato velja program te liste.</p>
  {program_links}
</div>

<h2 class="sect">Kandidati liste {lime}</h2>
<p class="sect-intro">Kandidati iste liste za občinski svet (vrstni red po volilnih enotah).</p>
{kandidati}
""".format(
        ime=e(z["ime"]), dan=e(D.DAN_VOLITEV), sifra=e(z["sifra"]), pred=e(z["predlagatelj"]),
        letnik=e(z["letnik"]), lid=e(l["id"]), lime=e(l["kratko"]),
        povzetek=e(z["povzetek"]), claimbadge=badge("claim", "samoocena"), bio=bio,
        preverjeno=preverjeno_blok(z["preverjeno"], "Uradni izidi in javne evidence"),
        samoocena=samoocena_blok(z["samoocena"], "Predstavitev kandidata oziroma liste",
                                 "Navedbe kandidata"),
        planbadge=badge("plan", "načrt"),
        program_links='<p><a href="lista-%s.html">Celoten program in dosedanje delo liste →</a></p>'
                      % e(l["id"]),
        kandidati=kandidati_liste(l),
    )
    return page("%s – kandidat za župana Logatec 2026" % z["ime"], body, "zupani.html",
                "Predstavitev, preverjeni podatki in program kandidata za župana občine Logatec "
                "%s." % z["ime"])


def stran_kandidati():
    options = "".join(
        '<option value="%s">%s</option>' % (e(l["sifra"]), e(l["naziv"])) for l in D.LISTE)
    rows = []
    for r in sorted(SVET_DVK, key=lambda x: (x["sifra_liste"], x["ve"], int(x["mesto"]))):
        l = next(x for x in D.LISTE if x["sifra"] == r["sifra_liste"])
        sv = '1' if r["naziv"] in D.SVETNIKI_2022 else '0'
        opis = D.OPISI_KANDIDATOV.get(r["naziv"], "")
        rows.append(
            '      <tr data-lista="%s" data-ve="%s" data-svetnik="%s" '
            'data-iskalnik="%s">\n'
            '        <td data-th="Kandidat">%s</td>\n'
            '        <td data-th="Lista"><a href="lista-%s.html">%s</a></td>\n'
            '        <td data-th="Volilna enota">%s</td>\n'
            '        <td data-th="Mesto na listi" class="num">%s.</td>\n'
            '        <td data-th="Letnik">%s</td>\n'
            '        <td data-th="Prejšnji mandat">%s</td>\n'
            '        <td data-th="Opis" class="opis">%s</td>\n'
            '      </tr>' % (
                e(r["sifra_liste"]), e(r["ve"]), sv,
                e(slug(r["naziv"] + " " + l["naziv"])),
                e(prikaz_imena(r["naziv"])),
                e(l["id"]), e(l["kratko"]),
                e(r["ve"]),
                e(r["mesto"]),
                e(r["letnik"]),
                ("<span class=\"mini ok\">2022–2026</span>" if sv == '1'
                 else '<span class="muted">–</span>'),
                e(opis) if opis else '<span class="muted">ni javnega opisa</span>',
            ))

    body = """
<h1>Vsi kandidati za občinski svet občine Logatec 2026</h1>
<p class="lead">Skupaj {n} kandidatov na {m} listah. Volilna enota je navedena, mesto na listi pa
pomeni vrstni red znotraj liste v tej volilni enoti (vir: uradni izvoz DVK).</p>

<div class="filterbar" role="search">
  <label>Iskanje po imenu ali listi
    <input id="q" type="search" placeholder="npr. Vidic ali Naša Notranjska" autocomplete="off">
  </label>
  <label>Lista
    <select id="f-lista"><option value="">vse liste</option>{options}</select>
  </label>
  <label>Volilna enota
    <select id="f-ve">
      <option value="">vse enote</option>
      <option value="01">1. volilna enota</option>
      <option value="02">2. volilna enota</option>
      <option value="03">3. volilna enota</option>
    </select>
  </label>
  <label class="check"><input id="f-svetnik" type="checkbox"> samo bivši svetniki 2022–2026</label>
  <button id="reset" type="button" class="btn">Ponastavi</button>
</div>
<p class="filtercount"><span id="count">{n}</span> od {n} kandidatov</p>

<div class="tablewrap">
  <table class="kandidati-tab" id="tab">
    <thead>
      <tr><th>Kandidat</th><th>Lista</th><th>Volilna enota</th><th class="num">Mesto</th>
      <th>Letnik</th><th>Prejšnji mandat</th><th>Opis</th></tr>
    </thead>
    <tbody>
{rows}
    </tbody>
  </table>
</div>
<p class="src">Opomba: opis je na voljo le za kandidate, katerih lista je objavila predstavitev
(Naša Notranjska in Občanska lista Logatec). Za ostale kandidate javnega opisa nismo našli.</p>
""".format(n=len(SVET_DVK), m=len(D.LISTE), options=options, rows="\n".join(rows))
    return page("Vsi kandidati za občinski svet – Logatec 2026", body, "kandidati.html",
                "Seznam vseh 129 kandidatov za občinski svet občine Logatec na volitvah 2026 z "
                "iskanjem in filtri.")


def stran_ks():
    skupnosti = {}
    for r in KS_DVK:
        skupnosti.setdefault(r["cskv"], []).append(r)
    blocks = []
    for ime in sorted(skupnosti):
        rows = skupnosti[ime]
        liste = {}
        for r in rows:
            liste.setdefault(r["lista"], []).append(r)
        lparts = []
        for ln in sorted(liste):
            items = "\n".join(
                '          <li><span class="kand-num">%s.</span> '
                '<span class="kand-ime">%s</span> <span class="kand-letnik">(%s)</span></li>'
                % (e(r["mesto"]), e(priimak_prikaz(r["naziv"])), e(r["letnik"]))
                for r in sorted(liste[ln], key=lambda x: int(x["mesto"])))
            lparts.append("""      <details class="prog">
        <summary>%s <span class="muted">(%d)</span></summary>
        <ol class="kand-list">
%s
        </ol>
      </details>""" % (e(ln), len(liste[ln]), items))
        blocks.append("""
  <section class="panel">
    <h3>%s <span class="muted">– %d kandidatov</span></h3>
%s
  </section>""" % (e(ime), len(rows), "\n".join(lparts)))

    body = """
<h1>Sveti krajevnih, četrtnih in vaških skupnosti</h1>
<p class="lead">Hkrati z občinskim svetom se volijo tudi sveti krajevnih skupnosti; vsak volivec
glasuje v svoji skupnosti. V občini Logatec je {n} skupnosti s skupaj {k} kandidati. Za te kandidate
javnih programov ali predstavitev v obravnavanih virih nismo našli, zato so navedeni samo osnovni
podatki iz uradnega izvoza DVK.</p>
<div class="empty">{bnone} Za svete krajevnih skupnosti objavljenih programov ali opisov kandidatov
nismo našli.</div>
{blocks}
""".format(n=len(skupnosti), k=len(KS_DVK), bnone=badge("none", "ni javnega podatka"),
           blocks="\n".join(blocks))
    return page("Krajevne skupnosti – kandidati 2026 Logatec", body, "krajevne-skupnosti.html",
                "Kandidati za svete krajevnih skupnosti v občini Logatec na volitvah 2026.")


def priimak_prikaz(ime):
    return prikaz_imena(ime)


def stran_metodologija():
    body = """
<h1>Metodologija in omejitve podatkov</h1>
<p class="lead">Ta stran pojasnjuje, od kod prihajajo podatki, kako so označeni in katerih podatkov
v javnih virih ni bilo mogoče najti.</p>

<h2 class="sect">1. Vir seznama kandidatov</h2>
<div class="panel">
  <p>Seznam kandidatov je povzet po izhodiščnem viru
  (<a href="https://obcan.si/obcina/logatec/kandidati">obcan.si/obcina/logatec/kandidati</a>) in
  nato preverjen ter dopolnjen z <strong>uradnim izvozom Državne volilne komisije</strong> za
  lokalne volitve 2026 za občino Logatec (šifra občine 64). Iz izvoza so prevzeti:</p>
  <ul>
    <li>imena kandidatov,</li>
    <li>letnice rojstva,</li>
    <li>volilna enota in vrstni red na glasovnici (mesto na listi),</li>
    <li>predlagatelj in naziv liste.</li>
  </ul>
  <p>Uradni izvoz ne vsebuje akademskih naslovov. Kjer naslov izhaja iz drugih javnih objav (npr.
  »dr.«, »mag.«, »dr. med.«), je dodan pri imenu; takšna dopolnitev je kozmetična in ne vpliva na
  podatke o kandidaturi.</p>
</div>

<h2 class="sect">2. Označevanje podatkov</h2>
<div class="panel">
  <ul class="legend">
    <li>{bok} podatek iz uradnega vira ali javne evidence (DVK/OVK, občinsko glasilo, uradne objave).</li>
    <li>{bclaim} lastna navedba kandidata ali liste. Objavljena je javno, vendar je nismo neodvisno
    preverjali, zato je ni mogoče šteti za preverjeno dejstvo.</li>
    <li>{bplan} program, cilj ali obljuba za prihodnji mandat – torej načrt, ne dosežek.</li>
    <li>{bnone} podatka v javnih virih nismo našli.</li>
  </ul>
  <p><strong>Zakaj je ločevanje pomembno:</strong> poročila svetniških skupin o mandatu 2022–2026,
  ki so bila objavljena v občinskem glasilu Logaške novice, so njihove lastne ocene. Objavljena so
  bila javno in vsebujejo konkretne navedbe, vendar jih nismo preverjali po primarnih dokumentih
  (npr. po zapisnikih sej občinskega sveta). Zato so prikazana kot <em>samoocena</em> in ne kot
  preverjeni dosežki.</p>
</div>

<h2 class="sect">3. Katerih podatkov v virih ni</h2>
<div class="panel">
  <ul>
    <li><strong>Program Demokratov</strong> ni objavljen kot enoten dokument, ampak po posameznih
    ukrepih na Instagramu in Facebooku (oktober 2026). Povzeti so vsi objavljeni ukrepi.</li>
    <li><strong>Program NSi Logatec</strong> ima po navedbah stranke tri krovne stebre in program
    TOP 10, ki ga predstavljajo na pogovornih večerih. Celotnega seznama TOP 10 v berljivi obliki
    nismo našli; povzete so tiste točke, ki so objavljene v njihovih objavah in v občinskem
    glasilu.</li>
    <li><strong>Program SDS Logatec</strong> je objavljen v objavi na Facebooku (24. 10. 2026) kot
    seznam ciljev in v oglasu v občinskem glasilu. Podrobnejši predvolilni nagovor je bil
    dostavljen v gospodinjstva in ni objavljen na spletu.</li>
    <li><strong>Posamezni opisi kandidatov</strong> so na voljo le za dve listi (Naša Notranjska in
    Občanska lista Logatec). Za kandidate ostalih petih list javnih opisov v obravnavanih virih
    nismo našli; v tabeli je to izrecno označeno.</li>
    <li><strong>Programi za svete krajevnih skupnosti</strong> niso javno objavljeni.</li>
    <li><strong>Naslovi prebivališča kandidatov</strong> so sicer del uradnega izvoza DVK, vendar
    jih zaradi zasebnosti ne objavljamo.</li>
  </ul>
</div>

<h2 class="sect">4. Nevtralnost</h2>
<div class="panel">
  <p>Stran ne podpira nobene stranke, liste ali kandidata. Povzetki programov so skrajšani in
  poskušajo ostati opisni; za polno vsebino je pri vsaki listi povezava na izvirni vir. Vrstni red
  list na straneh je vrstni red na glasovnici, vrstni red županskih kandidatov pa prav tako.</p>
  <p>Kjer je bilo mogoče, so navedena tudi dejstva, ki so za posamezno listo manj ugodna, in
  opozorila na omejitve podatkov.</p>
</div>

<h2 class="sect">5. Kako so nastale te strani</h2>
<div class="panel">
  <p>Stran je statična (HTML in CSS, brez strežnika). Podatki o kandidatih so bili strojno prebrani
  iz uradnega izvoza DVK, vsebinski deli (programi, samooocne, biografije) pa ročno povzeti iz virov,
  navedenih na strani <a href="viri.html">Viri</a>. Del programov (Demokrati, SDS, NSi) je objavljen
  le na družbenih omrežjih; povzet je po posameznih objavah. Datum zajema podatkov: {dostop}.</p>
</div>
""".format(bok=badge("ok", "preverjeno"), bclaim=badge("claim", "samoocena"),
           bplan=badge("plan", "načrt / obljuba"), bnone=badge("none", "ni javnega podatka"),
           dostop=e(V.DOSTOP))
    return page("Metodologija – Logatec 2026", body, "metodologija.html",
                "Kako so zbrani in označeni podatki ter katere omejitve veljajo.")


def stran_viri():
    sekcije = []
    for naslov, viri in V.VIRI:
        items = []
        for naziv, url, opis in viri:
            items.append("""
      <li>
        <a href="%s" rel="noopener">%s</a>
        <span class="src">%s</span>
      </li>""" % (e(url), e(naziv), e(opis)))
        sekcije.append("""
<h2 class="sect">%s</h2>
<div class="panel">
  <ul class="viri">
%s
  </ul>
</div>""" % (e(naslov), "\n".join(items)))

    opoz = "\n".join("    <li>%s</li>" % e(x) for x in V.OPOZORILA)
    body = """
<h1>Viri</h1>
<p class="lead">Vsi podatki na teh straneh izhajajo iz spodaj navedenih javnih virov. Dostop do vseh
povezav: {dostop}.</p>
{sekcije}
<h2 class="sect">Opozorila</h2>
<div class="panel">
  <ul>
{opoz}
  </ul>
</div>
""".format(dostop=e(V.DOSTOP), sekcije="\n".join(sekcije), opoz=opoz)
    return page("Viri – Logatec 2026", body, "viri.html",
                "Seznam vseh virov za pregled kandidatov in list v občini Logatec 2026.")


# --------------------------------------------------------------------- pisanje
def pis(fn, text):
    with open(os.path.join(ROOT, fn), "w", encoding="utf-8") as f:
        f.write(text)
    print("  %-42s %6d B" % (fn, len(text.encode("utf-8"))))


def main():
    print("Generiram strani ...")
    pis("index.html", stran_index())
    pis("zupani.html", stran_zupani())
    pis("liste.html", stran_liste())
    pis("kandidati.html", stran_kandidati())
    pis("krajevne-skupnosti.html", stran_ks())
    pis("metodologija.html", stran_metodologija())
    pis("viri.html", stran_viri())
    for z in D.ZUPANI:
        pis("zupan-%s.html" % z["id"], stran_zupan(z))
    for l in D.LISTE:
        pis("lista-%s.html" % l["id"], stran_lista(l))
    print("Končano.")


if __name__ == "__main__":
    main()
