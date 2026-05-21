---
title: "Novinky ve verzi k 10. 3. 2026"
version: 4
updated_at: 2026-03-09
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/297140225
---

# Novinky a vylepšení

#### Tlačítko Objednat ve vyšetření

Do záložky **Prohlídky a vyšetření** bylo přidáno nové tlačítko **„Objednat“** v horní liště.

Po kliknutí se otevře **modul objednání** s automaticky vyplněným:

- pacientem,
- ordinací.

Funkcionalita je stejná jako u stávajícího tlačítka „Objednat“ dostupného na jiné záložce.

#### Přejmenování položky BWR na Syfilis v anamnéze pacienta

V modulu Ordinace byla v záložce Anamnéza upravena položka BWR, která se nyní uživateli zobrazuje pod srozumitelnějším názvem Syfilis. Změna se projeví při výběru pacienta v pravé části anamnézy.

#### Rozšíření pravidla „Nepovolená kombinace výkonů" o kontrolu diagnózy

V modulu **správy pravidel** bylo rozšířeno nastavení pravidla typu **Nepovolená kombinace výkonů** o novou volitelnou podmínku **„Shodná diagnóza“**.

##### Co se změnilo

Na řádku výkonu v definici pravidla je nyní možné přidat podmínku **„Shodná diagnóza“**, která může mít tyto hodnoty:

- **Hlavní diagnóza** – kombinace je zakázaná, mají-li výkony shodnou hlavní diagnózu.
- **Řádková diagnóza** – kombinace je zakázaná, mají-li výkony shodnou řádkovou diagnózu.
- **Hlavní nebo řádková diagnóza** – kombinace je zakázaná, pokud se shoduje hlavní *nebo* řádková diagnóza.

##### Chování systému

- Pokud je podmínka nastavena **a výkony mají ve stejný den u jednoho pacienta shodnou diagnózu** ›
   **vykázání je zablokováno** a zobrazí se chybová hláška.
- Pokud je podmínka nastavena **a výkony mají různé diagnózy** ›
   **vykázání je povoleno**.
- Pokud podmínka **není nastavena** ›
   chování pravidla zůstává beze změny
   *(kombinace je zakázaná vždy, bez ohledu na diagnózu).*

#### Zobrazení rozdílu hmotnosti v záznamu preventivní prohlídky

V záznamu **preventivní prohlídky** bylo vedle kolonky **Hmotnost** doplněno zobrazení rozdílu oproti poslední zaznamenané hodnotě hmotnosti pacienta.

##### Co se změnilo

Pokud je u pacienta evidována předchozí hodnota hmotnosti, zobrazí se nyní automaticky informace o **přírůstku nebo úbytku váhy** od posledního záznamu.

Tato hodnota je vizuálně zvýrazněna (*tooltip*), aby lékař okamžitě viděl, zda u pacienta nastala významná změna hmotnosti.

##### Chování systému

- **Je-li evidována předchozí hmotnost:**
   Zobrazí se vedle pole **Hmotnost** informace o rozdílu (přírůstek/úbytek) oproti poslednímu záznamu.
- **Není-li předchozí hmotnost evidována:**
   Žádná dodatečná informace se nezobrazuje.

##### Přínos

Tato úprava usnadňuje lékařům **rychlé vyhodnocení změn hmotnosti pacienta**, což je obzvláště přínosné při péči o:

- kojence,
- obézní pacienty.

#### Podpora předávání dat o centrové léčbě do registru ÚZIS

V systému **FONS Galen** byla implementována podpora pro povinné předávání dat o **centrové léčbě** do registru **ÚZIS** v souladu s legislativními požadavky Ministerstva zdravotnictví ČR.

##### Funkčnost zahrnuje:

- konfiguraci propojení s ÚZIS,
- evidenci podání inovativních léčivých přípravků u pacientů,
- elektronické odeslání hlášení přes **API ÚZIS**,
- automatické vykazování výkonů a ZUM zdravotní pojišťovně.

##### Více informací

[https://stapro-galen.atlassian.net/wiki/x/AQDLE](https://stapro-galen.atlassian.net/wiki/x/AQDLE)

#### Funkce zobrazení/skrývání hesla

Do polí pro zadávání hesla byla doplněna ikona **„očička“**, která umožňuje dočasné **zobrazení nebo skrytí hesla**. Z bezpečnostních důvodů se ikona pro zobrazení hesla přestane zobrazovat, pokud uživatel opustí pole pro zadání hesla (překlikne se jinam).

##### Kde je funkce dostupná:

- při změně hesla v **profilu uživatele**,
- ve **Správě organizace – Uživatelé**,
- na **přihlašovací obrazovce**.
