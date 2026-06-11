---
id: 78348323
title: "Výpočet KVO dle Score 2"
version: 1
updated_at: 2025-07-23T11:10:06.420Z
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/78348323
---

# Výpočet KVO dle Score 2

none

Tento manuál vysvětluje kroky potřebné pro konfiguraci a použití nové funkce pro výpočet rizika kardiovaskulárních onemocnění (zkratka KVO) na základě skóre 2 v měření a v prohlídce.

Funkcionalita "Výpočet rizika KVO dle Score2" je placenou službu. Pro aktivaci služby prosím kontaktujte naše obchodní oddělení.

## Výpočet rizika KVO dle SCORE2

Výpočet rizika lze provádět na dvou místech:

1. Obrazovka Měření návštěvy – přes dekurz pacienta
2. Prohlídka pacienta – prohlídka jejíž součástí je výpočet rizika KVO dle SCORE 2

Informace týkající se rizika KVO dle score 2 jsou součástí anamnézy pacienta.

### Výpočet rizika v měření

*Cesta: vybrat pracoviště -> modul Ordinace -> vybrat pacienta -> záložka Dekurz -> možnost Zadat měření*

1. Sekce Tlak, puls – zde doplnit hodnoty do položky Tlak (mmHg).

   1. Do výpočtu vstupuje pouze hodnota systolického krevního tlaku.
2. Sekce Riziko KVO dle score 2 – zde doplnit hodnoty do položky Cholesterol non-HDL (mmol/l)

   1. Pokud má pacient laboratorní výsledky, ve kterých je uvedena položka cholesterolu non-HDL, lze ji dohledat za pomocí tlačítka Doplnit z lab. v.
   2. Systém prohledává výsledky od nejnovější po nejstarší a doplní nejnovější hodnotu včetně data výsledku. Uživatel může doplněnou hodnotu přepsat.
3. Na základě hodnot se dopočítá hodnota Score 2 KVO a vyhodnotí se riziko (položka Hodnocení rizika).

### Výpočet rizika v prohlídce

*Cesta: vybrat pracoviště -> modul Ordinace -> vybrat pacienta -> záložka Prohlídky a vyšetření -> Nová prohlídka -> vybrat prohlídku*

1. Sekce Měření – zde doplnit hodnoty do položky Tlak a Cholesterol non-HDL (mmol/l).

   1. Do výpočtu vstupuje pouze hodnota systolického krevního tlaku.
2. Výpočet potvrdit klávesnicí Enter nebo tlačítkem Vypočítat.

   1. Pokud není hodnota cholesterolu vyplněna a uživatel stiskne tlačítko Vypočítat, systém automaticky doplní hodnotu z laboratorního vyšetření, pokud položka existuje. Uživatel může doplněnou hodnotu přepsat.
3. Na základě hodnot se dopočítá hodnota Score 2 KVO a vyhodnotí se riziko (položka Hodnocení rizika).

### Informace k výpočtu

Podbarvení u Score 2 KVO a Hodnocení rizika:

- Zelená barva znamená nízké až středně zvýšené KV-riziko
- Oranžová barva znamená vysoké KV-riziko
- Červená barva znamená velmi vysoké KV-riziko

Výpočet není proveden, pokud:

- Není uvedeno datum narození pacienta.
- Není uvedena hodnota non-HDL cholesterol.
- Není uveden systolický tlak v měření.
- Cholesterol je menší než 3 nebo je větší než 6,9.
- Pacient je mladší než 40 let nebo starší než 89 let.
- Pokud je pacient starší než 89 let, tak je bez výpočtu zařazen do kategorie velmi vysoké KV-riziko.

Riziko KVO ovlivňuje kouření, proto je nutné pro správný výpočet kouření uvést v anamnéze. Pokud v anamnéze tento údaj není uveden, výpočet považuje pacienta za nekuřáka.

## Filtr

Pacienty dle hodnot rizika lze vyhledat v kartotéce za pomocí podrobného filtru, kde jsou položky:

- KV Score 2 - riziko – vyhledání na základě hodnocení rizika

  - Lze vybrat více možností.
- KVO-Score 2 od … do – pro vyhledávání na základě konkrétních hodnot score 2

*Cesta: vybrat pracoviště -> modul Ordinace -> tlačítko Podrobný filtr*

## Modul Design

Přes modul Design lze nastavit položky týkající se výpočtu Score 2 do jakékoliv uživatelské prohlídky.

*Cesta: modul Správce -> modul Design -> tlačítko Prohlídky*

1. Uživatel vybere uživatelskou prohlídku.
2. Na záložce Položky stiskne tlačítko Přidat blok.
3. Vybere blok s názvem Měření a zvolí možnost Přidat jako editovatelnou kopii.
4. Do Položky měření přidá (tlačítko plus) položky týkající se Score 2, tj.:

   1. Tlak
   2. Cholesterol non-HDL (mmol/l)
   3. Score 2 KVO
   4. Hodnocení rizika dle score 2 KVO
5. Položky uživatel uspořádá v rámci prohlídky za pomocí tlačítek Posunout položku nahoru nebo Posunout položku dolů.

6. Následně změny uživatel potvrdí tlačítkem OK a zveřejní tlačítkem Zveřejnit.

7. Okno s potvrzením zveřejnění potvrdí tlačítkem OK.
