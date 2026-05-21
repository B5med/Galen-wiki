---
title: "Notifikace"
version: 1
updated_at: 2025-07-10
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/68616209
---

Notifikace pacientovi je možné zaslat pomocí tlačítka *Oslovit* v rámci individuálních notifikací (viz kapitola Funkční tlačítka modulu pro roli Správce), nebo automaticky pomocí hromadných notifikací.

### Nastavení času odeslání hromadných notifikací

V module Nástroje, v okně Hromadné notifikace, je nejdříve potřeba definovat v které časy budou hromadné notifikace odcházet.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Generování nároků z vyšetření/Notifikace/assets/image-20250710-124326.png]]

### Šablony notifikací

Pro odeslání hromadných notifikací je nutné vytvořit šablonu textu, která se zobrazí pacientovi. Nastavuje se na cestě: správce v modulu Nástroje – Šablony definuje šablony pro notifikace. Nastavení šablony je shodné s nastavením jiných šablon. V kolonce použití uživatel vybere „Nároky (hromadné)“, pokud se má šablona použít při rozesílání hromadných notifikací. Tento typ šablony je možné zvolit také pro individuální nároky, tj. při použití tlačítka *Oslovit*.

Ve chvíli, kdy je vybráno použití Nároky (hromadné) nebo Nároky (individuální), zobrazí se entita *Nárok*, která mj. slouží pro dotažení názvu vyšetření, na které se má pacient objednat, do šablony. Konkrétně se jedná o položku Podtyp.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Generování nároků z vyšetření/Notifikace/assets/image-20250710-124343.png]]

### Nastavení odesílaných nároků v hromadných notifikacích

Správce v modulu Nároky definuje jak často a v jakém počtu se mají hromadné notifikace automaticky rozesílat. Pomocí zeleného tlačítka Plus přidá řádek, ve kterém definuje termín, typ a podtyp(y) nároku, počet notifikací, které se mají rozeslat a případně pracoviště, na kterých nárok vznikl. Správce může také vyjmout pojišťovny pacientů, kterým notifikace nechce odesílat, a definovat rozestup notifikací.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Generování nároků z vyšetření/Notifikace/assets/image-20250710-124400.png]]
