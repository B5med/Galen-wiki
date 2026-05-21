---
title: "Vyhledání pacienta"
version: 2
updated_at: 2025-07-22
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/76972053
---

# Vyhledání pacienta

**Základní vyhledávání**

1. Pro vyhledání pacienta je možné použít několik způsobů. Nejjednodušší je prostě začít psát příjmení nebo rodné číslo. Je-li kurzor v kartotéce, program čeká, co uživatel udělá. Pokud začne psát písmena, automaticky se spustí vyhledávání dle příjmení, popř. po mezeře pokračuje ve vyhledávání i podle jména. Pokud začne psát číslice, program vyhledává dle rodného čísla. V obou případech si otevře vyhledávací okénko a v něm zobrazuje zapisovaný text.
2. Hledat pacienta je možné také tak, že se klikne myší na ikonku filtru a hledaný text se zapíše přímo do vyhledávacího okénka.

**Podrobný filtr**

![[pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Vyhledání pacienta/assets/image-20250722-081507.png]]
Je-li potřeba detailnější hledání pacienta, klikne se na ikonu Podrobný filtr, kde lze ve formuláři v několika záložkách zvolit kritéria vyhledávání. Vyhledávání se spustí tlačítkem *Aplikovat*.

V podrobném filtru lze ve 4 záložkách zadávat podrobnější parametry vyhledávání, přičemž vyplní-li uživatel parametry ve více záložkách, které nelze vidět všechny najednou, filtr drží všechny zadané údaje a výsledek vyhledávání zohledňuje parametry zadané ve všech záložkách podrobného filtru. Vyhledávání se spustí tlačítkem *Aplikovat*.

![[pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Vyhledání pacienta/assets/image-20250722-083149.png]]
**Podrobný filtr v kartotéce a ve Správě kartoték**

Podrobný filtr byl ze základní verze rozšířen o položky:

- Státní příslušnost
- Skupina PLS (u aktuálně platného zaměstnání)
- RID
- Evidenční číslo SÚZ (v centrální kartotéce chybí)
- Evidenční číslo ČSSZ
- Externí ID PACS
- Datum úmrtí (pouze parametr – checkbox – vyplněno/nevyplněno)
- Existence pohledávky (pouze parametr – checkbox – je/není)
- Neplatné očkování TAT (výběr z možností – platné očkování; po uplynutí povinného intervalu; není nevyplněné)

   - platné očkování – poslední očkování není starší než 15 let
   - po uplynutí povinného intervalu = poslední očkování je starší než 15 let
   - není vyplněné = pacient nemá žádné očkování proti tetanu
- Druh poslední provedené PLS prohlídky (výběr ze zadaných možností v PLS prohlídce) v zadaném intervalu (od-do)
- Platná budoucí objednávka v kalendáři v zadaném intervalu (od-do) - pokud hledáme na pracovišti, tak hledáme v kalendářích, které mají vazbu na dané pracoviště
