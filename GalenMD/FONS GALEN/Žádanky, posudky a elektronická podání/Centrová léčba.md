---
title: "Centrová léčba"
version: 2
updated_at: 2026-02-24
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/281739265
---

> [!info]
> **Modul Centrová léčba slouží k evidenci, správě a povinnému elektronickému hlášení dat o indikacích a podáváních inovativních léčivých přípravků v rámci tzv. centrové léčby.**
>
> Tato povinnost vyplývá z požadavků Ústavu zdravotnických informací a statistiky ČR (ÚZIS) a je legislativně závazná pro všechna pracoviště, která smluvně poskytují centrovou léčbu.

**Modul umožňuje:**

- evidovat léčby pacientů – zahájení, průběh, ukončení;
- zaznamenávat jednotlivá podání léčiva;
- sledovat stav každého podání;
- automaticky vykazovat výkon (kód 99991) po odeslání podání;
- filtrovat a přehledně zobrazovat seznam léčeb a podání;
- procházet historii změn u každé léčby.

---

### Kdy funkci použít

> [!info]
> Modul Centrová léčba je určen pro lékaře na pracovištích, která mají uzavřenu zvláštní smlouvu o centrové léčbě.

**Použijete jej ve chvíli, kdy:**

- zahajujete u pacienta léčbu inovativním léčivým přípravkem v rámci centrové léčby;
- aplikujete pacientovi dávku léčiva a potřebujete toto podání zaznamenat;
- potřebujete upravit nebo ukončit probíhající léčbu (a zadat důvod změny);
- chcete zkontrolovat stav odesílání dat na ÚZIS nebo zjistit, zda hlášení proběhlo bez chyby;
- potřebujete rychlý přehled všech léčeb nebo podání pro celé pracoviště nebo konkrétního pacienta.

V klinickém pracovním postupu typicky přistoupíte do modulu po ambulantní návštěvě pacienta léčeného centrovou léčbou, nebo pravidelně na konci ordinační doby, abyste zkontrolovali stavy odeslaných hlášení.

---

## Otevření modulu a orientace v přehledech

1. Otevřete modul Centrová léčba z hlavního menu systému FONS Galen.

   ![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Centrová léčba/assets/obrazek-20260224-080708.png]]
2. V modulu uvidíte dvě záložky: Léčby a Podání.
3. Záložka Léčby zobrazuje seznam všech léčeb (pacient, diagnóza, léčivo, paragraf, stav).
4. Záložka Podání zobrazuje přehled jednotlivých aplikací léčiva ke každé léčbě.
5. Použijte filtry v horní části obrazovky pro vyhledání podle pacienta, léčiva, stavu, paragrafu nebo časového období.
6. Dvojklikem na řádek otevřete detail léčby nebo detail podání.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Centrová léčba/assets/obrazek-20260224-081902.png]]

---

## Zahájení nové léčby pacienta

1. V záložce Léčby klikněte na tlačítko pro přidání nové léčby.
2. Vyplňte základní informace: vyberte pacienta, zadejte diagnózu, vyberte léčivo z číselníku, zvolte příslušný paragraf.
3. Nastavte datum zahájení léčby.
4. Uložte novou léčbu. Systém ověří, zda pro daného pacienta a léčivo již neexistuje aktivní léčba.
5. Po uložení se nová léčba zobrazí v přehledu.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Centrová léčba/assets/obrazek-20260224-082211.png]]

---

## Zaznamenání podání léčiva

1. V přehledu léčeb dvojklikem otevřete detail příslušné léčby, nebo přejděte přímo do záložky Podání.
2. Klikněte na tlačítko pro přidání nového podání.
3. Vyplňte: datum podání, léčivo, množství a další potřebné údaje.
4. Uložte podání. Systém automaticky zkontroluje, zda datum podání spadá do platnosti léčby.
5. Po uložení je podání evidováno ve stavu Rozpracováno.
6. Po odeslání do ÚZIS je podání evidováno ve stavu Odesláno.
7. Podání, které ještě nebylo odesláno na ÚZIS, lze upravit nebo smazat.
8. Podání, které již bylo odesláno na ÚZIS, lze upravit nebo stornovat.Odeslání podání na ÚZIS a automatické vykázání výkonu

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Centrová léčba/assets/obrazek-20260224-082445.png]]

---

## Změna nebo ukončení léčby

1. Otevřete detail léčby dvojklikem v záložce Léčby.
2. Zvolte akci Upravit léčbu nebo Ukončit léčbu.
3. Vyberte důvod změny nebo ukončení z číselníku (výběr je povinný).
4. Zadejte datum změny nebo ukončení.
5. Uložte. V detailu léčby se zaktualizuje stav a zobrazí se záznam o změně v historii.

---

## Odeslání podání na ÚZIS a automatické vykázání výkonu

> [!info]
> Odesílání hlášení na ÚZIS probíhá prostřednictvím integrovaného rozhraní přímo ze systému FONS Galen. Po úspěšném přijetí podání systém automaticky vytvoří výkon 99991 (je-li nasmlouván) a ZULP a přiřadí jej k pacientovi, léčbě a podání. Tento výkon je viditelný v detailu podání.

1. V přehledu podání vyberte podání ve stavu Rozpracováno, které chcete odeslat na ÚZIS.
2. Klikněte na tlačítko Odeslat.
3. Systém odešle data na ÚZIS a aktualizuje stav podání.
4. Zkontrolujte stav odeslání.
5. V případě stavu Chyba si přečtěte hlášení o chybě, opravte příslušné podání a odešlete znovu.
6. Po úspěšném přijetí (stav Přijato) systém automaticky zaúčtuje výkon 99991 určený pracovišti se zvláštní smlouvou.

---

## Příklady použití

### Příklad: Zahájení léčby a evidence prvního podání

MUDr. Novák je revmatolog, jehož pacient pan Kratochvíl (68 let) byl indikován k léčbě biologickým léčivým přípravkem v rámci centrové léčby revmatoidní artritidy. Pracoviště má uzavřenou smlouvu s pojišťovnou a je povinno každý měsíc reportovat data o podáních na ÚZIS.

#### Postup MUDr. Nováka v systému FONS Galen:

1. Otevře modul Centrová léčba a v záložce Léčby klikne na Nová léčba.
2. Vybere pacienta Kratochvíl, zadá diagnózu (M05 – séropozitivní revmatoidní artritida), vybere léčivo z číselníku a zvolí příslušný paragraf.
3. Uloží léčbu se dnešním datem zahájení.
4. Po první aplikaci přejde do záložky Podání, přidá nové podání: zadá datum aplikace, léčivo a množství.
5. Klikne na Odeslat – systém hlášení odešle na ÚZIS a stav podání se změní na Odesláno.
6. Po potvrzení příjmu ze strany ÚZIS se stav změní na Přijato a systém automaticky vytvoří výkon 99991 (ZULP) v přehledu výkonů pacienta.

## Doporučené postupy

- Podání evidujte co nejdříve po aplikaci, ideálně tentýž den – snížíte tím riziko opomenutí.
- Před odesláním vždy zkontrolujte stav podání v přehledu a ověřte správnost dávky a data aplikace.
- V případě stavu Chyba přečtěte hlášení a opravte konkrétní pole, které chybu způsobilo.
- Historii změn léčby využijte pro dohledání, kdo a kdy léčbu upravoval.
- Filtr v přehledu Podání podle stavu Chyba vám rychle zobrazí všechna neúspěšně odeslaná podání.

## Technická omezení

- Číselníky léčiv a paragrafů jsou automaticky aktualizovány jednou týdně ze zdrojů ÚZIS, je možné je ručně aktualizovat v případě potřeby.
- Napojení na API ÚZIS a samotné odesílání dat jsou součástí aktivní implementace a mohou být dále rozšiřovány.

> [!warning]
> - Modul Centrová léčba je určen pouze pro pracoviště, která mají uzavřenou zvláštní smlouvu o centrové léčbě. Pokud modul nevidíte, obraťte se na správce systému, aby jej aktivoval pro vaše pracoviště.
> - Automatické vykázání výkonu ZULP (kód 99991) probíhá pouze na pracovištích se zvláštní smlouvou. Pokud výkon není zasmluvněn, nebude vytvořen.
> - Pro jednoho pacienta nelze současně vést dvě aktivní léčby stejným léčivem. Systém na duplicitu upozorní.
