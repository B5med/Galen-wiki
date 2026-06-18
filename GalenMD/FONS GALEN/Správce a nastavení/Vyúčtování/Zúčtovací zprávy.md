---
title: "Zúčtovací zprávy"
version: 2
updated_at: 2026-06-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/461045784
---

# Zúčtovací zprávy

Projekt zúčtovacích zpráv má za cíl zajistit kompletní evidenci záznamů ze zúčtovacích zpráv v programu Galen, porovnání s odeslanými fakturami a dávkami, ke kterým se zúčtovací zpráva vztahuje, přiložení této zúčtovací zprávy k faktuře v Galen.

Modul zúčtovacích zprávy je nadstandardním placeným modulem.

## Typy zúčtovacích zpráv

V AIS Galen je možné evidovat více typů zúčtovacích zpráv

- Měsíční

- Kvartální

- Roční

- Revizní

**Měsíční** zúčtovací zpráva slouží jako centrální místo pro opravu chybných dokladů, výkonů, atp.

**Ostatní typy** zúčtovacích zpráv existují bez vazby na fakturu či podání. Význam ostatních typů zúčtovacích zpráv je pouze evidenční, tzn. nemají vazbu na doklady, výkony v AIS Galen.

## Manipulace se zúčtovacími zprávami

Pro zúčtovací zprávy je vytvořen nový modul, který se otevírá pomocí ikony *Zúčtovací zprávy*

![image-20260618-090427.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090427.png>)
 v modulu *Správce->Vyúčtování.*

Z tohoto seznamu je možné pracovat se všemi typy zúčtovacích zpráv.

![image-20260618-090449.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090449.png>)
Výjimkou je zakládání měsíční zúčtovací zprávy, které bude možné pouze ze seznamu faktur nebo ze seznamu podání.

### Zakládání a úprava měsíčních zúčtovacích zpráv ze seznamu faktur

Pro založení zúčtovací zprávy s vazbou na fakturu je nutné vstoupit do modulu *Správce->Vyúčtování->Faktury*. V zobrazeném seznamu faktur uživatel vybere fakturu/faktury, nad kterými chce založit zúčtovací zprávu.

![image-20260618-090512.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090512.png>)
Uživatel vybírá ty faktury, kterých se týká zúčtovací zpráva od pojišťovny, kterou chce zpracovat. Jedná o ty faktury, které mají společné období, pojišťovnu, pobočku pojišťovny, vyúčtovací skupinu a IČZ. Faktura může být navázána na právě jednu zúčtovací zprávu, a proto není možné vybrat fakturu, která již je v jiné zúčtovací zprávě v AIS Galen zahrnuta. Pokud vybrané faktury pravidlo splňují, zobrazuje se nad seznamem faktur aktivní tlačítko **Založit ZZp**.

Tlačítko **Zobrazit ZZp** bude aktivní v případě, kdy je vybrána alespoň jedna faktura, která již na je zúčtovací zprávu navázána.

![image-20260618-090535.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090535.png>)
Obě tlačítka zobrazí na detail **měsíční** zúčtovací zprávy.

- V případě *Založit ZZp*se vytvoří nová měsíční zúčtovací zpráva (zatím jen v paměti).

- V případě *Zobrazit ZZp*se načte již existující zúčtovací zpráva, včetně případných změn vyznačených uživatelem.

Poznámka: Pokud by bylo uživatelem označeno více faktur vázaných na různé zúčtovací zprávy, zobrazí se zúčtovací zpráva k poslední označené faktuře.

Pokud detail zúčtovací zprávy uživatel opustí tlačítkem OK, budou provedené změny uloženy. Pokud detail zúčtovací zprávy uživatel opustí tlačítkem Storno, nebudou provedené změny uloženy.

### Zakládání a úprava měsíčních zúčtovacích zpráv ze seznamu podání

Pro založení zúčtovací zprávy s vazbou na podání je nutné vstoupit do modulu *Správce->Vyúčtování->Přehled->záložka Podání*.

Uživatel vybírá ta podání, kterých se týká zúčtovací zpráva od pojišťovny, kterou chce zpracovat. Jedná o ta podání, která mají společné období, pojišťovnu, pobočku pojišťovny, vyúčtovací skupinu, IČZ a nejsou vázány k žádné zúčtovací zprávě. Pokud vybraná podání pravidlo splňují, zobrazuje se nad seznamem podání aktivní tlačítko ***Založit ZZp***.

![image-20260618-090611.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090611.png>)
Pokud je aspoň jedno z podání již navázáno na zúčtovací zprávu v AIS Galen, zobrazí se tlačítko ***Zobrazit ZZp***.

![image-20260618-090630.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090630.png>)
Obě tlačítka zobrazí na detail **měsíční** zúčtovací zprávy.

- V případě *Založit ZZp*se vytvoří nová měsíční zúčtovací zpráva (zatím jen v paměti).

- V případě *Zobrazit ZZp*se načte již existující zúčtovací zpráva, včetně případných změn vyznačených uživatelem.

Poznámka: Pokud by bylo uživatelem označeno více podání vázaných na různé zúčtovací zprávy, zobrazí se zúčtovací zpráva k poslednímu označenému podání.

Pokud detail zúčtovací zprávy uživatel opustí tlačítkem *OK*, budou provedené změny uloženy. Pokud detail zúčtovací zprávy uživatel opustí tlačítkem *Storno*, nebudou provedené změny uloženy.

### Zakládání ostatních typů zúčtovacích zpráv ze seznamu zúčtovacích zpráv

Základní scénář použití je:

1. Uživatel vstoupí do modulu *Správce -> Vyúčtování*, v horní liště klikne na ikonu *Zúčtovací zprávy*.

2. Systém zobrazí seznam evidovaných zúčtovaných zpráv.

   ![image-20260618-090703.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090703.png>)

3. Uživatel použije tlačítko pro vytvoření zúčtovací zprávy požadovaného typu (*Kvartální*, *Roční*, Revizní).

4. Zobrazí se prázdná zúčtovací zpráva, uživatel vyplní základní identifikační údaje.

5. Pokud detail zúčtovací zprávy uživatel opustí tlačítkem *OK*, budou provedené změny uloženy. Pokud detail zúčtovací zprávy uživatel opustí tlačítkem *Storno*, nebudou provedené změny uloženy.

### Zobrazování, editace zúčtovacích zpráv ze seznamu zúčtovacích zpráv

Již založené zúčtovací zprávy vč. Zúčtovacích zpráv měsíčních, je možné vyhledat a zobrazit v modulu *Zúčtovací zprávy* ![image-20260618-090726.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090726.png>)
 . Pomocí filtru uživatel vyhledá konkrétní zúčtovací zprávu, může zobrazit její detail a v závislosti na jejím stavu může provádět úpravy.

## Detail měsíční zúčtovací zprávy

Detail měsíční zúčtovací zprávy vypadá takto

![image-20260618-090757.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090757.png>)
Okno je rozděleno do několika částí, které na sebe vzájemně reagují.

1. Stav zúčtovací zprávy

Zúčtovací zprávy může nabývat stavů

- Ke zpracování – jedná se o novou zúčtovací zprávu, na které je nutné provést takové úpravy, aby byl rozdíl na zúčtovací zprávě roven nule.

- Zpracovaná – rozdíl na zúčtovací zprávě je roven nule, ale zpráva ještě nebyla uzavřená.

- Uzavřená – rozdíl na zúčtovací zprávě je roven nule a zpráva byla uzavřena. Nyní už na ní nelze provádět změny.

2. Možnost přidat ke zúčtovací zprávě přílohy, např. originál zúčtovací zprávy.

3. Seznam faktur/Seznam podání, ze kterých byla zúčtovací zpráva v AIS Galen vytvořena.

Pomocí tlačítka PLUS je možné přidat další faktury/podání, které splňují pravidla uvedená v kapitole Zakládání a úprava měsíčních zúčtovacích zpráv ze seznamu podání/faktur.

4. Rekapitulace

- **Požadováno** = Celkem za faktury/podání

- **Uznáno**= uživatel vyplní částku, kterou mu pojišťovna na zúčtovací zprávě uznala

- **Rozdíl**= rozdíl mezi celkovou požadovanou a uznanou platbou

- **K opravě**= částka, kterou je nutné v rámci zúčtovací zprávy v AIS Galen opravit. Rozdíl – suma za rozšiřující položky – suma rozdílů za kapitační dávky – suma za doklady ve stavech Odmítnutý/K opravě/K novému zúčtování/Opravený

- **Z toho kapitace uznáno**= uživatel vyplní částku, kterou mu pojišťovna na zúčtovací zprávě uznala za kapitace

- **Z toho kapitace rozdíl** = rozdíl mezi celkovou požadovanou částkou za kapitaci a uznanou platbou za kapitaci

- **Rozpočítat** = rozpočítání rozdílu mezi kapitační dávky

5. Rozšiřující položky

Umožňují korigovat rozdíl v částce k opravě.

6. Dávky

Seznam dávek z faktur/podání, ze kterých je zúčtovací zpráva vytvořena. Je možné označit právě jednu dávku a zobrazit tak doklady a výkony v ní obsažené.

7. Doklady

Jsou zobrazené pouze ty doklady, které patří do dávky, která je v sekci Dávky označena.

Nad doklady je možné v této části provádět opravy.

Pro změnu stavu dokladu slouží tlačítka nazvaná podle stavu, do kterého mají doklad převést. Aktivní jsou vždy pouze ta tlačítka, která provádí realizovatelný přechod stavu.

Pomocí multiselectu lze označit více dokladů. V tom případě jsou aktivní pouze ta tlačítka, která jsou realizovatelná u všech vybraných dokladů.

Změny provedené na dokladech (změna stavu, kód chyby) se následně promítnou do navázaných výkonů^^ a projeví se v hodnotách rozdílu v hlavičce.

![image-20260618-090847.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090847.png>)
- **Vyk. = vykázaný**
- **Odm. = odmítnutý**

K dokladu ve stavu *odmítnutý* je možné zadat kód chyby výběrem z číselníku a případně poznámku k chybě (ruční zápis).

S dokladem ve stavu *odmítnutý* se již v dalším případném vyúčtování nepracuje.

![image-20260618-090900.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090900.png>)
- **KO = K opravě**

Dokladům ve stavu *K opravě* budou po uzavření zúčtovací zprávy automaticky vytvořeny kopie ve stavu *Opravný* a tyto kopie budou připraveny k zařazení do opravného vyúčtování.

K dokladu ve stavu *K opravě* je možné zadat kód chyby výběrem z číselníku a případně poznámku k chybě (ruční zápis).

Dále je možné změnit datum, ke kterému má být nově vzniklý opravný doklad vykázán.

![image-20260618-090911.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090911.png>)
V rámci opravy dokladu je možné

- Upravit kartu pacienta

- Změnit pacienta, kterému výkony na dokladu budou vykázány

- Upravit registraci daného pacienta

   ![image-20260618-090927.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090927.png>)

Dále je možné u dokladu ve stavu *K opravě* změnit typ dokladu

![image-20260618-090935.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090935.png>)
- **KNV = K novému vyúčtování**

Dokladům převedeným do stavu *K novému vyúčtování* budou automaticky po uzavření zúčtovací zprávy vytvořeny kopie ve stavu *Nový*. Tyto kopie ve stavu *Nový* budou připraveny k zařazení do řádného vyúčtování.

K dokladu ve stavu *K novému vyúčtování* je možné zadat kód chyby výběrem z číselníku a případně poznámku k chybě (ruční zápis).

Dále je možné změnit datum, ke kterému má být nově vzniklý doklad vykázán.

![image-20260618-090945.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090945.png>)
V rámci změny *K novému vyúčtování* je možné

- Upravit kartu pacienta

- Změnit pacienta, kterému výkony na dokladu budou vykázány

- Upravit registraci daného pacienta

   ![image-20260618-090956.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-090956.png>)

Dále je možné u dokladu ve stavu *K novému vyúčtování* změnit typ dokladu

![image-20260618-091007.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-091007.png>)
8. Výkony/ZUM/Cesty/Foniatrické záznamy

Úpravy je možné dělat na úrovni dokladů tak, jak bylo popsaná v předchozí kapitole, nebo až na úrovní jednotlivých výkonů/ZUM/cest/foniatrických záznamů, které jsou na jednotlivých dokladech obsaženy.

Uživatel v přehledu dokladů vybere doklad, na kterém je obsažen výkon, který je potřeba upravit.

Opravy na úrovní výkonů poskytují stejné možnosti jako na úrovni dokladů, i když mírně omezené.

Výkony mohou nabývat stavů:

- Vykázaný

- Odmítnutý – s výkonem v tomto stavu se v případných dalších vyúčtování nepracuje.

- K novému vyúčtování – výkon v tomto stavu bude po uzavření zúčtovací zprávy převeden do stavu *Opravený* a zároveň bude vytvořena jeho kopie ve stavu *Nový* připravená k zařazení do řádného vyúčtování.

Tlačítko pro změnu stavů opět reagují na základě stavu vybraného výkonu/ů.

![image-20260618-091030.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-091030.png>)
U výkonu ve stavu K novému vyúčtování je možné upravit

![image-20260618-091041.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-091041.png>)
A – Údaje v kartě stávajícího pacienta nebo výkon vykázat k jinému pacientovi.

B – Změnit stav dokladu, na kterém bude výkon vykázán.

C – Zadat kód chyby výběrem z číselníku a případně připsat textovou poznámku k chybě.

D – Změnit datum, ke kterému bude nově vytvořený výkon vykázán. Nahradit původní výkon novým výkonem. Změnit počet nově vykazovaných výkonů. Změnit diagnózu, se kterou je nově vzniklý výkon vykazován. Pokud budou pole ponechána prázdná, budou použity údaje z původního výkonu.

## Uzavření zúčtovací zprávy

Po uzavření zúčtovací zprávy budou vytvořeny kopie dokladů a výkonů, které ve zúčtovací zprávě byly označeny stavem *K opravě* nebo k *Novému vyúčtování* a tyto kopie budou automaticky převedeny do příslušných stavů a připraveny k novému (řádnému)/opravnému vyúčtování, které uživatel následně provede standardním způsobem.

Uzavřít zúčtovací zprávu je možné ve chvíli, kdy je zúčtovací zpráva ve stavu Zpracovaná. To znamená, že hodnota v poli *K opravě* je rovna nule.

![image-20260618-091100.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-091100.png>)
Uživatel uzavře zúčtovací zprávu tlačítkem Uzavřít ![image-20260618-091108.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-091108.png>)
 .

Po uzavření zúčtovací zprávy si uživatel může zobrazit opravy provedené v rámci dané zúčtovací zprávy stisknutím tlačítka *Opravy* ![image-20260618-091125.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-091125.png>)
 .

Pokud v zúčtovací zprávě vznikly opravy, je potřeba je znovu odeslat na pojišťovnu standardním způsobem, tzn. stisknutím tlačítka Vyúčtovat ![image-20260618-091142.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Zúčtovací zprávy/assets/image-20260618-091142.png>)
 v modulu Vyúčtování.
