---
title: "Recepce a objednávání PLS"
version: 1
updated_at: 2026-06-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/461045761
---

# Recepce a objednávání PLS

Tato stránka popisuje práci s PLS v modulech Recepce a Objednávání — přehled lhůt zaměstnanců, správu objednávek a konfiguraci parametrů prohlídek a eŽádanek podle nákladových středisek.

---

## 1. Barevné rozlišení lhůt

V modulech Recepce a Objednávání jsou záznamy PLS pacientů barevně rozlišeny podle stavu lhůty příští prohlídky:

| Barva | Podmínka |
| --- | --- |
| **Šedá** | Na pacientovi a firmě neexistuje ukončená PLS prohlídka ovlivňující lhůtu, nebo datum plánované prohlídky je v minulosti, nebo datum zaměstnání „do" je menší než aktuální den. |
| **Zelená** | Datum plánované prohlídky je více než 90 dní v budoucnosti. |
| **Oranžová** | Datum plánované prohlídky je 15–90 dní v budoucnosti. |
| **Červená** | Datum plánované prohlídky je 0–15 dní (včetně dnešního dne). |

---

## 2. Klíčové informace zobrazené u pacienta

| Pole | Popis |
| --- | --- |
| **Interval prohlídky** | Zobrazuje se vždy, je-li vypočitatelný. Počítá se jako minimum z intervalů všech rizik přiřazených PLS skupině pacienta. |
| **Platnost posudku** | Přepisuje se na kartu pacienta. Určuje datum plánované prohlídky pouze tehdy, pokud: (1) neexistuje ukončená hlavní PLS prohlídka k dané firmě, (2) je v daném období na pobočce aktivní vedení lhůtníku, a (3) správce nestanovil datum prohlídky ručně. Zobrazuje se a lze přepsat i v případě, kdy je datum v minulosti. |
| **Výsledek poslední prohlídky** | Přepíše se okamžitě do PLS aplikace a PLS Admina. Do výpočtu plánované prohlídky vstupuje pouze v případě, kdy neexistuje výsledek předposlední prohlídky — tehdy se obě hodnoty porovnávají. |
| **Poslední prohlídka OL** | Zobrazuje datum návštěvy z prohlídky. Pro zobrazení prohlídky NL musí mít prohlídka v Designéru nastaven příznak „Ovlivňuje lhůtu — Ne". |

**Texty u pole Plánovaná prohlídka:**

- *určeno lékařem* — datum stanovil lékař přímo na prohlídce
- *určeno správcem* — datum nastavil správce v okně PLS Admin
- *z importu* — datum pochází z importu nebo z data platnosti posudku
- Bez textu — datum bylo dopočítáno systémem automaticky

---

## 3. Stav objednávky

Celkový přehled objednávek je zobrazen v postranním panelu u firmy. Aby se objednávka zobrazila, musí být typ objednávky **PLS** (vytvořená přes tlačítko PLS — vytváří se vazba na položku smlouvy PLS).

| Stav | Podmínka |
| --- | --- |
| **Není objednán** | Neexistuje PLS objednávka v kalendáři, nebo je objednávka v minulosti. |
| **Objednán** | Existuje PLS objednávka na dnešek nebo v budoucnosti, přičemž dosud nebyla vytvořena odpovídající PLS prohlídka. Zobrazuje se vždy nejpozdější budoucí objednávka. |
| **K objednání** | Stav nastavitelný pouze v PLS aplikaci. V Recepci a Objednávání se zobrazí poznámka z PLS aplikace a tlačítko „Zrušit" (nastaví stav zpět na Není objednán). |

> [!info]
> Tooltip nad objednávkou zobrazuje: uživatel, pracoviště a čas vytvoření objednávky. Při více objednávkách se zobrazuje vždy ta s nejvyšším datem (nejdále v budoucnosti). Nová objednávka přepíše záznam u všech firem ve stavu „Objednán", pokud má vyšší datum objednání.

---

## 4. Tlačítko PLS — vytvoření objednávky

Po kliknutí na tlačítko **PLS** v Recepci nebo Objednávání se zobrazí výběr prohlídek (stejný jako v okně Prohlídky a vyšetření). Po zvolení prohlídky se otevře okno s možností:

- Přidat další sortiment k objednávce.
- Vybrat skupinu pracovišť a konkrétní pracoviště.
- Zobrazit dostupné kalendáře vybraných pracovišť (defaultně zobrazeno od začátku aktuálního týdne).

Po vytvoření objednávky se do interní poznámky pro lékaře automaticky zapíše název prohlídky a přidané položky. U objednávky typu PLS prohlídka se nabídne combo-box s výběrem PLS prohlídky pro přiřazení. V combo-boxu jsou všechny položky ze všech smluv dané pobočky.

---

## 5. Konfigurace prohlídky a eŽádanky (nákladová střediska)

Funkce umožňuje přednastavit povinné parametry PLS prohlídek a předvyplněné položky eŽádanek na základě pracovního zařazení pacienta (nákladového střediska). Předejde se tím chybám — systém upozorní lékaře, pokud zadá parametry nad nebo pod doporučený výběr.

> [!info]
> Podmínka: Na společnosti musí být aktivní nadstandardní modul **Nákladová střediska**. Viz také stránku [[Nákladová střediska]].

Přístup: **Nadstandardní péče → detail firmy → záložka Nákladová střediska → označit středisko → tlačítko Konfigurace prohlídky / Konfigurace eŽádanky**

### 5.1 Konfigurace prohlídky

1. Vyberte **Sortiment prohlídky** — nabízejí se všechny PLS prohlídky definované v Ceníkách.
2. Označte položky, které budou při dané prohlídce **povinné** (měkká kontrola).
3. Při ukládání prohlídky systém upozorní, pokud povinné položky chybí — lékař může pokračovat bez změny.

### 5.2 Konfigurace eŽádanky

1. Vyberte **eŽádanku**, pro kterou chcete nastavit předvýběr.
2. Označte položky, které budou při otevření nové eŽádanky automaticky předvyplněné (zaškrtlé).
3. Pokud uživatel odškrtne předvyplněnou položku nebo přidá položku navíc, systém zobrazí informativní upozornění — lze potvrdit a pokračovat.
