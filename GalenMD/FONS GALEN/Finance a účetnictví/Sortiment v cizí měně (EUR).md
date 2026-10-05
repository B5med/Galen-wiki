---
title: "Sortiment v cizí měně (EUR)"
version: 5
updated_at: 2026-10-05
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/621019137
---

# Sortiment v cizí měně (EUR)

## K čemu funkcionalita slouží

Funkcionalita **Sortiment v cizí měně** umožňuje vést vybrané položky ceníku, platby a faktury kromě Kč také v eurech (EUR). Typicky se použije pro fakturaci v účtu pacienta v EUR. U komerčních pojišťoven je možné na faktuře přednastavit fakturační údaje pojišťovny.

Jedná se o nadstandardní placenou funkcionalitu, kterou je možné objednat prostřednictvím e-shopu. Dokud není aktivní, Galen pracuje beze změny pouze v Kč a pole Měna se nikde nezobrazuje.

Základní pravidla:

- **Jeden doklad = jedna měna.** Na jednom pokladním dokladu ani na jedné faktuře nelze kombinovat položky v Kč a v EUR. Na účtu pacienta se ale položky v obou měnách mohou v čase střídat.
- **Jedna pokladna = jedna měna.** Platby v EUR se přijímají do pokladny vedené v EUR.
- **Částky v EUR se přepočítávají na Kč** podle kurzovního lístku. Použitý kurz se na dokladu uloží a později se už nemění.

## Nastavení (správce)

### Kurzovní lístek

**Správa organizace → Konfigurace společnosti → záložka Kurzovní lístek** (kurz lze zadat také na detailu podřízené společnosti)

V poli **Měna** vyberte EUR a tlačítkem **+** přidejte nový řádek s hodnotami **Kurz**, **Platnost od** a případně **Platnost do**.

- Kurz EUR → Kč se zadává ručně na 3 desetinná místa. Platnost do může zůstat prázdná.
- Platnosti kurzů se nesmí překrývat. V jednom dni může platit jen jeden kurz.
- Kurz zadaný na podřízené společnosti má přednost před kurzem společnosti.
- Kurz se vždy hledá k rozhodnému datu: u položky na účtu k jejímu datu, u pokladního dokladu k datu platby a u faktury k datu vystavení.

> ⚠️ Pokud pro dané datum neexistuje platný kurz, nelze doklad ani fakturu v EUR vystavit. Systém zobrazí upozornění.

![image-20261005-081156.png](<../../../pages/FONS GALEN/Finance a účetnictví/Sortiment v cizí měně (EUR)/assets/image-20261005-081156.png>)

### Ceník (sortiment)

V detailu sortimentu přibyl v tabulce **Ceník** sloupec **Měna**, ve kterém se u každé ceny zvolí Kč nebo EUR. Stejná položka sortimentu může mít současně platnou cenu v Kč i v EUR.

![image-20261005-081209.png](<../../../pages/FONS GALEN/Finance a účetnictví/Sortiment v cizí měně (EUR)/assets/image-20261005-081209.png>)

### Bankovní spojení

V detailu bankovního spojení se v povinném poli **Měna** zaškrtne Kč, EUR, případně obě měny. Na faktuře se pak nabízí jen účty, které měnu faktury podporují.

![image-20261005-081332.png](<../../../pages/FONS GALEN/Finance a účetnictví/Sortiment v cizí měně (EUR)/assets/image-20261005-081332.png>)

### Pokladna

V detailu pokladny se v povinném poli **Měna** zvolí, zda je pokladna vedena v Kč, nebo v EUR. Pokladnu, na které už jsou doklady, nelze převést na jinou měnu. V seznamech se pokladna v EUR zobrazuje s označením měny (např. „Pokladna recepce | EUR“).

![image-20261005-081342.png](<../../../pages/FONS GALEN/Finance a účetnictví/Sortiment v cizí měně (EUR)/assets/image-20261005-081342.png>)

### Smlouva s komerční pojišťovnou

**Správa organizace → Struktura → vyberte IČZ → v pravém panelu Smlouvy přidejte nebo upravte smlouvu**

U smlouvy s komerční pojišťovnou se zobrazuje pole **Měna**, ve kterém lze zaškrtnout Kč, EUR nebo obě měny, vždy ale alespoň jednu. U zdravotních pojišťoven se pole nezobrazuje a smlouva je vždy v Kč. Na smlouvě se také vyplňuje **Bankovní spojení**.

Nastavená měna určuje, které položky ceníku se nabídnou pacientovi s touto pojišťovnou a v jaké měně lze pojišťovně fakturovat.

![image-20261005-081355.png](<../../../pages/FONS GALEN/Finance a účetnictví/Sortiment v cizí měně (EUR)/assets/image-20261005-081355.png>)

### Číselník pojišťoven

Komerční pojišťovny doplňuje do číselníku pojišťoven STAPRO, včetně IČO, DIČ a adresy sídla.

## Práce v ordinaci

### 1. Komerční pojišťovna v kartě pacienta

Do karty pacienta se zadá příslušná komerční pojišťovna.

### 2. Zadání položek na účet pacienta

**Stav účtu → Sortiment**

- V okně výběru položek je vidět sloupec **Měna** a filtr podle měny.
- U pacienta s komerční pojišťovnou se nabízí jen sortiment v měně nastavené na smlouvě s jeho pojišťovnou. Výkony se nabízejí vždy.

   ![image-20261005-081634.png](<../../../pages/FONS GALEN/Finance a účetnictví/Sortiment v cizí měně (EUR)/assets/image-20261005-081634.png>)
- Při ručním zadání závazku ve Stavu účtu zvolí uživatel měnu sám.

### 3. Platba v pokladně

- V dialogu Platba se nabízí jen pokladny ve stejné měně, jako mají vybrané položky.
- Pokud vyberete položky v různých měnách, systém platbu odmítne s hlášením, že vybrané položky mají různou měnu. Položky v Kč a v EUR je potřeba zaplatit zvlášť.

   ![image-20261005-081720.png](<../../../pages/FONS GALEN/Finance a účetnictví/Sortiment v cizí měně (EUR)/assets/image-20261005-081720.png>)

### 4. Vystavení faktury

Ve Stavu účtu označte položky a vystavte fakturu. V okně **Zadání údajů faktury**:

1. V části **Převzít údaje z** zvolte tlačítko **Komerční pojišťovna**. Tlačítko se zobrazí jen tehdy, když má pacient v kartě komerční pojišťovnu. Údaje odběratele (název, IČO, DIČ, adresa sídla) se doplní z číselníku pojišťoven a lze je upravit.

   ![image-20261005-081812.png](<../../../pages/FONS GALEN/Finance a účetnictví/Sortiment v cizí měně (EUR)/assets/image-20261005-081812.png>)
2. Zkontrolujte bankovní spojení. Nabízí se jen účty v měně faktury.

> ⚠️ Pokud měna vybraných položek neodpovídá měně nastavené na smlouvě s pojišťovnou, systém výběr pojišťovny jako plátce odmítne. V takovém případě vyberte položky ve správné měně, nebo upravte nastavení měny na smlouvě.

### 5. Úhrada faktury

Po obdržení platby převede uživatel modulu Finance fakturu do stavu **Uhrazená**.

## Zobrazení částek

- Dlaždice **Stav účtu** a hlavička **K zaplacení** zobrazují součty pro Kč a EUR odděleně. Pokud pacient nemá žádné položky v EUR, řádek EUR se nezobrazuje.

## Podrobný filtr v kartotéce

V podrobném filtru kartotéky lze pacienty filtrovat podle rozsahu částek **Úhrada celkem** a **Pohledávky celkem**. Částky se zadávají vždy v Kč a stejně se i vyhodnocují. Doklady a faktury v EUR se do součtu započítávají v Kč, přepočtené kurzem, který byl na dokladu použit. Pacienty s platbami v obou měnách tak lze filtrovat jedním rozsahem.

## Tisk

Faktury a pokladní doklady zobrazují částky v měně dokladu. Používá se tak jedna tisková předloha pro obě měny.

Platební QR kód lze použít i pro platbu v EUR. Ne všechny banky však měnu EUR z QR kódu načtou, záleží na bance plátce. Plátce proto musí po načtení QR kódu zkontrolovat, že platba je zadána ve správné měně.

## Omezení

- PLS zůstává pouze v Kč.
- Vyúčtování na pojišťovny nelze vést v EUR.
