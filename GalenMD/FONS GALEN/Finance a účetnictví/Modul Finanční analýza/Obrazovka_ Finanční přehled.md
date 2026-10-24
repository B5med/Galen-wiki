---
title: "Obrazovka: Finanční přehled"
version: 2
updated_at: 2026-10-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/113639430
---

# Obrazovka: Finanční přehled

Obrazovka **Finanční přehled** zobrazuje výsledky výpočtu úhrady po měsících. Je rozdělena do záložek **Limitovaná péče**, **Plně hrazená péče** a **Péče cizincům**. Záložky slouží pouze k prohlížení dat.

- Data lze filtrovat podle roku, IČZ a měsíce.
- Data lze exportovat do Excelu tlačítkem **Export**.
- Výpočty jednotlivých hodnot jsou popsány na stránce *Jak se počítá úhrada*.

## Limitovaná péče

Zobrazuje péči, jejíž úhrada je omezena maximální úhradou (segment P07L – fyzioterapie a ergoterapie s limitací). Uživatel zde vidí, zda byla limitace vyčerpána nebo překročena. Hodnoty jsou kumulované za období od ledna do daného měsíce.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Finanční přehled/assets/image-20250905-074343.png>)

| Sloupec | Popis |
| --- | --- |
| IČZ, Pojišťovna, Podsegment, Měsíc | Identifikace řádku. |
| Limitovaná úhrada | Ano – na zařízení se vztahuje limitace. Ne – zařízení nedosáhlo minimálního počtu pacientů (Výchozí údaje – Počet UOP limitní úhrada), limitace se neuplatňuje a péče je hrazena podle vykázaných výkonů. |
| Modelace *(pouze rozšířená verze)* | Ne – výpočet je proveden nad již vykázanými daty. Ano – jde o modelaci (odhad do konce roku). |
| Počet unikátů – základní pacient | Počet základních unikátních pojištěnců ošetřených v hodnoceném období, kumulovaně od ledna. |
| Počet unikátů – mimořádně nákladný pacient | Počet mimořádně nákladných unikátních pojištěnců ošetřených v hodnoceném období, kumulovaně od ledna. |
| PURO | Průběžné PURO za období od ledna do daného měsíce, rozložené podle referenčního období. Během roku roste a v prosinci dosáhne celoroční hodnoty. Pokud je ve Výchozích údajích zadané PURO (ref. obd.), vychází z něj. |
| Ocenění | Ocenění vykázaných výkonů včetně ZUM a ZULP. |
| Limitace | Maximální úhrada za limitovanou péči. |
| Úhrada | Výsledná úhrada – nižší z hodnot Ocenění a Limitace. |
| Překročení (Kč) *(pouze rozšířená verze)* | Ocenění − Limitace. Kladná hodnota (červeně) = objem péče, který nebude uhrazen. Nulová nebo záporná hodnota (zeleně) = limitace nebyla vyčerpána. |
| Překročení (%) *(pouze rozšířená verze)* | Překročení vyjádřené v procentech limitace. Barvy stejné jako u Překročení (Kč). |

> [!info]
> **Modelace:** V rozšířené verzi se pro měsíce, které ještě neproběhly, zobrazují odhadované hodnoty do konce roku (sloupec Modelace = Ano). Odhad vychází z rozložení péče v referenčním období. V základní verzi se sloupec Modelace ani modelované řádky nezobrazují.
>
> Při porovnávání s analýzou pojišťovny si ověřte, za jaký měsíc hodnotu čtete a zda nejde o modelovaný řádek.

## Plně hrazená péče

Zobrazuje péči hrazenou v plné výši bez limitace (segment P07V): výkonovou úhradu dle diagnóz, dopravu a poplatky. Hodnoty jsou kumulované za období od ledna do daného měsíce.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Finanční přehled/assets/image-20250905-074405.png>)

| Sloupec | Popis |
| --- | --- |
| IČZ, Pojišťovna, Podsegment, Měsíc | Identifikace řádku. Podsegmenty viz stránka *Pojmy a zkratky*. |
| Modelace *(pouze rozšířená verze)* | Stejný význam jako u Limitované péče. U podsegmentu Poplatky se modelace neprovádí. |
| Body K – výkonový segment | Počet bodů za výkony, kumulovaně od ledna. |
| Ocenění body K – výkonový segment | Body oceněné příslušnou hodnotou bodu, kumulovaně od ledna. |
| ZUM ZULP K – výkonový segment | Úhrada za ZUM a ZULP, kumulovaně od ledna. |
| Úhrada | Výsledná úhrada (ocenění bodů + ZUM a ZULP). |

## Péče cizincům

Zobrazuje péči poskytnutou pojištěncům z Členských států EU a ze států s mezinárodní smlouvou, po měsících.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Finanční přehled/assets/image-20250905-074420.png>)
**Sloupce:** IČZ, Pojišťovna, Odbornost, Podsegment, Měsíc, HB (hodnota bodu), Body, ZUM a ZULP, Úhrada.

Součet sloupců Body, ZUM a ZULP a Úhrada je uveden v záhlaví sloupce jako *(celkem: …)*.
