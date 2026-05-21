---
title: "Bezpečnostní logy"
version: 1
updated_at: 2025-09-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/120487956
---

## Úvod

Tato funkcionalita slouží k shromažďování, zobrazení a případnému exportu událostí, které mají bezpečnostní charakter, v AIS Galen. Exportované logy lze následně využít v SIEM k podrobnějšímu analýzám chování jednotlivých uživatelů. Funkcionalitu lze rozdělit na dvě části:

·         Přehled bezpečnostních logů

·         Pravidelný export bezpečnostních logů

## Zařazení funkcionality

Okno pro zobrazení bezpečnostních logů mohou otevřít uživatelé s oprávněním Správce. K funkcionalitě se dostanou následujícím způsobem:

1. Na úrovni Správce otevřít modul **Systémové logy.**
2. Dále je nutné otevřít submodul **Bezpečnostní logy**.

![[pages/FONS GALEN/Správce a nastavení/Bezpečnostní logy/assets/image-20250917-080801.png]]

## Přehled bezpečnostních logů

![[pages/FONS GALEN/Správce a nastavení/Bezpečnostní logy/assets/image-20250917-080905.png]]
1. **Typ logů**: Rozeznáváme následující typy logů, které se liší zaznamenávanými informacemi (sloupci v přehledu):

- **Autentizace:** Tento typ logů zaznamenává, kdo a kdy se přihlásil do AIS Galen. Dále se zobrazují informace o případném odhlášení. Přehled taktéž obsahuje jedinečné identifikátory jako je název počítače, IP adresa a Mac adresa.
- **Audit záznamu:**Tento typ logů zaznamenává, kdo a kdy pořídil, upravil nebo smazal záznam v AIS Galen. Dále se zobrazuje název a ID entity, ve které daná změna proběhla. Přehled taktéž obsahuje jedinečné identifikátory jako je název počítače, IP adresa a Mac adresa.
- **Nahlížení do dokumentace:**Tento typ logů zaznamenává, kdo a kdy nahlížel do dokumentace AIS Galen. Dále se zobrazuje název a ID dokumentace, do které bylo nahlíženo. Přehled taktéž obsahuje jedinečné identifikátory jako je název počítače, IP adresa a Mac adresa.
- **Tisk dokumentace:**Tento typ logů zaznamenává, kdo a kdy tiskl dokumentaci AIS Galen. Dále se zobrazuje název a ID dokumentace, která byla tisknutá. Přehled taktéž obsahuje jedinečné identifikátory jako je název počítače, IP adresa a Mac adresa.
- **Zástup:**Tento typ logů zaznamenává, kdo a kdy zastupoval a na kterém pracovišti. Přehled taktéž obsahuje jedinečné identifikátory jako je název počítače, IP adresa a Mac adresa.

1. **Datum od:** Uživatel pomocí této položky volí počátek časového intervalu, ze kterého chce zobrazit bezpečnostní logy.
2. **Datum do:** Uživatel pomocí této položky volí konec časového intervalu, ze kterého chce zobrazit bezpečnostní logy.
3. **Aplikovat**
4. **Exportovat:** Pomocí tohoto tlačítka se exportují logy, které definoval pomocí filtrů, do uživatelem určené složky

## Pravidelný export bezpečnostních logů

Při zapnutí pravidelného exportu dodavatel AIS Galen navolí na základě komunikace se zákazníkem složku, kam budou soubory s logy ukládány. Pravidelný export poté probíhá pravidelně 1x denně v nočních hodinách. Do příslušných souborů jsou vždy uloženy pouze logy, které vznikly od posledního exportu.

![[pages/FONS GALEN/Správce a nastavení/Bezpečnostní logy/assets/image-20250917-081147.png]]
Každý typ logů se exportuje do vlastního souboru. Název souboru je intuitivně pojmenován dle typu logů a data, ze kterého logy pocházejí (např. AuditZaznamu_2023-02-22). Data jsou exportována ve formátu JSON.

Následuje krátký popis jednotlivých klíčů exportovaného JSON souboru:

1. **Oblast:** V tomto klíči je uložená informace o typu logů v daném souboru.

1. **DatumOd:** V tomto klíči je uložená informace o začátku intervalu, ze kterého příslušné logy pocházejí.

1. **DatumDo:**V tomto klíči je uložená informace o konci intervalu, ze kterého příslušné logy pocházejí.

1. **Logy:** V tomto klíči je uložené pole objektů, kdy každý objekt představuje informace o jednom bezpečnostním záznamu.
