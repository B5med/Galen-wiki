---
title: "Sloučení karet pacienta"
version: 2
updated_at: 2026-05-13
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/399638530
---

Pokud se v systému FONS Galen vyskytuje pacient evidovaný pod dvěma různými kartami (například z důvodu chybného prvotního zadání), je možné tyto karty sloučit do jedné. Funkce sloučení zajistí převod veškeré dokumentace z rušené karty na kartu výslednou, včetně dekurzu a navázaných záznamů. Položky, které se při sloučení nepřenášejí (zůstávají z výsledné karty): adresa, kontakt, registrace, státní příslušnost, kategorie pojištěnce, anamnéza, etc.

![[pages/FONS GALEN/Správce a nastavení/Správa kartoték/Sloučení karet pacienta/assets/Snímka obrazovky 2026-04-30 104202.png]]
> [!info]
> Funkce je přístupná pouze uživatelům s rolí **Správce**.

Je nutné pečlivě zvolit:

- Pacienta, který zůstane zachován. Jeho karta bude výslednou se správným rodným číslem a pojišťovnou.
- Pacienta, který bude sloučen.  Dokumentace z této karty bude převedena na výslednou kartu pacienta.

Po výběru obou pacientů:

1. Klikněte na tlačítko Analyzovat – systém zobrazí přehled dat, která se při sloučení nepřenesou.
2. Klikněte na tlačítko Sloučit – dojde k trvalému sloučení duplicitních karet.

![[pages/FONS GALEN/Správce a nastavení/Správa kartoték/Sloučení karet pacienta/assets/Snímka obrazovky 2026-04-30 104100.png]]
> [!warning]
> Při slučování pacientů, u kterých jsou vyplněny údaje na obou kartách, systém uživatele na tuto skutečnost upozorní.
