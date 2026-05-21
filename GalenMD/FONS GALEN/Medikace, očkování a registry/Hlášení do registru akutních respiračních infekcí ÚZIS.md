---
title: "Hlášení do registru akutních respiračních infekcí ÚZIS"
version: 2
updated_at: 2026-05-13
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/167641089
---

Odesílání hlášení do Registru akutních respiračních infekcí je povinný pro praktické lékaře a pediatry. Více informací poskytuje [stránka ÚZIS](https://www.uzis.cz/index.php?pg=registry-sber-dat--ochrana-verejneho-zdravi--registr-akutnich-respiracnich-infekci).

V rámci FONS Galen se jedná o nadstandardní funkcionalitu.

## Potřebná nastavení

Pro zprovoznění funkcionality je potřeba

1. Zpřístupnění nadstandardní funkcionality Registr ARI

1. Šifrovací certifikát na pracovišti (aktuálně vydává SÚKL, od 1. 11. 2024 vydává ÚZIS)

1. Vyplněná hodnota pole *PČZ* v konfiguraci pracoviště

1. **Stažený číselník ÚZIS Diagnózy**: Modul *Nástroje* na pracovišti nebo v modulu *Správce*-> *Registr ÚZIS* -> Diagnózy

Naopak není potřeba žádat o žádnou roli na ÚZIS. Dle informace ÚZIS by tato role měla být všem praktikům přidána k certifikátu automaticky.

## Postup pro odeslání hlášení z editoru výkonů

Hlášení se primárně odesílají na základě vykázání výkonu, který má jako hlavní diagnózu uvedenou některou z diagnóz, která je uvedena v číselníku ÚZIS Diagnózy.

Pokud lékař vykáže výkon

1. Odb. 001: **01543** nebo **09557** nebo **01305**

1. Odb. 002: **09555** nebo **09556** nebo **09557** nebo **01543** nebo **01305**

A tento výkon bude mít jako hlavní diagnózu uvedenou diagnózu, která je uvedená v číselníku ÚZIS Diagnózy, pak se při ukládání výkonů bude na pozadí odesílat hlášení do Registru ARI.

## Přehled hlášení v modulu Registr ARI v ordinaci

V ordinaci praktického lékaře a pediatra přibyde v hodní modré liště modulu Registr ARI. Modul slouží pro přehled odeslaných hlášení, a zároveň pro možnost ručního zadání hlášení v případě, že nebyl uživatelem vykázán žádný z výše uvedených výkonů.

## Často kladené otázky

### Kdy je nutné hlášení odesílat?

Hlášení se má odeslat při začátku nemoci. Pokud by pacient přišel na kontrolu po ukončení, toto hlášení se už neodesílá. Výjimku tvoří to, že by epizoda nemoci trvala ještě další týden, to by se hlášení odeslat mělo. Stejně by se hlášení mělo odeslat ve chvíli, kdy pacienta přebírá jiný lékař a epizoda nemoci stále trvá.

### Při editaci data vykázaného výkonu se vyšetření v registru ARI automaticky smazalo. Jak postupovat?

Vyšetření, nebo též hlášení, se v registru ARI zpracovávají v týdenních cyklech (konkrétně od pátku do čtvrtka). Ve čtvrtek v nočních hodinách jsou vyšetření na straně ÚZIS uzavřena a není možné s nimi dále pracovat (nelze je ani mazat, ani editovat).

Pokud u výkonu, na základě kterého bylo odesláno vyšetření do registru ARI, změníte datum do období, kdy už jsou vyšetření na straně ÚZIS uzavřená, stávající hlášení se smaže, protože jste změnili datum výkonu od období, do kterého již není možné vyšetření do registru ARI zadávat.

### Při ukládání výkonu se FONS Galen dotazuje, zda si přeji vyšetření v registru ARI editovat. Jak postupovat?

V rámci jednoho týdne (od pátku do čtvrtka) by se mělo do registru odeslat pouze jedno hlášení. Ve výkonech pravděpodobně ukládáte výkon s diagnózou, na základě kterých by se hlášení odeslat mělo, ale zároveň FONS Galen vidí, že už jste hlášení za daný týden odeslali.

Tento scénář může nastat např. ve chvíli, kdy jste v pondělí vykázali dotčený výkon s danou diagnózou a vyšetření odeslali. Ve čtvrtek vykazujete dotčený výkon s danou diagnózou proto, že nemoc pacienta již pominula.

Pokud zvolíte možnost editace vyšetření, bude do registru ARI odeslána aktualizace stávajícího vyšetření, která se bude týkat změny data vyšetření nebo jeho diagnózy. Pokud editaci nezvolíte, v registru zůstane vyšetření s původním datem nebo diagnózou.

Pokud situace nastala z důvodu, který byl popsán výše (v rámci jednoho týdne pátek až čtvrtek byla epizoda zahájena i ukončena), vyšetření needitujte, protože se hlášení má odesílat při zahájení epizody nemoci.

### Při ukládání výkonu se FONS Galen dotazuje, zda si přeji odeslat vyšetření do registru ARI. Jak postupovat?

FONS Galen vyhodnotil, že v posledních 14 dnech bylo do registru ARI odesláno hlášení. Jedná se o pojistku, aby nebylo odesláno hlášení např. ve chvíli, kdy epizoda nemoci skočila.

Pokud pacient zahájil novou epizodu nemoci, nebo pokud tato epizoda trvá i další týden, vyšetření do registru ARI odešlete.

Pokud vykazujete výkony proto, že epizoda nemoci už skončila, vyšetření do registru ARI neodesílejte.
