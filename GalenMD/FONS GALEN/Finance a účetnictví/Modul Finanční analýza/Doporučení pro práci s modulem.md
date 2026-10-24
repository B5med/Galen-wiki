---
title: "Doporučení pro práci s modulem"
version: 2
updated_at: 2026-10-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/114262017
---

# Doporučení pro práci s modulem

## Obecně

- Po aktivaci modulu počkejte do následujícího dne, než budou data k dispozici.
- Změny vstupních údajů se projeví až po nočním zpracování, tedy následující den.
- Věnujte pozornost vysvětlivkám u sloupců a polí (ikona **i**).
- Pro další zpracování dat využijte export do Excelu.

## První nastavení vstupních údajů

1. Otevřete **Výchozí údaje → Úhradové parametry**.
2. U každé pojišťovny vyplňte **Vstupní úhradu** z vyúčtování pojišťovny za referenční období. Bez ní není výpočet kompletní.
3. Porovnejte hodnoty *Vypočteno systémem* (počet bodů a počet unikátních pojištěnců v referenčním období) s vyúčtováním. Pokud se liší, zadejte hodnoty z vyúčtování.
4. Druhý den zkontrolujte výsledky ve Finančním přehledu.

## Pojišťovna mi sdělila PURO

Pokud máte s pojišťovnou sjednané PURO, které se liší od vypočteného, zadejte ho do pole **PURO (ref. obd.)** ve sloupci *Zadaná hodnota* v detailu úhradového parametru dané pojišťovny. Zadaná hodnota má přednost před vypočtenou a použije se pro výpočet limitace.

## Splňuji podmínky pro navýšení

1. V rozšířené verzi zkontrolujte na obrazovce **Analytik** záložky *Navýšení hodnoty bodu* a *Navýšení koeficientu navýšení*.
2. Barva ukazuje splnění jednotlivé podmínky, nikoli nárok na navýšení. Nárok posuzuje pojišťovna.
3. Pokud vám pojišťovna navyšení přizná, zadejte ho ručně – Galen ho sám nezmění:

   - hodnotu bodu ve **Výchozí údaje → Hodnota bodu** (pole Navýšení hodnoty, případně Specifická navyšení pro konkrétní pojišťovnu nebo IČZ),
   - koeficient navýšení ve **Výchozí údaje → Úhradové parametry** (pole Koeficient navýšení v detailu úhradového parametru).

## Porovnání s analýzou nebo vyúčtováním pojišťovny

- Ověřte, že porovnáváte stejná období. Hodnoty ve Finančním přehledu jsou kumulované od ledna do zvoleného měsíce.
- V rozšířené verzi rozlišujte vykázaná data a modelaci (sloupec Modelace). Modelované řádky obsahují odhad do konce roku.
- Pole s označením *(ref. obd.)* ve Výchozích údajích se týkají referenčního období (předminulého roku), nikoli aktuálního roku.
- Galen počítá z vykázaných dat. Pojišťovna může vycházet z uznaných dokladů nebo z jiného období, proto se čísla mohou lišit.

## Nezobrazují se data

- Zkontrolujte vybraný rok a nastavené filtry.
- Některé záložky mohou být oprávněně prázdné (např. pokud nebyla poskytnuta péče cizincům).
- Po aktivaci modulu nebo po změně vstupních údajů počkejte na noční zpracování.
