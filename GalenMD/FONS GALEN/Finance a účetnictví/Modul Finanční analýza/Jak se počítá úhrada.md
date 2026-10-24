---
title: "Jak se počítá úhrada"
version: 1
updated_at: 2026-10-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/657620995
---

# Jak se počítá úhrada

Modul Finanční analýza modeluje výši úhrady za ambulantní péči v segmentu fyzioterapie a ergoterapie podle úhradové vyhlášky platné pro zvolený rok. Výpočet provádí systém FONS Reports, Galen předává vykázaná data a vstupní údaje a zobrazuje výsledky.

> [!info]
> Konkrétní hodnoty, jako je koeficient navýšení, hodnota bodu, minimální hodnota bodu nebo prahové hodnoty pro navýšení, stanovuje úhradová vyhláška pro příslušný rok.
>
> Výpočet probíhá každou noc. Změny výchozích údajů se proto projeví až následující den.

## Období

- **Aktuální období** – sledovaný rok.
- **Referenční období** – předminulý rok.
- **Mezidobí** – rok mezi referenčním a aktuálním obdobím.

Body všech období jsou přepočtené podle číselníku výkonů platného k 1. 1. aktuálního roku a oceněné hodnotou bodu aktuálního roku, aby byla data porovnatelná.

## 1. PURO (ref. obd.)

Pokud je ve *Výchozích údajích* vyplněná **Zadaná hodnota**, použije se ona. Jinak se použije hodnota **Vypočteno systémem**:

> [!abstract]
> ```
> PURO (ref. obd.) = MAX( A ; B )
>
> A = Vstupní úhrada ÷ Počet unik. pojištěnců (ref. obd.)
> B = (Počet bodů (ref. obd.) × minimální hodnota bodu + ZUM a ZULP (ref. obd.))
>     ÷ Počet unik. pojištěnců (ref. obd.)
> ```

U všech vstupních údajů platí, že zadaná hodnota má přednost před vypočtenou.

## 2. Koeficient navýšení

> [!abstract]
> ```
> Koeficient navýšení celkem = základní hodnota (dle vyhlášky) + navyšení
> ```

Pokud navyšení není vyplněné, počítá se jako 0. Od roku 2026 se navyšení zadává na záložce *Úhradové parametry*, pro rok 2025 a starší na záložce *Koeficient navýšení*.

## 3. Hodnota bodu a ocenění

> [!abstract]
> ```
> Hodnota bodu = Základní hodnota + Navýšení hodnoty
> Ocenění body = Body × Hodnota bodu
> Ocenění = Ocenění body + ZUM a ZULP
> ```

## 4. Finanční přehled – Limitovaná péče

Hodnoty se zobrazují po měsících a jsou kumulované za období od ledna do daného měsíce.

> [!abstract]
> ```
> Úhrada za základní pacienty = Koeficient navýšení celkem × PURO × Počet unikátů – základní pacient
> Úhrada za MNP               = Koeficient navýšení celkem × PURO × Počet unikátů – mimořádně nákladný pacient
> Úhrada MNP (aktuální)       = úhrada za výkony včetně ZUM a ZULP za mimořádně nákladné pacienty v aktuálním období
> Úhrada MNP (referenční)     = totéž v referenčním období
>
> Limitace = Úhrada za základní pacienty + MAX( Úhrada za MNP ; Úhrada MNP (aktuální) − Úhrada MNP (referenční) )
>
> Úhrada = MIN( Ocenění ; Limitace )
>
> Překročení (Kč) = Ocenění − Limitace
> Překročení (%)  = (Ocenění ÷ Limitace − 1) × 100, zaokrouhleno na 2 desetinná místa
> ```

- **Překročení** – kladná hodnota znamená objem péče, který nebude uhrazen (podbarveno červeně). Nulová nebo záporná hodnota znamená, že limitace nebyla vyčerpána (podbarveno zeleně).
- **PURO** se ve Finančním přehledu zobrazuje jako průběžné. Počítá se za období od ledna do daného měsíce podle rozložení péče v referenčním období, proto během roku roste a v prosinci dosáhne celoroční hodnoty PURO.
- **Limitovaná úhrada** – pokud zařízení v aktuálním nebo referenčním období nedosáhne minimálního počtu pacientů (pole *Počet UOP limitní úhrada*), limitace se neuplatňuje a péče je hrazena podle skutečně vykázaných výkonů.
- **Modelace** (pouze rozšířená verze) – u měsíců, které ještě neproběhly, jsou počty bodů a unikátních pojištěnců odhadnuté do konce roku podle rozložení referenčního období.

## 5. Finanční přehled – Plně hrazená péče

> [!abstract]
> ```
> Úhrada = Ocenění body K + ZUM ZULP K
> ```

Plně hrazená péče není omezená limitací. U podsegmentu Poplatky se modelace neprovádí, zobrazuje se pouze skutečnost.

## 6. Analytik – Nákladní pojištěnci

> [!abstract]
> ```
> Ocenění celkem  = Ocenění body + Ocenění ZUM a ZULP
> PURO5           = PURO × 5, zaokrouhleno na celé číslo
> Překročení (Kč) = Ocenění celkem − PURO5
> MNP poměr (%)   = Ocenění celkem ÷ PURO5 × 100, zaokrouhleno na 2 desetinná místa
> ```

Zelená barva znamená, že pojištěnec hranici mimořádně nákladného pacienta dosáhl (Překročení ≥ 0, MNP poměr ≥ 100 %). Červená barva znamená, že se k hranici teprve blíží.

## 7. Analytik – Navýšení hodnoty bodu a Navýšení koeficientu navýšení

> [!abstract]
> ```
> Poměr KNa (%)     = Výkony – počet KNa ÷ Výkony – počet vše × 100
> Poměr KNb (%)     = Výkony – počet KNb ÷ Výkony – počet vše × 100
> Poměr diagnóz (%) = POP diagnózy ÷ POP vše × 100
> ```

Seznam výkonů a diagnóz a prahové hodnoty pro nárok na navýšení stanovuje úhradová vyhláška. Jejich přesné znění je uvedeno ve vysvětlivce u sloupce. Splnění podmínky je v tabulce barevně označené; barva neznamená, že zařízení má na navýšení automaticky nárok. Hodnoty se počítají k určitému měsíci, během roku se proto mohou zvyšovat i snižovat.

> [!warning]
> Galen hodnotu bodu ani koeficient navýšení sám nezmění. Pokud nárok na navýšení vznikne, je potřeba navyšení zadat ručně ve *Výchozích údajích*.
