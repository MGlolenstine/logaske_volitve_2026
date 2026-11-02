# -*- coding: utf-8 -*-
"""Vsebina za statično stran o lokalnih volitvah 2026 v občini Logatec.

Podatki o kandidatih so strojno prebrani iz uradnega izvoza DVK
(data/obcine-kandidati/kandidati_064.json). Vsebina o programih in
dosežkih je ročno povzeta iz virov, navedenih v viri.py.
"""

DAN_VOLITEV = "15. november 2026"
DAN_DRUGEGA_KROGA = "29. november 2026"
DATUM_PODATKOV = "2. november 2026"
OBDOBJE_KAMPANJE = "16. oktober – 13. november 2026"

# ---------------------------------------------------------------- volilne enote
VOLILNE_ENOTE = {
    "01": {
        "naziv": "1. volilna enota",
        "opis": "Krajevne skupnosti Naklo in Ograje",
        "naselja": "Logatec (del), Kalce, Grčarevec, Hleviše",
    },
    "02": {
        "naziv": "2. volilna enota",
        "opis": "Krajevne skupnosti Tabor, Laze-Jakovica in Grčarevec",
        "naselja": "Logatec (del), Laze, Jakovica, Tabor",
    },
    "03": {
        "naziv": "3. volilna enota",
        "opis": "Krajevne skupnosti Rovte, Hotedršica, Trate, Vrh Sv. Treh Kraljev in Log-Zaplana",
        "naselja": "Rovte, Hotedršica, Zaplana, Vrh Sv. Treh Kraljev, Trate, Novi Svet, Medvedje Brdo",
    },
}

# ------------------------------------------------------------------- županski
# Besedila so povzeta po virih; oznaka "samoocena" pomeni navedbo kandidata.
ZUPANI = [
    {
        "id": "klemen-trpin",
        "ime": "Klemen Trpin",
        "sifra": "1",
        "letnik": "1988",
        "predlagatelj": "Naša Notranjska – NaNo; Slovenska demokratska stranka",
        "lista_id": "nasa-notranjska",
        "povzetek": "Kandidat Naše Notranjske, podprt tudi s strani občinskega odbora SDS Logatec. "
                    "V programu poudarja odzivnost občine, prometno ureditev, prostore za mlade in "
                    "pregledno porabo denarja.",
        "biografija": [
            "Prihaja iz Hotedršice, letnik 1988. Po lastnih navedbah je več kot 24 let vključen v "
            "družbeno življenje občine – v gasilstvu, mladinskih organizacijah, kulturi, športu in turizmu.",
            "14 let delovnih izkušenj v gospodarstvu, predvsem pri razvoju programske opreme za "
            "testiranje elektronskih in elektromehanskih izdelkov.",
            "Po lastnih navedbah 12 let v občinskem svetu (trije mandati), v zadnjem mandatu dve leti "
            "podžupan Občine Logatec, osem let na čelu Športne zveze Logatec.",
            "Navaja tudi članstvo v Izvršnem odboru Športne unije Slovenije in v Disciplinski komisiji "
            "Olimpijskega komiteja Slovenije – Združenja športnih zvez.",
        ],
        "preverjeno": [
            "Na lokalnih volitvah 2022 je bil izvoljen za občinskega svetnika v 3. volilni enoti "
            "z 35 glasovi na listi Naša Notranjska (uradni izid DVK/OVK).",
            "Na volitvah za župana 2022 je prejel 819 glasov oziroma 14,2 % in se ni uvrstil v drugi krog.",
            "Na volitvah 2026 je nosilec liste Naše Notranjske v 3. volilni enoti in prvi na glasovnici "
            "za župana.",
        ],
        "samoocena": [
            "Dve leti opravljanja funkcije podžupana in 12 let svetniškega dela (navedba kandidata; "
            "obcan.si navaja izvolitev 2022, funkcije podžupana ne potrjuje).",
            "Vodenje Športne zveze Logatec, počitniško varstvo za več kot 300 otrok letno in "
            "organizacija Dneva logaškega športa (navedbe kandidata in liste).",
        ],
    },
    {
        "id": "david-kogovsek",
        "ime": "mag. David Kogovšek",
        "sifra": "2",
        "letnik": "1977",
        "predlagatelj": "Jože Leskovec in skupina volivcev (Neodvisna lista Davida Kogovška)",
        "lista_id": "neodvisna-lista-davida-kogovska",
        "povzetek": "Neodvisni kandidat s programom »Moj Logatec«. Poudarja izkušnje pri vodenju "
                    "investicij, povezovalno cesto med obrtnima conama in enakomeren razvoj vseh "
                    "krajevnih skupnosti.",
        "biografija": [
            "Letnik 1977, iz Logatca. Po izobrazbi magistrant; večino kariere je gradil v "
            "telekomunikacijah (Telekom Slovenije), kjer je bil med drugim direktor prodaje poslovnim "
            "uporabnikom za osrednjo Slovenijo in nato zaposlen v nabavi.",
            "Od 1. novembra 2025 je zaposlen v Občini Logatec kot vodja investicij, kjer pripravlja in "
            "vodi občinske investicije (vir: Logaške novice, 5. 2. 2026).",
            "Predsednik sveta zavoda Knjižnica Logatec.",
            "V intervjuju februarja 2026 je dejal, da političnih ambicij takrat nima; kandidaturo za "
            "župana je javno napovedal septembra 2026.",
        ],
        "preverjeno": [
            "Zaposlen je v občinski upravi Občine Logatec kot vodja investicij od 1. 11. 2025 "
            "(Logaške novice, 5. 2. 2026, in njegov življenjepis).",
            "Na volitvah 2026 je drugi na glasovnici za župana in nosilec svoje liste v 1. volilni enoti.",
            "Lista je v občini Logatec nova; na lokalnih volitvah 2022 ni nastopila.",
        ],
        "samoocena": [
            "Vodenje in dokončanje kanalizacijskega sistema v Hotedršici (vrednost okoli 5 mio EUR) "
            "ter pridobitev okoli 1 mio EUR evropskih sredstev (navedba kandidata).",
            "Izkušnje pri gradnji optičnega omrežja, podatkovnih središč, omrežja IP/MPLS in mobilnega "
            "omrežja 5G (navedba kandidata).",
        ],
    },
    {
        "id": "matevz-podjed",
        "ime": "Matevž Podjed",
        "sifra": "3",
        "letnik": "1980",
        "predlagatelj": "Katja Stražiščar in skupina volivcev (Občanska lista Logatec)",
        "lista_id": "obcanska-lista-logatec",
        "povzetek": "Kandidat Občanske liste Logatec, ki je bila po volitvah 2022 največja svetniška "
                    "skupina. Poudarja vodenje razvojnih projektov in črpanje evropskih sredstev.",
        "biografija": [
            "Letnik 1980, Logatčan z Martinj hriba. Po izobrazbi sociolog in kadrovski menedžer.",
            "Skoraj desetletje je deloval kot novinar in urednik na RTV Slovenija.",
            "Po lastnih navedbah skoraj 15 let vodi ustanove: kot direktor Notranjskega parka naj bi "
            "ustanova pridobila več kot 15 milijonov evrov evropskih sredstev in prejela več nagrad; "
            "leta 2024 je prevzel vodenje Zavoda za ribištvo Slovenije.",
            "V prostem času nekdanji gimnastični državni prvak in odbojkar.",
        ],
        "preverjeno": [
            "Na lokalnih volitvah 2022 je bil v 1. volilni enoti izvoljen za občinskega svetnika s "
            "100 glasovi – največ med vsemi kandidati v tej volilni enoti (uradni izid DVK/OVK).",
            "Občanska lista Logatec je 2022 dobila 6 od 21 mandatov in je bila največja svetniška skupina.",
            "Na volitvah 2026 je tretji na glasovnici za župana in nosilec svoje liste v 1. volilni enoti.",
        ],
        "samoocena": [
            "Pridobitev več kot 15 milijonov evrov evropskih sredstev v Notranjskem parku in "
            "stabilizacija Zavoda za ribištvo Slovenije (navedbe kandidata).",
        ],
    },
]

# ---------------------------------------------------------------------- liste
LISTE = [
    {
        "id": "demokrati",
        "naziv": "DEMOKRATI. ANŽETA LOGARJA",
        "kratko": "Demokrati",
        "sifra": "1",
        "predlagatelj": "stranka Demokrati",
        "zupan": None,
        "povzetek": "Stranka v občini Logatec na lokalnih volitvah nastopa prvič. Program je "
                    "objavljala po posameznih ukrepih na družbenih omrežjih; skupno vodilo je "
                    "»Kompas uspešnosti«.",
        "program": {
            "naslov": "Program: ukrepi, objavljeni v kampanji",
            "stanje": "da",
            "uvod": "Demokrati so program objavljali po posameznih ukrepih na Instagramu in "
                    "Facebooku (oktober 2026). Skupno vodilo je »Kompas uspešnosti« – javni pregled "
                    "občinskih ciljev in rezultatov v aplikaciji Logatec Supermesto. Slogan liste je "
                    "»Sodelovanje. Odgovornost. Razvoj.« oziroma »Manj obljub. Več konkretnih "
                    "rešitev.«",
            "sklopi": [
                {"naslov": "1. Kompas uspešnosti – javni pregled dela občine", "tocke": [
                    "Javni pregled občinskih ciljev, projektov in rezultatov, vključen v aplikacijo "
                    "Logatec Supermesto.",
                    "Spremljanje ciljev na področju stanovanj, gospodarstva, infrastrukture, mladih, "
                    "športa, kulture in drugih javnih storitev.",
                    "Projekti in investicije: načrtovana vrednost, pogodbena cena, dosedanja poraba "
                    "in odgovorni za izvedbo.",
                    "Roki in napredek: kaj je narejeno, kaj je v teku in kaj zamuja – z "
                    "obrazložitvijo; javno naj bi bili vidni tudi zamiki in neizpolnjene obljube.",
                    "Obljube krajevnim skupnostim in spremljanje reševanja pobud občanov.",
                    "»Vsak cilj mora imeti rok. Vsak rok mora imeti odgovornost. In vsak rezultat "
                    "mora biti javno preverljiv.«",
                ]},
                {"naslov": "2. Občina kot dober gospodar (racionalizacija)", "tocke": [
                    "Celovit pregled občinskih nepremičnin, stroškov in delovanja občine.",
                    "Ugotoviti, katere nepremičnine občina potrebuje, katere bi lahko bolje "
                    "izkoristila in katere bi bilo smiselno oddati ali prodati.",
                    "Pregled pogodb in obratovalnih stroškov ter iskanje možnosti za cenejše skupne "
                    "nabave z drugimi občinami.",
                    "Preveriti, ali se posamezne naloge podvajajo, in iskati učinkovitejšo "
                    "organizacijo dela.",
                    "Aktivnejše iskanje sredstev države in Evropske unije.",
                    "Objava navaja: »Po 16 letih istega župana je prav, da pregledamo, kako stvari "
                    "delujejo danes.«",
                ]},
                {"naslov": "3. Več dostopnih stanovanj", "tocke": [
                    "Občina ima približno 50 neprofitnih stanovanj, kar po oceni liste ne zadošča.",
                    "Pregled obstoječih stanovanj: stanje, zasedenost, stroški in prihodnje potrebe.",
                    "Postopna prodaja izbranih stanovanj v centru, vendar samo tam, kjer je to "
                    "strokovno, finančno in pravno smiselno; pravice sedanjih najemnikov morajo biti "
                    "spoštovane.",
                    "Gradnja več dostopnih stanovanj po krajevnih skupnostih, tudi na podeželju.",
                    "Del kupnine naj bi ostal namenjen stanovanjski politiki – subvencijam najemnin "
                    "in drugim zakonsko dopustnim oblikam stanovanjske pomoči.",
                ]},
                {"naslov": "4. Gospodarski razvoj", "tocke": [
                    "»Logatec Fast Track« – ena kontaktna točka za investitorje.",
                    "»Logatec Invest« – aktivno iskanje novih investitorjev in boljši pregled nad "
                    "poslovnimi zemljišči.",
                    "Razvojne spodbude: preveritev možnosti olajšav pri komunalnem prispevku in "
                    "drugih spodbud, kjer so smiselne in izvedljive.",
                ]},
                {"naslov": "5. Močnejše krajevne skupnosti", "tocke": [
                    "Več neposredno razpoložljivih sredstev za krajevne skupnosti.",
                    "Nadaljnje povečevanje participativnega proračuna.",
                    "Periodična srečanja župana s predstavniki krajevnih skupnosti.",
                    "Pregledna merila za razdelitev sredstev (potrebe krajev, število prebivalcev, "
                    "stanje infrastrukture) – cilj ni enak znesek za vsak kraj, ampak utemeljene in "
                    "pregledne odločitve.",
                    "Spremljanje obljub posamezni krajevni skupnosti v Kompasu uspešnosti.",
                ]},
                {"naslov": "6. Sodelovanje s sosednjimi občinami", "tocke": [
                    "Skupne nabave in storitve za boljše pogoje in nižje stroške.",
                    "Skupna projektna pisarna za evropska sredstva.",
                    "Skupen nastop do države pri pomembnih vprašanjih.",
                    "Povezovanje gospodarstva in turizma v širši regiji.",
                    "Boljša mobilnost: usklajevanje avtobusnih in železniških povezav ter šolskih "
                    "prevozov.",
                ]},
                {"naslov": "7. Kultura, šport in turizem", "tocke": [
                    "Postopna vzpostavitev javnega zavoda za kulturo, šport in turizem.",
                    "Zavod bi začel z majhno ekipo; število zaposlenih bi se povečevalo skladno z "
                    "obsegom projektov in zagotovljenimi sredstvi.",
                    "Upravljanje kulturnih in športnih objektov bi sprva ostalo občini.",
                    "Povezovanje turističnih ponudnikov in društev, skupni koledar dogodkov in "
                    "usklajena promocija; turizem je prva prednostna naloga.",
                    "Podpora kulturnim ustvarjalcem in društvom, sodelovanje s športno zvezo in "
                    "klubi ter pomoč pri pripravi projektov za evropske in državne razpise.",
                ]},
                {"naslov": "8. Aktivni mladi", "tocke": [
                    "Uvedba občinskih štipendij za aktivne mlade, s ciljem najmanj 10 štipendij "
                    "letno.",
                    "Upoštevanje prispevka lokalni skupnosti: delo v društvih, klubih, kulturnih in "
                    "prostovoljskih projektih, pomoč starejšim in socialno ogroženim.",
                    "Jasna in javno objavljena merila ter enake možnosti za mlade iz vseh krajev "
                    "občine.",
                ]},
                {"naslov": "9. Prostor za mlade, društva in šport", "tocke": [
                    "Vzpostavitev dialoga z Vlado Republike Slovenije in pristojnimi institucijami o "
                    "uporabi posameznih prostorov nekdanje vojašnice za potrebe mladih, športa in "
                    "rekreacije ter društev.",
                ]},
            ],
            "vir": "Objave Demokratov Logatec na Instagramu in Facebooku, oktober 2026",
        },
        "mandat": {
            "naslov": "Mandat 2022–2026",
            "stanje": "brez",
            "opomba": "Stranka v občinskem svetu Občine Logatec v mandatu 2022–2026 ni imela "
                      "svetnikov, zato svojega mandata ni mogla opisati.",
            "samoocena": [],
        },
        "preverjeno": [
            "Lista v občini Logatec nima primerljive liste iz leta 2022.",
            "Predsednik stranke Anže Logar je iz Logatca. Na državnozborskih volitvah marca 2026 je bil "
            "v okraju Logatec izvoljen za poslanca, lista Demokrati pa je v občini Logatec prejela "
            "8,29 % glasov (podatek Logaških novic, 25. 3. 2026).",
        ],
    },
    {
        "id": "obcanska-lista-logatec",
        "naziv": "OBČANSKA LISTA LOGATEC",
        "kratko": "Občanska lista Logatec",
        "sifra": "2",
        "predlagatelj": "skupina volivcev (Katja Stražiščar)",
        "zupan": "matevz-podjed",
        "povzetek": "Največja svetniška skupina v mandatu 2022–2026 s šestimi od 21 svetnikov. "
                    "Za župana kandidira Matevž Podjed.",
        "program": {
            "naslov": "Logatec – več kot dom",
            "stanje": "da",
            "uvod": "Program temelji na petih stebrih. Lista poudarja, da Logatec lahko postane občina "
                    "z najvišjo kakovostjo bivanja v državi.",
            "sklopi": [
                {"naslov": "1. Premišljen infrastrukturni razvoj", "tocke": [
                    "Živo mestno središče: celostna ureditev središča od pokopališča do Tržaške in od "
                    "Narodnega doma do Tuša; srce naj bo mestni trg.",
                    "Nov gasilski dom v Dolenjem Logatcu kot kritična infrastruktura, ki naj se začne takoj.",
                    "Telovadnici pri OŠ Rovte in OŠ Tabor.",
                    "Kolesarske povezave (Kalce–Grčarevec–Hotedršica, Logatec–Rovte, Martinj Hrib–Laze) "
                    "s pomočjo evropskih sredstev.",
                    "Vodovod in kanalizacija povsod, kjer te infrastrukture še ni.",
                    "Prenova Narodnega doma že v prvem mandatu.",
                    "Šole, vrtci in zdravstvo: dolgoročna politika selitve novo grajenih javnih ustanov "
                    "na obrobje mesta.",
                    "Infrastruktura v vaseh in zaselkih, začenši s pločniki v Rovtah in Lazah.",
                    "Športni park Sekirica: sanacija nogometnega stadiona in nato celovito urejanje "
                    "parka, tudi smučarsko tekaška in skakalna infrastruktura.",
                    "Infrastruktura za razvoj obrti in podjetništva.",
                    "Stanovanja za prihodnost: občinski stanovanjski program in dostopna najemna "
                    "stanovanja za mlade, družine in ključne kadre.",
                ]},
                {"naslov": "2. Živahno družabno in kulturno življenje za vse generacije", "tocke": [
                    "Narodni dom naj po prenovi postane osrednja kulturna hiša za vsa logaška društva.",
                    "Celovita prenova in posodobitev knjižnice.",
                    "Mestno središče s trgom kot osrednji prostor druženja skozi vse leto.",
                    "Podpora društvom po logaških vaseh.",
                    "Vzpostavitev Mladinskega centra Logatec.",
                    "Programi, ki povezujejo generacije, in boljša podpora društvom ter ustvarjalcem.",
                    "Sodelovanje s festivali in partnerji, skupni koledar dogajanja.",
                    "Prostori za neformalno druženje.",
                ]},
                {"naslov": "3. Več evropskih sredstev za razvoj Logatca", "tocke": [
                    "Občinska projektna pisarna iz obstoječih zaposlenih.",
                    "Zunanji mentor in usposabljanje zaposlenih za delo z evropskimi programi.",
                    "Razpisna mapa in pravočasno pripravljeni projekti.",
                    "Partnerstva doma in v Evropi.",
                    "Merljiv cilj: vsako leto evropska sredstva za najmanj en občinski projekt, do "
                    "leta 2030 vsaj en projekt v skupni vrednosti najmanj pet milijonov evrov.",
                ]},
                {"naslov": "4. Živo in povezano logaško podeželje (»Logaško podeželje 2040«)", "tocke": [
                    "Srečanja župana, občinske uprave in predstavnikov krajevnih skupnosti najmanj "
                    "vsake tri mesece; kontaktna oseba za vsako skupnost.",
                    "Vključevanje prebivalcev v pripravo rešitev in strokovna podpora lokalnim "
                    "predstavnikom.",
                    "Uravnotežen razvoj, investicije presojane po varnosti, dostopnosti in razvojnem "
                    "zaostanku.",
                    "»Logaška hrana na logaške mize«: lokalna hrana v šole in vrtce ter trgovina "
                    "Logatčanka.",
                    "Mobilna upravna pisarna enkrat mesečno po vaseh.",
                    "Subvencije za mlade družine, ki obnovijo in naselijo starejši prazni objekt.",
                    "Butični turizem in mreža kolesarskih ter pohodnih poti.",
                    "Uporaba domačega lesa pri javnih gradnjah, energetske skupnosti.",
                ]},
                {"naslov": "5. Podjetništvo, obrtništvo in turizem kot temelj razvoja", "tocke": [
                    "Povezane in urejene poslovne cone s skupnim razvojnim načrtom.",
                    "Podjetniški center in inkubator s subvencionirano najemnino in coworking prostorom.",
                    "Enotna podporna točka za podjetnike.",
                    "»Logaški gospodarski forum« in skupna znamka »Ustvarjeno v Logatcu«.",
                    "Privabljanje podjetij z višjo dodano vrednostjo prek investicijskega kataloga.",
                    "Povezovanje šol, podjetij in drugih ustanov pri praksah, štipendijah in mentorstvu.",
                    "Boljša prometna dostopnost poslovnih con in digitalna infrastruktura.",
                    "Butični in trajnostni turizem v povezavi s sosednjimi notranjskimi občinami.",
                ]},
            ],
            "vir": "oll.si/program (Občanska lista Logatec)",
        },
        "mandat": {
            "naslov": "Mandat 2022–2026",
            "stanje": "da",
            "preverjeno": [
                "Na volitvah 2022 je lista dobila 6 od 21 mandatov in postala največja svetniška "
                "skupina: v 1. volilni enoti 29,9 %, v 2. 28,8 %, v 3. 14,9 % glasov.",
                "Svetniki v mandatu 2022–2026: Matevž Podjed, Katja Stražiščar, Luka Loštrek, "
                "Ana Kermavnar Marinšek, Bogdan Lipovšek, Davor Loštrek.",
            ],
            "samoocena": [
                "Lista navaja, da je v mandatu na občinski svet in vodstvo občine podala vrsto "
                "konkretnih pobud (na svoji strani objavlja več kot 18 pobud) – od prostorskega "
                "načrtovanja in komunalne infrastrukture do športa, otroškega varstva, preglednosti "
                "javnega naročanja in črpanja evropskih sredstev.",
                "V svojem poročilu o mandatu (Logaške novice, julij 2026) je skupina mandat ocenila "
                "kritično: da je bila kljub volilnemu uspehu odrinjena v opozicijo, da obsežnejše "
                "investicije niso bile uresničene in da je občinsko upravo zapustilo več strokovnih "
                "kadrov; kot ključen predlog navaja ustanovitev strateškega sveta in pisarne za "
                "pridobivanje državnih in evropskih sredstev.",
            ],
            "vir": "Logaške novice, julij 2026 (prispevek Luka Loštrek); oll.si/mandat-2022-2026",
        },
        "preverjeno": [],
    },
    {
        "id": "nasa-notranjska",
        "naziv": "NAŠA NOTRANJSKA",
        "kratko": "Naša Notranjska (NaNo)",
        "sifra": "3",
        "predlagatelj": "Naša Notranjska",
        "zupan": "klemen-trpin",
        "povzetek": "Za župana kandidira Klemen Trpin, ki ga podpira tudi občinski odbor SDS Logatec. "
                    "Program ima 7 področij in 53 ukrepov.",
        "program": {
            "naslov": "Volilni program za razvojno, povezano in odzivno občino",
            "stanje": "da",
            "uvod": "Program navaja 7 programskih področij, 53 konkretnih ukrepov in 9 ukrepov v prvih "
                    "100 dneh. Temeljna zaveza: »Poslušali bomo ljudi in dokončali projekte, ki jih "
                    "Logatec potrebuje.«",
            "sklopi": [
                {"naslov": "1. Občina, ki posluša in odgovarja", "tocke": [
                    "Redne mesečne odprte ure župana brez predhodnega naročanja.",
                    "Krajevni zbori in srečanja vodstva občine po vseh krajevnih skupnostih.",
                    "Enotna digitalna platforma za pobude, vprašanja in prijave težav s sledenjem fazi "
                    "obravnave.",
                    "Jasni roki za odgovore občinske uprave in letno javno poročilo o pobudah.",
                    "Participativni proračun.",
                ]},
                {"naslov": "2. Prometni načrt Logatec 2030", "tocke": [
                    "Ureditev prometa in parkiranja v centru.",
                    "Boljši dostop do železniške postaje in več parkirnih mest za dnevne migrante.",
                    "Določitev nevarnih prometnih točk in postopno urejanje manjkajočih pločnikov ter "
                    "varnih šolskih poti.",
                    "Kolesarske povezave med naselji s črpanjem evropskih sredstev.",
                    "Nadzor tranzitnega in težkega tovornega prometa po lokalnih cestah.",
                    "Izboljšanje javnega prevoza in povezav z železniško postajo.",
                ]},
                {"naslov": "3. Logatec potrebuje živo srce mesta", "tocke": [
                    "Gradnja Narodnega doma v sedanjih okoliščinah po oceni liste ni realno izvedljiva, "
                    "zato razvoj kulturnega življenja ne bi bil vezan na en sam objekt.",
                    "Celovit program kulturnih, družabnih in medgeneracijskih vsebin.",
                    "Boljša uporaba in povezovanje obstoječih kulturnih in društvenih prostorov.",
                    "Oživljanje središča z prireditvami, razstavami, koncerti in delavnicami.",
                    "Pregleden sistem podpore lokalnim kulturnim pobudam.",
                ]},
                {"naslov": "4. Logatec, prijazen mladim in družinam", "tocke": [
                    "Mladinski center oziroma prostor za organizirano druženje mladih.",
                    "Več celoletnih kulturnih, športnih in ustvarjalnih programov.",
                    "Vzdrževanje in posodabljanje otroških in športnih igrišč.",
                    "Varna pot do šol, vrtcev, športnih objektov in postajališč.",
                    "Sodelovanje občine pri stanovanjih za mlade in mlade družine.",
                    "Počitniške aktivnosti in vključevanje mladih v odločanje (projekt Mladi župan).",
                ]},
                {"naslov": "5. Pregledna občina in jasna komunikacija", "tocke": [
                    "Pregleden spletni prikaz vseh večjih občinskih projektov z vrednostmi, roki, viri "
                    "financiranja in stanjem izvedbe.",
                    "Razumljivi povzetki občinskega proračuna.",
                    "Redno obveščanje o zaporah in gradbiščih ter neposredno obveščanje krajevnih skupnosti.",
                    "Javno poročanje župana o izpolnjevanju volilnega programa.",
                ]},
                {"naslov": "6. Uravnotežen razvoj vseh krajevnih skupnosti", "tocke": [
                    "Prednostni seznam lokalnih potreb: ceste in pločniki, varne šolske poti, vodovod in "
                    "kanalizacija, javna razsvetljava, športne in družabne površine, prometna varnost.",
                    "Krepitev mreže avtobusnih postaj in razmislek o obnovitvi železniške postaje Laze.",
                    "Urejanje in vzdrževanje javnih površin.",
                ]},
                {"naslov": "7. Ohranimo tisto, kar je v Logatcu dobro", "tocke": [
                    "Varovanje naravnega okolja in prepoznavne krajine.",
                    "Ohranjanje visoke ravni osnovnega zdravstva in boljša dostopnost storitev.",
                    "Trajnostni razvoj in premišljeno prostorsko načrtovanje.",
                    "Razvoj športa in rekreacije.",
                    "Podpora lokalnim podjetnikom, obrtnikom, kmetijam in novim delovnim mestom.",
                ]},
                {"naslov": "Prvih 100 dni (9 ukrepov)", "tocke": [
                    "Redne odprte ure župana in sistem spremljanja pobud občanov.",
                    "Začetek srečanj po vseh krajevnih skupnostih.",
                    "Posodabljanje prometne strategije Logatec 2030.",
                    "Javna predstavitev stanja projekta Narodnega doma.",
                    "Pregled vseh večjih občinskih projektov z vrednostmi in roki.",
                    "Pospešitev gradnje gasilskega doma Dolnji Logatec.",
                    "Seznam najnujnejših prometnih in infrastrukturnih ukrepov.",
                    "Koledar rednega javnega poročanja o delu občine.",
                ]},
            ],
            "nacin_dela": [
                "Vsak večji projekt mora imeti jasen cilj, odgovornega nosilca, realno oceno stroškov, "
                "opredeljene vire financiranja, časovnico izvedbe in javno dostopno poročilo o napredku.",
            ],
            "vir": "nasanotranjska.si/obcina/logatec (program) in oglas v Logaških novicah, oktober 2026",
        },
        "mandat": {
            "naslov": "Mandat 2022–2026",
            "stanje": "da",
            "preverjeno": [
                "Na volitvah 2022 je lista dobila 3 mandate: Klemen Stoševski in Irena Vidic v 1. "
                "volilni enoti ter Klemen Trpin v 3. volilni enoti.",
            ],
            "samoocena": [
                "Skupina navaja tri svetnike, več kot 95-odstotno prisotnost na sejah ter en "
                "predsedniški in dva podpredsedniška mandata v delovnih telesih.",
                "Irena Vidic: zavzemanje za odgovorno ravnanje z javnimi sredstvi, nasprotovanje "
                "nakupu dodatnih radarjev, razprava o javnem potniškem prometu in umeščanju sončnih "
                "elektrarn (navedba liste).",
                "Klemen Stoševski: kot predsednik Mladinskega sveta Logatec sodelovanje pri Strategiji "
                "za mlade, subvencija za prvo stanovanjsko vprašanje mladih, odkup objekta na "
                "Kettejevem vrtu za Mladinski center Logatec (navedba liste).",
                "Klemen Trpin: izgradnja enote Vrtca Kurirček, kanalizacija v Hotedršici, druga faza "
                "Športnega parka Sekirica, obnove športnih igrišč in dvoran, počitniško varstvo, "
                "Dan logaškega športa in Praznično kolo Logatca (navedba liste).",
            ],
            "vir": "Logaške novice, julij 2026 (prispevek Irene Vidic, Klemna Stoševskega in Klemna Trpina)",
        },
        "preverjeno": [],
    },
    {
        "id": "sds",
        "naziv": "SLOVENSKA DEMOKRATSKA STRANKA",
        "kratko": "SDS",
        "sifra": "4",
        "predlagatelj": "SDS",
        "zupan": None,
        "podpira_zupana": "klemen-trpin",
        "povzetek": "SDS v občini Logatec ne kandidira za župana, ampak javno podpira Klemna Trpina "
                    "(Naša Notranjska). V oglasu poudarja investicijski cikel v družbeno infrastrukturo.",
        "program": {
            "naslov": "Program: konkretni cilji in zavezništvo z Našo Notranjsko",
            "stanje": "da",
            "uvod": "SDS Logatec je 24. oktobra 2026 na Facebooku objavila, da program temelji na "
                    "konkretnih ciljih. V oglasu v Logaških novicah (oktober 2026) stranka dodaja "
                    "programske zaveze in podporo Klemnu Trpinu za župana; podrobnejši predvolilni "
                    "nagovor je bil dostavljen v gospodinjstva in ni objavljen na spletu.",
            "sklopi": [
                {"naslov": "Cilji programa (objava SDS Logatec, 24. 10. 2026)", "tocke": [
                    "Boljša infrastruktura.",
                    "Podpora mladim družinam.",
                    "Razvoj gospodarstva.",
                    "Skrb za starejše.",
                    "Varnost.",
                    "Izgradnja kritične infrastrukture.",
                    "Kakovostno življenje v vseh krajevnih skupnostih občine Logatec.",
                ]},
                {"naslov": "Zaveze iz oglasa v Logaških novicah (oktober 2026)", "tocke": [
                    "»Logatcu bomo vdihnili novo življenje, zagnali bomo investicijski cikel v "
                    "prepotrebno družbeno infrastrukturo.«",
                    "»Športnih površin je premalo.«",
                    "»Z velikimi prostorskimi težavami se soočajo gasilci v Dolenjem Logatcu.«",
                    "»Potrebujemo tudi projekt premestitve centralne knjižnice.«",
                ]},
                {"naslov": "Zavezništvo z Našo Notranjsko", "tocke": [
                    "SDS Logatec in Naša Notranjska – Logatec skupaj podpirata Klemna Trpina za "
                    "župana pod geslom »Zavezništvo za več posluha, več razvoja in več Logatca«.",
                    "Na glasovnici je SDS lista številka 4.",
                ]},
            ],
            "vir": "Objava SDS Logatec na Facebooku, 24. 10. 2026; Logaške novice, oktober 2026 "
                   "(oglas SDS Logatec)",
        },
        "mandat": {
            "naslov": "Mandat 2022–2026: »Mandat izgubljenih priložnosti«",
            "stanje": "da",
            "preverjeno": [
                "Na volitvah 2022 je SDS dobila 3 mandate: Zoran Mojškerc (1. volilna enota), "
                "Nevenka Kerezović (2. volilna enota) in Bogomir Jurca (3. volilna enota).",
                "Zoran Mojškerc je bil marca 2026 izvoljen za poslanca v državnem zboru v okraju "
                "Logatec; lista SDS je v občini Logatec prejela 28,93 % glasov (podatek Logaških "
                "novic, 25. 3. 2026).",
            ],
            "samoocena": [
                "Skupina svoj mandat opisuje kot »mandat izgubljenih priložnosti«: župan naj bi po "
                "njeni oceni sestavil in nato razpustil koalicijo, dogovori o Športnem parku Sekirica "
                "in novem gasilskem domu naj ne bi bili izvedeni (navedba liste).",
                "Kot dosežke navaja kanalizacijo v Hotedršici in modernizacijo več cest, kot "
                "neuresničeno pa povezovalno cesto med obrtnima conama (navedba liste).",
                "Navaja tudi, da so vseskozi zagovarjali večjo preglednost porabe javnega denarja in "
                "opozarjali na pomanjkanje osnovne infrastrukture (vodovod, cestna povezava) na "
                "podeželju (navedba liste).",
            ],
            "vir": "Logaške novice, julij 2026 (prispevek Zorana Mojškercka)",
        },
        "preverjeno": [],
    },
    {
        "id": "neodvisna-lista-davida-kogovska",
        "naziv": "NEODVISNA LISTA DAVIDA KOGOVŠKA",
        "kratko": "Neodvisna lista Davida Kogovška",
        "sifra": "5",
        "predlagatelj": "Jože Leskovec in skupina volivcev",
        "zupan": "david-kogovsek",
        "povzetek": "Nova lista, za župana kandidira mag. David Kogovšek s programom »Moj Logatec«. "
                    "Poudarek na infrastrukturi, gospodarstvu in enakomernem razvoju vseh krajevnih "
                    "skupnosti.",
        "program": {
            "naslov": "Moj Logatec",
            "stanje": "da",
            "uvod": "Program je razdeljen na 6 prioritet in 7 področij s konkretnimi ukrepi, "
                    "dopolnjuje pa ga program po krajevnih skupnostih. Lista navaja, da je program "
                    "delovni dokument, ki ga dopolnjujejo na zborih krajanov.",
            "sklopi": [
                {"naslov": "6 prioritet", "tocke": [
                    "Urejen Logatec: ceste, pločniki, kanalizacija, vodovodi, javna razsvetljava in "
                    "varne povezave.",
                    "Močno gospodarstvo: boljši pogoji za podjetnike in obrtnike, razvoj industrijskih "
                    "con in povezovalna cesta – nova delovna mesta.",
                    "Mladi in družine: poenostavitev stanovanjske gradnje, finančna podpora mladim "
                    "družinam, vlaganja v vrtce, šole, mladinski center in šport.",
                    "Vsak kraj šteje: pravičen razvoj vseh desetih krajevnih skupnosti.",
                    "Ljudje in kakovost življenja: zdravstvo, pomoč starejšim, društva, gasilstvo, "
                    "kultura, šport in programi za ranljive skupine.",
                    "Občina, ki posluša: odprta, hitra in pregledna uprava, več odločanja skupaj z "
                    "zbori krajanov in krajevnimi skupnostmi.",
                ]},
                {"naslov": "1. Infrastruktura, promet in komunala", "tocke": [
                    "Sistematična obnova cest in pločnikov po javno objavljenem večletnem načrtu.",
                    "Asfalt do vsake hiše, kjer bodo lastniki prenesli lastništvo parcele ceste na "
                    "občino in pripravili spodnji ustroj.",
                    "Nadaljevanje širitve kanalizacijskega omrežja izven mesta Logatec.",
                    "Kolesarske povezave med naselji in varna pot do šol.",
                    "Dogovor z Direkcijo za vode o obnovi zadrževalnika Reka in čiščenju vodotokov.",
                    "Javna razsvetljava po enotnih, energetsko varčnih standardih.",
                    "Boljša ureditev parkirišč v središču in ob zaposlitvenih conah.",
                    "Zavzemanje za boljše javne prevozne povezave.",
                ]},
                {"naslov": "2. Gospodarstvo, podjetništvo in zaposlovanje", "tocke": [
                    "Komunalno opremljanje obeh industrijskih con (Logatec, Zapolje).",
                    "Poenostavitev in pohitritev občinskih postopkov za podjetnike, obrtnike in kmete.",
                    "Podpora lokalnim obrtnikom in promocija lokalne ponudbe (»Kupujmo Logaško«).",
                    "Razvoj turistične ponudbe in vzpostavitev TIC-a.",
                    "Spodbujanje mladinskega podjetništva in sodelovanja s šolami ter univerzo.",
                ]},
                {"naslov": "3. Okolje in trajnostni razvoj", "tocke": [
                    "Zaščita Planinskega polja, Rovtarskega hribovja in Hotedršice pred neustreznimi posegi.",
                    "Spodbujanje lesne biomase in obnovljivih virov, širitev plinovodnega omrežja.",
                    "Sanacija in nadgradnja centralne čistilne naprave ter boljše ravnanje z odpadki.",
                    "Selitev predelave blata iz čistilne naprave izven mesta.",
                    "Ohranjanje kmetijskih zemljišč in podpora lokalnim kmetom.",
                ]},
                {"naslov": "4. Mladi, izobraževanje in družine", "tocke": [
                    "Zadostne kapacitete vrtcev in osnovnih šol v vseh delih občine, vključno z "
                    "glasbeno šolo.",
                    "Zagotovitev srednjih poklicnih šol v Logatcu.",
                    "Podpora mladim družinam pri prvem stanovanjskem vprašanju.",
                    "Obšolske in obštudijske dejavnosti, mladinski center in prostori za druženje "
                    "(Cankarjeva ulica).",
                ]},
                {"naslov": "5. Šport, kultura in društva", "tocke": [
                    "Vzdrževanje in nadgradnja športnih igrišč in dvoran v mestu in po krajevnih "
                    "skupnostih.",
                    "Redno in pravočasno sofinanciranje športnih, kulturnih in gasilskih društev po "
                    "jasnih merilih.",
                    "Podpora prireditvam, ki gradijo skupnost (praznik občine, prireditve v KS).",
                    "Ohranjanje kulturne dediščine in podpora društvom pri urejanju spomenikov, "
                    "cerkva in vaških jeder.",
                ]},
                {"naslov": "6. Zdravstvo in socialna skrb", "tocke": [
                    "Krepitev Zdravstvenega doma Logatec in prizadevanje za dodatne specialistične "
                    "ambulante.",
                    "Podpora domovom za starejše in razvoj pomoči na domu po vseh krajevnih skupnostih.",
                    "Socialni program za ranljive skupine.",
                    "Povečanje obsega prevozov za starejše.",
                ]},
                {"naslov": "7. Pregledna in odzivna občinska uprava", "tocke": [
                    "Redna javna poročila o porabi proračuna, razumljiva vsakemu občanu.",
                    "Digitalizacija občinskih storitev.",
                    "Najmanj letni zbori krajanov v vsaki krajevni skupnosti.",
                    "Okrepitev vloge svetov krajevnih skupnosti pri odločanju o lokalnih projektih.",
                ]},
            ],
            "vir": "mojlogatec.org/program.html (Moj Logatec)",
        },
        "mandat": {
            "naslov": "Mandat 2022–2026",
            "stanje": "brez",
            "opomba": "Lista je nova; na volitvah 2022 v občini Logatec ni nastopila, zato svojega "
                      "mandata nima. Posamezni kandidati so v občinskem svetu sedeli na drugih listah "
                      "(glej oznake pri kandidatih).",
            "samoocena": [],
        },
        "preverjeno": [
            "Lista v občini Logatec nima primerljive liste iz leta 2022.",
            "Nosilec liste in županski kandidat mag. David Kogovšek je od 1. 11. 2025 zaposlen v "
            "občinski upravi Občine Logatec kot vodja investicij.",
            "Na listi je tudi Sabina Kurent, ki je bila v mandatu 2022–2026 občinska svetnica na listi "
            "Neodvisna lista Berto Menard.",
        ],
    },
    {
        "id": "gibanje-svoboda",
        "naziv": "GIBANJE SVOBODA",
        "kratko": "Gibanje Svoboda",
        "sifra": "6",
        "predlagatelj": "Gibanje Svoboda",
        "zupan": None,
        "povzetek": "Stranka v Logatcu ne kandidira za župana. Program za lokalne volitve obsega pet "
                    "konkretnih projektov.",
        "program": {
            "naslov": "Program za lokalne volitve 2026: »Za več življenja v Logatcu«",
            "stanje": "da",
            "uvod": "Program v oglasu in v poročilu o mandatu navaja pet ključnih projektov.",
            "sklopi": [
                {"naslov": "Pet ključnih projektov", "tocke": [
                    "Celovita ureditev območja Logaščice in Jačke: dolgoročna rešitev in prestavitev "
                    "centralne čistilne naprave, nadaljevanje protipoplavnih ukrepov, ureditev ponora "
                    "Jačke ter pešpot ob vodotoku Logaščica.",
                    "Prenova Kulturnega doma Logatec ter ustanovitev Zavoda za kulturo, šport in "
                    "turizem Logatec.",
                    "Dokončanje in oživitev Športnega parka Sekirica kot večnamenskega prostora za "
                    "šport, rekreacijo in druženje vseh generacij.",
                    "Nov gasilski dom PGD Dolnji Logatec.",
                    "Povezava obeh obrtnih con in celostna ureditev območja zaradi razvoja gospodarstva "
                    "in prometne razbremenitve središča Logatca.",
                ]},
                {"naslov": "Dodatni poudarki iz poročila o mandatu", "tocke": [
                    "Ustanovitev Zavoda za kulturo, šport in turizem Logatec za usklajen razvoj "
                    "dogodkov skozi vse leto.",
                    "Strokovno vzdržen projekt za novi kulturni dom in več sredstev na javnih razpisih "
                    "za društva z večletnim financiranjem.",
                    "Urbanistična zasnova osrednjega mestnega trga s parkovnimi površinami, urbano "
                    "opremo, otroškimi igrali, pokritim prostorom za tržnico in večnamenskim prostorom "
                    "za koncerte ter poletni kino.",
                    "Dolgoročna rešitev za umestitev centralne čistilne naprave izven strnjenega naselja.",
                    "Projektna dokumentacija za novo športno dvorano pri OŠ Tabor, načrt širitve šolskih "
                    "kapacitet in začetek postopkov za umestitev nove osnovne šole.",
                    "Sodelovanje z ministrstvom, šolami in gospodarstvom za razvoj srednješolskih "
                    "programov v Logatcu.",
                ]},
            ],
            "vir": "Logaške novice, oktober 2026 (oglas) in avgust 2026 (poročilo o mandatu)",
        },
        "mandat": {
            "naslov": "Mandat 2022–2026: »Za vizijo in strategijo ter več življenja v Logatcu«",
            "stanje": "da",
            "preverjeno": [
                "Na volitvah 2022 je Gibanje Svoboda dobilo 3 mandate: Angela Menart in Primož "
                "Godina v 1. volilni enoti ter Ivan Pergovnik v 2. volilni enoti.",
                "Poslanka Gibanje Svoboda iz okraja Logatec je Tereza Novak, izvoljena marca 2026; "
                "stranka je v občini Logatec prejela 25,64 % glasov (podatek Logaških novic, "
                "25. 3. 2026).",
            ],
            "samoocena": [
                "Skupina navaja, da je bila pobudnica celovitega strateškega načrtovanja občine; "
                "občasno delovno telo je vodila Monika Rudolf, za pripravo strategije pa naj bi "
                "zagotovili zunanjega izvajalca in financiranje (navedba liste).",
                "Kot dosežek navaja protipoplavno varnost: izgradnjo suhega zadrževalnika Črni Potok, "
                "ki naj bi bil uvrščen v državni načrt razvojnih programov (navedba liste).",
                "Navaja, da se veliko pomembnih investicij, zlasti Narodni dom, v mandatu ni izvedlo "
                "(navedba liste).",
            ],
            "vir": "Logaške novice, avgust 2026 (poročilo svetniške skupine Gibanje Svoboda)",
        },
        "preverjeno": [],
    },
    {
        "id": "nsi",
        "naziv": "NOVA SLOVENIJA – KRŠČANSKI DEMOKRATI",
        "kratko": "NSi",
        "sifra": "7",
        "predlagatelj": "NSi",
        "zupan": None,
        "povzetek": "Stranka v Logatcu ne kandidira za župana. Program ima tri krovne stebre in "
                    "program TOP 10; v berljivi obliki je objavljen le del programskih točk.",
        "program": {
            "naslov": "Program: trije krovni stebri in program TOP 10",
            "stanje": "delno",
            "opomba": "NSi Logatec navaja, da ima program tri krovne stebre in konkretne rešitve v "
                      "programu TOP 10, ki jih predstavlja na pogovornih večerih (Rovte, 3. 11. 2026, "
                      "in Hotedršica, 6. 11. 2026) in v objavah na družbenih omrežjih. Celotnega "
                      "seznama TOP 10 v berljivi obliki nismo našli; spodnje točke so tiste, ki so "
                      "objavljene v njihovih objavah in v prispevku v Logaških novicah (julij 2026). "
                      "Gre za navedbe stranke same.",
            "navedki": [
                "Strateški svet za gospodarski in družbeni napredek občine Logatec: ustanovitev "
                "krovnega posvetovalnega in strokovnega telesa s predstavniki gospodarstva, "
                "kmetijstva, šolstva, zdravstva, sociale, krajevnih skupnosti, športa in kulture, "
                "kot neformalnega posvetovalnega telesa občinskega sveta in župana. Cilj naj bi bilo "
                "uravnoteženo razporejanje občinskih investicij in dvig družbenega ter socialnega "
                "standarda vseh krajev.",
                "Infrastruktura v mestu in na podeželju: prednostna izgradnja nove športne "
                "telovadnice pri OŠ Tabor v Gornjem Logatcu, dokončanje in posodobitev športne "
                "infrastrukture v Športnem parku Sekirica ter ureditev varnih šolskih poti s "
                "pločniki do vseh šol v občini.",
                "Mladi: aktivno soustvarjanje naslednje Strategije za mlade in vključevanje mladih v "
                "lokalno upravljanje; občina je od leta 2023 nosilka naziva Mladim prijazna občina.",
                "Ključno vodilo naj bo konstruktivna politika namesto blokad; strokovnost naj bo pred "
                "politiko.",
                "Enakomerna in pravična porazdelitev proračunskega denarja po vseh delih občine.",
                "Nujna gradnja novega kulturnega središča, ki bi rešilo dotrajani Narodni dom in "
                "prostorsko stisko Knjižnice Logatec; sredstva v proračunu za širitev vrtcev in šol "
                "ter urejanje varnih šolskih poti.",
                "Podpora športu kot prostočasni dejavnosti, dostopni čim širšemu krogu otrok.",
                "Stabilno socialno varstvo v občini, zlasti programi pomoči in oskrbe na domu za "
                "starejše.",
                "Kakovostna delovna mesta z visoko dodano vrednostjo in pogoji za tehnološko "
                "napredna podjetja.",
                "Vključitev novih prostorov za knjižnico, Narodnega doma in gospodarskega dviga "
                "podeželja v novo Strategijo občine Logatec 2026–2036.",
                "Bolj neposredna vključitev krajevnih skupnosti v oblikovanje participativnega "
                "proračuna in v odločanje občinskega sveta.",
            ],
            "vir": "Objave NSi Logatec na Instagramu in Facebooku (oktober–november 2026); "
                   "Logaške novice, julij 2026 (okrogla miza NSi Logatec)",
        },
        "mandat": {
            "naslov": "Mandat 2022–2026: »Konstruktivno delovanje za skladen razvoj Logatca«",
            "stanje": "da",
            "preverjeno": [
                "Na volitvah 2022 je NSi dobila 2 mandata: dr. Bojan Doljak (1. volilna enota) in "
                "Rafael Cepič (3. volilna enota).",
            ],
            "samoocena": [
                "Skupina navaja, da je na njeno pobudo stekel politični dialog, ki je omogočil "
                "nadaljevanje in zaključek izgradnje kanalizacije v Hotedršici (navedba liste).",
                "Navaja, da je prek široke podpore uspelo povečati sredstva za participativni "
                "proračun (navedba liste).",
                "Svetnik Marko Kržišnik se je delu občinskega sveta pridružil sredi mandata "
                "(nadomestni mandat); ob koncu mandata je bil član Odbora za gospodarstvo, "
                "kmetijstvo, turizem in finance (navedba liste).",
            ],
            "vir": "Logaške novice, julij 2026 (prispevek NSi Logatec)",
        },
        "preverjeno": [],
    },
]

# ---------------------------------------------- 2022: izvoljeni občinski svetniki
SVETNIKI_2022 = {
    "Matevž Podjed", "Katja Stražiščar", "Luka Loštrek", "Ana Kermavnar Marinšek",
    "Bogdan Lipovšek", "Davor Loštrek",
    "Sabina Kurent", "Florijan Masle", "Boštjan Mivšek",
    "Angela Menart", "Primož Godina", "Ivan Pergovnik",
    "Klemen Stoševski", "Irena Vidic", "Klemen Trpin",
    "Zoran Mojškerc", "Nevenka Kerezović", "Bogomir Jurca",
    "Bojan Doljak", "Rafael Cepič",
}

# Naslovi, ki jih uradni izvoz DVK ne vsebuje, so povzeti po objavah obcan.si in
# spletnih strani list. Uporabljajo se samo za prikaz imena.
NASLOVI = {
    "Bojan Doljak": "dr.",
    "Anže Zorman": "dr. med.",
    "Mojca Kumin Horvat": "dr.",
    "Jure Smole": "dr.",
    "Katarina Turk": "dr. med.",
    "Ana Kermavnar Marinšek": "dr. med.",
    "Anton Velušček": "dr.",
    "David Kogovšek": "mag.",
    "Boštjan Zajec": "dr.",
}

# Kratki opisi kandidatov, kjer jih je lista objavila (samo NaNo in OLL).
OPISI_KANDIDATOV = {
    # Naša Notranjska – naziv/poklic po navedbi liste
    "Irena Vidic": "Pravnica, mediatorka in operativna direktorica podjetja.",
    "Aljoša Peček": "Vodja projektov in diplomirani ekonomist.",
    "Nives Varga": "Zavarovalna zastopnica in prostovoljka.",
    "Ožbej Istenič": "Vzdrževalec v proizvodnji in prostovoljec.",
    "Alenka Veber": "Podjetnica.",
    "Miha Bošnjak": "Prostovoljni gasilec in komunalni delavec.",
    "Diana Ivančič Šumer": "Asistentka v prodaji.",
    "Anže Zorman": "Zdravnik in član KS Naklo.",
    "Miha Klopčič": "Strokovni sodelavec za cenitve avtomobilskih škod in član komisije za "
                    "preprečevanje zavarovalniških prevar.",
    "Jernej Osterman": "Vodja oddelka in predsednik Turistično-kulturnega-športnega društva "
                       "Grčarevec.",
    "Vita Nagode": "Diplomirana medicinska sestra.",
    "Blaž Kranjc": "Podjetnik, predsednik KS Tabor in govedorejskega društva.",
    "Mojca Kumin Horvat": "Doktorica jezikoslovnih znanosti.",
    "Nejc Klevišar": "Razvojni inženir in član KS Tabor.",
    "Anja Turk": "Poročna in družinska fotografinja.",
    "Petja Škrubej": "Učiteljica in umetnica.",
    "Jure Berzelak": "Podjetnik in predsednik KS Rovte.",
    "Aleksander Rupnik": "Prostovoljni gasilec, član KS Hotedršica in samostojni podjetnik.",
    "Klemen Trpin": "Kandidat Naše Notranjske za župana in nosilec liste v 3. volilni enoti; "
                    "občinski svetnik v mandatu 2022–2026.",
    # Občanska lista Logatec – poklic in lastna izjava kandidata
    "Matevž Podjed": "Direktor Zavoda za ribištvo. »Logatec je v preteklih dveh desetletjih povsem "
                     "obstal. Kandidiram za župana, ker verjamem, da je s celovito prenovo načina "
                     "vodenja občine možno narediti hitre in velike korake naprej.«",
    "Katja Stražiščar": "Pravnica, državna uradnica. »Želim, da bi občina svoje delo opravljala "
                        "strokovno, transparentno, učinkovito in gospodarno.«",
    "Luka Loštrek": "Profesor glasbe. »Ponosen sem, da sem del skupine ljudi, ki je v logaški "
                    "občini okrepila zavedanje o razvojnih pomanjkljivostih našega okolja in hkrati "
                    "ponudila konstruktivno vizijo prihodnosti.«",
    "Zala Jereb": "Vodja projektov in organizatorka dogodkov. »Kot nekdanja predsednica Kluba "
                  "logaških študentov dobro vem, kako pomemben je utrip našega kraja.«",
    "Tomaž Lukančič": "Magister ekonomije, diplomirani inženir strojništva. »Moja velika želja je, "
                      "da Logatec postane razvita občina z urejenim in prepoznavnim središčem mesta.«",
    "Laura Kores": "Profesorica glasbe, ustvarjalka digitalnih vsebin. »Želim si Logatca, ki diha z "
                   "ljudmi, ponuja priložnosti za razvoj in povezuje skupnost.«",
    "Jure Smole": "Razvoj strateških trgov. »Moj cilj je Logatec, v katerem bodo ljudje radi živeli, "
                  "delali in ustvarjali.«",
    "Andreja Smiljanić": "Samostojna podjetnica. »Sem podjetnica, ki verjame, da največ štejejo "
                         "dejanja, odgovornost in odnos do ljudi.«",
    "Vid Hrovatin": "Študent. »Zavzemal se bom za aktivno mladinsko politiko, šport in raznoliko "
                    "lokalno dogajanje.«",
    "Katarina Turk": "Dr. med., specialistka splošne medicine. »Zavzemam se za podporo in širitev "
                     "stabilne zdravstvene in socialne oskrbe.«",
    "Tadej de Gleria": "Profesor športne vzgoje, ravnatelj. »Logatec si zasluži pravo strategijo "
                       "razvoja mesta in naših lepih okoliških zaselkov.«",
    "Jana Jureš": "Upokojena učiteljica. »Delujem v okviru Univerze za tretje življenjsko obdobje "
                  "Logatec, kjer vodim tematske sprehode po Logatcu in okolici.«",
    "Sonja Vidonja": "Ekonomistka in diplomirana sociologinja, podjetnica. »Več kot deset let sem "
                     "bila predsednica TSK Logatec.«",
    "Bogdan Lipovšek": "Upokojenec. »Logaško občino je potrebno vrniti občankam in občanom, da bodo "
                       "pri načrtovanju prihodnosti vključeni v sprejemanje pomembnih odločitev.«",
    "Ana Kermavnar Marinšek": "Zdravnica. »Želim prispevati k zdravemu in varnemu bivalnemu okolju "
                              "za vse občane naše občine.«",
    "Anže Šemrov": "Glasbenik. »Kot glasbenik verjamem, da kultura povezuje ljudi in daje kraju "
                   "dušo.«",
    "Milojka Rupnik": "Upokojena učiteljica. »Polovico svoje delovne dobe sem opravila na OŠ Tabor, "
                      "Logatec.«",
    "Lovro Nagode": "Zdravstveni reševalec. »Menim, da Logatec potrebuje skupen prostor za "
                    "medgeneracijsko druženje in povezovanje.«",
    "Davor Loštrek": "Profesor glasbe, ravnatelj. »Dialog in sodelovanje sta vrednoti, s katerima "
                     "me je OLL prepričala, da lahko skupaj gradimo in oblikujemo prihodnost.«",
    "Špela Moroz": "Družboslovna informatičarka. »V domačem kraju želim soustvarjati še naprej, se "
                   "zavzemati za zmanjševanje razkoraka med stopnjo razvitosti krajev občine.«",
    "Simon Corn": "Operater. »Menim, da je čas za svež veter in stojim za vizijo, ki jo ponuja naša "
                  "Občanska lista Logatec.«",
    "Urška Leskovec": "Vzgojiteljica. »Matevža podpiram, ker verjamem vanj in vem, da mu zastavljene "
                      "cilje uspe doseči.«",
    "Boštjan Čuk": "Samostojni podjetnik. »Zavzemal se bom predvsem za kvaliteto bivanja v občini.«",
}

# ------------------------------------------------------------------- 2022 izid
IZID_2022 = {
    "udelezba_1": "51,6 % (5.774 od 11.186 volilnih upravičencev)",
    "udelezba_2": "48,3 % (5.409 od 11.190)",
    "zupan_1": [
        ("Berto Menard", "DOMEN MENARD IN SKUPINA VOLIVCEV", "2.248", "39,1 %"),
        ("Bogdan Lipovšek", "KATJA STRAŽIŠČAR IN SKUPINA VOLIVCEV", "1.808", "31,4 %"),
        ("Klemen Trpin", "NAŠA NOTRANJSKA", "819", "14,2 %"),
        ("Zoran Mojškerc", "SLOVENSKA DEMOKRATSKA STRANKA", "503", "8,7 %"),
        ("Aljoša Peček", "SOCIALNI DEMOKRATI", "371", "6,5 %"),
    ],
    "zupan_2": [
        ("Berto Menard", "izvoljen", "2.747", "50,9 %"),
        ("Bogdan Lipovšek", "", "2.648", "49,1 %"),
    ],
    "svet": [
        ("OBČANSKA LISTA LOGATEC 2030", "838 / 408 / 214", "29,9 / 28,8 / 14,9 %", "6"),
        ("NEODVISNA LISTA BERTO MENARD", "497 / 272 / 324", "17,8 / 19,2 / 22,6 %", "4"),
        ("GIBANJE SVOBODA", "454 / 239 / 91", "16,2 / 16,9 / 6,4 %", "3"),
        ("NAŠA NOTRANJSKA", "279 / 159 / 241", "10,0 / 11,2 / 16,8 %", "3"),
        ("SLOVENSKA DEMOKRATSKA STRANKA", "322 / 176 / 276", "11,5 / 12,4 / 19,3 %", "3"),
        ("NOVA SLOVENIJA – KRŠČANSKI DEMOKRATI", "222 / 162 / 248", "7,9 / 11,4 / 17,3 %", "2"),
        ("SOCIALNI DEMOKRATI", "186 / – / 39", "6,6 / – / 2,7 %", "0"),
    ],
}
