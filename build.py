#!/usr/bin/env python3
# Generator voor kyrameubels.nl - onafhankelijke meubel- en interieurgids.
import os, json, html, hashlib
def _ver(p):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),p),'rb').read()).hexdigest()[:8]
    except Exception: return "1"
BASE="https://kyrameubels.nl"; SITE="Kyra Meubels"; EMAIL="info@kyrameubels.nl"
AUTEUR="Kyra Bosman"; AUTEUR_ROL="Interieurredacteur"
SRC=os.path.dirname(__file__); OUT=os.path.join(SRC,"site"); CSS_VER=_ver("assets/css/style.css")
def esc(s): return html.escape(str(s), quote=True)

IC={
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "sofa":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3"/><path d="M2 13a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5H2z"/><line x1="5" y1="18" x2="5" y2="21"/><line x1="19" y1="18" x2="19" y2="21"/></svg>',
 "tree":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 5 12h4l-4 6h14l-4-6h4z"/><line x1="12" y1="18" x2="12" y2="22"/></svg>',
 "brush":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l9-9 3 3-9 9z"/><path d="M9 12l-3 6 6-3z"/><path d="M4 20c1-2 3-2 4 0"/></svg>',
 "ruler":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="8" width="20" height="8" rx="2"/><line x1="7" y1="8" x2="7" y2="12"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="17" y1="8" x2="17" y2="12"/></svg>',
 "book":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7a3 3 0 0 1 3 3v13a2.5 2.5 0 0 0-2.5-2.5H4z"/><path d="M20 4h-3a3 3 0 0 0-3 3v13a2.5 2.5 0 0 1 2.5-2.5H20z"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}
NAV=[("Home","/"),("Materialen","/materialen/"),("Gidsen","/gidsen/"),("Nieuws","/nieuws/"),("Over","/over/"),("Contact","/contact/")]

def head(title,desc,path,ld=None):
    can=BASE+path
    j="".join('<script type="application/ld+json">'+json.dumps(b,ensure_ascii=False)+'</script>' for b in (ld or []))
    nav="".join(f'<a class="navlink" href="{h}">{esc(l)}</a>' for l,h in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website"><meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}"><meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{can}">
<meta name="theme-color" content="#1F4A47">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}
</head>
<body>
<header class="site-head"><nav class="nav" id="nav">
  <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Kyra Meubels</b><span>Interieurgids</span></span></a>
  {nav}
  <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
</nav></header>
"""

def footer():
    return f"""<footer class="foot"><div class="wrap">
  <div class="cols">
    <div><a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Kyra Meubels</b><span style="color:#89A09D">Interieurgids</span></span></a>
      <p class="note">Kyra Meubels is een onafhankelijke gids over meubels en interieur: materialen, onderhoud en inrichten. Het platform verkoopt geen meubels en is geen woonwinkel.</p></div>
    <div><h4>Ontdekken</h4><a href="/materialen/">Alle materialen</a><a href="/gidsen/">Gidsen</a><a href="/nieuws/">Nieuws</a><a href="/redactie/">Over de redactie</a></div>
    <div><h4>Informatie</h4><a href="/over/">Over dit platform</a><a href="/contact/">Contact</a><a href="/privacybeleid/">Privacybeleid</a><a href="/cookiebeleid/">Cookiebeleid</a></div>
  </div>
  <div class="foot-bottom"><span>&copy; 2026 {esc(SITE)}</span>
  <span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span></div>
</div></footer>
</body></html>"""

def crumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]}
def crumbs_html(items):
    o=[f'<a href="{u}">{esc(n)}</a>' for n,u in items[:-1]]; o.append(f'<span>{esc(items[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(o)+'</nav></div>'
def write(path,c):
    f=os.path.join(OUT,"index.html") if path=="/" else os.path.join(OUT,path.strip("/"),"index.html")
    os.makedirs(os.path.dirname(f),exist_ok=True); open(f,"w",encoding="utf-8").write(c)
def blocks(bs):
    o=[]
    for b in bs:
        if b[0]=="p": o.append(f"<p>{esc(b[1])}</p>")
        elif b[0]=="h2": o.append(f"<h2>{esc(b[1])}</h2>")
        elif b[0]=="ul": o.append("<ul>"+"".join(f"<li>{esc(x)}</li>" for x in b[1])+"</ul>")
        elif b[0]=="callout": o.append(f'<div class="callout"><p>{esc(b[1])}</p></div>')
        elif b[0]=="plink": o.append(f"<p>{b[1]}</p>")
    return "".join(o)
def byline():
    return f'<div class="byline"><img src="/assets/img/auteur.svg" alt="{esc(AUTEUR)}"><div class="who">{esc(AUTEUR)}<small>{esc(AUTEUR_ROL)}</small></div></div>'

MATERIALEN=[
 {"slug":"massief-eiken","naam":"Massief eiken","kind":"Hout","kleuren":["#C9A26B","#B08A50","#8E6C3A"],
  "resume":"Het meest gebruikte meubelhout in Nederland, herkenbaar aan de grove nerf en de neiging tot nadonkeren.",
  "specs":[("Hardheid","Hoog"),("Nerf","Grof, open"),("Kleurverloop","Donkert na"),("Onderhoud","Olie of lak")],
  "secties":[("Werken en krimpen","Massief hout blijft bewegen met de luchtvochtigheid. Een eikenhouten tafelblad kan in de winter enkele millimeters smaller worden dan in de zomer. Goede constructies houden daar rekening mee met zwaluwstaarten of slobgaten; een blad dat strak vastgeschroefd zit, scheurt op termijn."),
   ("Geolied of gelakt","Olie trekt in het hout, laat de nerf voelbaar en is plaatselijk bij te werken. Lak legt een laag over het hout, is beter bestand tegen vocht en vlekken, maar een beschadiging is alleen te herstellen door het hele blad te schuren. De keuze bepaalt vooral hoeveel onderhoud er in de jaren daarna volgt."),
   ("Europees en Amerikaans","Europees eiken heeft doorgaans een levendiger tekening met meer noesten, Amerikaans eiken is gelijkmatiger en lichter van toon. Het prijsverschil komt vooral voort uit beschikbaarheid en de mate van uitsortering.")],
  "punten":["Beweegt mee met de luchtvochtigheid","Geolied is bij te werken, gelakt niet plaatselijk","Donkert na onder invloed van licht","Zware constructie, houd rekening met gewicht"]},
 {"slug":"notenhout","naam":"Notenhout","kind":"Hout","kleuren":["#6B4A33","#8A6448","#4E3626"],
  "resume":"Donker, fijn van nerf en aanzienlijk duurder dan eiken, met een kleur die juist lichter wordt in plaats van donkerder.",
  "specs":[("Hardheid","Middelhoog"),("Nerf","Fijn, gesloten"),("Kleurverloop","Vervaagt"),("Onderhoud","Olie")],
  "secties":[("Lichter in plaats van donkerder","Waar eiken nadonkert, verbleekt noten juist onder invloed van zonlicht. Een blad dat jarenlang half onder een kleed of vaas staat, laat dat verschil zien. Regelmatig verplaatsen van voorwerpen voorkomt vlekpatronen."),
   ("Waarom de prijs hoger ligt","Notenbomen groeien langzamer en leveren minder bruikbaar stamhout op dan eiken. Daarbij is de kleurvariatie binnen een stam groot, waardoor er meer moet worden uitgesorteerd om een gelijkmatig blad te maken."),
   ("Fineer en massief","Vanwege de prijs wordt noten vaak als fineer toegepast op een plaatmateriaal. Dat is niet per definitie minder: fineer werkt minder en blijft vlakker. Wel is schuren maar beperkt mogelijk, omdat de fineerlaag dun is.")],
  "punten":["Verbleekt onder zonlicht","Fijne, gelijkmatige tekening","Vaak toegepast als fineer","Hogere prijs door langzame groei"]},
 {"slug":"leer","naam":"Leer","kind":"Bekleding","kleuren":["#8B5E3C","#A9764F","#5F4028"],
  "resume":"Een bekleding die met de jaren mooier wordt, mits het om de juiste soort gaat en het onderhoud klopt.",
  "specs":[("Soorten","Anilin, gepigmenteerd"),("Slijtage","Zeer goed"),("Vlekken","Afhankelijk van finish"),("Onderhoud","Voeden")],
  "secties":[("Anilineleer en gepigmenteerd leer","Anilineleer is doorgeverfd en houdt de natuurlijke structuur zichtbaar. Het voelt zacht, krijgt patina, maar neemt vlekken makkelijk op. Gepigmenteerd leer heeft een dekkende toplaag: minder karakter, veel beter bestand tegen vlekken en zonlicht. Voor een bank met kinderen of huisdieren is dat verschil doorslaggevend."),
   ("Split en nerfleer","Nerfleer is de bovenste laag van de huid en het sterkst. Split komt uit de onderliggende lagen en wordt vaak van een kunststof toplaag voorzien. Dat oogt bij aankoop vergelijkbaar, maar slijt sneller door en laat op termijn los."),
   ("Voeden zonder overdrijven","Leer droogt uit door warmte en zonlicht, wat scheurtjes geeft. Twee keer per jaar voeden met een passend middel volstaat. Vaker of te veel middel maakt het oppervlak plakkerig en trekt juist vuil aan.")],
  "punten":["Anilin is mooier, gepigmenteerd is praktischer","Nerfleer gaat langer mee dan split","Uit de buurt van radiator en direct zonlicht","Twee keer per jaar voeden is genoeg"]},
 {"slug":"rotan-en-riet","naam":"Rotan en riet","kind":"Natuurlijk","kleuren":["#D9B98A","#C4A272","#E8D3AE"],
  "resume":"Licht, veerkrachtig vlechtwerk dat na jaren van afwezigheid weer volop in interieurs opduikt.",
  "specs":[("Gewicht","Laag"),("Vocht","Gevoelig"),("Herkomst","Zuidoost-Azië"),("Onderhoud","Stofzuigen")],
  "secties":[("Rotan, riet en bamboe","Rotan is een klimplant waarvan de stengel massief is en gebogen kan worden. Webbing of Weens vlechtwerk is het fijne rasterpatroon in kastdeuren en stoelruggen. Bamboe is hol en breekt eerder, en wordt daarom minder gebruikt voor draagconstructies."),
   ("Vocht is de zwakke plek","Te droge lucht maakt het vlechtwerk bros, te vochtige lucht laat het uitzetten en doorhangen. Een woonkamer met vloerverwarming en lage luchtvochtigheid vraagt om af en toe licht bevochtigen van het vlechtwerk, wat de veerkracht terugbrengt."),
   ("Doorgezakt vlechtwerk","Een doorgezakte zitting is vaak te herstellen door de onderzijde licht te bevochtigen en de zitting te laten drogen. Terugkerende doorzakking wijst op verzwakte vezels, waarbij vervanging van het vlechtwerk de enige duurzame oplossing is.")],
  "punten":["Licht en makkelijk te verplaatsen","Gevoelig voor extreem droge lucht","Vlechtwerk is te vervangen","Niet geschikt voor buiten"]},
 {"slug":"boucle-en-meubelstof","naam":"Bouclé en meubelstof","kind":"Bekleding","kleuren":["#E5DCCB","#CFC2AB","#B8A98F"],
  "resume":"De stofkeuze bepaalt meer over de levensduur van een bank dan het frame, en de cijfers op het label zeggen precies wat.",
  "specs":[("Slijtvastheid","Martindale"),("Bouclé","Lusstructuur"),("Vlekken","Behandeling"),("Onderhoud","Stofzuigen")],
  "secties":[("Wat het Martindale-getal betekent","Meubelstof wordt getest door er onder druk overheen te schuren tot slijtage zichtbaar wordt. Rond de vijftienduizend toeren is geschikt voor licht gebruik, vanaf ongeveer vijfentwintigduizend voor een bank die dagelijks gebruikt wordt. Hogere getallen zeggen iets over slijtvastheid, niet over hoe prettig een stof aanvoelt."),
   ("De keerzijde van bouclé","De lusstructuur geeft bouclé zijn typische uiterlijk, maar die lussen blijven haken achter nagels, ritsen en huisdierklauwen. Een uitgetrokken lus is niet te herstellen zonder dat het zichtbaar blijft. In een huishouden met katten is dat een reëel bezwaar."),
   ("Afneembare hoezen","Stoffen banken met afneembare hoezen zijn aanzienlijk makkelijker schoon te houden, omdat een enkel deel gewassen kan worden zonder de hele bank te behandelen. Wel is krimp bij wassen een aandachtspunt; het wasvoorschrift is hier geen formaliteit.")],
  "punten":["Martindale zegt iets over slijtvastheid","Bouclé is gevoelig voor haken","Afneembare hoezen schelen veel werk","Wasvoorschrift bepaalt de levensduur"]},
 {"slug":"metaal-in-meubels","naam":"Metaal in meubels","kind":"Constructie","kleuren":["#8E9296","#6D7276","#B4B8BB"],
  "resume":"Stalen frames en poten maken slanke constructies mogelijk, met roest en stabiliteit als aandachtspunten.",
  "specs":[("Materiaal","Staal, aluminium"),("Afwerking","Poedercoating"),("Roest","Bij beschadiging"),("Gewicht","Wisselend")],
  "secties":[("Poedercoating en de zwakke plek","De meeste stalen meubels zijn gepoedercoat: een gebakken laklaag die goed hecht en slijtvast is. Zolang die laag intact blijft, roest het staal niet. Een schilfer door een stoot of een schroef die door de laag heen gaat, is het punt waar corrosie begint."),
   ("Buis en massief","Meubels met dunne, slanke poten zijn meestal van buismateriaal in plaats van massief staal. Dat scheelt aanzienlijk in gewicht en prijs. De stevigheid zit in de verbinding en de wanddikte, niet in de diameter die zichtbaar is."),
   ("Aluminium en buiten","Aluminium roest niet en is licht, wat het geschikt maakt voor buitenmeubels. Wel is het zachter dan staal, waardoor het eerder deukt. Voor een tuinset weegt de weerbestendigheid meestal zwaarder dan die gevoeligheid.")],
  "punten":["Coating intact houden voorkomt roest","Stevigheid zit in de verbinding","Aluminium is licht maar zachter","Vilt onder poten spaart de vloer"]},
]
def mat(s): return next(x for x in MATERIALEN if x["slug"]==s)

GIDSEN=[
 {"slug":"meubels-onderhouden","titel":"Meubels onderhouden: wat per materiaal werkt","ic":"brush",
  "resume":"De meeste schade ontstaat door het verkeerde middel op het juiste moment. Per materiaal verschilt de aanpak sterk.",
  "body":[("p","Meubels gaan zelden kapot door gebruik. Ze verslijten door de verkeerde behandeling: een allesreiniger op geolied hout, een vochtige doek op vlechtwerk, of een bank pal naast de radiator."),
   ("h2","Hout"),("p","Geolied hout vraagt een droge of licht vochtige doek en een of twee keer per jaar een onderhoudsbeurt met dezelfde olie. Gelakt hout verdraagt een vochtige doek, maar geen schuurmiddel. Kringen op geolied hout zijn plaatselijk weg te schuren en bij te oliën; op gelakt hout niet."),
   ("h2","Leer"),("ul",["Stof wekelijks afnemen met een droge doek.","Twee keer per jaar voeden met een middel dat past bij het type leer.","Vlekken direct deppen, niet wrijven.","Nooit een oplosmiddel of allesreiniger gebruiken."]),
   ("h2","Stof"),("p","Regelmatig stofzuigen met een zachte borstel voorkomt dat vuil tussen de vezels schuurt, wat de belangrijkste oorzaak van slijtage is. Vlekken worden gedept van buiten naar binnen; wrijven duwt het vuil dieper de vezel in."),
   ("h2","Vlechtwerk"),("p","Stofzuigen met een borstelopzetstuk en incidenteel licht bevochtigen houdt rotan soepel. Doorweken is schadelijk: het vlechtwerk zet uit, droogt scheef en zakt door."),
   ("callout","Test elk nieuw middel eerst op een onopvallende plek, bijvoorbeeld de achterkant of onderzijde. Een verkleuring die daar ontstaat, valt niemand op."),
   ("h2","Waar meubels staan"),("p","Direct zonlicht laat hout verkleuren en leer uitdrogen. Een radiator vlak achter een bank versnelt datzelfde proces. Twintig centimeter afstand en een gordijn tegen de felste middagzon schelen jaren.")]},
 {"slug":"kleine-ruimte-inrichten","titel":"Een kleine ruimte inrichten zonder dat het vol oogt","ic":"ruler",
  "resume":"Kleinere meubels zijn zelden de oplossing. Zichtlijnen, hoogte en pootruimte doen meer.",
  "body":[("p","De eerste reflex bij een kleine kamer is alles kleiner kopen. Dat werkt vaak averechts: veel kleine meubels geven meer visuele drukte dan een paar goed gekozen stukken."),
   ("h2","Zichtlijnen vrijhouden"),("p","Een ruimte oogt groter zolang de vloer en de wanden doorlopen in het zicht. Meubels op pootjes laten de vloer eronder zien en maken een kamer optisch ruimer dan kasten die tot de grond doorlopen, ook bij hetzelfde volume."),
   ("h2","De hoogte gebruiken"),("ul",["Kasten tot aan het plafond in plaats van halfhoog, met de bovenste planken voor spullen die zelden nodig zijn.","Wandplanken boven deuropeningen en in hoeken.","Hangende verlichting in plaats van een vloerlamp die ruimte inneemt."]),
   ("h2","Meubels die meer dan een ding doen"),("p","Een bank met bergruimte onder de zitting, een bijzettafel die als kruk dient, of een uitschuifbare tafel neemt in dagelijkse toestand weinig plaats in en levert op het moment dat het nodig is precies genoeg."),
   ("h2","Doorloop van zeventig centimeter"),("p","Een looppad tussen meubels wordt oncomfortabel onder ongeveer zeventig centimeter. Dat is een harde grens waar formaatkeuze op afgestemd hoort te worden, ongeacht hoe goed een bank verder past."),
   ("callout","Plak de omtrek van een meubel met schilderstape op de vloer voordat het besteld wordt. Dat laat direct zien of de doorloop klopt.")]},
]

ARTIKELEN=[
 {"slug":'eetkamerstoelen-slijtage-punten','titel':'Eetkamerstoelen: de punten die pas na een jaar opvallen',"cat":'Praktijk',"datum":'2026-08-19',"datum_nl":'19 augustus 2026','lees':5,
  'resume':'Comfort in de winkel zegt weinig over hoe een stoel zich houdt bij dagelijks gebruik.',
  "body":[
  ('p', 'Een eetkamerstoel wordt gekozen op uiterlijk en op vijf minuten zitten in een toonzaal. De punten die na een jaar bepalen of de keuze goed was, komen in die vijf minuten niet aan bod.'),
  ('h2', 'Waar slijtage begint'),
  ('p', 'De eerste plek is de voorrand van de zitting. Daar rust het gewicht bij het aanschuiven en daar schuurt de stof over het schuim. Bij een strak overtrokken zitting zonder extra versteviging is dat de plek waar de stof het eerst dun wordt.'),
  ('p', 'De tweede plek is de verbinding tussen poot en zitting. Een stoel wordt dagelijks een stukje verschoven, en die zijdelingse kracht komt volledig op die verbinding. Een houten frame met deuvels en lijm blijft steviger dan een verbinding die alleen op schroeven rust.'),
  ('h2', 'Stof en onderhoud'),
  ('ul', ['Geweven stof met een hoge schuurwaarde gaat langer mee dan een zachte velours.', 'Een afneembare hoes klinkt praktisch en zit na wassen zelden weer strak.', 'Bij een lichte kleur telt vlekbestendigheid zwaarder dan de kleurkeuze zelf.', 'Leer en kunstleer scheuren bij droge lucht, dus niet vlak bij een radiator zetten.']),
  ('plink', 'Voor een tafel waar dagelijks gegeten wordt, weegt schuurbestendigheid zwaarder dan zachtheid. Uitvoeringen die daarop zijn gebouwd staan bij <a href="https://vansoestliving.nl/collections/robuuste-eetkamerstoelen" rel="nofollow">Van Soest Living</a>.'),
  ('h2', 'Verhouding tot de tafel'),
  ('p', 'De maat die het vaakst wordt vergeten is de ruimte tussen zitting en tafelblad. Vijfentwintig tot dertig centimeter zit prettig; minder geeft klem zittende bovenbenen en bij stoelen met armleuning het probleem dat ze niet onder het blad passen.'),
  ('plink', 'Meet daarom niet alleen de tafelhoogte maar ook de dikte van het blad en de positie van een eventuele schort onder het blad. Bij een tafel tegen de wand of in een smalle ruimte scheelt een draaibare uitvoering bovendien de ruimte die anders nodig is om aan te schuiven; die modellen staan op <a href="https://vansoestliving.nl/collections/draaibare-eetkamerstoelen" rel="nofollow">vansoestliving.nl</a>.'),
  ('h2', 'Vloerbescherming'),
  ('p', 'Viltjes onder de poten zijn geen detail. Zonder viltjes komen er binnen een jaar krassen in een houten of gietvloer, en die zijn zichtbaarder dan de stoel zelf.'),
  ('p', 'Vervang ze bovendien voordat ze doorgesleten zijn. Een viltje dat op de spijker is versleten, kerft dieper dan helemaal geen viltje, omdat het gewicht dan op één punt komt.'),
  ('h2', 'Aantal en variatie'),
  ('p', 'Zes identieke stoelen rond een tafel is de gebruikelijke keuze en niet altijd de beste. Twee stoelen met armleuning aan de koppen en vier zonder geeft de tafel een duidelijke richting en biedt bovendien meer zitcomfort op de plekken waar het langst wordt gezeten.'),
  ('p', 'Houd bij een dergelijke combinatie wel dezelfde stof en pootkleur aan. Verschil in model werkt; verschil in materiaal maakt het geheel onrustig en dat effect wordt sterker naarmate de ruimte kleiner is.'),
 ]},
 {"slug":"waarom-massief-hout-werkt","titel":"Waarom massief hout blijft werken, ook na jaren","cat":"Materiaal","datum":"2026-07-14","datum_nl":"14 juli 2026","lees":4,
  "resume":"Een scheur in een tafelblad is zelden een fabricagefout. Vaak is het de luchtvochtigheid in huis.",
  "body":[("p","Massief hout blijft vocht opnemen en afgeven aan de lucht, ook decennia nadat de boom gekapt is. Dat is geen gebrek maar een eigenschap, en verklaart het grootste deel van de klachten over massieve tafels."),
   ("h2","Wat er precies gebeurt"),("p","Bij hoge luchtvochtigheid neemt hout vocht op en zet het uit, vooral in de breedte. Bij droge lucht krimpt het weer. Een blad van een meter breed kan over de seizoenen enkele millimeters verschillen. In de lengterichting is die beweging verwaarloosbaar."),
   ("h2","Waarom vloerverwarming meespeelt"),("p","Vloerverwarming en goede isolatie geven in de winter een lagere luchtvochtigheid dan vroeger gebruikelijk was. Waarden onder de dertig procent zijn niet uitzonderlijk, en dat is voor massief hout een zware belasting."),
   ("h2","Wat helpt"),("ul",["Luchtvochtigheid tussen ongeveer veertig en zestig procent houden.","Tafelbladen niet strak vastschroeven maar met slobgaten bevestigen.","Bladen niet pal boven een radiator of vloerverwarmingsverdeler plaatsen.","Bij een nieuwe tafel het hout eerst enkele weken laten acclimatiseren."])]},
 {"slug":"tweedehands-meubels-beoordelen","titel":"Tweedehands meubels beoordelen: waar op te letten","cat":"Praktijk","datum":"2026-06-26","datum_nl":"26 juni 2026","lees":4,
  "resume":"Constructie en verbindingen zeggen meer over de restlevensduur dan het uiterlijk van het oppervlak.",
  "body":[("p","Bij tweedehands meubels bepaalt de constructie of iets nog decennia meegaat. Oppervlakteschade is vaak te herstellen; een losse constructie meestal niet zonder flink werk."),
   ("h2","Verbindingen eerst"),("p","Wiebelen bij het optillen aan een hoek wijst op losse verbindingen. Bij gelijmde houtverbindingen is dat te herstellen, bij geniete plaatmateriaalconstructies zelden. Kijken onder en achter een meubel zegt in dertig seconden meer dan de voorkant."),
   ("h2","Plaatmateriaal en massief"),("ul",["Kijk naar de zijkant van een blad: een doorlopende nerf wijst op massief hout.","Fineer op spaanplaat is herkenbaar aan een randafwerking die anders loopt dan het vlak.","Opgezwollen randen bij spaanplaat betekenen vochtschade en zijn onherstelbaar."]),
   ("h2","Bekleding"),("p","Bij een bank zegt de vulling meer dan de stof. Zittingen die niet terugveren zijn doorgezakt, en het vervangen van schuim of veren kost al snel meer dan de bank waard is."),
   ("h2","Geur"),("p","Rook- of vochtgeur trekt zelden weg uit textiel en schuim. Bij houten meubels is dat vaak nog op te lossen, bij gestoffeerde meubels meestal niet.")]},
]

def swatch(c):
    return '<span class="sw">'+"".join(f'<i style="background:{x}"></i>' for x in c)+'</span>'
def tile(s):
    return f"""<a class="tile" href="/materialen/{s['slug']}/">{swatch(s['kleuren'])}
  <span class="tb"><span class="kind">{esc(s['kind'])}</span><h3>{esc(s['naam'])}</h3><p>{esc(s['resume'][:90].rsplit(' ',1)[0])}...</p></span></a>"""
def newscard(a):
    return f"""<article class="news"><span class="cat">{esc(a['cat'])}</span>
  <h3><a href="/nieuws/{a['slug']}/" style="color:inherit;text-decoration:none">{esc(a['titel'])}</a></h3>
  <p>{esc(a['resume'])}</p><div class="meta">{esc(a['datum_nl'])} &middot; {a['lees']} min lezen</div></article>"""

def p_home():
    ld=[{"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#w","url":BASE+"/","name":SITE,"inLanguage":"nl-NL",
         "description":"Onafhankelijke gids over meubels en interieur: materialen, onderhoud en inrichten."},
        {"@context":"https://schema.org","@type":"Organization","@id":BASE+"/#o","name":SITE,"url":BASE+"/","email":EMAIL},crumb([("Home","/")])]
    gids="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p></div>' for g in GIDSEN)
    h=head("Kyra Meubels | gids over meubels, materialen en interieur",
      "Onafhankelijke interieurgids over meubelmaterialen, onderhoud en inrichten. Uitleg over hout, leer, stof en vlechtwerk, zonder verkooppraat.","/",ld)
    h+=f"""<section class="hero"><div class="wrap hero-inner">
  <div><span class="eyebrow">{IC['sofa']}Interieurgids</span>
  <h1>Meubels die <em>meegaan</em></h1>
  <p class="lead">Welk materiaal past waar, wat vraagt het aan onderhoud, en hoe blijft een kleine ruimte werkbaar. Deze gids legt uit waarop een keuze berust, zonder iets te verkopen.</p>
  <div class="hero-actions"><a class="btn btn-teal" href="/materialen/">Bekijk de materialen {IC['arrow']}</a><a class="btn btn-ghost" href="/gidsen/">Naar de gidsen</a></div>
  <div class="hero-meta"><span>{IC['check']}6 materialen</span><span>{IC['check']}Onderhoud per soort</span><span>{IC['check']}Geen webshop</span></div></div>
  <div class="hero-art"><img src="/assets/img/interieur.svg" alt="Illustratie van een woonkamerhoek" width="500" height="360"></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['tree']}Materialen</span><h2>Waar meubels van gemaakt zijn</h2>
  <p class="lead">Per materiaal de eigenschappen, de zwakke plekken en het onderhoud dat erbij hoort.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in MATERIALEN)}</div></div></section>

<section class="section panel"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span><h2>Twee praktische gidsen</h2></div>
  <div class="grid cols-2">{gids}</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{IC['brush']}Nieuws</span><h2>Laatste artikelen</h2></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div>
  <p style="margin-top:22px"><a class="more" href="/nieuws/">Alle artikelen {IC['arrow']}</a></p></div></section>

<section class="section tight"><div class="wrap"><div class="cta">
  <h2>Een materiaal gemist?</h2><p>De gids groeit op basis van vragen die binnenkomen. Suggesties en correcties zijn welkom.</p>
  <a class="btn btn-clay" href="/contact/">Mail de redactie {IC['arrow']}</a></div></div></section>"""
    write("/",h+footer())

def p_mat_index():
    path="/materialen/"; c=[("Home","/"),("Materialen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Materialen","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":s["naam"],"url":BASE+f"/materialen/{s['slug']}/"} for i,s in enumerate(MATERIALEN)]},crumb(c)]
    h=head("Alle meubelmaterialen | "+SITE,"Overzicht van meubelmaterialen met eigenschappen, zwakke plekken en onderhoud: hout, leer, stof, vlechtwerk en metaal.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['tree']}Overzicht</span>
  <h1>Alle materialen</h1><p class="lead">Zes materialen die in vrijwel elk interieur terugkomen, elk met de eigenschappen die de keuze bepalen.</p></div>
  <div class="grid cols-3">{"".join(tile(s) for s in MATERIALEN)}</div></div></section>"""
    write(path,h+footer())

def p_mat(s):
    path=f"/materialen/{s['slug']}/"; c=[("Home","/"),("Materialen","/materialen/"),(s["naam"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":s["naam"],"description":s["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    sp="".join(f"<div><dt>{esc(l)}</dt><dd>{esc(v)}</dd></div>" for l,v in s["specs"])
    sec="".join(f"<h2>{esc(t)}</h2><p>{esc(p)}</p>" for t,p in s["secties"])
    pt="".join(f'<li>{IC["check"]}<span>{esc(x)}</span></li>' for x in s["punten"])
    anders=[x for x in MATERIALEN if x["slug"]!=s["slug"]][:3]
    h=head(f"{s['naam']} | eigenschappen en onderhoud | {SITE}", s["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section tight"><div class="wrap prose"><span class="eyebrow">{IC['tree']}{esc(s['kind'])}</span>
  <h1>{esc(s['naam'])}</h1><p class="lead">{esc(s['resume'])}</p></div>
  <div class="wrap"><dl class="specs">{sp}</dl></div>
  <div class="wrap prose">{sec}<h2>Kort samengevat</h2><ul class="ticks" style="margin-bottom:18px">{pt}</ul>{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Andere materialen</h2></div>
  <div class="grid cols-3">{"".join(tile(x) for x in anders)}</div></div></section>"""
    write(path,h+footer())

def p_gidsen():
    path="/gidsen/"; c=[("Home","/"),("Gidsen",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Gidsen","inLanguage":"nl-NL"},crumb(c)]
    cards="".join(f'<div class="card"><div class="ic">{IC[g["ic"]]}</div><h3><a href="/gidsen/{g["slug"]}/" style="color:inherit;text-decoration:none">{esc(g["titel"])}</a></h3><p>{esc(g["resume"])}</p><p style="margin-top:10px"><a class="more" href="/gidsen/{g["slug"]}/">Lees de gids {IC["arrow"]}</a></p></div>' for g in GIDSEN)
    h=head("Gidsen | onderhoud en inrichten | "+SITE,"Praktische gidsen over het onderhouden van meubels per materiaal en over het inrichten van een kleine ruimte.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['book']}Gidsen</span><h1>Gidsen</h1>
  <p class="lead">Twee onderwerpen die bij vrijwel elk interieur spelen: onderhoud en indeling.</p></div>
  <div class="grid cols-2">{cards}</div></div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['book']}Extra</span><h2>Ook interessant</h2></div>
<div class="grid cols-2">
<div class="card"><h3><a href="https://www.stofzakkie.nl/" target="_blank" rel="noopener">Stofzakkie webshop</a></h3><p>Webshop voor stofzuigerzakken en stofzuigerbenodigdheden, praktisch bij het schoonhouden van stoffen meubels.</p></div>
<div class="card"><h3><a href="https://www.cf-kunststofprofielen.nl/profielen/hoekprofielen" target="_blank" rel="noopener">Hoekprofiel</a></h3><p>Kunststof hoekprofielen voor het afwerken en beschermen van hoeken en randen.</p></div>
<div class="card"><h3><a href="https://www.woon-boerderijmaja.nl/houten-vloeren/wit/" target="_blank" rel="noopener">Witte houten vloer kopen</a></h3><p>Woon Boerderij Maja biedt witte houten vloeren, een lichte en tijdloze keuze voor wie een fris interieur wil.</p></div>
</div></div></section>"""
    write(path,h+footer())

def p_gids(g):
    path=f"/gidsen/{g['slug']}/"; c=[("Home","/"),("Gidsen","/gidsen/"),(g["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":g["titel"],"description":g["resume"],
         "inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{g['titel']} | {SITE}", g["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC[g['ic']]}Gids</span>
  <h1>{esc(g['titel'])}</h1><p class="lead">{esc(g['resume'])}</p>{blocks(g['body'])}{byline()}</div></section>"""
    write(path,h+footer())

def p_nieuws():
    path="/nieuws/"; c=[("Home","/"),("Nieuws",path)]
    ld=[{"@context":"https://schema.org","@type":"CollectionPage","@id":BASE+path,"url":BASE+path,"name":"Nieuws","inLanguage":"nl-NL"},crumb(c)]
    h=head("Nieuws | artikelen over materiaal en praktijk | "+SITE,"Artikelen over meubelmaterialen en over de praktijk van kopen, onderhouden en beoordelen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="section-head"><span class="eyebrow">{IC['brush']}Nieuws</span><h1>Artikelen</h1>
  <p class="lead">Achtergrond bij wat er met materiaal gebeurt en waar in de praktijk op te letten valt.</p></div>
  <div class="grid cols-2">{"".join(newscard(a) for a in ARTIKELEN)}</div></div></section>"""
    write(path,h+footer())

def p_art(a):
    path=f"/nieuws/{a['slug']}/"; c=[("Home","/"),("Nieuws","/nieuws/"),(a["titel"],path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":a["titel"],"description":a["resume"],
         "datePublished":a["datum"],"inLanguage":"nl-NL","author":{"@type":"Person","name":AUTEUR},"publisher":{"@type":"Organization","name":SITE}},crumb(c)]
    h=head(f"{a['titel']} | {SITE}", a["resume"], path, ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['brush']}{esc(a['cat'])}</span>
  <h1>{esc(a['titel'])}</h1><p class="meta" style="margin-bottom:22px">Door {esc(AUTEUR)} &middot; {esc(a['datum_nl'])} &middot; {a['lees']} min lezen</p>
  {blocks(a['body'])}{byline()}</div></section>
<section class="section panel"><div class="wrap"><div class="section-head"><h2>Meer lezen</h2></div>
  <div class="grid cols-2">{"".join(newscard(x) for x in ARTIKELEN if x['slug']!=a['slug'])}</div></div></section>"""
    write(path,h+footer())

def p_over():
    path="/over/"; c=[("Home","/"),("Over",path)]
    ld=[{"@context":"https://schema.org","@type":"AboutPage","@id":BASE+path,"url":BASE+path,"name":"Over","inLanguage":"nl-NL"},crumb(c)]
    h=head("Over Kyra Meubels | wat dit platform is | "+SITE,
      "Kyra Meubels is een onafhankelijke interieurgids over meubelmaterialen en onderhoud. Uitleg over de opzet en de grenzen van het platform.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['book']}Over het platform</span>
  <h1>Een gids, geen woonwinkel</h1>
  <p class="lead">Kyra Meubels legt uit waar meubels van gemaakt zijn, wat dat betekent in dagelijks gebruik en hoe een interieur werkbaar blijft. Zonder assortiment en zonder verkoopbelang.</p>
  <h2>Waarom deze gids bestaat</h2>
  <p>Bij de aanschaf van een tafel of een bank draait het gesprek in de winkel vaak om uiterlijk en prijs, terwijl de vragen die later opkomen over materiaal gaan. Waarom scheurt een blad, waarom zakt een zitting door, waarom laat vlechtwerk los. Die vragen staan hier centraal.</p>
  <h2>Onafhankelijk</h2>
  <p>Er worden geen meubels verkocht en er zijn geen afspraken met leveranciers of winkels. Merken worden alleen genoemd wanneer dat nodig is om een materiaal of techniek te beschrijven.</p>
  <div class="callout"><p><strong>Geen verband met bestaande bedrijven.</strong> Dit platform is een redactionele uitgave. Overeenkomsten met namen van bestaande meubelzaken berusten niet op enige samenwerking of betrokkenheid.</p></div>
  <h2>Werkwijze</h2>
  <p>Elk materiaal volgt dezelfde opzet: eigenschappen in het kort, gevolgd door de punten die in de praktijk verschil maken, en een samenvatting. De gidsen behandelen onderwerpen die daar los van staan.</p>
  <h2>Correcties</h2>
  <p>Onderbouwde correcties zijn welkom en worden verwerkt wanneer ze kloppen.</p>
  <p style="margin-top:16px"><a class="btn btn-teal" href="/redactie/">Over de redactie {IC['arrow']}</a> <a class="btn btn-ghost" href="/materialen/">Naar de materialen</a></p></div></section>"""
    write(path,h+footer())

def p_redactie():
    path="/redactie/"; c=[("Home","/"),("Over de redactie",path)]
    ld=[{"@context":"https://schema.org","@type":"Person","@id":BASE+"/#kyra","name":AUTEUR,"jobTitle":AUTEUR_ROL,"worksFor":{"@type":"Organization","name":SITE}},
        {"@context":"https://schema.org","@type":"ProfilePage","@id":BASE+path,"url":BASE+path,"name":"Over de redactie","inLanguage":"nl-NL"},crumb(c)]
    h=head(f"Over de redactie: {AUTEUR} | {SITE}", f"{AUTEUR} schrijft de materiaalprofielen en gidsen van Kyra Meubels.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap"><div class="persona">
  <div class="persona-photo"><img src="/assets/img/auteur.svg" alt="Illustratie van {esc(AUTEUR)}"></div>
  <div><span class="eyebrow">{IC['sofa']}De redactie</span><h1>{esc(AUTEUR)}</h1>
  <p class="lead">{esc(AUTEUR_ROL)}. Kyra schrijft de materiaalprofielen, de gidsen en de artikelen op deze site.</p></div></div></div></section>
<section class="section panel"><div class="wrap prose">
  <h2>Van meubelmakerij naar redactie</h2>
  <p>Kyra werkte bij een meubelmakerij en later bij een stoffeerderij, waar meubels binnenkwamen die net niet goed genoeg gemaakt waren om lang mee te gaan. Wat daar zichtbaar werd over constructie en materiaal, vormt de kern van deze gids.</p>
  <h2>Uitleggen wat een keuze betekent</h2>
  <p>Een geolied blad of een gelakt blad is geen kwestie van beter of slechter, maar van wat er de jaren daarna gebeurt. Diezelfde afweging speelt bij leer, bij stof en bij vlechtwerk. Die afwegingen staan hier uitgeschreven.</p>
  <h2>Een getekend portret</h2>
  <p>De illustratie op deze pagina is een tekening, geen foto. Het onderwerp van deze site is het interieur, niet de schrijver.</p>
  <h2>Contact</h2>
  <p>Vragen, correcties en suggesties komen binnen via <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>"""
    write(path,h+footer())

def p_contact():
    path="/contact/"; c=[("Home","/"),("Contact",path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Vraag, correctie of suggestie voor Kyra Meubels? Een e-mail komt rechtstreeks bij de redactie binnen.",path,ld)+crumbs_html(c)
    h+=f"""<section class="section"><div class="wrap prose"><span class="eyebrow">{IC['mail']}Contact</span>
  <h1>Contact met de redactie</h1>
  <p class="lead">Deze site heeft geen contactformulier. Een e-mail komt rechtstreeks bij de redactie binnen.</p>
  <div class="callout"><p><strong>E-mailadres</strong></p><p style="margin:.3em 0"><a href="mailto:{EMAIL}" style="font-size:1.1rem;font-weight:600">{EMAIL}</a></p></div>
  <h2>Waar de redactie iets mee kan</h2>
  <ul><li>Een correctie op een materiaalbeschrijving.</li><li>Een materiaal of onderwerp dat nog ontbreekt.</li><li>Een praktijkvraag die nergens goed beantwoord wordt.</li></ul>
  <h2>Waar niet</h2>
  <p>Dit platform verkoopt geen meubels, bemiddelt niet bij aankoop en behandelt geen klachten over bestellingen bij winkels. Daarvoor is de verkoper de aangewezen partij.</p></div></section>"""
    write(path,h+footer())

def legal(path,titel,bs):
    c=[("Home","/"),(titel,path)]
    ld=[crumb(c),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":titel,"inLanguage":"nl-NL"}]
    h=head(f"{titel} | {SITE}", f"{titel} van {SITE}.",path,ld)+crumbs_html(c)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(titel)}</h1>{"".join(bs)}</div></section>'
    write(path,h+footer())

def p_legal():
    legal("/privacybeleid/","Privacybeleid",[
      "<p>Kyra Meubels is een redactioneel platform en verwerkt zo min mogelijk persoonsgegevens.</p>",
      "<h2>Welke gegevens</h2><p>De site bevat geen contactformulier. Wie per e-mail contact opneemt, deelt uitsluitend wat in dat bericht staat, en dat wordt alleen gebruikt om te antwoorden.</p>",
      "<h2>Statistieken</h2><p>Als bezoekcijfers worden bijgehouden, gebeurt dat zo privacyvriendelijk mogelijk en zonder verkoop aan derden.</p>",
      "<h2>Bewaartermijn</h2><p>E-mails worden niet langer bewaard dan nodig is voor de afhandeling.</p>",
      f"<h2>Vragen</h2><p>Vragen over privacy kunnen naar {EMAIL}.</p>"])
    legal("/cookiebeleid/","Cookiebeleid",[
      "<p>Deze site gebruikt zo min mogelijk cookies en plaatst geen advertentiecookies.</p>",
      "<h2>Functioneel</h2><p>Alleen cookies die nodig zijn voor het functioneren van de pagina's kunnen worden geplaatst.</p>",
      "<h2>Lettertypen</h2><p>De lettertypen worden geladen via een externe dienst, wat bij het tonen van een pagina een verzoek naar die dienst met zich meebrengt.</p>",
      f"<h2>Vragen</h2><p>Vragen over cookies kunnen naar {EMAIL}.</p>"])

def p_404():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
  <span class="eyebrow" style="justify-content:center">404</span><h1>Deze pagina bestaat niet</h1>
  <p class="lead">De link is mogelijk verouderd. Het materialenoverzicht is een goed vertrekpunt.</p>
  <p><a class="btn btn-teal" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/materialen/">Alle materialen</a></p></div></section>"""
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h+footer())

def extras():
    u=["/","/over/","/redactie/","/materialen/","/gidsen/","/nieuws/","/contact/","/privacybeleid/","/cookiebeleid/"]
    u+=[f"/materialen/{s['slug']}/" for s in MATERIALEN]+[f"/gidsen/{g['slug']}/" for g in GIDSEN]+[f"/nieuws/{a['slug']}/" for a in ARTIKELEN]
    open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{x}</loc></url>\n" for x in u)+"</urlset>\n")
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write(f"https://www.kyrameubels.nl/* {BASE}/:splat 301!\n")

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT,exist_ok=True)
    shutil.copytree(os.path.join(SRC,"assets"), os.path.join(OUT,"assets"))
    p_home(); p_over(); p_redactie(); p_mat_index()
    for s in MATERIALEN: p_mat(s)
    p_gidsen()
    for g in GIDSEN: p_gids(g)
    p_nieuws()
    for a in ARTIKELEN: p_art(a)
    p_contact(); p_legal(); p_404(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__": main()
