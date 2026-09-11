---
title: "Registrace a evidence pacienta na pracovištích"
version: 2
updated_at: 2026-09-10
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/584220674
---

# Registrace a evidence pacienta na pracovištích

> [!info]
> Funkcionalita umožňuje v modulu Objednávání (na recepci i na pracovišti) vidět v kartotéce pacienta přehled všech aktuálně platných registrací na kapitačních pracovištích a přehled dalších pracovišť, kde je pacient evidován.

## Vysvětlení pojmů

| Pojem | Význam |
| --- | --- |
| **Registrující pracoviště** | Kapitační pracoviště s odborností **001** (všeobecné praktické lékařství), **002** (PLDD) nebo **603** (gynekologie a porodnictví), u kterého má pacient v kartě aktuálně platnou registraci. Jde tedy o pracoviště/lékaře, ke kterému je pacient formálně zaregistrován. |
| **Evidující pracoviště** | Pracoviště **mimo** odbornosti 001, 002 a 603, na kterém má pacient vykázán alespoň jeden výkon. |

## Chování při chybějícím pracovišti

- Pokud pacient **nemá žádné registrující (kapitační) pracoviště**, informace o tom se na kartotéce pacienta přesto **vypíše** (zobrazí se text/stav upozorňující, že pacient nemá platnou registraci).
- Pokud pacient **nemá žádné evidující pracoviště**, celá sekce s evidujícími pracovišti se u daného pacienta **vůbec nezobrazí**.

## Nastavení zobrazení

Zobrazení registrujících a evidujících pracovišť lze nezávisle zapnout/vypnout na dvou úrovních:

### 1. Na úrovni společnosti

Přístup: **Konfigurace společnosti → záložka Info panel pacienta (Recepce)**

Zde je možné u volby zobrazení nastavit, zda se mají registrující a evidující pracoviště zobrazovat pro celou společnost.

![image-20260910-130726.png](<../../../../../../../../pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/UI konfigurace/Info panel pacienta/Registrace a evidence pacienta na pracovištích/assets/image-20260910-130726.png>)

### 2. Na úrovni pracoviště

Přístup: **UI konfigurace pracoviště → záložka Info panel pacienta**

Stejná volba lze nastavit i na konkrétním pracovišti – nastavení na úrovni pracoviště tak umožňuje upravit chování odlišně od výchozí konfigurace společnosti.

![image-20260910-130814.png](<../../../../../../../../pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/UI konfigurace/Info panel pacienta/Registrace a evidence pacienta na pracovištích/assets/image-20260910-130814.png>)
> [!info]
> Výchozí nastavení je zobrazení **obou** – registrujících i evidujících pracovišť.

## Zobrazení na kartotéce pacienta (modul Objednávání / Recepce)

V kartotéce pacienta se v pravém panelu zobrazí:

- Seznam všech aktuálně platných **registrací** na kapitačních pracovištích (001/002/603) v rámci přihlášené provozovny, seřazený v pořadí **praktik → PLDD → gynekologie**.
- Rozbalovací sekce **„Další pracoviště, kde je pacient evidován“** se seznamem pracovišť mimo tyto tři odbornosti, na kterých má pacient vykázán alespoň jeden výkon.

Díky tomu má recepce rychlejší a přesnější přehled o tom, ke kterému konkrétnímu lékaři/pracovišti pacienta objednat, a to i na pracovištích s více lékaři stejné odbornosti (např. více gynekologů).

![image-20260910-130917.png](<../../../../../../../../pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/UI konfigurace/Info panel pacienta/Registrace a evidence pacienta na pracovištích/assets/image-20260910-130917.png>)
