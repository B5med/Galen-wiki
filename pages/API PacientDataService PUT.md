---
id: 39583745
title: "API PacientDataService PUT"
version: 7
updated_at: 2025-06-11T13:29:08.983Z
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/39583745
---

# API PacientDataService PUT

none

## Obecné informace

### pohlavi

Muz  
Zena  
Neuvedeno

### pojistovna

111 = Všeobecná zdravotní pojišťovna České republiky  
201 = Vojenská zdravotní pojišťovna České republiky  
205 = Česká průmyslová zdravotní pojišťovna  
207 = Oborová zdravotní pojišťovna zaměstnanců bank a pojišťoven  
209 = Zaměstnanecká pojišťovna ŠKODA  
211 = Zdravotní pojišťovna Ministerstva vnitra ČR  
213 = RBP, zdravotní pojišťovna  
333 = Pojišťovna VZP a.s.  
747 = MAXIMA  
777 = Slavia pojišťovna a.s.  
999 = Samoplátci

### druhPojisteni

Může nabývat hodnot

0 = Bez pojistného vztahu  
1 = Veřejné zdravotní  
2 = Smluvní připojištění  
4 = EU a mezinár. smlouvy

### kodPojisteni

A = 1A – Žadatel o mezinárodní ochranu (azyl)

C = 1C – Cizinec s trvalým pobytem

E = 1E – Osoba ze země EU pojištěná v ČR dle Nařízení

F = 1F – Nezaopatřený rodinný příslušník dle Nařízení

O = 1O – Občan ČR s trvalým pobytem

S = 1S – Zaměstnaný cizinec ze státu s MS (stát mimo EU mající smlouvu s ČR

Z = 1Z – Zaměstnaný cizinec ze země mimo EU

### Obecná logika

Pokud nezasílám parametr, který není povinný, obsah entity nebude změněn.

Např. Pokud ve volání bude vynechán parametr adresaTrvalaPsc, nebude stávající hodnota změněna.

Pokud zasílám parametr, jehož hodnota se liší od stávající hodnoty, obsah entity bude změněn.

Např. Pokud volám "adresaTrvalaUlice": "", bude obsah této entity smazán.

## Pacient

`{`

`cisloPojistence (string): Číslo pojištěnce ,`

`datumNarozeni (string): Datum narození (ddMMyyyy) ,`

`prijmeni (string): Příjmení ,`

`jmeno (string): Jméno ,`

`titul (string, optional): Titul před jménem ,`

`titulZa (string, optional): Titul za jménem ,`

`pohlavi (string): Pohlaví (Muz, Zena, Neuvedeno) ,`

`pojistovna (string): Kód aktuální pojišťovny ,`

`druhPojisteni (string): Druh pojištění ,`

`kodPojisteni (string, optional): Kód pojištění ,`

`email (string, optional): E-mail ,`

`telefon (string, optional): Telefon ,`

`adresaTrvalaUlice (string, optional): Ulice trvalé adresy ,`

`adresaTrvalaCisloOrientacni (string, optional): Číslo orientační trvalé adresy ,`

`adresaTrvalaCisloPopisne (string, optional): Číslo popisné trvalé adresy ,`

`adresaTrvalaCisloEvidencni (string, optional): Číslo evidenční trvalé adresy ,`

`adresaTrvalaObec (string, optional): Obec trvalé adresy ,`

`adresaTrvalaPsc (string, optional): PSČ trvalé adresy`

`}`

### Povinné údaje pro vytvoření karty pacienta

cisloPojistence

datumNarozeni

prijmeni

jmeno

pohlavi

pojistovna

druhPojisteni

kodPojisteni

- Pokud je pojišťovna =

111 = Všeobecná zdravotní pojišťovna České republiky  
201 = Vojenská zdravotní pojišťovna České republiky  
205 = Česká průmyslová zdravotní pojišťovna  
207 = Oborová zdravotní pojišťovna zaměstnanců bank a pojišťoven  
209 = Zaměstnanecká pojišťovna ŠKODA  
211 = Zdravotní pojišťovna Ministerstva vnitra ČR  
213 = RBP, zdravotní pojišťovna

tak druhPojisteni = 1 a kodPojisteni musí být vyplněn NEBO druhPojisteni = 4 a kodPojisteni nesmí být vyplněn.

- Pokud je pojišťovna =

333 = Pojišťovna VZP a.s.  
747 = MAXIMA  
777 = Slavia pojišťovna a.s.

tak druhPojisteni = 2 a kodPojisteni nesmí být vyplněn.

- Pokud je pojišťovna =

999 = Samoplátci

tak druhPojisteni = 0 a kodPojisteni nesmí být vyplněn.

### Založení nové karty pacienta/aktualizace stávající

Pokud je zasláno číslo pojištěnce pacienta, které není dohledáno v databázi, je založena nová karta pacienta.

Pokud je dohledáno dané číslo pojištěnce v databázi, je stávající karta pacienta aktualizována.

Z toho vyplývá, že touto metodou není možné aktualizovat číslo pojištěnce pacienta, neboť by to vedlo k založení nové karty, nikoli k aktualizaci stávající.

## Návštěva

`cisloPojistence (string): Číslo pojištěnce ,`

`datumCas (string): Datum a čas návštěvy (ddMMyyyyTHH:mm:ss) ,`

`typNavstevy (string): Typ návštěvy (Navsteva/Pristroj) ,`

`diagnozy (Array[string], optional): Diagnózy ,`

`nalez (string): Text nálezu ,`

`poznamka (string, optional): Poznámka ,`

`odpovednyLekarId (string): Odpovědný lékař`

### Povinné údaje pro vytvoření návštěvy

cisloPojistence

datumCas

typNavstevy

nalez

odpovednyLekarId

### Založení nové návštěvy/aktualizace stávající

Stávající návštěvu není možné aktualizovat. Při provolání metody PUT je vždy založená nová návštěva bez ohledu na to, že u stejného pacienta je na stejném pracovišti již návštěva ke stejnému datu a času založena.

## Anamnéza

`{`

`cisloPojistence (string): Číslo pojištěnce,`

`osobniAnamneza (string, optional): Osobní anamnéza,`

`alergologickaAnamneza (string, optional): Alergologická anamnéza,`

`profesniAnamneza (string, optional): Profesní anamnéza,`

`cave (string, optional): CAVE,`

`kurak (string, optional): Kuřák (A – ano / N – ne / B – bývalý),`

`pocetCigaret (integer, optional): Cigaret za den,`

`krevniSkupina (string, optional): Krevní skupina (Ap – A Rh+ / Am – A Rh- / Bp – B Rh+ / Bm – B Rh- / Op – 0 Rh+ / Om – 0 Rh- / ABp – AB Rh+ / ABm – AB Rh- / A1p – A1 Rh+ / A1m – A1 Rh- / A2p – A2 Rh+ / A2m – A2 Rh- / A1Bp – A1B Rh+ / A1Bm – A1B Rh- / A2Bp – A2B Rh+ / A2Bm – A2B Rh-),`

`pozitivni (Array[string], optional): Pozitivní (HIV, HBsAg, BWR, HCV, TBC),`

`demence (string, optional): Demence (BezDemence – Bez demence / KognitivniPorucha – Kognitivní porucha / KognitivniDeficitZmenaOsobnosti – Kognitivní deficit, změna osobnosti / LehciDemece – Lehčí forma demence / StredneTezkaDemence – Středně těžká demence / TezkaDemence – Těžká demence),`

`kategoriePece (string, optional): Kategorie péče (V1 – 1 / V2 – 2 / V3 – 3 / V4 – 4 / V5 – 5 / V6 – 6),`

`mobilita (string, optional): Mobilita (Mobilni – Mobilní / NejistaChuze – Mobilní, nejistá chůze / CastecneMobilni – Částečně mobilní / Imobilni – Imobilní),`

`inkontinence (boolean, optional): Inkontinence,`

`ridicskyPrukaz (boolean, optional): Řidičský průkaz,`

`zbrojniPrukaz (boolean, optional): Zbrojní průkaz`

`}`

### Povinné údaje pro vytvoření anamnézy

cisloPojistence

### Založení nové anamnézy/aktualizace stávající

Anamnéza se vztahuje k pacientovi bez vazby na konkrétní pracoviště.

Anamnéza se verzuje k datu, nikoli k datu a času. To znamená, že v případě první aktualizace daný den je automaticky založená verze anamnézy platná od daného data. V případě další aktualizace stejný den se jedná o editaci téže verze anamnézy.

Při editaci je potřeba vždy zaslat stávající text, který má být ponechán a k němu přidat nový text. Pokud by byl v rámci aktualizace zaslán pouze nový text, původní text bude dostupný pouze ve starších verzích anamnézy a bude tak považován za aktuálně neplatný.

## Příloha

`{`

`datum (string): Datum (ddMMyyyy),`

`nazevPrilohy (string): Název přílohy,`

`nazevSouboru (string): Název souboru,`

`poznamka (string, optional): Poznámka,`

`cisloPojistence (string): Číslo pojištěnce,`

`icpPracoviste (string): IČP pracoviště,`

`nazevPracoviste (string): Název pracoviště`

`}`

### Povinné údaje pro vytvoření přílohy

datum

nazevPrilohy

nazevSouboru

cisloPojistence

OdpovednyLekarId

### Založení nové přílohy/aktualizace stávající

Touto metodou je možné zakládat nové přílohy. Není možné již zaslanou přílohu nahradit za jiný soubor. Odeslané přílohy není možné smazat (smazat je možné smazat přímo v aplikaci, nikoli přes API).
