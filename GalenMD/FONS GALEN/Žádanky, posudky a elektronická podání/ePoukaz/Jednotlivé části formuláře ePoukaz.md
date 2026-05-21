---
title: "Jednotlivé části formuláře ePoukaz"
version: 3
updated_at: 2026-01-27
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/52690999
---

**Typ dokumentace** – výběrové pole s možnostmi Kurativa a PLS. Při volbě PLS se zobrazí další pole Zaměstnání, kde je nutné vybrat z číselníku Zaměstnání pacienta.

### Údaje pacienta

·        tlačítko **Aktualizovat** dle kartotéky: Po kliknutí na tlačítko dochází k aktualizaci položek na hodnoty, které má příslušný pacient uvedené v kartě pacienta. Tlačítko je aktivní pouze v případě, že daný ePoukaz nebyl odeslán do centrálního úložiště SÚKL (ePoukaz nemá přidělené ID).

·        položka **E-mail:** V případě vyplnění této položky posílá SÚKL na danou e-mailovou adresu

·        položka **Telefon**: V případě vyplnění této položky posílá SÚKL na dané telefonní číslo

·        **průvodku** k příslušnému ePoukazu. Tuto položku je uživatel povinen vyplnit pouze v případě, že není vyplněná položka Kontaktní adresa.

·        **Notifikovat pacienta**je možné prostřednictvím e-mailu nebo SMS na telefon. Výchozí nastavení je ovlivněno typem kontaktu s příznakem *SÚKL* v kartě pacienta. V případě, že si na pracovišti nepřejete zasílat notifikace pacientovi, je možné provést nastavení uživatelem s rolí *Správce* dle tohoto [[Záložka UI konfigurace|návodu]].

·        položka**Trvalá adresa**: Do této položky i položek s ní související, jako je Ulice, Obec, Č. p., Č. or., PSČ, se v základním stavu přenáší trvalá adresa, kterou má příslušný pacient uvedenou v kartě pacienta. Uživatel ovšem může vybrat, že do těchto položek chce přenést kontaktní adresu z karty pacienta. Dané položky může taktéž přepsat na libovolné hodnoty.

·        položka **Kontaktní adresa**: Chování této položky je obdobné jako položky Trvalá adresa s tím rozdílem, že se v základním stavu přenáší z karty pacienta kontaktní adresa. Tuto položku je uživatel povinen vyplnit pouze v případě, že není vyplněná položka Telefon.

## EPoukaz - Základní údaje

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Jednotlivé části formuláře ePoukaz/assets/image-20250623-100335.png]]
·        položka **Datum vystavení**: Aktuální datum, kdy byl ePoukaz uložen do centrálního úložiště elektronických poukazů.

·        položka **Primární stav**: Uživatel AIS Galen, který bude v procesu systému ePoukaz vždy vystupovat v roli předepisujícího, může definovat dva primární stavy:

·        **Předepsaný**: Výchozí stav předpisů po založení předepisujícím.

·        **Čeká na podklady výdejny**: Zdravotnický prostředek vyžaduje schválení zdravotní pojišťovnou a lékař potřebuje od výdejny ještě další informace – např. cenovou předkalkulaci, technický popis. Předepisující tyto podklady vyžaduje pro předání ke schválení na zdravotní pojišťovnu.

·        položka **Pro rodinu**: Řada lékařů, zejména těch, kteří jsou v penzi, předepisuje zdravotnické prostředky pouze pro svou potřebu či pro potřebu svých rodinných příslušníků. V takovém případě na ePoukaz uvede informaci, že se jedná o předpis na ePoukaz pro potřebu rodiny.

·        položka **Platnost do**: Elektronický poukaz lze u výdejce uplatnit do 30 dnů od jeho vystavení, neurčí-li předepisující jinak, nejpozději však do 1 roku.

·        Položka **Stav schválení**: Hodnotu této položky nastaví automaticky AIS Galen na základě informace z číselníku Seznam cen a úhrad ZP pro vybraný zdravotnický prostředek.

## Předpis

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Jednotlivé části formuláře ePoukaz/assets/image-20250623-100409.png]]
**Skupina -**výběrem z číselníku (šipečka vpravo) doplníme kód skupiny ZP.

**Název skupiny** - doplní se automaticky po výběru kódu skupiny ZP.

**Kód** - výběrem z číselníku doplníme kód skupiny zdravotnického prostředku.

**Název**- doplní se automaticky po výběru kódu ZP.

**Množství** - doplníme požadované množství. Ve výchozím stavu se nastavuje množství 1.

**Měrná jednotka** - výběrem z číselníku (šipečka vpravo) doplníme měrnou jednotku (npř. balení, kus, gram, sada, mililiitr tad. ).

**Úhrada** - pokud je ze strany pojišťovny hrazena základní úhrada, ve výchozím stavu se při předpisu pomůcky nastavuje Úhrada 1. Pokud je nastaven stupeň inkontinence, nastaví se úhrada v závislosti na zvoleném stupni.

Další hodnoty se nastavují výběrem z číselníku (šipečka vpravo) doplníme typ úhrady (např. Pacient: hradí pacient, Uhrada1: základní úhrada, Pacient-Zaměstnavatel: hradí pacientův zaměstnavatel, Zaměstnavatel1: základní úhrada s doplatkem hrazeným zaměstnavatelem pacienta). Využití dalších úhrad (2 a 3) závisí od jednotlivých skupin zdravotnických prostředků.

**Nezaměňovat** - stejně jako u eReceptů určuje, zda lze vydat alternativní zdravotnický prostředek nebo ne.

**Ikonka i** – po najetí myší v tooltipu vidíme celý název ZV a zobrazí se také doprovodný text.

**Tlačítko Kód 9999999 lze využít v následujících případech:**

·        ZP Z V.Z.P. HRAZENÉ, ALE V NEUVEDENÉ V SEZNAMU SÚKL: U zdravotnických

prostředků, které jsou hrazené ze zdravotního pojištění, ale nejsou uvedené v seznamu

hrazených zdravotnických prostředků, bude použitý kód 9999999, který je dnes

zdravotními pojišťovnami standardně využíván (u všech takto předepisovaných ZP

musí být zadáno ev.č. schválení revizním lékařem).

·        „ZP NEHRAZENÉ Z V.Z.P. DLE PŘÍLOHY 3C ZÁKONA Č. 48/1997 SB.“ NEBO „ZP

NEHRAZENÉ Z V.Z.P. VYDÁVANÉ VÝHRADNĚ NA POUKAZ DLE §28 ODST. 2

ZÁKONA Č. 89/2021 SB.“: Pokud předepsaný ZP není uveden v Seznamu SÚKL –

bude použit kód 9999999. V případě, že ZP má kód přidělen, použije se standardní

kódu uvedeného v Seznamu SÚKL.

·        V případě zadání kódu 9999999 je uživateli umožněno do položky Název vepsat Volný text. V tomto specifickém případě je dále nutné vyplnit položku Měrná jednotka.

### Přílohy

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Jednotlivé části formuláře ePoukaz/assets/image-20250623-100430.png]]
K příslušnému ePoukazu má uživatel možnost připojit přílohu. Příloha se může nacházet

v následujících stavech:

a)     **K odeslání**: Příloha byla uložená v AIS Galen, nebyla ovšem odeslaná do centrálního úložiště SÚKL.

b)     **Odeslaná**: Příloha byla uložená v AIS Galen a zároveň byla odeslaná do centrálního úložiště SÚKL.

c)     **Ke zrušení**: Daný stav nebývá příslušná příloha pouze v AIS Galen. Jestliže si uživatel přeje, aby byla příloha zrušená i v centrálním úložišti SÚKL, je nutné stisknout tlačítko Odeslat (Opravit).

## Údaje pro schválení zdravotní pojišťovnou

Jestliže uživatel předepisuje zdravotnický prostředek, u kterého je nutné schválení zdravotní

pojišťovnou, zobrazí se ve AIS Galen následující formulář:

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Jednotlivé části formuláře ePoukaz/assets/image-20250623-100452.png]]
Položky

*Stanovisko revizního lékaře, Poznámka pojišťovny pro předepisujícího, Číslo*

*povolení přidělené ZP, IČZ výdejny, Evidenční číslo zdrav. prostř., Datum předběžného*

*schválení, Datum omezení, Datum vyjádření ZP, Příjmení schvalujícího, Jméno*

*schvalujícího, Požadovaná úhrada* přísluší k vyplnění zdravotní pojišťovnou. V systému

ePoukaz ovšem tyto položky v současné době vyplňuje předepisující na základě doručeného

vyrozumění od zdravotní pojišťovny (revizního lékaře). Uživatel AIS Galen to provede

následovně:

1. V přehledu ePoukazů (levá část modulu) uživatel klikne pravým tlačítkem myši na příslušný ePoukaz.

1. Na základě výsledku vyrozumění od zdravotní pojišťovny uživatel vybere, zda se daný ePoukaz schvaluje či zamítá.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Jednotlivé části formuláře ePoukaz/assets/image-20250623-100510.png]]
1. Následně je nutné vyplnit příslušné položky a výsledek stiskem tlačítka Odeslat odeslat na SÚKL.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Jednotlivé části formuláře ePoukaz/assets/image-20250623-100528.png]]
