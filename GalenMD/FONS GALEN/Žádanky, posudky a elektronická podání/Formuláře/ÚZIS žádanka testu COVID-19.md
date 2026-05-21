---
title: "ÚZIS žádanka testu COVID-19"
version: 3
updated_at: 2025-11-20
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/162856962
---

> [!info]
> Pomocí formuláře *ÚZIS žádanka testu COVID-19* lékař odesílá informace do systému ÚZIS ISIN v souvislosti v provedením testu Covid-19 a/nebo vystavením žádanky na test Covid-19.

Pro uživatele jsou připravené dvě varianty formulářů. Obě mají stejný obsah a účel, rozdíl je ve jejich formě.

## ÚZIS žádanka testu COVID-19

Pro odeslání této žádanky je nutné vyplnit pole Klíč ÚZIS v nastavení společnosti (*Správce → Správa organizace →* Společnost *→* Klíč ÚZIS).

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/ÚZIS žádanka testu COVID-19/assets/image-20251120-081638.png]]
Lékař vyplní formulář a odešle stiskem tlačítka Odeslat, čímž se otevře formulář v internetovém prohlížeči.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/ÚZIS žádanka testu COVID-19/assets/image-20251120-081840.png]]
Obsah formuláře v internetovém prohlížeči uživatel zkontroluje a pomocí tlačítka Odeslat uloží.

## ÚZIS žádanka testu COVID-19 ISIN

### Prerekvizity

#### Identifikace uživatele

Uživatel, který má mít možnost hlášení do ISIN odesílat, musí mít vyplněné pole *Číslo NRZP* (číslo uživatele z Národního registru zdravotnických pracovníků). Číslo zadá uživatel s rolí *Správce*v modulu Správa organizace – Uživatelé

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/ÚZIS žádanka testu COVID-19/assets/image-20250414-095636.png]]

#### Certifikát na pracovišti

Pro komunikaci s ISIN je nutné, aby byl na pracovišti, ze kterého se bude ohlášení odesílat, nastaven šifrovací certifikát SÚKL (aktuálně vydává též ÚZIS).

Správa organizace – v rámci stromové struktury vyhledat pracoviště a nastavit platný certifikát.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/ÚZIS žádanka testu COVID-19/assets/image-20250414-095739.png]]

#### Vyplněná hodnota PČZ - pořadové číslo zařízení

Na úrovni pracoviště je dále nutné vyplnit položku PČZ - pořadové číslo zařízení.

*Správce → Správa organizace →* Struktura společnosti *→* úroveň pracoviště

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/ÚZIS žádanka testu COVID-19/assets/image-20250422-045812.png]]

#### Číselníky

Na základě objednávky nadstandardního modulu je uživatelům zpřístupněn modul ISIN – Hlášení infekčního onemocnění. Po zpřístupnění funkcionality je potřeba aktualizovat číselníky, které jsou pro toto hlášení nutné:

Nástroje – ISIN:

- Registr zdravotnických pracovníků
- Odběrová místa
- Výrobci testů

Uživatel pomocí tl. *Aktualizovat* načte aktuální číselníky.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/ÚZIS žádanka testu COVID-19/assets/image-20250414-095825.png]]

### Vystavení žádanky

Uživatel vyplní formulář, který se obsahově rovná první variantě

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/ÚZIS žádanka testu COVID-19/assets/image-20251120-082920.png]]
a tlačítkem Odeslat odesílá.

Na rozdíl od první varianty se tato odeslání přímo z aplikace FONS Galen do ISIN (a proto se v tomto případě neotevírá internetový prohlížeč).
