---
title: "Novinky ve verzi k 28. 7. 2026"
version: 2
updated_at: 2026-07-27
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/515670018
---

# Novinky ve verzi k 28. 7. 2026

# Novinky a vylepšení

---

### Anamnéza – výpočet balíčkoroků (kalkulačka)

V souvislosti se změnami v preventivních prohlídkách (od 1. 1. 2026) přibyl v Anamnéze automatický výpočet balíčkoroků. Hodnoty potřebné pro výpočet nyní zadáte přímo v Anamnéze a systém hlídá jejich správné vyplnění.

### Fráze – zrušen limit pro počet znaků

Při vytváření a editaci frází byl odstraněn limit počtu 5000 znaků. Fráze je tak nově bez omezení. Omezení počtu znaků je tak kontrolováno až při konkrétním použití, kde v případě, že entita má omezení na počet znaků, je o tom uživatel informován.

### Vyúčtování – zvláštní oprávnění uživatele „Specialista vyúčtování"

Umístění: Uživatel → sekce Zvláštní oprávnění. Uživateli s tímto zaškrtnutým oprávněním se v modulu Vyúčtování zpřístupní záložka Smlouvy, kde lze spravovat nastavení smluv pro vyúčtování (pracoviště, zařízení, hromadná správa). Bez tohoto oprávnění se záložka v menu modulu vůbec nezobrazí. Oprávnění umožňuje editovat smlouvy s pojišťovnami a smluvní výkony přímo z modulu Vyúčtování, bez nutnosti přístupu do modulu Správa organizace.

### Správa společností – kontrola duplicitního IČO

Galen nově kontroluje, aby se stejné IČO nevyskytovalo u dvou různých společností nebo podřízených společností. Kontrola se spouští jen při skutečné změně IČO. Pokud je zadané IČO již použité u jiného aktivního subjektu, zobrazí se hláška „Zadané IČO je v systému již použito. Zkontrolujte prosím správnost zadaného IČO. Požadovaná změna nebyla uložena." a změna se neuloží.
