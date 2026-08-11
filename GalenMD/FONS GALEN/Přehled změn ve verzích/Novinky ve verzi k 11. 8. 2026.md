---
title: "Novinky ve verzi k 11. 8. 2026"
version: 1
updated_at: 2026-08-10
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/535003154
---

# Novinky ve verzi k 11. 8. 2026

# Novinky a vylepšení

## Společné

### Dávky ČSSZ - nový stav „Vyřazená"

U neschopenky, ošetřovného a dlouhodobého ošetřovného lze nově dávku ručně označit jako **Vyřazená**. Tento stav slouží k označení dávek, které ČSSZ ve svém systému neeviduje. Vyřazená dávka se chová obdobně jako ukončená – nezobrazuje se v dlaždici pacienta ani v přehledu neodeslaných lístků na peníze a není aktivní pro další zpracování.

Dávku vyřadíte v přehledu dávek pravým tlačítkem myši → **Změnit stav na vyřazená**. Zpět do původního stavu ji vrátíte volbou **Obnovit původní stav** nebo akcí **Aktualizovat dle ČSSZ**; systém dávku obnoví také automaticky, jakmile k ní přijde notifikace z ČSSZ. Obnovení stavu **neaktivuje** opětovné odesílání dat na ČSSZ, jde pouze o interní změnu. Každá změna stavu se zaznamenává do nové tabulky **Historie vyřazení**.

Vyřazené dávky si zobrazíte zatržením nového checkboxu **Vyřazené** ve filtru dávek i v historii pacienta (sekce ČSSZ). Ve výchozím stavu je checkbox nezatržený a vyřazené dávky se nezobrazují.

Detailní popis a práci se stavem vyřazená naleznete zde: [[Vyřazení dávky (stav „Vyřazená“)|https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/518717444/Vy+azen+d+vky+stav+Vy+azen]]

## Prohlídky a vyšetření

### Prohlídky a vyšetření - tlačítka

V části Prohlídky a vyšetření se mohla tlačítka „Fyziologický nález" a „Převzít" skrýt poté, co uživatel formulář opustil (např. za účelem doplnění anamnézy) a vrátil se zpět.

Nyní je dostupnost tlačítek řízena tím, zda je prohlídku možné editovat, a ne tím, zda je vyšetření již vyplněné. U editovatelné prohlídky jsou tlačítka „Fyziologický nález" a „Převzít" k dispozici i po opětovném otevření formuláře. U uzavřené nebo uzamčené prohlídky zůstávají tlačítka nedostupná, čímž je zachována ochrana proti zápisu do uzamčených záznamů.
