---
title: "Obrazovka: Výchozí údaje"
version: 3
updated_at: 2026-10-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/113999874
---

# Obrazovka: Výchozí údaje

Obrazovka **Výchozí údaje** se otevře jako první po vstupu do modulu. Slouží k zadávání a kontrole vstupních údajů, ze kterých se počítá úhrada. Obsahuje záložky **Úhradové parametry**, **Hodnota bodu** a **Koeficient navýšení**.

> [!info]
> - Řádky v tabulkách dodává výpočet FONS Reports. Po aktivaci modulu jsou tabulky prázdné a údaje lze zadávat až po prvním nočním zpracování. Řádky nelze přidávat ani mazat, pouze upravovat.
> - Pole s šedým pozadím jsou vypočtená systémem a nelze je upravit. Pokud vyplníte **Zadanou hodnotu**, má přednost před hodnotou **Vypočteno systémem**.
> - Po uložení změny se zobrazí upozornění *„Změna úhradových parametrů se projeví až následující den.“* Výsledky se přepočítají při nočním zpracování.
> - Vstupní údaje je potřeba vyplnit pro všechny pojišťovny.

## Záložka: Úhradové parametry

Záložka obsahuje vstupní údaje pro výpočet limitované péče za jednotlivé pojišťovny a IČZ. Hodnoty se zjišťují z vyúčtování od zdravotní pojišťovny za referenční období. Tabulku lze filtrovat podle IČZ.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20260512-060429.png>)

### Sloupce tabulky

| Sloupec | Popis |
| --- | --- |
| Rok, Pojišťovna, IČZ, Segment, Podsegment, Odbornost | Identifikace řádku. |
| Počet bodů (ref. obd.) | Počet bodů v referenčním období |
| Hodnota bodu | Skutečná hodnota bodu v referenčním období. |
| PURO (ref. obd.) – vypočteno | PURO vypočtené z referenčního období |
| Počet UOP lim. úhrady | Minimální počet pacientů pro uplatnění limitace. |
| Koeficient navýšení / Navýšení koeficientu | Pouze pro rok 2026 a novější. Základní hodnota koeficientu navýšení stanovená vyhláškou / dodatečné navyšení zadané uživatelem. |

### Detail úhradového parametru

Detail otevřete dvojklikem na řádek nebo tlačítkem **Otevřít záznam** (ikona tužky). V titulku je uvedena pojišťovna a IČZ. Detail má dva sloupce: **Zadaná hodnota** (lze upravit) a **Vypočteno systémem** (šedé pole, pouze pro čtení). Změny potvrďte tlačítkem **OK**.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20260512-060503.png>)

| Pole | Zadaná hodnota | Vypočteno systémem | Kdy vyplnit |
| --- | --- | --- | --- |
| **Vstupní úhrada** | ano | – | Vždy. Hodnotu najdete ve vyúčtování od zdravotní pojišťovny za referenční období. Bez jejího vyplnění není výpočet kompletní. |
| **Počet bodů (ref. obd.)** | ano | ano | Pouze pokud se vypočtená hodnota liší od vyúčtování pojišťovny. Jinak systém hodnotu dopočítá. |
| **Počet unik. pojištěnců (ref. obd.)** | ano | ano | Pouze pokud se vypočtená hodnota liší od vyúčtování pojišťovny. Jde o počet pojištěnců v **referenčním období**, nikoli v aktuálním roce. |
| **PURO (ref. obd.)** | ano | ano | Pouze pokud je s pojišťovnou dohodnuto použít jiné PURO než vypočtené (např. proto, že vypočtené je nevýhodné). Zadaná hodnota se použije pro výpočet limitace. |
| **Počet UOP limitní úhrada** | ano (povinné) | – | Minimální počet pacientů, jehož dosažení je podmínkou pro uplatnění limitační úhrady. Pokud zařízení tohoto počtu nedosáhne, limitace se neuplatní a péče je hrazena podle skutečně vykázaných výkonů. |
| **Koeficient navýšení** (rok 2026 a novější) | ano – navyšení | ano – základní hodnota | Základní hodnotu stanovuje vyhláška a automaticky se nemění, ani když výpočet nárok na navýšení indikuje. Pokud máte nárok na navýšení (viz Analytik – Navýšení koeficientu navýšení), zadejte dodatečné navyšení. Pokud není zadáno, považuje se za 0. |

## Záložka: Hodnota bodu

Záložka slouží ke kontrole a navyšení hodnoty bodu pro jednotlivé segmenty a podsegmenty. Základní hodnotu stanovuje vyhláška; pro všechny podsegmenty je stejná s výjimkou Dopravy a Poplatků.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20250905-065341.png>)
**Sloupce tabulky:** Rok, Segment, Podsegment, Základní hodnota, Navýšení hodnoty.

**Detail** (dvojklik na řádek nebo ikona tužky):

| Pole | Lze upravit | Popis |
| --- | --- | --- |
| Podsegment | ne | Podsegment, jehož hodnota bodu se upravuje. |
| Základní hodnota | ne | Hodnota bodu stanovená vyhláškou. Automaticky se nemění, ani když výpočet nárok na navýšení indikuje. |
| Navýšení hodnoty | ano | Dodatečné navyšení základní hodnoty bodu. Pokud není zadáno, považuje se za 0. |
| Specifická navyšení | ano | Tabulka pro navyšení platné jen pro konkrétní pojišťovnu a/nebo IČZ (sloupce Pojišťovna, IČZ, Navýšení hodnoty). Řádek přidáte tlačítkem plus, odeberete tlačítkem mínus. |

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20250905-065359.png>)
Pravidla pro specifická navyšení:

- Musí být vyplněna alespoň pojišťovna nebo IČZ (jinak se zobrazí hláška *„Vyplňte prosím alespoň jednu z položek pojišťovna/IČZ.“*).
- Stejnou kombinaci pojišťovny a IČZ nelze zadat dvakrát.
- Konkrétnější nastavení má přednost. Pro pojišťovny a IČZ bez specifického řádku platí obecná hodnota.

## Záložka: Koeficient navýšení

> [!warning]
> Záložka slouží pro rok 2025 a starší. Pro rok 2026 a novější se zobrazí informace *„Pro rok 2026 a novější je správa koeficientu navýšení přesunuta na záložku Úhradové parametry.“* a koeficient se zadává v detailu úhradového parametru.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20250905-065424.png>)
**Sloupce tabulky:** Rok, Segment, Název, Základní hodnota, Navýšení hodnoty.

**Detail** obsahuje Segment a Základní hodnotu (pouze pro čtení), pole **Navýšení hodnoty** a tabulku **Specifická navyšení** pro konkrétní pojišťovnu a/nebo IČZ. Platí stejná pravidla jako u záložky Hodnota bodu. Pokud není navyšení zadáno, považuje se za 0.

![](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20250905-065456.png>)
