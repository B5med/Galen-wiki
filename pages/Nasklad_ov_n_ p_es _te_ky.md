---
id: 83001345
title: "Naskladňování přes čtečky"
version: 3
updated_at: 2026-04-23T13:13:57.862Z
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/83001345
---

# Naskladňování přes čtečky

Připojení čteček schopných číst 2D kódy s FONS Galen pro účely naskladňování očkovacích vakcín. Funkcionalita je zpoplatněna.

# 1          Doporučený HW a jeho konfigurace

Seznam podporovaných čteček 2D kódů a jejich konfigurace je uváděn v podkapitolách.

# 2          Nastavení výchozích hodnot

*Cesta: modul Správce -> modul Správa organizace -> Agendy -> záložka Skladový sortiment - očkování*

V seznamu na záložce „Skladový sortiment - očkování“ jsou zobrazeny skladové karty týkající se očkování. V detailu skladové karty se definuje provázanost mezi SÚKL kódem, PC a typem naskladnění (Látka na volný prodej, …).

V záložce je možné filtrovat dle očkovací látky a zobrazit jen aktivní skladový sortiment za pomocí checkboxu „Jen aktivní“.

## 2.1       Nový skladový sortiment

Přidání nového skladového sortimentu týkající se očkování, kde uživatel definuje provázanost mezi očkovací látkou, SÚKL kódem, PC a typem úhrady.

1. Uživatel stiskne tlačítka Přidat nový záznam (tlačítko „plus“).

2. Uživateli se zobrazí okno Skladový sortiment – očkování.

3. Uživatel vybere Očkovací látku ze seznamu.

4. Uživatel stiskne v části Identifikace tlačítko Přidat nový záznam, kde vyplní SÚKL kód, PC a vybere Typ ze seznamu. Podle potřeby přidá další záznamy.

5. Údaje uloží tlačítkem OK.

## 2.2       Smazání skladového sortimentu

Smazání skladového sortimentu týkající se očkování pro případ, kdy není záznam již potřeba.

1. Uživatel vybere ze seznamu skladový sortiment a stiskne tlačítko Smazat vybraný záznam.

2. Uživateli se zobrazí upozornění „Opravdu smazat vybraný záznam“.

3. Uživatel potvrdí tlačítkem „Ano“.

4. Záznam je smazán.

## 2.3       Editace skladového sortimentu

Za pomocí editace skladového sortimentu lze upravovat (případně mazat) údaje týkající se identifikace, tj. SÚKL kód, PC a typ. Očkovací látku nelze editovat.

1. Uživatel vybere ze seznamu skladový sortiment a stiskne tlačítko Otevřít vybraný záznam.

- Záznam lze otevřít dvojklikem.

2. Uživateli se zobrazí Skladový sortiment – očkování pro editaci.

3. Uživatel upraví údaje:

- Přepíš již existující data
- Přidá další řádek identifikace
- odebere řádek identifikace
- Zneaktivní skladový sortiment za pomocí checkboxu „Aktivní“

4. Uživatel údaje uloží tlačítkem OK.

# 3          Naskladňování

*Cesta 1: modul Správce -> modul Sklad*

*Cesta 2: vybrat pracoviště -> modul Sklad*

Pro naskladňování je nutné mít zapojenou a nakonfigurovanou čtečku kódu. Samotný proces naskladňování vyžaduje pouze výběr skladu. Následně již uživatel jen načítá 2D kódy.

1. V modulu Sklad uživatel vybere sklad.

a. Pokud je definovaný pouze jeden sklad, není třeba nic vybírat.

2. Uživatel začne načítat 2D kódy za pomocí čtečky.

3. Jednotlivý skladový sortiment se zapisuje k příslušným skladovým kartám s načtenými údaji.

**Poznámky:**

Pokud načtené údaje neodpovídají formátu 2D kódu nebo jsou poškozen, zobrazí se uživateli informace: „Nelze naskladnit, protože se nepodařilo rozpoznat kód. Ujistěte se, že kód není poškozený nebo zkreslený. Zkuste skenování opakovat.“

Pokud systém na základě načteného PC nedohledá informace k naskladnění, tj. není definované výchozí nastavení, zobrazí se uživateli informace: „Nelze naskladnit, protože pro načtený PC není v nastavení definovaný způsob naskladnění.“

Pokud nebude skladová karta na skladu definována, zobrazí se uživateli upozornění: „Nelze naskladnit, protože pro vybraný sklad není definovaná skladová karta pro načtený PC.“

Pokud bude mít jeden PC nadefinováno více SÚKL kódů nebo typů úhrady (látka na volný prodej, …), zobrazí se uživateli upozornění, ve kterém vybere způsob naskladnění.

Údaje týkající se Počtu balení a Počet dávek vychází z definice skladové karty ve skladu.

Pokud na vybraném skladu je položka již naskladněna, tj. má shodné údaje, navýší se pouze počet o jedno. Nový řádek se nevytváří.

## 3.1       Vyskladnění

*Cesta: modul Správce -> modul Sklad -> vybrat sklad -> vybrat skladovou kartu -> vybrat šarži -> tlačítko Vyskladnit*

Pokud uživatel omylem naskladní větší množství sortimentu, může údaje o množství opravit.

1. Uživatel vybere Důvod vyskladnění „Chyba“

2. Uživatel vyplní Počet vysklad. dávek.

3. Uživatel údaje potvrdí tlačítkem OK.
