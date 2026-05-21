---
title: "Export dokladů do účetního systému POHODA"
version: 2
updated_at: 2025-10-16
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/130809857
---

# Export dokladů do účetního systému POHODA

Export vybraných dokladů (faktury, pokladní doklady, stavy skladů, pohyby) ze systému FONS Galen do účetního systému **POHODA** ve formátu XML. Funkcionalita je zpoplatněna.

Exportní tlačítka se nachází v následujících modulech:

| **Modul** | **Cesta** | **Exportované doklady** |
| --- | --- | --- |
| **Vyúčtování** | Správce → Vyúčtování → Faktury | Faktury |
| **Finance** | Správce → Finance → Faktury / Pokladní doklady | Faktury, pokladní doklady |
| **Sklad** | Správce → Sklad → výběr skladu | Stavy skladů, pohyby (příjemky, výdejky) |

## Postup exportu

**Export faktur / pokladních dokladů (Vyúčtování a Finance)**

1. Otevřete požadovaný modul a přejděte na seznam dokladů.
2. Označte doklady, které chcete exportovat.
3. Klikněte na tlačítko **„Vybrané“** nebo **„Zobrazené“** v sekci **Exportovat.**

   - Vybrané = budou exportované označené doklady
   - Zobrazení = budou exportované doklady zobrazené na stránce

![image-20251003-080912.png](<../../../pages/FONS GALEN/Finance a účetnictví/Export dokladů do účetního systému POHODA/assets/image-20251003-080912.png>)
4. Vyberte umístění a název souboru v dialogovém okně „**Uložit jako**“.
5. Potvrďte a soubor se uloží ve formátu XML.

**Export stavů a pohybů skladu**

1. Otevřete **modul Sklad** a vyberte konkrétní sklad.
2. Klikněte na tlačítko **„Stavy skladu“** nebo **„Pohyby“** v sekci **Exportovat**.

![image-20251003-081016.png](<../../../pages/FONS GALEN/Finance a účetnictví/Export dokladů do účetního systému POHODA/assets/image-20251003-081016.png>)
3. V dialogovém okně „Uložit jako“ zadejte název a umístění souboru.
4. Potvrďte – doklady se uloží jako XML.

## Oprávnění k exportu

Exportovat mohou pouze uživatelé, kteří mají:

- přístup do **modulu Správce**
- a zároveň přístup do některého z těchto modulů:

   - Vyúčtování
   - Finance
   - Sklad

## Import do systému POHODA

Probíhá ručně pomocí funkce XML import v systému POHODA.

## Historie exportu

Po každém úspěšném exportu se do agendy uloží informace:

| **Sloupec** | **Význam** |
| --- | --- |
| **Exportováno** | Datum a čas posledního exportu |
| **Exportoval** | Jméno uživatele, který export provedl |

Pokud je doklad exportován vícekrát, staré hodnoty se přepíší.

## Důležitá upozornění

- Import stavy skladů do POHODA nemění stavy. Stavy jsou změněny importem pohybů.
- Šarže ve skladech jsou podporovány pouze ve verzích POHODA E1 a SQL.
- Při exportu historických faktur se způsobem úhrady „Hotově/Kartou“ se v systému Pohoda automaticky nastaví způsob platby „Příkazem“.
