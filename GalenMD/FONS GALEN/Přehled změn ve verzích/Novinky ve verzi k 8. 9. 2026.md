---
title: "Novinky ve verzi k 8. 9. 2026"
version: 2
updated_at: 2026-09-07
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/577437697
---

# Novinky ve verzi k 8. 9. 2026

# Novinky a vylepšení

---

## Laboratoře

### Integrace laboratorních žádanek WebLims 2 do FONS Galen

Přinášíme vám novou funkcionalitu – přímé propojení FONS Galen s laboratorním systémem WebLims 2 (WL2).

Pokud vaše laboratoř používá WebLims, můžete si od ní vyžádat individuální přihlašovací údaje do WL2 (sdílený účet za pracoviště není podporován) a po jejich nastavení dle návodu vyplňovat laboratorní žádanky přímo z karty pacienta ve FONS Galen – bez přepínání do jiné aplikace.

Co integrace přináší:

- Otevření předvyplněné žádanky WL2 přímo z modulu Formuláře na kartě pacienta (údaje o pacientovi, diagnózy, pojišťovna se předvyplní automaticky).
- Po odeslání žádanky ve WL2 se ve FONS Galen automaticky založí záznam se seznamem vyžádaných metod.
- Živý přehled všech odeslaných žádanek přímo z WL2, dostupný z modulu Komunikace (záložka „WebLims").
- Vždy aktuální nabídku metod, protože ji spravuje přímo laboratoř.

Jak začít:

1. Vyžádejte si od vaší laboratoře přístup na portál WebLims (jde o jiný přístup než stávající zákaznický portál FG) a individuální přihlašovací údaje pro každého lékaře.
2. Správce pracoviště nastaví integraci v detailu pracoviště (tlačítko „Konfigurace lab. žádanek") – zadá formulář/laboratoř, URL WL2 a přístupové údaje pro OAuth komunikaci (Client ID a Client Secret).
3. Po aktivaci konfigurace se lékařům v modulu Formuláře zobrazí karta dané laboratoře a mohou začít žádanky vyplňovat.

Podrobný návod najdete zde: [[Laboratorní žádanky WebLims 2 ve FONS Galen]]

## Přílohy

### Úprava oznámení o nahrání příloh na cloud

Při migraci příloh z lokálního úložiště na cloud se už automaticky negenerují upozornění o jejich nahrání. Nově lze nastavit, zda se mají tato oznámení zobrazovat vůbec, nebo je mít vypnutá.

## Centrová léčba

### Přidání lišty záložek do modulu centrové léčby

V modulu centrové léčby přibyla spodní lišta záložek, díky které se uživatel snadněji pohybuje mezi jednotlivými částmi centrové léčby pacienta.

## eŽádanky

### Zobrazení EZD zámku i pro personál bez zapnuté funkcionality

Informace o uzamčení dokumentu elektronickým zdravotnickým dokumentem (EZD zámek) se nově zobrazí i uživatelům, kteří nemají tuto funkcionalitu aktivně zapnutou – mají tak vždy přehled o tom, že je záznam uzamčen.

## Očkování

### Možnost zadat zahraniční vakcínu mimo číselník SÚKL

Při zadávání očkování je nyní možné vytvořit záznam i bez očkovací látky vedené v číselníku SÚKL (typicky u zahraničních vakcín). Systém u takové látky zobrazí informaci, že není v číselníku SÚKL registrována, a tyto látky se zobrazují i v plánování.

## Recepce

### Zobrazení registrací a evidencí pacienta na pracovištích

Na recepci se nově zobrazují registrace a evidence pacienta na jednotlivých pracovištích, včetně jejich načítání podle prováděného výkonu – recepční tak má rychlejší přehled o tom, kam je pacient zaregistrován.

V konfiguraci info panelu pacienta lze nastavit, a to jak na úrovni společnosti, tak i na úrovni provozovny, zda se mají zobrazovat registrující a evidující pracoviště. Výchozí nastavení je zobrazení obou. Registrující pracoviště zahrnují pouze kapitační pracoviště s odborností 001, 002 a 603, u kterých má pacient v kartě registraci. Evidující pracoviště zobrazují pracoviště mimo tyto odbornosti (001, 002 a 603), na kterých má pacient vykázán alespoň jeden výkon.

## Dekurz – Události

### Použití frází i při zadávání Událostí v Historii

Fráze, které uživatelé dosud využívali i jinde v Galenu, lze nově použít i při zadávání Událostí v Historii pacienta.

## Přístroje

### Export diagnózy z dekurzu do přístroje

Ve výstupní šabloně konfigurace přístroje je nově možné doplnit parametr pro export diagnózy z dekurzu do externího programu ve formátu GDT/TXT. Diagnóza se exportuje ve standardním formátu (kód MKN). Pokud pacient nemá v dekurzu diagnózu vyplněnou, do šablony se žádná diagnóza nevyplní. V případě zájmu o nastavení pro konkrétní přístroj se, prosím, obraťte na podporu Galen.

## Kartotéka

### Vyhledávání pacientů podle výše úhrad a pohledávek v Podrobném filtru

V Podrobném filtru (záložka Základní, sekce Finance pacienta) lze nově vyhledávat pacienty podle rozsahu částek Úhrada celkem a Pohledávky celkem. Díky tomu lze rychle dohledat pacienty s vysokou pohledávkou nebo vysoce uhrazenou částkou, aniž by bylo nutné procházet jednotlivé karty pacientů.
