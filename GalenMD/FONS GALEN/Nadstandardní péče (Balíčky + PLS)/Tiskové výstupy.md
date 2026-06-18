---
title: "Tiskové výstupy"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/435224579
---

# Tiskové výstupy

Modul Nadstandardní péče poskytuje následující tiskové sestavy a výstupy:

| **Výstup** | **Oblast** | **Kde spustit** | **Poznámka** |
| --- | --- | --- | --- |
| Pokladní doklad (stvrzenka) | Balíčky NP | Karta pacienta → Závazky → Tisk | Generuje se automaticky při platbě hotově |
| Tisk přehledu závazků | Balíčky NP | Karta pacienta → Závazky → Tisk přehledu | Export plateb a závazků pacienta |
| Tisk vyúčtování PLS | PLS | PLS → Fakturace → Tisk vyúčtování | Tisková sestava faktury pro zaměstnavatele; operace TiskPLSVyuctovaniOperation |
| Faktura PLS | PLS | PLS → Faktury PLS → detail faktury → Tisk | Faktura s položkami, DPH, identifikací pacientů a čísly objednávek |

> [!tip]
> Faktura PLS obsahuje automaticky doplněná čísla navázaných PLS objednávek — zaměstnavatel tak může spárovat fakturu s objednávkou, kterou zaslal.
