---
title: "Obrazovka: Analytik"
version: 3
updated_at: 2026-10-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/114032645
---

# Obrazovka: Analytik

Obrazovka **Analytik** obsahuje rozšířené přehledy o bodech, pojištěncích, mimořádně nákladných pacientech a o splnění podmínek pro navýšení. Je rozdělena do záložek **Body a unikátní pojištěnci**, **Nákladní pojištěnci**, **Navýšení hodnoty bodu** a **Navýšení koeficientu navýšení**. Záložky slouží pouze k prohlížení dat.

- Data lze filtrovat podle roku a IČZ.
- Data lze exportovat do Excelu tlačítkem **Export**.
- Záložky Navýšení hodnoty bodu a Navýšení koeficientu navýšení jsou dostupné pouze v rozšířené verzi.

## Body a unikátní pojištěnci

Porovnává počet bodů, jejich ocenění a počet unikátních pojištěnců ve třech obdobích:

- **Aktuální období** – vybraný rok,
- **Mezidobí** – předchozí rok,
- **Referenční období** – předminulý rok.

*Příklad: pro rok 2026 je mezidobím rok 2025 a referenčním obdobím rok 2024.*

Všechna období jsou přepočtená podle číselníku výkonů platného k 1. 1. aktuálního roku a oceněná hodnotou bodu aktuálního roku, aby byla data porovnatelná. Hodnoty zahrnují také péči poskytnutou cizincům a nejsou omezeny limitací.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Analytik/assets/image-20250905-074611.png>)

| Skupina sloupců | Popis |
| --- | --- |
| IČZ, Pojišťovna, Segment, Podsegment | Identifikace řádku. |
| Body celkem / Body / Body MNP | Počet bodů za všechny pojištěnce / za základní pojištěnce / za mimořádně nákladné pojištěnce. Body celkem = Body + Body MNP. |
| Kč za body celkem / Kč za body / Kč za body MNP | Ocenění bodů příslušnou hodnotou bodu. Kč za body celkem = Kč za body + Kč za body MNP. |
| POP celkem / POP / POP MNP | Počet unikátních ošetřených pojištěnců. POP celkem = POP + POP MNP. |

Každá skupina je uvedena zvlášť pro aktuální období, mezidobí a referenční období (např. *Body celkem – aktuální období*, *POP – referenční období*). Součet každého číselného sloupce je uveden v záhlaví sloupce jako *(celkem: …)*.

## Nákladní pojištěnci

Zobrazuje mimořádně nákladné pojištěnce v limitované péči – ty, kteří již překročili hranici mimořádné nákladnosti (PURO5), i ty, kteří se k ní blíží. Seznam pojištěnců dodává výpočet FONS Reports. Záznamy jsou seřazeny podle data posledního výkonu od nejnovějšího.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Analytik/assets/image-20250905-074700.png>)

| Sloupec | Popis |
| --- | --- |
| IČZ, Pojišťovna, Odbornost, Číslo pojištěnce, Pacient | Identifikace pojištěnce. |
| Datum posledního výkonu, Vykazující odp. lékař, Vykazující pracoviště | Informace o posledním vykázaném výkonu pojištěnce. Datum se nevztahuje jen k vybranému roku. |
| Ocenění body | Body za výkony pojištěnce oceněné hodnotou bodu. |
| Ocenění ZUM a ZULP | Úhrada za ZUM a ZULP pojištěnce. |
| PURO | PURO pro aktuální rok vypočtené z referenčního období. |
| PURO vstup | PURO zadané ve Výchozích údajích (pokud je vyplněno, má přednost). |
| Ocenění celkem *(pouze rozšířená verze)* | Ocenění body + Ocenění ZUM a ZULP. |
| PURO5 *(pouze rozšířená verze)* | Pětinásobek PURO – hranice mimořádně nákladného pojištěnce. |
| Překročení (Kč) *(pouze rozšířená verze)* | Ocenění celkem − PURO5. Zeleně, pokud je hodnota 0 nebo kladná (pojištěnec hranici dosáhl), červeně, pokud je záporná. |
| MNP poměr (%) *(pouze rozšířená verze)* | Poměr ocenění celkem vůči PURO5. Zeleně od 100 %, červeně pod 100 %. |

> [!info]
> Pozor: barvy mají opačný význam než na záložce Finanční přehled – Limitovaná péče. Zde zelená znamená, že pojištěnec hranici mimořádně nákladného pacienta dosáhl a úhrada za něj se počítá samostatně.

## Navýšení hodnoty bodu (pouze rozšířená verze)

Ukazuje, zda zařízení splňuje podmínku pro navýšení hodnoty bodu podle podílu pojištěnců s vybranými diagnózami.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Analytik/assets/image-20250905-074721.png>)

| Sloupec | Popis |
| --- | --- |
| IČZ, Pojišťovna, Rok | Identifikace řádku. |
| POP vše | Počet všech unikátních ošetřených pojištěnců. |
| POP diagnózy | Počet unikátních pojištěnců ošetřených s některou z diagnóz stanovených vyhláškou. |
| Poměr diagnóz | POP diagnózy ÷ POP vše × 100 (bez desetinných míst). Zeleně, pokud je podmínka vyhlášky splněna, jinak červeně. |

## Navýšení koeficientu navýšení (pouze rozšířená verze)

Ukazuje, zda zařízení splňuje podmínky pro navýšení koeficientu navýšení podle podílu vybraných výkonů a diagnóz. Podmínky musí být splněny v hodnoceném i referenčním období.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Analytik/assets/image-20250905-074842.png>)

| Sloupec | Popis |
| --- | --- |
| IČZ, Pojišťovna, Rok | Identifikace řádku. |
| POP vše | Počet všech unikátních ošetřených pojištěnců. |
| Výkony – počet vše | Počet všech vykázaných a uznaných výkonů. |
| Výkony – počet KNa, Výkony – počet KNb | Počet výkonů, které vyhláška uvádí pro podmínku a) a b). Seznam výkonů je ve vysvětlivce sloupce. |
| POP diagnózy | Počet unikátních pojištěnců ošetřených s některou z diagnóz stanovených vyhláškou. |
| Poměr KNa, Poměr KNb, Poměr diagnóz | Podíl příslušných výkonů, resp. pojištěnců s diagnózami na celku v % (bez desetinných míst). Barva označuje splnění nebo nesplnění podmínky. Přesné znění podmínky je ve vysvětlivce sloupce. |

> [!warning]
> - Barva odráží splnění či nesplnění jednotlivé podmínky, nikoli to, zda má zařízení na navýšení nárok.
> - Hodnoty se počítají k určitému měsíci, během roku se proto mohou měnit.
> - Galen hodnotu bodu ani koeficient navýšení automaticky nezmění. Pokud vám nárok vznikne, zadejte navyšení ve *Výchozích údajích* (hodnota bodu na záložce Hodnota bodu, koeficient na záložce Úhradové parametry).
