---
title: "Smluvní výkony"
version: 2
updated_at: 2025-12-10
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/75464891
---

# Smluvní výkony

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/Smluvní výkony/assets/image-20250618-112716.png]]
Jedním kliknutím na IČP se otevře vpravo dole přehled nasmlouvaných pojišťoven, které jsou k jednotlivým ambulancím. Dvojitým kliknutím na číslo pojišťovny otevřeme přehled výkonů, které máme ve smlouvě s pojišťovnou.

V okně Smlouvy je možné přidat výkon, určit hodnotu bodu či kapitačního paušálu.

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/Smluvní výkony/assets/image-20250618-112824.png]]

## **Verzování a aktualizace výkonů**

Hodnoty parametrů výkonu se prvotně načítají z číselníků, které jsou automaticky v IS Galen aktualizovány a verzovány.

Pokud měníme v čase hodnoty jedné položky (např. výkonu) číselníku, je nutné zadat nový řádek se stejným kódem a jinými hodnotami.

Příkladem takové změny může být změna bodové hodnoty výkonu nebo ceny výkonu. V takovém případě je nutné u první položky zadat datum platnosti Do, přidat nový řádek a u toho vyplnit datum platnosti od:

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/Smluvní výkony/assets/image-20250618-112850.png]]
Není správné původní záznam smazat nebo přepsat!

Při přepočtu nevyúčtovaných výkonů, zpětném či opravném vyúčtování by byly změněny hodnoty i tam, kdy platily hodnoty původní. Nicméně pro případ potřeby systém umožňuje smazání řádku nebo přepsání jeho hodnot.

Tzn. provádíme-li opravy výkonů z minulosti, systém bere v úvahu číselníky i změny výkonů, které byly aktuální v datu vykázaného výkonu
