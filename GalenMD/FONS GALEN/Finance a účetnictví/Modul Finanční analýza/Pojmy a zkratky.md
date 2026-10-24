---
title: "Pojmy a zkratky"
version: 2
updated_at: 2026-10-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/658505742
---

# Pojmy a zkratky

Přehled pojmů a zkratek, které se používají v modulu Finanční analýza. Konkrétní hodnoty (např. koeficient navýšení, hodnota bodu nebo prahové hodnoty pro navýšení) stanovuje úhradová vyhláška pro příslušný rok.

## Pojmy

| Pojem | Význam |
| --- | --- |
| **Aktuální období** | Rok vybraný v horní části obrazovky (hodnocené období). |
| **Referenční období (ref. obd.)** | Předminulý rok vůči aktuálnímu období. Např. pro rok 2026 je referenčním obdobím rok 2024. |
| **Mezidobí** | Rok mezi referenčním a aktuálním obdobím. Např. pro rok 2026 je mezidobím rok 2025. |
| **Unikátní pojištěnec (POP, UOP)** | Pojištěnec ošetřený v daném období, který se počítá pouze jednou bez ohledu na počet návštěv. |
| **PURO** | Průměrná úhrada na jednoho unikátního ošetřeného pojištěnce. Odvozuje se z referenčního období, případně se zadává ručně, pokud je s pojišťovnou sjednané jiné PURO. |
| **PURO5** | Pětinásobek PURO. Hranice, od které se pojištěnec považuje za mimořádně nákladného. |
| **Mimořádně nákladný pacient (MNP)** | Pojištěnec, jehož ocenění péče (body a ZUM a ZULP) dosáhlo hodnoty PURO5. Úhrada za tyto pacienty se počítá samostatně. |
| **Základní pacient** | Pojištěnec, který není mimořádně nákladný. |
| **Hodnota bodu (HB)** | Hodnota v Kč, kterou se násobí body za výkony. Skládá se ze základní hodnoty stanovené vyhláškou a případného navyšení. |
| **Koeficient navýšení (KN)** | Koeficient stanovený vyhláškou, kterým se násobí PURO při výpočtu limitace. Při splnění podmínek lze základní hodnotu navyšit. |
| **Ocenění** | Hodnota vykázané péče v Kč: body × hodnota bodu + ZUM a ZULP. |
| **Limitace** | Maximální úhrada za limitovanou péči vypočtená podle úhradové vyhlášky. Viz stránka *Jak se počítá úhrada*. |
| **Úhrada** | Výsledná úhrada. U limitované péče nižší z hodnot Ocenění a Limitace, u plně hrazené péče celé ocenění. |
| **Překročení** | Rozdíl mezi Oceněním a Limitací. Kladná hodnota znamená objem péče, který nebude uhrazen. |
| **Modelace** | Odhad hodnot do konce roku podle rozložení péče v referenčním období. Dostupné pouze v rozšířené verzi. |
| **Kumulovaná hodnota (K)** | Hodnota sečtená za období od ledna do daného měsíce. Sloupce s kumulovanou hodnotou mají v názvu písmeno K. |
| **ZUM a ZULP** | Zvlášť účtovaný materiál a zvlášť účtované léčivé přípravky. |
| **Limitovaná úhrada** | Příznak, zda se na zařízení vztahuje limitace. Neuplatňuje se, pokud zařízení nedosáhne minimálního počtu pacientů (pole *Počet UOP limitní úhrada*). Pak je péče hrazena podle skutečně vykázaných výkonů. |

## Segmenty a podsegmenty

Vykázaná péče se pro účely výpočtu člení na segmenty a podsegmenty.

| Segment | Podsegment | Název podsegmentu | Kde se zobrazuje |
| --- | --- | --- | --- |
| **P07L** – fyzioterapie a ergoterapie s limitací (péče omezená maximální úhradou) | 1A_902 | 902 – fyzioterapie | Finanční přehled – Limitovaná péče |
| 1B_917 | 917 – ergoterapie |  |  |
| **P07V** – fyzioterapie a ergoterapie bez limitace (péče hrazená bez omezení) | 1A_902_VYK | 902 – fyzioterapie – výkonová úhrada dle diagnóz | Finanční přehled – Plně hrazená péče |
| DOP | Doprava |  |  |
| NEZL | Poplatky – výkony 09555, 09556, 09557 |  |  |

> [!info]
> Pro rok 2025 se v datech vyskytují také podsegmenty **C_ODB** (Cizinci) a **C_DOP** (Cizinci – doprava). Péče poskytnutá cizincům se zobrazuje na záložce Finanční přehled – Péče cizincům.

## Úrovně modulu

| Úroveň | Význam |
| --- | --- |
| Neaktivní | Modul je vypnutý. |
| Základní | Základní přehledy bez modelace a bez výpočtů překročení. |
| Rozšířená | Kompletní funkcionalita včetně modelace do konce roku, výpočtů překročení a hodnocení nároku na navýšení. Viz stránka *Rozdíly mezi verzemi*. |
