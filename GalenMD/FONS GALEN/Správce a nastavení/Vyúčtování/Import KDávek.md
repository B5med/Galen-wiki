---
title: "Import KDávek"
version: 3
updated_at: 2026-06-29
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/75792496
---

# Import KDávek

Správce -> Správa organizace -> Vyúčtování ->  Import KDavek

![image-20250618-131627.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Import KDávek/assets/image-20250618-131627.png>)
Přes Tlačítko Import KDavek v modulu Vyúčtování vkládáme KDavku obsahující vykázané výkony, tedy přesně takovou, jakou odesíláme do zdravotní pojišťovny.

![image-20250618-131717.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Import KDávek/assets/image-20250618-131717.png>)
Zeleným + vlevo nahoře vytváříme nový import, klikem na modrou tužku editujeme stávající importovaný soubor a červeným mínusem lze označený naimprotovaný soubor smazat.

#### **Nový import KDavek**

Po stisku zeleného + se zobrazí okno, ve kterém vybíráme soubor s názvem např. KDAVKA.211, pokud se jedná o soubor zdravotní pojišťovny 211.

Po vybrání správného souboru se zobrazí okno s obsahem vybraného souboru:

![image-20250618-131859.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Import KDávek/assets/image-20250618-131859.png>)
V tomto místě je vhodné zkontrolovat zejména fakt, zda se jedná o správné IČZ a IČP. Po této kontrole zvolíme tlačítko Importovat. Odtržení zvolených checkboxů lze některé položky z importu vyloučit.

![image-20250618-131919.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Import KDávek/assets/image-20250618-131919.png>)
Po úspěšném, importu zvolíme tlačítko Aktivovat. Poté dochází ke kontrole a zobrazení nesouladů, které je nutné před aktivací upravit:

![image-20250618-131936.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Import KDávek/assets/image-20250618-131936.png>)
Vlevo před jménem pojištěnce je vždy uvedeno, zda je výkon pro import v pořádku označením zelenou „fajfkou“. V případě potřeby úpravy je před číslem pojištěnce vykřičník ve žlutém poli. Takový řádek je nutné označit a v pravém sloupci se zobrazí důvod problému. Takový výkon lze vyjmout z aktivace či úplně smazat z dávky. Po úpravách je nutné zvolit OK.

![image-20250618-131951.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Import KDávek/assets/image-20250618-131951.png>)
Po stisku OK se zobrazí okno, kde v levém horním rohu zvolíme tlačítko Dokončit.

![image-20250618-132010.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Import KDávek/assets/image-20250618-132010.png>)
Import a aktivace importu nemusí být vždy zcela dokončeny.

**IS Galen eviduje tyto stavy Importovaných souborů**:

- Rozpracovaný
- V průběhu aktivace
- Aktivovaný
- Uzavřený

Po dokončení Aktivace je import označen jako Aktivovaný.

![image-20250618-132032.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Import KDávek/assets/image-20250618-132032.png>)

#### **Přiřazení ZUM k výkonu při aktivaci dávky**

Při importu K-dávky se ZUM z dokladů typu Z (samostatný doklad ZUM bez výkonu) navazuje na skutečný výkon z dokladu A takto:

1. ZUM z dokladu se naváže na výkon z bezprostředně předcházejícího dokladu (doklady seřazené dle pořadového čísla).
2. Pokud je takových výkonů více, naváže se na první v pořadí.
3. Pomocný výkon 01999 se vytváří až jako poslední možnost – jen když na dokladu žádný vhodný nosný výkon není.

**Registrovaný vs. neregistrovaný pacient:**

- **Registrovaný pacient** – logika kapitačních / nekapitačních výkonů funguje i při importu. ZUM se nenavazuje přímo na kapitační výkon (např. 09215), ale vytváří se pomocný výkon 01999.
- **Neregistrovaný pacient** (doklad 05, nepravidelná péče) – ZUM je navázán přímo na nosný výkon (např. 09215), pomocný výkon 01999 se v tomto případě nevytváří.

**Ruční přeřazení ZUM**

Na obrazovce Aktivace výkonů lze ZUM ručně přeřadit k jinému výkonu metodou drag & drop. Řádek ZUM má na začátku úchopovou ikonu (tooltip „Přetáhněte k jinému výkonu"); při tažení se zvýrazní povolené cílové výkony. Slouží jako manuální korekce tam, kde automatické přiřazení neodpovídá potřebě.
