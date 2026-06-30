---
title: "Novinky ve verzi k 29. 6. 2026"
version: 1
updated_at: 2026-06-29
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/476381186
---

# Novinky ve verzi k 29. 6. 2026

# Novinky a vylepšení

---

## Společné

### Formátovaný dekurz – zjednodušení nastavení

V rámci této úpravy bylo nastavení formátovaného dekurzu přesunuto výhradně na úroveň jednotlivého uživatele.

Formátovaný dekurz umožňuje psát záznamy z návštěvy jako formátovaný text – tedy s možností tučného písma, kurzívy, odrážek a dalšího vizuálního členění, místo prostého nečleněného textu.

Každý uživatel si může formátovaný dekurz zapnout nebo vypnout sám v **Konfiguraci Galen** (záložka **Nastavení**) zaškrtnutím volby **„Formátovat dekurz"**.

### Vypnout odřádkování vyšetření v dekurzu

V nastavení pracoviště byla přidána nová konfigurační volba **„Vypnout odřádkování vyšetření"**. Po jejím zapnutí se vyšetření i těhotenské prohlídky zobrazí v dekurzu, denním záznamu, tisku vyšetření i v EZD PDF jako jeden souvislý řádek – obdobně jako u laboratorních výsledků. Součástí úpravy je také doplnění tlačítka Tisk DZ u těhotenské prohlídky v dekurzu a sjednocení jeho umístění vedle jména odpovědného lékaře.

### Přístup k EZPR (externím zprávám) na úrovni pracoviště

Zpracování nových a nezpracovaných EZPR je nově povoleno i jinému než původně odpovědnému lékaři. Lékař vidí a může zpracovat všechny nezpracované EZPR adresované libovolnému lékaři se stejným pracovištěm (IČP) jako on.

## Kalendáře a objednávání

### Storno objednávky v kalendáři – důvod storna a rozšíření statistiky

Funkcionalita „Storno objednávek v kalendáři" je nově dostupná pro všechny uživatele.

**Dialog stornování objednávky**

Při stornu objednávky v kalendáři se v dialogu „Stornovat vybranou objednávku?" pole Důvod stornování mění z volného textu na nepovinný výběr z číselníku s těmito hodnotami:

- Pacient se nedostavil
- Nemoc pacienta
- Nemoc / nepřítomnost lékaře
- Přeobjednání na jiný termín
- Chybná objednávka
- Jiný důvod – po výběru se zobrazí textové pole pro zadání vlastního popisu

Vybraný důvod se ukládá k objednávce a zobrazuje se u objednávky, v historii objednávek a ve statistice. U pole je tooltip vysvětlující výběr ze seznamu a možnost zvolit „Jiný důvod".

**Statistika Přehled objednávek – pacient**

Do statistiky přibyly tři nové prvky, vždy se sloupcem a odpovídajícím filtrem (hodnoty se načítají z existujících polí objednávky):

- **Storno (ano/ne)** – filtr checkbox zobrazí jen stornované, seskupování celkem / s detailem
- **Stornoval (jméno uživatele)** – filtr výběr uživatele, seskupování celkem / s detailem
- **Storno důvod** – filtr výběr ze seznamu

# Opravy chyb

---

## Přiřazení ZUM k výkonu při importu dávky

Při importu K-dávky se ZUM z dokladů typu Z (samostatný doklad ZUM bez výkonu) chybně navazoval na automaticky vytvořený pomocný výkon 01999 místo na skutečný výkon z dokladu A. Po opravě se ZUM přiřazuje správně:

1. ZUM z dokladu Z se naváže na výkon z bezprostředně předcházejícího dokladu A (doklady seřazené dle pořadového čísla).
2. Pokud je takových výkonů více, naváže se na první v pořadí.
3. Pomocný výkon 01999 se vytváří až jako poslední možnost – jen když na dokladu A žádný vhodný nosný výkon není.

**Registrovaný vs. neregistrovaný pacient:**

- **Registrovaný pacient** – logika kapitačních / nekapitačních výkonů nyní funguje i při importu (dříve byla pouze při ručním zadávání). ZUM se nenavazuje přímo na kapitační výkon (např. 09215), ale vytváří se pomocný výkon 01999.
- **Neregistrovaný pacient** (doklad 05, nepravidelná péče) – ZUM je navázán přímo na nosný výkon (např. 09215), pomocný výkon 01999 se v tomto případě nevytváří.

**Ruční přeřazení ZUM (nová funkce)**

Na obrazovce Aktivace výkonů lze ZUM ručně přeřadit k jinému výkonu metodou drag & drop. Řádek ZUM má na začátku úchopovou ikonu (tooltip „Přetáhněte k jinému výkonu"); při tažení se zvýrazní povolené cílové výkony. Slouží jako manuální korekce tam, kde automatické přiřazení neodpovídá potřebě.
