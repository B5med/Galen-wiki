---
title: "Novinky ve verzi k 5. 5. 2026"
version: 4
updated_at: 2026-05-04
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/383877123
---

# Novinky ve verzi k 5. 5. 2026

# Novinky a vylepšení

---

### Elektronické lékařské posudky

Byla přidána podpora **elektronických lékařských posudků** umožňující vystavování a podepisování posudků v elektronické podobě přímo z aplikace. Podrobný popis funkcionality je dostupný v [uživatelské dokumentaci](https://stapro-galen.atlassian.net/wiki/x/BQBmFQ). Před prvním použitím je nutné provést [nastavení certifikátu](https://stapro-galen.atlassian.net/wiki/x/AQB-Fg) pro elektronický podpis.

### Automatické ukončení neaktivních relací

Systém FONS Galen nově automaticky ukončuje uživatelské relace, které nebyly korektně odhlášeny – například při restartu serveru, výpadku spojení nebo po uplynutí více než 24 hodin bez aktivity. Tato změna zajišťuje, že evidujeme pouze skutečně aktivní přihlášení a zabraňuje tak falešnému překročení licenčních limitů. Současně je potřeba počítat s tím, že v případě neaktivity delší než 24 hodin není možné využívat tzv. "relogin" – pokračovat ve stejném modulu, kde došlo k opuštění práce, a je třeba se místo toho standardně přihlásit.

### Zapamatování výchozího formátu skenu

Při skenování příloh si systém nově pamatuje naposledy zvolený formát souboru. Uživatel tak nemusí při každém skenování znovu vybírat preferovaný formát – systém automaticky předvyplní ten, který byl použit naposledy.

### Vyhledávání v nastavení (zapínačích)

V okně Konfigurace (Správce -> Správa organizace) na úrovni Společnost a Pracoviště bylo přidáno textové vyhledávání. Správci systému nyní mohou rychle filtrovat a dohledat konkrétní nastavení zadáním klíčového slova, bez nutnosti ručně procházet všechny záložky a sekce.

### Název skenované přílohy – pohyb šipkami

Při zadávání názvu skenované přílohy bylo opraveno chování kurzorových šipek. Šipky nahoru a dolů nyní v textovém poli fungují správně pro pohyb v textu, místo aby přesouvaly výběr v nadřazeném seznamu.

---

# Opravy chyb

---

## EKG data do uzamčeného dekurzu

Opravena chyba, kdy se data z přístroje EKG (např. BTL) nepřenášela do dekurzu v případě, že lékař uzamknul záznam dříve, než sestra dokončila měření. V takovém případě, pokud není dohledána návštěva k danému dni a danému odpovědnému lékaři, se založí nová návštěva, do které jsou informace vepsány. O založení nové návštěvy je uživatel informován.

## Statistiky ÚZIS – rehabilitace

Opravena chyba ve výpočtu statistik ÚZIS pro rehabilitační pracoviště. Hodnoty ve sloupcích (zejména FT – fyzikální terapie) jsou nyní počítány správně a odpovídají požadovanému členění dle ÚZIS.

## Smazání očkování u pacienta

Odstraněna chyba, která znemožňovala smazání záznamu o očkování u pacienta. Při pokusu o smazání se zobrazovala chybová hláška o nenalezení vakcinační dávky – tato chyba je nyní opravena.

## eNeschopenky – opakované zobrazení upozornění

Opravena chyba, kdy systém opakovaně zobrazoval upozornění k ošetřovnému a dlouhodobému ošetřovnému přesto, že již bylo uživatelem potvrzeno. Notifikace jsou nyní správně označovány jako zpracované.

## Signální výkon vykázaný navzdory pravidlu

Opravena chyba ve vyúčtování tak, aby uživatel v modulu V*yúčtování* mohl vykázat výkon, který je v rozporu s definovaným pravidlem. O této skutečnosti (že je vykazován výkon v rozporu s pravidlem), je uživatel informován.

## Přetahování dělicí lišty (splitter)

Opraveno chování dělicí lišty (splitteru) v obrazovkách s více panely. Lišta nyní respektuje nastavená minimální a maximální omezení velikosti panelů a nelze ji přetáhnout mimo povolený rozsah.
