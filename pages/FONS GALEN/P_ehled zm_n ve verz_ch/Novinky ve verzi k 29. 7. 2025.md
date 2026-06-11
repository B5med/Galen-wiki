---
id: 83427332
title: "Novinky ve verzi k 29. 7. 2025"
version: 2
updated_at: 2025-08-13T11:17:31.376Z
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/83427332
---

# Novinky ve verzi k 29. 7. 2025

# 🧪 Bonifikační program – PSA

## Funkcionalita

- Umožňuje **zadání hodnoty PSA** jako položku měření.
- Hodnotu lze zadat:

  - **ručně**, nebo
  - **dotáhnout z posledních laboratorních výsledků**.
- V rámci prohlídky **Vyšetření karcinomu prostaty** je dostupná stejná položka měření PSA.

  - Pokud je hodnota zadána v dekurzu, automaticky se propisuje i do prohlídky.

## Automatický návrh výkonu

Na základě zadané číselné hodnoty PSA je nabízen **výkon k vykázání**:

- `01131`
- `01132`
- `01133`

### Dostupnost:

- **Praktický lékař pro dospělé**
- **Urolog**
- Funkcionalita je **zpoplatněna**

---

# 💊 Preferovaná medikace VZP – *„Nezaměňovat“*

## Popis funkce

Cílem je automaticky nastavit příznak **„Nezaměňovat“** u léků preferovaných VZP. Příznak lze **ručně zrušit** před odesláním eReceptu.

### Uživatelské chování:

1. **Výběr medikace**

   - Pokud je lék na seznamu **preferované medikace VZP**, aktivuje se příznak **„Nezaměňovat“**.
2. **Zobrazení v rozhraní**

   - Pole „Nezaměňovat“ je **předem zaškrtnuté**.
3. **Možnost změny**

   - Lékař může **pole odškrtnout**, pokud chce umožnit výdej ekvivalentního přípravku.
4. **Odeslání receptu**

> Funkcionalita je **zpoplatněna.**

### Kontaktní osoby pro aktivaci:

| Jméno | E-mail | Telefon |
| --- | --- | --- |
| Radka Loubalová | [radka.loubalova@stapro.cz](mailto:radka.loubalova@stapro.cz) | 775 511 502 |
| Ing. Gabriela Pořízková | [gabriela.porizkova@stapro.cz](mailto:gabriela.porizkova@stapro.cz) | 732 595 497 |
| Zuzana Krejčí | [zuzana.krejci@stapro.cz](mailto:zuzana.krejci@stapro.cz) | 604 353 138 |
| Ing. Jessica Keszi | [jessica.keszi@stapro.cz](mailto:jessica.keszi@stapro.cz) | 734 509 010 |

---

# 👂 Audiologie / Foniatrie – Modul **Plánování**

## Nová funkcionalita

Rozšíření modulu **Plánování** o možnost zahrnutí **neregistrovaných pacientů**.

### Nový prvek rozhraní:

- **Checkbox:** `Včetně neregistrovaných pacientů`

  - Výchozí stav: **nezaškrtnutý**
  - Po zaškrtnutí: seznam je rozšířen i o neregistrované pacienty

### Speciální chování:

- Pokud se jedná o pracoviště bez registrací (např. odbornosti), **checkbox není zobrazen** a systém pracuje pouze s neregistrovanými pacienty.

---

# 🔌 API – Správa zaměstnání pacienta

## Nové možnosti:

- Zakládání, úprava a načítání zaměstnání pacienta
- Možnost napojení na:

  - Firmu
  - Její **pobočky**
  - Její **skupiny PLS**

## Dokumentace:

- [Zaměstnání – přehled](https://stapro-galen.atlassian.net/wiki/x/AYDmB)
- [Pobočky a skupiny PLS – přehled](https://stapro-galen.atlassian.net/wiki/x/CoDmB)

---

# 🛠 Opravy chyb

## Modul Plánování

- Oprava **nefunkčního filtru**
- Oprava chyby při použití tlačítka **Objednat**

## Slučování karet pacientů

- Při slučování pacientů s vyplněnými údaji je uživatel **upozorněn**

## PLS – Diagnózy

- Pokud je diagnóza **dotažena z dekurzu**, diagnóza z přebírané prohlídky **není dotažena**
- Diagnóza z přebírané prohlídky se dotahuje **jen tehdy**, pokud v dekurzu žádná není

## Dekurz – GDT výstup

- Nové nastavení formátu desetinných čísel:

  - Hodnota může být oddělena **čárkou** nebo **tečkou**
  - Určuje se pomocí **checkboxu v konfiguraci přístroje**
