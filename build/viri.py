# -*- coding: utf-8 -*-
"""Seznam virov z dnevi dostopa."""

DOSTOP = "2. november 2026"

# (kategorija, naziv, url, kaj dokazuje / opombe)
VIRI = [
    ("Primarni viri – uradni podatki", [
        ("Državna volilna komisija – Lokalne volitve 2026 (uradni izvoz kandidatov za občino Logatec)",
         "https://volitve.dvk-rs.si/lv2026/data/obcine-kandidati/kandidati_064.json",
         "Uradni seznam vseh kandidatov: županski kandidati (3), kandidati za občinski svet (129) "
         "in kandidati za svete ožjih delov (89). Iz tega izvoza so povzeta imena, letnice rojstva, "
         "volilne enote, predlagatelji in vrstni red na glasovnici."),
        ("Državna volilna komisija – Lokalne volitve 2026 (uvodna stran)",
         "https://volitve.dvk-rs.si/lv2026/",
         "Nadrejeni vir uradnih podatkov o volitvah 15. novembra 2026."),
        ("DVK/OVK – uradni izid lokalnih volitev 2022 v občini Logatec",
         "https://www.dvk-rs.si/arhivi/volitve2022/lv2022/data/prvikrog/obcine-data/data_064.json",
         "Uradni izidi 2022: udeležba, izid za župana v obeh krogih in izid za občinski svet z "
         "izvoljenimi svetniki."),
    ]),
    ("Izhodiščni vir (seznam kandidatov)", [
        ("obcan.si – Kandidati 2026 v občini Logatec",
         "https://obcan.si/obcina/logatec/kandidati",
         "Izhodiščni seznam kandidatov in list, iz katerega izhaja ta pregled. Podatki so označeni "
         "kot prevzeti od DVK 28. 10. 2026. Isti vir daje tudi povezave do posameznih oseb."),
        ("obcan.si – Občinski svet občine Logatec (sestava po izidu 2022)",
         "https://obcan.si/obcina/logatec/svet",
         "Sestava občinskega sveta 2022–2026 po listah in svetnikih."),
        ("obcan.si – Lokalne volitve 2022 v občini Logatec",
         "https://obcan.si/obcina/logatec/volitve/2022",
         "Podrobni uradni izidi 2022 po volilnih enotah in kandidatih."),
    ]),
    ("Programi in predstavitve list ter kandidatov", [
        ("Naša Notranjska – Občina Logatec (predstavitev, program, ekipa, novice)",
         "https://www.nasanotranjska.si/obcina/logatec",
         "Program za Logatec s 7 področji in 53 ukrepi, prvih 100 dni, predstavitev Klemna Trpina "
         "in ekipe kandidatov."),
        ("Neodvisna lista Davida Kogovška – program »Moj Logatec«",
         "https://mojlogatec.org/program.html",
         "Program po področjih in prioritetah; tudi ciljna vizija občine."),
        ("Neodvisna lista Davida Kogovška – predstavitev in življenjepis kandidata",
         "https://mojlogatec.org/kandidat.html",
         "Življenjepis mag. Davida Kogovška in razlogi za kandidaturo (navedbe kandidata)."),
        ("Občanska lista Logatec – program",
         "https://oll.si/program/",
         "Program s petimi stebri."),
        ("Občanska lista Logatec – kandidati za občinski svet",
         "https://oll.si/kandidati-za-obcinski-svet/",
         "Poklici in lastne izjave vseh 23 kandidatov liste."),
        ("Občanska lista Logatec – kandidat za župana Matevž Podjed",
         "https://oll.si/matevz-podjed-kandidat-za-zupana-logatca/",
         "Življenjepis in razvojni poudarki kandidata (navedbe liste)."),
        ("Občanska lista Logatec – mandat 2022–2026",
         "https://oll.si/mandat-2022-2026/",
         "Samoocena dela liste v občinskem svetu 2022–2026 in seznam pobud."),
    ]),
    ("Programi, objavljeni na družbenih omrežjih", [
        ("Demokrati Logatec – profil na Instagramu",
         "https://www.instagram.com/demokrati_logatec/",
         "Program po posameznih ukrepih, objavljen oktobra 2026: Kompas uspešnosti, "
         "racionalizacija občine, stanovanja, gospodarstvo, krajevne skupnosti, medobčinsko "
         "sodelovanje, kultura in šport, štipendije za mlade, prostori nekdanje vojašnice."),
        ("Demokrati Logatec – profil na Facebooku",
         "https://www.facebook.com/61570976491848/",
         "Isti ukrepi in napovedi srečanj z županskim kandidatom."),
        ("SDS Logatec – objava o programu (24. 10. 2026)",
         "https://www.facebook.com/sds.logatec/",
         "Program, ki temelji na konkretnih ciljih: boljša infrastruktura, podpora mladim "
         "družinam, razvoj gospodarstva, skrb za starejše, varnost, izgradnja kritične "
         "infrastrukture in kakovostno življenje v vseh krajevnih skupnostih. Profil vsebuje tudi "
         "objave o zavezništvu z Našo Notranjsko in podpori Klemnu Trpinu."),
        ("NSi Logatec – profil na Instagramu",
         "https://www.instagram.com/nsi_logatec/",
         "Programske objave: strateški svet za gospodarski in družbeni napredek občine, "
         "infrastruktura (telovadnica pri OŠ Tabor, Športni park Sekirica, varne šolske poti), "
         "mladi in Strategija za mlade; napoved programa s tremi krovnimi stebri in programom "
         "TOP 10."),
        ("NSi Logatec – profil na Facebooku",
         "https://www.facebook.com/prihodnostlogatca/",
         "Iste programske objave in vabila na pogovorne večere (Rovte 3. 11. 2026, "
         "Hotedršica 6. 11. 2026)."),
        ("obcan.si – Župani občine Logatec skozi čas",
         "https://obcan.si/obcina/logatec/zupani",
         "Izvoljeni župani po volitvah 2006, 2010, 2014, 2018 in 2022 (arhiv DVK)."),
    ]),
    ("Občinsko glasilo Logaške novice (oktober 2026 – volilni oglasi)",
        [
        ("Logaške novice, oktober 2026 (celotna številka, PDF)",
         "https://www.mojaobcina.si/e_izdaje/logatec/LN_10_2026_ZASPLET..pdf",
         "Volilni oglasi list: Demokrati, Neodvisna lista Davida Kogovška, SDS Logatec (s podporo "
         "Klemnu Trpinu), Občanska lista Logatec, Gibanje Svoboda in Naša Notranjska."),
        ("Logaške novice, julij 2026 (celotna številka, PDF)",
         "https://www.mojaobcina.si/e_izdaje/logatec/LN_07_2026_K8..pdf",
         "Poročila svetniških skupin o mandatu 2022–2026: NSi, Naša Notranjska, SDS, Neodvisna "
         "lista Berto Menard in Občanska lista Logatec."),
        ("Logaške novice, avgust 2026 (celotna številka, PDF)",
         "https://www.mojaobcina.si/e_izdaje/logatec/LN_09_2026_koncnaZASPLET..pdf",
         "Poročilo svetniške skupine Gibanje Svoboda o mandatu 2022–2026 in program za prihodnost."),
    ]),
    ("Lokalni mediji in drugo", [
        ("Logaške novice (spletni portal) – intervju z mag. Davidom Kogovškom",
         "https://logaske-novice.si/david-kogovsek-kljucne-bodo-tiste-investicije-ki-dolgorocno-"
         "izboljsujejo-kakovost-zivljenja-obcanov/",
         "Zaposlitev Davida Kogovška kot vodje investicij v Občini Logatec, opis projektov in "
         "takratna izjava, da nima političnih ambicij (5. 2. 2026)."),
        ("Logaške novice – volilni izid državnozborskih volitev 2026 v občini Logatec",
         "https://logaske-novice.si/volitve-v-drzavni-zbor-rs-na-logaskem-najvecja-podpora-listi-"
         "sds-z-zoranom-mojskercem",
         "Deleži list v občini Logatec na državnozborskih volitvah marca 2026."),
        ("Logaške novice – pravila o predstavitvi kandidatov v času kampanje 2026",
         "https://logaske-novice.si/pravila-o-izrabi-casopisnega-prostora-logaskih-novic-za-"
         "predstavitev-kandidatov-politicnih-strank-in-njihovih-programov-v-casu-volilne-kampanje-"
         "za-lokalne-volitve-2026-v-obcini-logatec/",
         "Pravila glasila o volilnih oglasih in predstavitvah v oktobrski številki."),
        ("Občina Logatec (uradna spletna stran)",
         "https://logatec.si/",
         "Uradne objave, proračun, projekti in informacije o volitvah."),
    ]),
    ("Za kontekst (kandidati, ki se pojavljajo v več virih)", [
        ("Kdo bo zmagal – Logatec (participativni barometer)",
         "https://logatec.emesto.si/kdobozmagal",
         "Pregled list in kandidatov; uporabljen le za navzkrižno preverjanje števila kandidatov. "
         "Barometer sam po sebi ni reprezentativna raziskava javnega mnenja."),
    ]),
]

OPOZORILA = [
    "Ta stran ni povezana z nobeno stranko, listo ali kandidatom in ni volilno propagandno sporočilo.",
    "Povzetki programov so skrajšani. Za celovito vsebino vedno glejte izvirni vir, povezan pri "
    "vsaki listi.",
    "Poročila svetniških skupin o mandatu 2022–2026 so njihove lastne navedbe; objavljena so bila v "
    "občinskem glasilu, vendar jih nismo neodvisno preverjali.",
    "Podatki o kandidatih so prevzeti iz uradnega izvoza DVK. Naslovov prebivališča kandidatov "
    "namerno ne objavljamo.",
    "Stanje podatkov: 2. november 2026. Volilna kampanja se je začela 16. oktobra 2026, zato se "
    "gradiva kandidatov in list še lahko dopolnjujejo.",
]
