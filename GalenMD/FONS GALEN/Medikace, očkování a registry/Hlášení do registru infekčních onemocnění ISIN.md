---
title: "Hlášení do registru infekčních onemocnění ISIN"
version: 2
updated_at: 2025-11-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/16809985
---

# Hlášení do registru infekčních onemocnění ISIN

> [!info]
> Na základě novely vyhlášky č. 306/2012 Sb. o podmínkách předcházení vzniku a šíření infekčních onemocnění a o hygienických požadavcích na provoz zdravotnických zařízení a vybraných zařízení sociálních služeb k 1. 7. 2025, která nařizuje hlášení infekčních chorob odesílat elektronicky (čímž nahrazuje stávající tzv. červenou hlášenku), bylo implementováno toto hlášení do FONS Galen. Hlášení je uživatelům zpřístupněno v rámci placeného modulu. Uživatel, který má vyplněné NRZP na pracovišti, které má přiřazen platný SÚKL certifikát, může u pacienta vystavit toto hlášení a odeslat jej na ÚZIS. Nahlížení na hlášení vystavená jiným pracovištěm (nebo společností) poskytováno není.

## Prerekvizity

### Identifikace uživatele

Uživatel, který má mít možnost hlášení do ISIN odesílat, musí mít vyplněné pole *Číslo NRZP* (číslo uživatele z Národního registru zdravotnických pracovníků). Číslo zadá uživatel s rolí *Správce*v modulu Správa organizace – Uživatelé

![[pages/FONS GALEN/Medikace, očkování a registry/Hlášení do registru infekčních onemocnění ISIN/assets/image-20250414-095636.png]]

### Certifikát na pracovišti

Pro komunikaci s ISIN je nutné, aby byl na pracovišti, ze kterého se bude ohlášení odesílat, nastaven šifrovací certifikát SÚKL (aktuálně vydává též ÚZIS).

Správa organizace – v rámci stromové struktury vyhledat pracoviště a nastavit platný certifikát.

![[pages/FONS GALEN/Medikace, očkování a registry/Hlášení do registru infekčních onemocnění ISIN/assets/image-20250414-095739.png]]

### Vyplněná hodnota PČZ - pořadové číslo zařízení

Na úrovni pracoviště je dále nutné vyplnit položku PČZ - pořadové číslo zařízení.

*Správce → Správa organizace →* Struktura společnosti *→* úroveň pracoviště

![[pages/FONS GALEN/Medikace, očkování a registry/Hlášení do registru infekčních onemocnění ISIN/assets/image-20250422-045812.png]]

### Číselníky

Na základě objednávky nadstandardního modulu je uživatelům zpřístupněn modul ISIN – Hlášení infekčního onemocnění. Po zpřístupnění funkcionality je potřeba aktualizovat číselníky, které jsou pro toto hlášení nutné:

Nástroje – ISIN:

- Místo izolace

- Klasifikace zaměstnání

- Diagnózy pro hlášení infekčního onemocnění

Uživatel pomocí tl. *Aktualizovat* načte aktuální číselníky.

![[pages/FONS GALEN/Medikace, očkování a registry/Hlášení do registru infekčních onemocnění ISIN/assets/image-20250414-095825.png]]

## Vystavení hlášení

Uživatel v ordinaci označí pacienta v kartotéce a vejde do modulu *ISIN*

![[pages/FONS GALEN/Medikace, očkování a registry/Hlášení do registru infekčních onemocnění ISIN/assets/image-20250414-095913.png]]
V okamžiku, kdy se otevírá modul *ISIN*, dochází k načtení resortního identifikátoru pacienta (RID). V případě, že se RID nepodaří získat, není možné hlášení vystavit a je nutné podniknout kroky pro získání RID v kartě pacienta.

V modulu *ISIN (1)*je potřeba vybrat záložku *Hlášení infekčního onemocnění (2)*a stisknout tlačítko *Vytvořit hlášení (3).*

![[pages/FONS GALEN/Medikace, očkování a registry/Hlášení do registru infekčních onemocnění ISIN/assets/image-20250414-100000.png]]
Formulář pro zadání hlášení se otevře v modálním okně.

Položky, které je povinné pro odeslání vyplnit, jsou označeny *.

Hlášení je uloženo až poté, co je úspěšně odesláno na ÚZIS.

![[pages/FONS GALEN/Medikace, očkování a registry/Hlášení do registru infekčních onemocnění ISIN/assets/image-20251118-074728.png]]
> [!abstract]
> Stav hlášení (podezření nebo potvrzené) není ze strany laboratoře aktualizováno. Po obdržení výsledků z laboratoře si může sám stav aktualizovat, ale tato informace má pouze informační charakter pro lékaře samotného. ÚZIS aktualizaci stavu nevyžaduje, neboť aktuální stav hlášení obdrží přímo z laboratoře.

> [!abstract]
> Do hlášení se uvádí maximálně jedno zaměstnání pacienta.
