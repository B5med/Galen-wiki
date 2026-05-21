---
title: "Příkaz ke zdravotnímu transportu"
version: 2
updated_at: 2025-07-21
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/61145127
---

**Základní konfigurace**

Příkaz ke zdravotnímu transportu jsou nadstavbovou funkcionalitou FONS Galen.

V případě zakoupení příslušné licence jsou ze strany Stapro označena pracoviště určená zákazníkem jako pracoviště poskytující dopravu.

Následně je možné ze strany zákazníka v modulu Správa organizace definovat, která pracoviště mohou na pracoviště dopravy zasílat elektronické žádanky.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Příkaz ke zdravotnímu transportu/assets/image-20250701-105148.png]]
![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Příkaz ke zdravotnímu transportu/assets/image-20250701-105206.png]]
Pro pracoviště dopravy se definují výkony přes smlouvu s pojišťovnou. Po otevření smlouvy uživatel vybere záložku *Dopravy*, kde za pomocí funkčních tlačítek přidává/odebírá výkony dopravy.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Příkaz ke zdravotnímu transportu/assets/image-20250701-105229.png]]
Chování aplikace se pak liší v závislosti na tom, zda je uživatel přihlášen na pracovišti dopravy, nebo na pracovišti, které o dopravu žádá.

**Příkaz ke zdravotnímu transportu**

Příkaz ke zdravotnímu transportu je speciální objekt, který se od ostatních objektů ve FONS Galen odlišuje tím, že s ním během jejího životního cyklu mohou pracovat dvě různá pracoviště (žádající pracoviště a pracoviště provádějící dopravu).

Příkaz ke zdravotnímu transportu nabývá v průběhu času několika stavů:

- **Nová -**Jedná se o vytvořenou žádanku, kterou pracoviště provádějící dopravu ještě

nepřebralo.

- **Předaná** (= předaná ke zpracování) Do tohoto stavu se žádanka dostává ve chvíli, kdy pracovník zatrhne možnost Předat dopravci a dá uloží. Pracoviště dopravy s žádankou může začít pracovat.
- **K vyúčtování** (= byly zadány údaje pro vyúčtování) Do tohoto stavu se žádanka dostává ve chvíli, kdy příslušný pracovník na pracovišti dopravy doplní informace včetně výkonů dopravy a zatrhne „K vyúčtování“.
- **Vyúčtovaná**(= výkony na žádance byly vyúčtovány)

**Pracoviště žádající o provedení dopravy**

Na pracovišti, které má možnost zadávat žádanky dopravy, se v horní liště zobrazuje ikona *Transport*.

Pozn.: Pokud je pracoviště oprávněné vystavovat také *Poukazy FT* nebo *RDG žádanky* – hledejte *Transport*pod ikonou *Žádanky*

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Příkaz ke zdravotnímu transportu/assets/image-20250701-105317.png]]
Pomocí této ikony se zobrazuje seznam žádanek, které byly pro daného pacienta vytvořeny. V tomto seznamu jsou zobrazeny žádanky, které byly vytvořeny na daném pracovišti, nebo které byly vytvořena na pracovišti, na které je definováno nahlížení. Žádanky z ostatních pracovišť jsou zobrazovány šedým písmem.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Příkaz ke zdravotnímu transportu/assets/image-20250701-105338.png]]
Novou žádanku pro daného pacienta je možné vytvořit pomocí ikony (+) nad seznamem žádanek.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Příkaz ke zdravotnímu transportu/assets/image-20250701-105403.png]]
Hlavička žádanky obsahuje:

- Č. žádanky – nelze editovat, bude přiřazeno žádance automaticky
- Var. symbol
- Poř. číslo – nelze editovat, bude přiřazeno žádance automaticky
- Pojišťovna – nelze editovat, údaj z karty pacienta
- Druh pojištění – nelze editovat, údaj z karty pacienta
- Datum vystavení – nelze editovat, aktuální datum
- Typ dokumentace – přednastaveno Kurativa, lze změnit na PLS.

Identifikační údaje žadatele jsou dotahované kontextově a nelze je měnit.

Údaje o transportu obsahují detailní informace o transportu včetně výběru cílového pracoviště dopravy – pokud je k dispozici právě jedno, je předvyplněno.

Při kliknuté do jakéhokoliv z polí *Odkud*nebo *Kam*lze použít klávesovou zkratku CTRL+K pro načtení trvalé adresy pacienta nebo zkratku CTRL+L pro načtení adresy pracoviště lékaře.

Po potvrzení žádanky tlačítkem *OK*se žádanka ukládá a od tohoto okamžiku je dostupná určenému pracovišti dopravy. Případné opravy jsou možné pouze do chvíle, než si pracoviště dopravy žádanku přebere.

**Pracoviště provádějící dopravu**

**Vyhledání nebo tvorba Příkazu k transportu**

Pracoviště provádějící dopravu má dvě možnosti, jak s žádankami pracovat:

1. Pracovat se žádankami konkrétního vybraného pacienta
2. Pracovat se všemi žádankami, které jsou směrovány na pracoviště RDG z ostatních pracovišť (napříč různými pacienty). Žádanky, které byly odeslány na dané pracoviště dopravy, jsou zobrazeny modře, žádanky odeslaná na ostatní pracoviště, jsou zobrazeny šedou barvou.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Příkaz ke zdravotnímu transportu/assets/image-20250701-105505.png]]
V obou případech je možné využít filtr, který je možné předdefinovat a uložit. V seznamu se zobrazují i žádanky pacientů, které dané pracoviště nemusí mít v kartotéce (pokud organizace nemá sdílenou kartotéku).  Tito pacienti jsou do kartotéky zařazeni automaticky.

Pracoviště dopravy má rovněž možnost vytvořit žádanku, která přišla v listinné formě. V takovém případě musí nejprve založit kartu pacienta a následně vstoupit do seznamu žádanek tohoto pacienta (nelze přes seznam žádanek nad celým pracovištěm). Zde se zpřístupní tlačítko (+) pro založení nové žádanky.

Dialog pro vytváření žádanky na pracovišti dopravy je obdobný. Rozdíl je v tom, že na pracovišti dopravy je možné vyplnit i identifikaci žadatele.

**Převzetí Příkazu ke zdravotnímu transportu**

Pracovník dopravy převezme žádanku a začne s ní pracovat. Doplní údaje o dopravě, jako jsou *Odjezd, Příjezd, Vozidlo a Řidič*. Zároveň vykáže výkony vztahující se k dopravě. Případně má možnost vykázat i výkony žadatele.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Příkaz ke zdravotnímu transportu/assets/image-20250701-105537.png]]
Výkony zadané přes žádanku jsou vykázané úplně stejně, jako by byly zadány v editoru výkonů (přes tlačítko Výkon v horní liště ordinace). Po vyúčtování jsou tyto výkony přeneseny na záložku *Vyúčtované výkony žadatele*.

Po zatržení K vyúčtování lze výkony přes modul *Vyúčtování* vyúčtovat na pojišťovnu. Po vyúčtování lze cesty dopravy sledovat v záložce *Transport*.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Příkaz ke zdravotnímu transportu/assets/image-20250701-105600.png]]
**Formuláře**

Přes tlačítko *Formuláře*se uživateli zobrazí seznam Příkaz ke zdravotnímu transportu, ze kterého lze vybrat jeden konkrétní. Tisková podoba formuláře obsahuje přenesená data z příkazu.

**Číselník Míst, Vozidel a Řidičů**

V modulu *Nástroje*(-> *Číselník* -> záložka *Doprava*) lze definovat číselník nabízející se pro položky žádanky, kdy:

- Číselník Místo je pro položky Odkud a Kam

- Číselník Vozidla je pro položky Vozidlo

- Číselník Řidiči je pro položky Řidičů

Nové položky číselníků se přidávají/editují/mažou za pomocí funkčních tlačítek.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Příkaz ke zdravotnímu transportu/assets/image-20250701-105626.png]]
