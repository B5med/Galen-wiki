---
title: "Vyhledání termínu v kalendáři"
version: 1
updated_at: 2026-06-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/461176852
---

# Vyhledání termínu v kalendáři

Funkce **Vyhledání termínu** umožňuje rychle najít nejbližší volný časový slot v ordinačním kalendáři bez nutnosti procházet den po dni. Místo ručního listování kalendářem systém automaticky vyhledá první dostupný termín, který splňuje zadaná kritéria. Jedná se o nadstandardní placenou funkcionalitu, která není součástí základní dodávky systému FONS Galen.

## Jak funkci spustit

Funkce je dostupná přímo v kalendáři při objednávání pacienta. V horní části kalendáře jsou k dispozici tři navigační tlačítka:

![image-20260618-133603.png](<../../../../pages/FONS GALEN/Objednávání, komunikace a notifikace/Objednávání, kalendáře, notifikace/Vyhledání termínu v kalendáři/assets/image-20260618-133603.png>)
- **První** – přejde na úplně první volný termín od aktuálního data
- **Předchozí** – přejde na nejbližší volný termín před aktuálně zobrazeným datem
- **Další** – přejde na nejbližší volný termín po aktuálně zobrazeném datu

## Parametry vyhledávání

Při vyhledávání lze ovlivnit, co systém považuje za „obsazený" slot, pomocí parametru:

- **Zahrnout rezervace** – zatržítko, které určuje, zda se mají rezervace v kalendáři považovat za obsazené termíny. Pokud je zatrženo, vyhledávání rezervované sloty přeskakuje. Pokud není zatrženo, rezervace se ignorují a systém je vyhodnotí jako volné.

## Co vyhledávání respektuje

Systém při hledání volného termínu zohledňuje:

- **Objednané pacienty** z kartotéky
- **Záznamy v kalendáři** (blokace, rezervace dle nastavení výše)
- **První vyšetření** (záznamy pro neznámého/nového pacienta)
- **Ordinační dobu** lékaře – vyhledává pouze v rámci nastavené ordinační doby

## Výsledek vyhledávání

Po kliknutí na tlačítko se kalendář automaticky přesune na nalezený volný termín a zobrazí příslušný den a čas. Pokud vyhledávání narazí na čas v minulosti, automaticky vybere nejbližší budoucí dostupný čas v daném bloku.
