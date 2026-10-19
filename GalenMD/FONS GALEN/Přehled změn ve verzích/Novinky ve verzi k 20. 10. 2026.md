---
title: "Novinky ve verzi k 20. 10. 2026"
version: 1
updated_at: 2026-10-19
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/646610945
---

# Novinky ve verzi k 20. 10. 2026

# Novinky a vylepšení

---

## Pediatrie

### Percentilové grafy krevního tlaku

V ordinaci pediatra se na záložce **Tlak** v grafu výsledků měření nově zobrazují percentilová pásma systolického a diastolického tlaku (50., 90., 95. a 99. percentil) podle pohlaví, věku a výškového percentilu dítěte. Po najetí myší na bod v grafu se zobrazí věk, naměřená hodnota a percentil TK. Podrobný popis naleznete [[Percentilové grafy krevního tlaku (pediatr)|zde]].

## Rehabilitace – FT poukazy

### Lhůta pro zahájení terapie

V přehledu **Poukazy FT**, v detailu poukazu a v panelu Poukazy FT na obrazovce **Výkony** se nově zobrazuje datum **Zahájení do**. Je to nejzazší termín, do kdy musí být terapie na poukaz zahájena. Počítá se od data vystavení podle nastavení **Výchozí doba do zahájení [dny]** v *Nástroje → Specializované moduly → Rehabilitace*. Výchozí hodnota je 40 dní.

### Platnost FT poukazu v měsících

**Výchozí platnost poukazu** se v *Nástroje → Specializované moduly → Rehabilitace* nově zadává v kalendářních měsících (1–12). Podle ní se počítá platnost nově vystavených FT poukazů. Dosavadní nastavení pracovišť se při nasazení verze automaticky převede ze dnů na měsíce.

### Přehled FT poukazů za celé pracoviště

Ikona **Poukazy FT** v Kartotéce je nově dostupná i bez výběru pacienta. Přehled má záložky **Pracoviště** a **Pacient** a rozšířený filtr: IČP žadatele, Platnost do, Datum zahájení, Stav, Aktuálně platný a Diagnóza.

## Elektronické zdravotnictví

### Obnova certifikátu PZS přímo ve FONS Galen

Mění se místo, kde se certifikát PZS nastavuje. Celá konfigurace komunikace PZS je nově na jednom místě, pod tlačítkem **Konfigurace PZS** v detailu společnosti:

- hlavní společnost: *Správce → Správa organizace → Struktura → společnost*
- podřízená společnost: *Správce → Správa organizace → Agendy → Podřízené společnosti → společnost*

Tady lze platnost certifikátu nově obnovit přímo ve FONS Galen, bez práce v portálu EZCA. Stačí zadat a potvrdit nové heslo a kliknout na **Obnovit**. Průběh i historie pokusů jsou vždy vidět a při chybě lze obnovu zopakovat. Obnovit jde jen aktivní certifikát, kterému ještě neskončila platnost. Podrobný postup naleznete [[Obnova certifikátu PZS ve FONS Galen|zde]].

## Správa systému

### Nová role Administrátor (omezená práva)

Přibyla role **Administrátor (omezená práva)** pro administrátory, kteří nepotřebují upravovat uživatele a pracovníky. Uživatelé s touto rolí mají záložky **Uživatelé** a **Struktura** jen pro čtení, bez možnosti úprav a zakládání nových záznamů. Podrobný popis naleznete [[Role uživatele|zde]].

# Opravy chyb

---

## Návrat adresy pobytu v eDPN

Opravena chyba, kdy se po skončení dočasné změny adresy pobytu v eDPN adresa nevrátila včas na původní. Neschopenku pak po ukončení nešlo vytisknout bez ručního doplnění adresy.
