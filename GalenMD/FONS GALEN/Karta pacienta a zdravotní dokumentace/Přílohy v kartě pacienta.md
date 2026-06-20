---
title: "Přílohy v kartě pacienta"
version: 4
updated_at: 2026-06-19
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/463699982
---

# Přílohy v kartě pacienta

## Co jsou přílohy

Přílohy slouží k ukládání souborů (dokumentů, obrázků, výsledků z přístrojů apod.) přímo v kartě pacienta. Přílohy jsou součástí zdravotnické dokumentace a jsou přístupné oprávněným uživatelům ze všech pracovišť.

Typicky se přikládají PDF dokumenty, obrázky (JPG, PNG), RTF soubory nebo výstupy z přístrojů.

Každá příloha má nastavenou **maximální povolenou velikost**, která je určena administrátorem v nastavení společnosti.

## Kam se přílohy ukládají

Ve výchozím nastavení se přílohy ukládají lokálně. Uživatel s rolí *Správce* na úrovni *Společnost*nebo *Pracoviště*v modulu *Správa organizace* nastaví složku, kam se budou přílohy ukládat. Může se jednat o umístění v počítači uživatele nebo o cestu ke sdílenému disku.

V rámci nadstandardní funkcionality je možné aktivovat ukládání příloh do cloudu. Každá příloha tak bude přístupná na všech počítačích, na kterých Galen spustíte.

## Kde lze přílohy v Galenu vkládat

Přílohy lze připojit na více místech v systému, vždy v kontextu konkrétního záznamu:

**Návštěva** – příloha je vázána ke konkrétní návštěvě (dekurzu).

**Těhotenství** – přílohy lze vkládat v rámci záznamu o těhotenství.

**Poukaz FT** – příloha k poukazům na fyzioterapii.

**Upozornění** – příloha v rámci modulu upozornění pacienta.

## Kde lze přílohy zobrazit

Přílohy vložené k pacientovi jsou dostupné na několika místech v systému, a to v závislosti na kontextu jejich vložení a nastavení pracoviště.

**Historie v kartě pacienta** je hlavním místem pro přehled veškeré přílohové dokumentace pacienta. Zobrazují se zde přílohy vázané přímo na pacienta, ale i přílohy z návštěv, žádanek a dalších záznamů. Seznam lze filtrovat podle kategorie, data vložení. Každou přílohu lze z tohoto seznamu otevřít, stáhnout nebo smazat (v závislosti na pravidlech editace).

**V rámci návštěvy (dekurzu)** se přílohy přiložené ke konkrétní návštěvě zobrazují přímo v záznamu návštěvy.

**V kontextu konkrétního záznamu** – přílohy vázané na žádanku, těhotenství, poukaz FT nebo upozornění jsou dostupné vždy přímo v daném záznamu, nikoliv v globálním seznamu příloh pacienta.

## Kategorie příloh

Každá příloha musí být zařazena do **kategorie**. Kategorie slouží k přehledné organizaci a umožňují filtrování. Správce společnosti může seznam kategorií upravovat v nastavení Galenu.

Výchozí kategorie v systému:

| Kategorie | Účel / poznámka |
| --- | --- |
| Laboratorní výsledky | Výsledky z laboratoře |
| Lékařská zpráva | Zprávy od jiných lékařů, propouštěcí zprávy apod. |
| EKG | Záznamy EKG |
| Ultrazvuk | Ultrazvukové snímky a zprávy |
| RTG | Rentgenové snímky a nálezy |
| Obrazová dokumentace | Fotografie, obrázky |
| Hospitalizace | Dokumentace z hospitalizace |
| Přístroj | Výstupy z diagnostických přístrojů |
| Žádanka | Přílohy k žádankám |
| Upozornění | Přílohy k upozorněním |
| Sledování defektů | Fotodokumentace defektů (ran, kožních lézí apod.) |
| PLS | Přílohy pro modul PLS (pracovnělékařské služby) |
| Jiné | Obecná kategorie pro ostatní dokumenty |

> Kategorie označené speciálním účelem (Ultrazvuk, Sledování defektů, PLS) jsou provázány s konkrétními moduly Galenu a mohou ovlivňovat dostupnost přílohy v daném kontextu. Tyto kategorie nelze deaktivovat.

---

## Vlastnosti přílohy

Při vkládání přílohy uživatel vyplňuje nebo systém automaticky doplní:

**Název** – popisný název přílohy, který se zobrazuje v seznamu. Název odpovídá jménu souboru bez přípony a lze ho před vložením upravit. Galen při uložení automaticky odstraní znaky, které nejsou v názvech souborů povoleny – konkrétně řídicí znaky a znaky `\ / : * ? " < > |`. Pokud název po odstranění těchto znaků zůstane prázdný, Galen ho nahradí aktuálním datem a časem ve formátu `RRRR-MM-DD_HH-mm`. O provedené úpravě názvu Galen uživatele upozorní hlášením.

**Kategorie** – povinné zařazení přílohy (viz výše).

**Datum** – datum přílohy (výchozí je dnešní den).

**Poznámka** – volitelný textový komentář k příloze.

## Vkládání příloh

Přílohy lze vložit několika způsoby:

**Manuální vložení** – uživatel klikne na tlačítko pro přidání přílohy, vybere soubor ze svého počítače a potvrdí.

**Skenování** – pokud je nakonfigurován skener, lze dokument naskenovat přímo z rozhraní Galenu.

**Automatické přiložení ze zařízení** – u přístrojů (EKG, ultrazvuk apod.) lze nakonfigurovat automatické přebírání výstupních souborů. Galen sleduje nastavený adresář a soubory nabídne k přiložení do přílohy.

## Práce s přílohami

**Zobrazení** – přílohu lze otevřít kliknutím. Galen ji zobrazí v interním prohlížeči nebo předá operačnímu systému ke spuštění příslušnou aplikací.

**Stažení / uložení** – přílohu lze uložit na lokální disk.

**Smazání** – přílohu může smazat oprávněný uživatel. Smazaná příloha je označena jako odstraněná, ale z databáze se fyzicky nevymaže (soft delete).

**Filtrování** – v seznamu příloh je možné filtrovat podle kategorie, data a dalších parametrů.

**Zamčení dokumentace** – pokud je na kartě pacienta aktivní zámek dokumentace, může být editace (včetně vkládání příloh) omezena.

## Podpisování příloh

Některé kategorie příloh podporují **elektronický podpis pacientem** (biometrický podpis). Přílohy, které byly podepsány, jsou v systému označeny příznakem „Podepsáno pacientem". Tato funkce vyžaduje aktivovaný modul biometrického podpisu.
