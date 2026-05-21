---
title: "Možnost editace vlastních pravidel pro vykazování výkonů"
version: 5
updated_at: 2026-03-09
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/57999370
---

Rozšíření modulu Design o záložku Pravidla uživatelům umožňuje
• Vytvářet vlastní pravidla pro vykazování výkonů

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-085637.png]]
- Neuplatňovat pro společnost pravidla, která jsou zadávána ze strany správců FONS Galen
- Vytvářet pravidla, která

   - omezují frekvenci vykazování výkonů

      ![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-085724.png]]
   - zakazují vykázat kombinaci výkonů
   - zakazují vykázat výkon za určité podmínky
   - definují svázané výkony
- Pravidla vytvořená správcem společnosti je možné uplatnit na

   - Celou společnost
   - Vybranou podřízenou společnost
   - Vybrané IČZ
   - Vybrané IČP
   - Vybranou odbornost
   - Vybranou pojišťovnu

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-085911.png]]

## Popis pravidel

Všechny typy pravidel mají společný základ, konkrétně se jedná o tato pole

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-085930.png]]
**Zveřejnit**

Slouží pro zveřejnění pravidla pro uživatele. Dokud není pravidlo zveřejněno, je dostupné pouze jako testovací definice, kterou si uživatel aktivuje v konfiguraci ![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-090003.png]]
 zatržením položky „Načítat testovací definice“.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-090040.png]]
Tímto způsobem uživatel otestuje nastavení pravidla před tím, než jej publikuje všem uživatelům společnosti.

**Historie**

Uživatel má možnost se vrátit k předcházející publikované definici.

**Definice**

Zobrazí definici ve formátu xml. Tímto způsobem, pokud je to pro uživatele přívětivější, může pravidlo také definovat. Uživatel však musí dodržovat pravidla syntaxe xml. Zde definované pravidlo podporuje pouze ty vlastnosti, které je možné definovat v uživatelském rozhraní.

**OK**

Tlačítko ukládá práci a opouští detail pravidla. Pravidlo se tímto tlačítkem nezveřejňuje, pouze ukládá.

**Uložit**

Umožňuje průběžné uložení rozpracovaného pravidla. Pravidlo se tímto tlačítkem nezveřejňuje, pouze ukládá.

**Zpět**

Opouští detail pravidla bez uložení.

**Aktivní**

Určuje dostupnost publikovaného nebo testovacího pravidla pro uživatele. Při deaktivaci zvažte, zda je potřeba pravidlo deaktivovat, nebo pouze ukončit jeho platnost.

**Název**

Uživatelsky definovaný název pravidla.

**Verze**

Zobrazuje pořadí verze.

**Typ**

Vychází z uživatelem definovaného typu pravidla. Typ není možné změnit.

**Hláška**
Uživatelem specifikovaný vysvětlující text pro ostatní uživatele, který se zobrazuje v editoru výkonů pod tlačítkem![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-090316.png]]
 .

**Omezit pro odbornost**

Je možné nastavit podmínku pravidla, aby bylo uplatňováno pouze při vykazování na konkrétní odbornosti.

**Podmínka**

Umožňuje definovat podmínku, která bude platit pro všechna uvedená pravidla.

## Frekvenční omezení

Frekvenční omezení definují, kolikrát za časové období je možné výkon vykázat.

### Základní definice

Základní definice pravidla říká, kolikrát za časové období je možné výkon vykázat. Např. výkon 01543 je možné vykázat pouze jednou za den. Překročení takto definovaného pravidla je tvrdou chybou, tzn. aplikace nedovolí uživateli frekvenci překročit.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-095151.png]]

#### Přerušení péče

V případě zaškrtnutí checkboxu „Přerušení péče“ probíhá kontrola nejen na počet výkonů za dané časové období, ale také na to, zda byla v daném období přerušena péče, tzn. zda nebyl v definovaném rozsahu (IČP, IČZ, podřízená společnost, společnost) vykázán jiný výkon.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-095228.png]]
V případě takto definované podmínky bude možné výkon vykázat pouze jednou za 2 roky v případě, že byla přerušena péče, tzn. nebyl za poslední 2 roky vykázán jiný výkon.

#### Definice s podmínkou

Definice s podmínkou specifikuje, za kterých podmínek je možné výkon v daném počtu vykázat. Např. výkon 15119 je možné u pacienta ve věku 50-55 let vykázat jednou ročně, u pacienta ve věku nad 55 let je možné výkon vykázat jednou za dva roky. Překročení takto definovaného pravidla je tvrdou chybou, tzn. aplikace nedovolí uživateli frekvenci překročit.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-095313.png]]

### Rozšíření vybraného základního pravidla

Jeden výkon může mít v základním pravidle definován frekvenční omezení, které může být za určité podmínky překročeno. Např. výkon 09113 lze vykázat pouze 1x za den, ale v případě pacientů s respirační insuficiencí před indikací DDOT lze vykázat 6x za den. Při překročení pravidla, které má definovaný tzv. speciální typ, se bude jednat o měkkou chybu. Uživatel bude na překročení frekvence upozorněn, ale systém mu umožní překročenou frekvenci vykazovaného výkonu uložit.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-095339.png]]
Při vykazování výkonu bude uživatel upozorněn, ale pokud volbu potvrdí, systém mu umožní uložit výkon v počtu 8.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-095401.png]]

## Svázané výkony

Svázané výkony definují výkon, který je nutné vykázat v případě vykázání jiného výkonu. Svázané výkony je možné zadat ve dvou režimech.

### Definice právě jednoho doplňovaného výkonu

V případě, že je ve sloupci „Doplňované výkony“ zadán právě jeden výkon, je tento výkon automaticky na pozadí (v případě, že je nasmlouván) vykázán v případě, že je uživatelem vykázán hledaný výkon.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-095523.png]]

### Definice více doplňovaných výkonů

V případě, že je ve sloupci „Doplňované výkony“ zadáno více výkonů, není žádný z uvedených, v případě vykázání hledaného výkonu, vykázán automaticky, ale uživatel je vyzván k výběru jednoho z doplňovaných výkonů.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-095554.png]]
![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250627-095600.png]]

### Svázané výkony vykazované z vyšetření

V definici svázaných výkonů, které se vykazují z vyšetření, je možné zadat podmínky, za kterých bude svázaný výkon vykázán.

## Nepovolené kombinace

Nepovolené kombinace definují kombinace výkonů, které nemohou být zároveň vykázány.

### Definice hlavního výkonu a výkonů, které je možné vykázat

Hlavní výkon definuje podmínku, kdy v případě, že je v daném časovém období daný výkon vykázán, tak je dále v časovém období možné vykázat pouze výkony dále definované.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250721-083801.png]]
Např. pokud je v jeden den vykázán výkon 01022, tak ten stejný dej je možné vykázat pouze výkon 01543. Žádný jiný výkon vykázat nelze.

### Definice výkonů, které nelze společně vykázat

Pokud není definován hlavní výkon, funguje pravidlo jinak, než je uvedeno výše. Pokud jsou definovány pouze výkony bez výkonu hlavního, funguje pravidlo tak, že v daný časový úsek není možné zde uvedené výkony vykázat současně.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250721-083837.png]]
Např. Pokud je vykázán výkon 01022, tak v ten samý den nelze vykázat výkon 01023, a opačně.

### Podmínka *Shoda diagnóz*

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20260309-125056.png]]
Při zadání výkonů, které nelze společně vykázat, je možné definovat, zda se mají při spuštění pravidla kontrolovat diagnózy zadané u jednotlivých výkonů.

- **Nekontrolovat**- výkony nebude možné v rámci definovaného období společně vykázat
- **Hlavní diagnóza** – kombinace je zakázaná, mají-li výkony shodnou hlavní diagnózu
- **Řádková diagnóza** – kombinace je zakázaná, mají-li výkony shodnou řádkovou diagnózu
- **Hlavní nebo řádková diagnóza** – kombinace je zakázaná, shoduje-li se hlavní nebo řádková diagnóza

## Zakázat výkony

Pravidlo typu *Zakázat výkony* definuje podmínky, za kterých nesmí být určitý výkon vykázán. Např. je možné nastavit pravidlo, aby nebylo možné u odbornosti 002 vykázat výkon preventivní prohlídky u neregistrovaného pacienta

## **Kombinace výkonu a diagnózy**

Pravidlo typu *Kombinace výkonu a diagnózy* umožňuje definovat povolené a nepovolené kombinace výkonů a diagnóz. Pro tento typ pravidla lze definovat množinu povolených a nepovolených kombinaci pro výkon.

Pro přidání nové kombinaci se definuje výkon, pro nej pak povolené diagnózy (může být víc než jedna), nebo nepovolené diagnózy (může být víc než jedna). Pro výkon nelze současně definovat povolené i nepovolené diagnózy. Záleží tak na tom, zda je jednodušší vypsat množinu Diagnóz, které mohou být vykázané, nebo naopak množinu pouze zakázaných.

![[pages/FONS GALEN/Správce a nastavení/Design/Možnost editace vlastních pravidel pro vykazování výkonů/assets/image-20250721-084008.png]]
Pokud byla definice pravidla vytvořena pouze s jednou povolenou diagnózou pak je při pořizování výkonu tato diagnóza automaticky doplněna. Pokud byla definice pravidla vytvořena s množinou diagnóz a pokud pak je při pořizování výkonu zadáno více diagnóz pak je otevřeno upozornění, že může být při pořizování výkonu zadána pouze některá z uvedených diagnóz.
