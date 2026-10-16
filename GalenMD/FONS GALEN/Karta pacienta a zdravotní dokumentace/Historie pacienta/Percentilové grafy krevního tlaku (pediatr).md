---
title: "Percentilové grafy krevního tlaku (pediatr)"
version: 6
updated_at: 2026-10-16
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/638517250
---

# Percentilové grafy krevního tlaku (pediatr)

## Popis funkcionality

Záložka **Tlak** v grafu výsledků měření zobrazuje pro odbornost **Praktický lékař pro děti a dorost (002)** percentilová pásma systolického (STK) a diastolického (DTK) krevního tlaku. Hodnocení vychází z referenčních hodnot dle pohlaví, věku a výškového percentilu dítěte (Cor Vasa 2009).

![image-20261016-083758.png](<../../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Historie pacienta/Percentilové grafy krevního tlaku (pediatr)/assets/image-20261016-083758.png>)

## Kde funkci najdu

Modul Ordinace → vybrat pacienta → záložka **Historie** → **Měření** → tlačítko **Grafy měření** → tlačítko **Tlak**

## Popis grafu

Graf zobrazuje naměřené hodnoty STK a DTK pacienta v čase a jejich polohu vůči percentilovým pásmům. Pásma jsou zobrazena ve dvou sadách — pro systolu (fialová) a diastolu (zelená).

| Pásmo | Barva | Klinický význam |
| --- | --- | --- |
| 99. percentil | nejsvětlejší | hranice hypertenze 2. stupně |
| 95. percentil | střední | hranice hypertenze 1. stupně |
| 90. percentil | nejtmavší | hranice vysokého normálního TK |
| 50. percentil | bílá čára | medián referenčních hodnot |

Systola je zobrazena modrou křivkou, diastola zelenou křivkou.

## Tooltip

Po najetí na bod měření se zobrazí:

- věk pacienta v době měření (např. 10r2m)
- naměřená hodnota v mmHg
- TK percentil
- ⚠ upozornění na stav výšky — pokud výška není ze stejného dne nebo není k dispozici

## Výška pacienta

Percentilová pásma se počítají s ohledem na výšku pacienta. Systém hledá výšku prioritně ze stejného dne jako měření TK. Pokud výška ze stejného dne není k dispozici, použije nejbližší dostupnou hodnotu a upozorní na to v tooltipu.

## Omezení

- Graf se zobrazuje pouze pro věk **1–17 let**. Pro pacienty mimo tento rozsah se záložka Tlak zobrazí bez percentilových křivek.
- Pokud pohlaví pacienta není vyplněno, použijí se referenční hodnoty pro chlapce.
- U malých dětí (věk 1–5 let) se mohou fialová a zelená pásma vizuálně prekývat — jde o běžný stav daný biologickými hodnotami.

## Zdroj referenčních hodnot

Referenční hodnoty krevního tlaku vycházejí z guidelines ESH 2016. Tabulky hodnot jsou dostupné na: [Hypertenze (pediatrie) – tabulka – WikiSkripta](https://www.wikiskripta.eu/w/Hypertenze_(pediatrie)_-_tabulka)
