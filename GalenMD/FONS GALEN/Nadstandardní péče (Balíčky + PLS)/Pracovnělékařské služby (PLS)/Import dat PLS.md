---
title: "Import dat PLS"
version: 2
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/436731905
---

# Import dat PLS

![obrazek-20260617-134928.png](<../../../../pages/FONS GALEN/Nadstandardní péče (Balíčky + PLS)/Pracovnělékařské služby (PLS)/Import dat PLS/assets/obrazek-20260617-134928.png>)
Importy PLS slouží k hromadnému naplnění dat modulu Pracovnělékařské služby pro novou firmu — skupin pracovních pozic, smluvního rámce a seznamu zaměstnanců.

> [!info]
> **Importy se musí provádět v tomto pořadí:** skupiny → smlouvy → pacienti. Každý krok závisí na předchozím.

| Krok | Import | Co se importuje | Soubor (vzor) |
| --- | --- | --- | --- |
| 1 | **Import skupin PLS** | Pracovní pozice (skupiny) firmy včetně přiřazených rizik. Musí existovat před importem smluv. | import_skupin_PLS.csv — 6 sloupců |
| 2 | **Import smluv PLS** | Smluvní rámec pobočky včetně ceníkových položek pro jednotlivé skupiny. | import_smluv_PLS.csv — 34 sloupců |
| 3 | **Import pacientů PLS** | Zaměstnanci firmy přiřazení do skupin PLS. Vytvoří nebo aktualizuje záznamy zaměstnání. | import_pacientu_PLS.csv — 25 nebo 23 sloupců |

Podrobné návody pro každý typ importu jsou dostupné v podstránkách níže.
