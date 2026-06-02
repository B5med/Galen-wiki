---
title: "Prohlídky"
version: 10
updated_at: 2026-06-01
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/50102315
---

# Prohlídky

![image-20250619-062338.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-062338.png>)
Nástroj pro definování prohlídek a vyšetření, které se nabízí u konkrétního pacienta na liště v dolní části obrazovky Prohlídky a vyšetření.

![image-20250619-062355.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-062355.png>)
Změna spočívá mj. v tom, že uživatel nyní vidí prohlídky definované ze strany Stapro, které může

- pro uživatele své společnosti zakázat
- kopírovat do uživatelské definice prohlídky.

Pokud má prohlídka příznak Uživatelské=Ano, pak byla prohlídka vytvořena správcem dané společnosti a tento správce může prohlídku libovolně modifikovat.

Pokud má prohlídka příznak Uživatelské=Ne, pak byla prohlídka vytvořena správcem FONS Galen. Takovou prohlídku správce společnosti nemůže měnit, ale může ji zakázat pro uživatele své společnosti, nebo z ní může vytvořit kopii, kterou již bude mít možnost měnit.

## Funkční tlačítka

- Zveřejnit

   - slouží ke zveřejnění prohlídky uživatelům dané společnosti
   - Prohlídky pracují stejně jako formuláře s testovacími definicemi. Ve chvíli, kdy uživatel vytváří vyšetření, které ještě nemá být dostupné uživatelům, prohlídku nezveřejňuje. Prohlídka je dostupná pouze po zaškrtnutí checkboxu „Načítat testovací definice“ po kliku na ikonu ![image-20250619-062547.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-062547.png>)
      v záložce Design.
- Historie

   - zobrazuje audit změn provedených v definici prohlídky s možností se k dané verzi prohlídky vrátit

## Položky definice prohlídky

![image-20250619-062706.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-062706.png>)
- Aktivní

   - pokud se prohlídka nemá uživatelům zobrazovat, je potřeba ji označit jako neaktivní
   - prohlídku se nedoporučuje mazat, protože by tím byly smazány všechny již vytvořené prohlídky u pacientů
- Název

   - název prohlídky, který se zobrazuje uživatelům
- Verze

   - pořadí právě zobrazené verze prohlídky
- Doplněk názvu

   - odkaz na položku z prohlídky, jejíž hodnota se má zobrazit v seznamu prohlídek pod názvem prohlídky
- Interval (dny)

   - je možné zadat interval ve dnech mezi jednotlivými vyšetřeními
   - např. u preventivní prohlídky je interval 730 dní, a pokud tento interval neuplyne, uživateli není povoleno toto vyšetření zadat
- Věk od (dny)

   - prohlídku je možné uskutečnit v minimálním věku, který je uveden ve dnech, např. prohlídka v 6 měsících věku je definována ve věku 180 dní
   - pokud je potřeba přepočítat věk prohlídky ve dnech u prohlídky, která je definovaná obvykle v letech, pak je potřeba počet let násobit 365,25 a zaokrouhlit na celé číslo nahoru (prohlídka v 15 letech bude mít definovaný počet dnů 5479)
   - v návaznosti na použité bloky prohlídky je nutné definovat věk přesně
- Věk do (dny)

   - podobně jako Věk od (dny) definuje věk pacienta ve dnech, do kdy nejpozději je možné pacientovi prohlídku vytvořit
   - pokud je potřeba přepočítat věk prohlídky ve dnech u prohlídky, která je definovaná obvykle v letech, pak je potřeba počet let násobit 365,25 a zaokrouhlit na celé číslo dolů (prohlídka v 15 letech bude mít uveden věk do 6209 dní)
- Tolerance věku (dny)

   - Určuje, o kolik dní před dosažením věku nebo po překročení stanoveného věku, je možné vytvořit pacientovi prohlídku.
- Omezit pro odbornost

   - pro jakou odbornost je daný formulář zpřístupněn
- Nezobrazovat v dekurzu

   - pokud je zapnuta, není náhled na prohlídku zobrazován v dekurzu

![image-20250619-063051.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-063051.png>)
- Datum bez času

   - do tisku prohlídky se generuje datum a čas návštěvy, který je uveden v horní části prohlídky
- v případě, že je checkbox zaškrtnut, tak se do tisku bude generovat pouze datum bez uvedeného času
- Anamnéza, Trvalé medikace, Trvalé diagnózy

   - je možné definovat, zda se mají údaje uvedené v těchto kolonkách zobrazovat ve vyšetření a dále generovat do tisku
- Následná prohlídka

   - uživatel vybere prohlídku, která na právě definovanou prohlídku navazuje (např. na preventivní prohlídku ve věku 6 měsíců navazuje preventivní prohlídka ve věku 8 měsíců)
- Přebírat vyšetření

   - v samotném vyšetření se zobrazuje tlačítko Převzít ![image-20250619-063204.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-063204.png>)
       ,které dovoluje převzít údaje z předchozího vyšetření
   - pokud je daná kolonka nevyplněna, přebírají se údaje ze stejného vyšetření
- Počet pro přebrání

   - pokud je nastaven počet 1, přebírají se údaje z posledního vyšetření
   - pokud je počet větší než jedna, má uživatel na výběr, ze kterého vyšetření chce údaje přebrat
- Navazující formuláře

   - pokud je definován alespoň jeden navazující formulář, zobrazuje se ve vyšetření tlačítko ![image-20250619-063302.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-063302.png>)
      , po jehož stisku se uživateli otevře formulář, kam jsou přeneseny informace zadané do vyšetření (formulář, co kterého se údaje přenáší, uživatel vybírá ze seznamu již existujících formulářů)

      - položky vyšetření a formuláře jsou propojeny na základě uživatelem definované xsl transformace, která je blíže popsána v kapitole XSL transformace
- Šablona fyz. nález

   - vedle tlačítka Převzít může být ve vyšetření tlačítko ![image-20250619-063435.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-063435.png>)
   - stisknutím tohoto tlačítka se do vyšetření doplní hodnoty, které jsou předdefinované jako fyziologické
   - tyto hodnoty se definují v modulu Design po stisknutí tlačítka Upravit
   - následně je potřeba vybrat libovolného pacienta (fyziologický nález je definován pro všechny pacienty stejně, vyšetření u tohoto pacienta nebude vytvořené) do vyšetření zadat údaje, které definují fyziologický nález – definice pracuje s kódy položek bloků a jejich hodnotami
   - Např. `<VYZ H="1" N="přiměřená" /><KUZ H="1" N="normální nález" /><OKO H="1" N="normální nález" /><BAR H="1" N="fyziologický" /><VISP H="1" N="normální nález" /><VISL H="1" N="normální nález" /><SLCH H="1" N="normální nález" /><REC H="1" N="řeč a hlas bez odchylek" /><ZUB H="1" N="chrup sanován" /><NDU H="1" N="normální" /><KON H="1" N="normální nález" /><PER H="1" N="fyziologický nález" /><PAT H="1" N="fyziologický nález" /><DRZ H="1" N="normální nález" /><LYM H="1" N="nezvětšeny" /><KAR H="1" N="souměrné, bez šelestu" /><STI H="1" N="fyziologický nález, struma nezjištěna" /><HRU H="1" N="fyziologický nález" /><BRI H="1" N="fyziologický nález" /><EKG H="1" N="normální nález" /><PRS H="1" N="normální nález" /><MOC H="1" N="normální nález" /><RCT H="1" N="fyziologický nález" /><HEM H="1" N="negativní" /><SOC H="1" N="normální" /><POS H="1" N="žádné" /><CZS H="1" N="stav velmi dobrý" />`

## Položky

V dolní části okna se definují samotné položky vyšetření.

Každé vyšetření se skládá z tzv. bloků. Každý blok obsahuje alespoň jednu položku. Každé vyšetření obsahuje alespoň jeden blok (a proto nelze smazat blok v případě, že je zadefinován pouze jeden).

![image-20250619-063616.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-063616.png>)
Název bloku se v daném vyšetření zobrazuje zvýrazněný modře.

![image-20250619-063639.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-063639.png>)
Do definice vyšetření je možné přidat prázdný blok s jednou položkou pomocí tlačítka „Přidat položku“. Pomocí tlačítka Přidat blok je možné přidat celý již dříve definovaný blok.

Po výběru konkrétního bloku má uživatel dvě možnosti jeho vložení.

![image-20250619-063658.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-063658.png>)
Pokud je blok přidán jako odkaz na původní blok, pak přidaný blok není možné měnit. Pokud uživatel přidá blok jako editovatelnou kopii, může blok do vyšetření vložit a následně jej upravovat.

Na úrovni bloku je také možné definovat měření, které je potřeba do vyšetření zadat.

V definici bloku je možné určit jeho

- Název
- Typ zobrazení

   - Row (textová pole v řádku)
   - CheckBoxPanel (panel checkboxů, který je oddělen od ostatních bloků horizontální čarou)
   - Separator (je zadán před a za blok, který má být zobrazen pouze za daných podmínek
   - DatePanel (panel položek typu datum, data se řadí horizontálně)
- Omezit pro - obě pravidla je možné vzájemně kombinovat

   - Věk - blok se zobrazí pouze u pacienta, jehož věk spadá od definovaného rozmezí
   - Pohlaví - blok se zobrazí pouze u pacienta, jehož pohlaví v kartě odpovídá zadanému

### Jak přidat blok měření

Měření je možné zadat dvěma způsoby

A) **Jako položku**

Ke stávající editovatelné položce vyšetření nebo k nové položce vyšetření je možné připojit položku měření

![image-20260601-113439.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20260601-113439.png>)
V takovém případě bude ve vyšetření textové pole (nebo checkbox), protože každá položka vyšetření musí mít alespoň jednu položku a k té bude přiřazeno měření. Nejnovější hodnoty zadané v měření v dekurzu se budou dotahovat do nově vytvořené prohlídky do stejnojmenných polí.

B) **Jako měření**

V případě, že je potřeba vytvořit samostatný blok měření bez jakékoli další položky, tak je možné pomocí tlačítka Přidat blok ![image-20260601-113726.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20260601-113726.png>)
 . Zde vybrat jakoukoli položku Měření a zvolit možnost Přidat jako editovatelnou kopii.

![image-20260601-113841.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20260601-113841.png>)
Tímto způsobem bude přidána položka měření, kde uživatel dodefinuje konkrétní měření (přidá nebo ubere ze stávajících) hodnot měření.

![image-20260601-114133.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20260601-114133.png>)

## Položky vyšetření

Položky vyšetření lze přidávat pomocí tlačítka plus

![image-20250619-063848.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-063848.png>)
U samotné položky lze definovat:

- Název – pod jakým názvem se položka zobrazí ve vyšetření
- Kód – měl by být v rámci daného vyšetření unikátní
- ToolTip - vysvětlivka, jejíž text se zobrazí po najetí myši nad položku v dané prohlídce
- Převzít hodnotu - indikuje, zda se má v rámci použití tlačítka *Převzít* obsah tohoto pole přebírat

   - Převzít vždy - obsah pole v nové prohlídce se nahradí obsahem pole z přebírané prohlídky bez ohledu na to, zda již bylo pole právě založené prohlídky uživatelem vyplněno
   - Převzít při prázdné hodnotě - obsah pole v nové prohlídce se nahradí obsahem pole z přebírané prohlídky pouze za předpokladu, že je pole v nově vytvořené prohlídce aktuálně prázdné
   - Nepřebírat - obsah pole se nikdy z původní prohlídky nepřevezme
- Omezení položky podle věku pacienta nebo pohlaví - pokud je zobrazení položky omezeno věkem, pak se položka zobrazuje za těchto podmínek

   - Pokud je v definici prohlídky definován Věk od (dny), pak se tento údaj považuje za věk pacienta bez ohledu na jeho aktuální věk. Např. preventivní prohlídka v 15 letech má vyplněn Věk od (dny) 5479. Pokud je pacientovi vystavena tato prohlídka, bere se tento věk jako aktuální věk pacienta pro zobrazení bloků omezených věkem. Není tak nutné pro každou preventivní prohlídku definovat speciální blok. Je možné vytvořit pouze jeden a až jednotlivé položky omezit věkem. Např. blok „Řeč“ je možné vložit do vložit do všech preventivních prohlídek a až na jednotlivých položkách definovat podmínku pro věk, kdy se mají zobrazovat

![image-20250619-063929.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-063929.png>)
![image-20250619-063946.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250619-063946.png>)
- Hodnoty – zda se má jednat o varianty, textové pole, checkbox nebo datum

## Výkony

V záložce Výkony je možné definovat výkony, které může uživatel vykázat přímo z dané prohlídky po stisku tlačítka ![image-20250627-083536.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250627-083536.png>)
.

![image-20250627-083555.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250627-083555.png>)
Zadané výkony mohu mít tři různé podmínky, za kterých jsou vykazovány

- Hlavní výkony

   - Při vykazování výkonů lze vybrat právě jeden z hlavních výkonů

Např. pro preventivní prohlídku budou definované dva hlavní výkony: KOMPLEXNÍ VYŠETŘENÍ PRAKTICKÝM LÉKAŘEM nebo OPAKOVANÉ KOMPLEXNÍ VYŠETŘENÍ PRAKTICKÝM LÉKAŘEM

- Svázané výkony

   - Uživatel bude mít možnost vybrat žádný až více svázaných výkonů

Např. pro preventivní prohlídku může být jako svázaný výkon definován Signální výkon 01543

- **Volitelné výkony**

   - Uživatel bude mít možnost vybrat žádný až více volitelných výkonů

Např. pro preventivní prohlídku může být jako volitelný výkon definován výkon ČASNÝ ZÁCHYT DEMENCE V ORDINACI PRAKTICKÉHO LÉKAŘE

## XSL transformace

Po kliku na tlačítko Navazující formuláře se otevře okno pro definici transformace.

![image-20250627-083835.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250627-083835.png>)
Zeleným tlačítkem Plus je možné přidat formulář, do kterého mají být přeneseny údaje zadané do vyšetření. K jednomu vyšetření může být zadáno více formulářů.

V levé části uživatel vybere předlohu tisku (formulář) a jeho konkrétní variantu.

Na konkrétním příkladu budou demonstrovány způsoby definice xsl transformace. Jedná se o toto vyšetření:

![image-20250627-083958.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250627-083958.png>)
Transformace:

`<?xml version="1.0" encoding="UTF-8"?>`

`<xsl:stylesheet version="1.0" xmlns:xsl="`[http://www.w3.org/1999/XSL/Transform](http://www.w3.org/1999/XSL/Transform)` ">`

`                <xsl:output method="xml" omit-xml-declaration="yes" indent="yes" />`

`                <xsl:template match="/">`

`                               <values>`

`                 <xsl:apply-templates select="Galen.Vysetreni" />`

`                               </values>`

`                </xsl:template>`

### Varianty 1

*<!--V  následující části je definovaná transformace této položky vyšetření. Položka má kód „posuzovaný“ a jedná se o položku typu varianty se třemi hodnotami. V konkrétním formuláři se jedná po položku propertyname „posouzeny“. V případě, že uživatel ve vyšetření vybere třetí variantu, tak se do formuláře dotáhne také text u této varianty lékařem zadaný.-->*

![image-20250627-084225.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250627-084225.png>)
`<xsl:template match="Galen.Vysetreni">`

`<!-- Část A) Posuzované dítě k účasti na zotavovací akci -->`

`<xsl:choose>`

`<!-- a)   je zdravotně způsobilé *) -->`

`<xsl:when test="DataProhlidky/posuzovany/@H=1">`

`<posouzeny>0</posouzeny>`

`</xsl:when>`

`<!-- b)   není zdravotně způsobilé -->`

`<xsl:when test="DataProhlidky/posuzovany/@H=2">`

`<posouzeny>1</posouzeny>`

`</xsl:when>`

`<!-- c)    je zdravotně způsobilé za podmínky (s omezením) a text k tomu -->`

`<xsl:when test="DataProhlidky/posuzovany/@H=3">`

`<posouzeny>2</posouzeny>`

`</xsl:choose>`

### Varianty 2

*<!-- V následující části je definovaná transformace této položky.Opět se jedná o položku typu varianty s kódem „podr“. Položka formuláře má propertyname „ocko“.-->*

![image-20250627-084808.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250627-084808.png>)
`<!-- a)   se podrobilo stanoveným pravidelným očkováním-->`

`<xsl:choose>`

`<!-- ano-->`

`<xsl:when test="DataProhlidky/podr/@H=1">`

`<ocko>0</ocko>`

`</xsl:when>`

`<!-- ne-->`

`<xsl:when test="DataProhlidky/podr/@H=2">`

`<ocko>1</ocko>`

`</xsl:when>`

`</xsl:choose>`

### Text

*<!--Dalšími položkami je položka typu text. V prohlídce má položka kód „*nak*“, ve formuláři se jedná o položku propertyname „*imun*“.-->*

![image-20250627-084951.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250627-084951.png>)
`<!--b)    je proti nákaze imunní  -->`

`<xsl:if test="DataProhlidky/nak">`

`<imun><xsl:value-of select="DataProhlidky/nak"/></imun>`

`</xsl:if>`

` `

`<!--c)     má trvalou kontraindikaci proti očkování (typ/druh)   -->`

`<xsl:if test="DataProhlidky/ock">`

`<kontra><xsl:value-of select="DataProhlidky/ock"/></kontra>`

`</xsl:if>`

` `

`<!--d)    je alergické na   -->`

`<xsl:if test="DataProhlidky/aler">`

`<alerg><xsl:value-of select="DataProhlidky/aler"/></alerg>`

`</xsl:if>`

`               `

`<!--e)    dlouhodobě užívá léky (typ/druh, dávka) -->`

`<xsl:if test="DataProhlidky/leky">`

`<leky><xsl:value-of select="DataProhlidky/leky"/></leky>`

`</xsl:if>`

`</xsl:template>`

`</xsl:stylesheet>`

Informace z vyplněného očkování

![image-20250627-085223.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250627-085223.png>)
se přenesou do formuláře

![image-20250627-085234.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Prohlídky/assets/image-20250627-085234.png>)
