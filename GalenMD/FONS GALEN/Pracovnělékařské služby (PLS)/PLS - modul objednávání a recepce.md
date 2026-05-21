---
title: "PLS - modul objednávání a recepce"
version: 2
updated_at: 2025-06-26
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/57016366
---

Moduly slouží jako přehled pacientů a PLS prohlídek.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/PLS - modul objednávání a recepce/assets/image-20250626-135851.png]]
Pod údaji o firmě jsou zobrazena rizika, která jsou pacientovi přidělena

**Barevné rozlišení**

**o Šedá** – pokud na pacientovi a konkrétní firmě neexistuje ukončená PLS prohlídka (neplatí na PLS prohlídky které neovlivňují lhůtu, nebo prohlídky s výsledkem „Dlouhodobě pozbyl zdravotní způsobilost“), nebo datum plánované prohlídky je v minulosti, nebo je-li datum zaměstnání do < jako aktuální den.

**o Zelená**– pokud datum plánované prohlídky je větší než 90 dní

**o Oranžová** – pokud datum plánované prohlídky je v rozmezí 15 až 90 dnů

**o Červená** – je-li datum plánované prohlídky v rozmezí 0 až 15 dní (včetně aktuálního dne)

**Interval prohlídky**

o Zobrazuje se vždy, je-li vypočitatelný

o Počítá se jako MIN z rizik v rámci PLS skupiny

**Platnost posudku**

Přepisuje se také na kartu pacienta. Určuje datum plánované prohlídky v případech pouze v případě:

1. Pokud neexistuje ukončená (hlavní) PLS prohlídka (OL) na pacientovi k dané firmě.
2. Je v daném období na pobočce aktivní vedení lhůtníku.
3. Není určen datum plánované prohlídky správcem Pokud tento datum plánované prohlídky je určen pomocí data platnosti posudku, je označen slovně („z importu“). Zobrazuje se a přepisuje (ručně i importem) i v případě že je < jako dnešní datum

**Výsledek poslední prohlídky**

Tato změna se přepíše okamžitě takové do PLS aplikace a PLS admina. Do výpočtu plánované prohlídky se tato hodnota bere pouze v případě, kdy neexistuje výsledek předposlední PLS prohlídky, následně se srovnává tato hodnota s hodnotou výsledku poslední prohlídky. Podrobně v diagramu výpočtu lhůty.

## Stav objednávky

Celkový přehled všech objednávek je zobrazen v postranním panelu pod kontaktními údaji o pacientovi. Aby se objednávka v postranním panelu u firmy zobrazila, musí být typ objednávky PLS, to znamená že musí být vytvořena skrze tlačítko PLS (vytváří se vazba na položku ve smlouvě PLS). Nad objednávkou funguje tooltip, který zobrazuje informaci o tom, jaký uživatel objednávku vytvořil, z jakého pracoviště a kdy byla objednávka vytvořena. Zobrazuje se vždy objednávka, která je nejvíce v budoucnosti (nejvyšší datum objednání) a objednávka která má datum >= jako dnešek. Záznam o objednání se přepíše na všech firmách, které mají stav objednávky objednán (přepíše se v případě splnění podmínky, že nově vytvořená objednávka má datum objednání > jako stávající)

Aktuálně se zobrazují 3 hodnoty stavů objednávky:

**Není objednán**

Není vytvořen záznam v kalendáři, který by byl navázaný na PLS prohlídku dané firmy, nebe je objednávka v minulosti

**Objednán**

- Je vytvořen záznam v kalendáři, viz bod výše – Zobrazuje se pouze v případě kdy je objednávka na dnešek nebo v budoucnosti, pokud v případě že ještě nebyla vytvořena PLS prohlídka

**K objednání**

- Tento stav lze nastavit pouze v PLS aplikaci

- Do GUI v Recepci a Objednávání se přepíše poznámka z PLS aplikace a objeví se tlačítko „Zrušit“, které nastaví stav opět na Není objednán (Tlačítko Zrušit se v PLS aplikaci neobjeví)

o Filtr nad stavy objednávky v podrobném filtru funguje také pouze na těmito stavy

**Poslední prohlídka OL**

o Zobrazené datum je datum návštěvy z prohlídky.

o V GUI IS Galen se v sekci Poslední prohlídka OL nezobrazuje výsledek prohlídky, narozdíl od PLS aplikace. Pro zobrazení prohlídky NL, je nutné, aby měla prohlídka nastavená v designéru

explicitně „Ovlivňuje lhůtu – Ne” a byla PLS přehlídkou

**Plánovaná prohlídka**

o Je-li zadaná lékařem na prohlídce, zobrazí se vedle data text „určeno lékařem“

o Pokud je zadána administrátorem v okně PLS admin, zobrazí se text „určeno správcem“ Je zobrazena i poznámka, pokud byla zadána.

o Je-li zadána importem nebo pomocí data platnosti posudku, zobrazí se text „z importu“

o Je-li dopočítána, doprovodný text se nezobrazí

**Tlačítko PLS**

o Po kliku na toto tlačítko se objeví výběr prohlídek, jako v okně Prohlídky a vyšetření.

o Po zvolení prohlídky se otevře okno, viz obrázek, s možností přidat další sortiment a výběrem skupin pracovišť, jim přiřazeným pracovištím a zobrazí se všechny dostupné kalendáře u vybraných pracovišť.

o Zobrazení kalendáře je defaultně na začátku aktuálního týdne

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/PLS - modul objednávání a recepce/assets/image-20250626-135916.png]]
Po vytvoření objednávky v kalendáři se do interní poznámky pro lékaře přepíše název prohlídky a dodatečné položky přiřazené prohlídce. U typu objednávky PLS prohlídka se automaticky nabídne combo-box s výběrem PLS prohlídky, kterou označíme tuto objednávku.  Je-li jiný typ objednávky než PLS, objednávka se nezobrazí.

Aktuálně má pouze informativní charakter, objednávka se přiřadí prohlídce z prvotního výběru. V seznamu v combo-boxu jsou všechny položky na všech smlouvách na dané pobočce, mohou být rozličné PLS skupiny

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/PLS - modul objednávání a recepce/assets/image-20250626-135926.png]]
**Nastavení základních parametrů PLS prohlídek a eŽádanek na základě pracovního zařazení pacienta (nákladového střediska)**

Tato funkcionalita slouží k nastavení základních parametrů vyšetření i odběrů u PLS prohlídek na základě pracovního zařazení pacienta. Předejde se tím chybám lidského faktoru, kdy jsou provedeny odběry a vyšetření, které nejsou v dané kategorii pracovního zařazení pacienta potřeba. Jedná se o základní kategorie, které by mohl lékař vždy rozšířit o další parametry, ale bude systémem upozorněn, že zadává parametry navíc.

### Nastavení parametrů

Nastavení parametrů může provádět uživatel s oprávněním Správce. K funkcionalitě se dostane následujícím způsobem:

1. Na úrovni Správce otevřít modul **Nadstandardní péče.**
2. Následně vybrat firmu, pro kterou chcete dané parametry nastavit.
3. V pravé horní sekci se přepnout na záložku Nákladová střediska.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/PLS - modul objednávání a recepce/assets/image-20250626-135937.png]]
Následně je nutné označit nákladové středisko, pro které chcete parametry nastavit. Po označení se zaktivní tlačítka **Konfigurace prohlídky** a **Konfigurace eŽádanky**.

### Konfigurace prohlídky

Po kliknutí na tlačítko Konfigurace prohlídky se uživateli zobrazí okno, kde nejprve v položce **Sortiment prohlídky** vybere prohlídku, pro kterou chce nadefinovat parametry. V položce se nabízí všechny PLS prohlídky, které jsou nadefinované v modulu Ceníky.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/PLS - modul objednávání a recepce/assets/image-20250626-135948.png]]
Uživatel má v okně následně možnost zvolit ty položky, které budou při vyplnění dané PLS prohlídky povinné.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/PLS - modul objednávání a recepce/assets/image-20250626-135959.png]]
Jelikož se ale jedná pouze o měkkou kontrolu, tak se při ukládání příslušné prohlídky v případě, že uživatel nevyplnil některou z „povinných“ položek, zobrazí následující hláška:

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/PLS - modul objednávání a recepce/assets/image-20250626-140011.png]]
Hláška má ovšem pouze informativní charakter, tudíž uživatel může po kliknutí na tlačítko **Ano**pokračovat v plánovaných krocích, aniž by musel v prohlídce cokoliv změnit.

### Konfigurace eŽádanky

Po kliknutí na tlačítko Konfigurace eŽádanky se uživateli zobrazí okno, kde nejprve v položce **eŽádanka**vybere žádanku, pro kterou chce nadefinovat parametry. Dále v okně zvolí ty položky, které budou při otevření nové eŽádanky automaticky předvyplněné (zaškrtlé).

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/PLS - modul objednávání a recepce/assets/image-20250626-140218.png]]
Jestliže následně uživatel při vyplňování eŽádanky odškrtne položku vyplněnou automatickým předvýběrem či naopak zaškrtne položku, která je oproti doporučenému výběru navíc, zobrazí se uživateli obdobná hláška:

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/PLS - modul objednávání a recepce/assets/image-20250626-140233.png]]
Hláška má ovšem pouze opět informativní charakter, tudíž uživatel může po kliknutí na tlačítko **Ano**pokračovat v plánovaných krocích, aniž by musel v žádance cokoliv měnit.
