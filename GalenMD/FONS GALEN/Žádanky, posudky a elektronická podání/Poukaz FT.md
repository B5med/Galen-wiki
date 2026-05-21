---
title: "Poukaz FT"
version: 2
updated_at: 2025-12-01
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/61440018
---

Na pracovišti s odborností 902 je možné využívat aparát pro práci s přijatými poukazy FT. Tento aparát umožní:

- Evidovat přijaté poukazy pro konkrétního pacienta.

- Využívat informace z tohoto poukazu pro vykazování poskytnuté péče.

- Vázat k tomuto poukazu informace o poskytnuté péči (výkony, zápisy, formuláře).

- Vytvářet na základě vazeb k poukazu zdravotnickou dokumentaci.

## **Základní evidence**

Pro konkrétního pacienta je možné zobrazit seznam evidovaných poukazů pomocí tlačítka *Poukazy FT* v horní liště modulu *Ordinace.*

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084227.png]]
Pozn.: Pokud je pracoviště oprávněné vystavovat také Žádanky RDG – hledejte Poukazy FT pod ikonou Žádanky.

Okno s evidovanými poukazy obsahuje základní filtrace (v levé části) a seznam již evidovaných poukazů (v pravé části).

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084312.png]]
Do vytvářeného poukazu se nakopírují základní identifikační údaje z kartotéky. Dále je nutné zadat několik povinných informací, které jsou ve formuláři označeny červenou hvězdičkou. Zejména se jedná o:

- Přiřazen na prac. - pracoviště, na které je poukaz FT přiřazen

- Platnost poukazu do

- Počet návštěv, během kterých mají být předepsané výkony realizovány

- Požadovaná adresa poskytování péče (v případě, že se jedná o domácí péči, jinak je možné ponechat prázdné)

- Informace o předepisujícím lékaři (zejména IČP a odbornost)

- Diagnóza.

Pole Typ dokumentace je přednastaveno na hodnotu Kurativa a lze jej změnit na PLS. Při volbě PLS se zobrazí doplňkové pole Zaměstnání, kde je potřeba vybrat z číselníku zaměstnání pacienta.

U některých polí (např. adresa, předepisující lékař, …) je možné využít informace z navázaných objektů. K tomu slouží ikona černého trojúhelníku vedle příslušného pole.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084356.png]]
Dále je zapotřebí vyplnit seznam požadovaných výkonů. K tomu slouží editovatelná tabulka ve spodní části dialogu.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084420.png]]
Zde se zadává informace o jednotlivých výkonech a předepsaných počtech těchto výkonů. Ve sloupci *Počet k vykázání* se ve výchozím stavu zrcadlí údaj zadaný jako *Předepsaný počet*. Vůči této hodnotě následně systém kontroluje počty vykázaných výkonů.

Konfiguračně (viz kapitola Konfigurace) lze u určitého výkonu umožnit zadat jinou hodnotu počtu pro vykázání.

**Stav FT poukazu:**

Stav poukazu může editovat pouze pracoviště, na které je FT poukaz přiřazen.

## **Detail pole Stav**

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084516.png]]
Stavy, do kterých nemůže být FT poukaz převeden, je zašedlý.

### **Stavy**

- Nový

Na poukaz není navázána žádná objednávka, ani z něj není vykázán žádný výkon.

- Přijatý

Na poukaz je navázána alespoň jedna objednávka, ale není na něj navázán žádný výkon.

- Ve zpracování

Na FT poukaz je navázán alespoň jeden výkon.

- Zpracován

Tohoto stavu FT poukaz nabývá pouze po ruční změně.

- Neplatný

Tohoto stavu FT poukaz nabývá pouze po ruční změně.

## **Vykazování péče**

Evidované poukazy FT slouží jako „šablony“ pro zadávání výkonů v okně *Výkony*. Seznam těchto poukazů se zobrazuje v pravé části pod šablonami výkonů.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084644.png]]
Kliknutím na příslušné tlačítko se zobrazí dialogové okno pro zadání provedených výkonů.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084706.png]]
Zde je ve sloupci *Vykázat* nutné zadat počty výkonů, které mají být vykázány. Výkony, u kterých bude vykázán počet 0, nebudou následně přeneseny do editoru výkonů.

Dále je možné v části *Svázat záznamy* provázat zápisy v dekurzu z daného dne s daným poukazem. Je zde uveden náhled, a o tom, zda má být vazba vytvořena, rozhoduje škrtátko vedle tohoto náhledu.

Vykázání vybraných výkonů a vytvoření případné vazby mezi zápisem v dekurzu a poukazem se provede pomocí tlačítka *Vykázat výkony*.

(Poznámka: Pokud následně v okně *Výkony*uživatel klikne na tlačítko *Storno*, pak se výkony neuloží, ale vazba mezi záznamem dekurzu a poukazem již zůstane vytvořená.)

## **Podepisování FT poukazů**

*Obě pracoviště, žádající i pracoviště s odborností 902, mají možnost poukaz FT podepsat a následně archivovat.*

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084745.png]]
*Po kliknutí na ikonu EZD  a následně tlačítko Nová  lze zvolit poukaz, který má být podepsán.*

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084807.png]]
*Po jejím zobrazením je možné žádanku upravit/formátovat a po stisknutí tlačítka EZD, resp. ikony v levé části Přehledů poukazů FT, následně podepsat.*

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084829.png]]
![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084843.png]]
Po kliknutí na Podepsat se dokument podepíše a je připraven na odeslání do archívu. Po kliknutí na Odejít dokument nebude podepsán.

## **Evidence dalších vazeb vůči poukazům FT**

### **Záznamy v dekurzu**

Vazbu záznamu v dekurzu na poukaz je možné provést také manuálně a to z okna dekurzu. V šedé liště u zápisu je nutné kliknout na odkaz *Zadat vazbu na poukaz FT*.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084923.png]]

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-084939.png]]

Po kliknutí na tento odkaz se zobrazí dialog *Výběr poukazu FT*, kde uživatel vybere příslušný poukaz a po potvrzení je zápis v dekurzu s poukazem svázán.

Pokud je zapotřebí naopak vazbu mezi dekurzem a poukazem zrušit, je to možné provést kliknutím pravým tlačítkem na odkaz indikujícím navázaný poukaz.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-085002.png]]

### **Vyšetření**

Dalším objektem, který je možné vázat na poukaz FT jsou vyšetření. Zde je vazba doplňována vždy ručně pomocí odkazu *Zadat vazbu na poukaz FT* z detailu vyšetření.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-085026.png]]
Další postup je identický, jako u ručního navázání dekurzu na tento poukaz. Obdobně probíhá i případné odvázání vyšetření z tohoto poukazu.

### **Tvorba dokumentace**

**Zdravotní dokumentace FT**

V modulu *Zpráva* je možné vytvářet zprávy typu *Zdravotní dokumentace FT.*

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-085106.png]]
Pomocí ikony *Nová* v horní liště se zobrazí dialog pro tvorbu zprávy.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-085122.png]]
Zde je nutné zvolit v položce *Typ zprávy* hodnotu *Zdravotní dokumentace FT* a vybrat správný poukaz. Po potvrzení pomocí tlačítka *Ok* je vygenerovaná zpráva z údajů vázaných k tomuto poukazu.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-085136.png]]
Vygenerovanou zprávu je možné dále ručně upravovat.

### **Prázdná hlavička**

V případě potřeby je možné vytvořit také zprávu typu *Prázdná hlavička*. Zde je vygenerována pouze samotná hlavička s definovanými údaji, samotný obsah musí uživatel dopsat kompletně sám.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/Poukaz FT/assets/image-20250701-085209.png]]

## **Konfigurace**

Konfigurace se provádí v modulu *Nástroje*. V horní liště je nutné zvolit ikonu *Rehabilitační výkony* (vedle ikony *Těhotenské akce*).

Zde se zobrazuje tabulka s následujícími sloupci:

- Výkon

Slouží pro zadání kódu výkonu, jehož chování v rámci poukazu FT má být ovlivněno.

- Ruční změna

Jde o příznak, které umožňuje uživateli v rámci poukazu ručně nastavit jiný počet výkonu k vykázání, než jaký lékař předepsal.

- Výchozí násobek

Jedná se o celé číslo určující, jaký násobek předepsaného výkonu se má ve výchozím stavu nastavit jako počet k vykázání.

## **Poukaz FT a Sortiment z recepce**

Z role recepce v modulu Objednávání byly zpřístupněny dvě již používané funkcionality, a to konkrétně FT Poukazy a Sortiment. K oběma funkcionalitám je nutné mít na společnosti zaškrtnutý checkbox Poukaz FT, Sortiment. V horním modrém menu vznikla dvě nová tlačítka FT poukaz a Sortiment. V obou funkcionalitách je oproti stávajícím pouze nový mezikrok výběr pracoviště, jinak jsou funkcionality totožné jako byly doposud. Protože se u zákazníka platí veškerá vyšetření před jeho samotným absolvováním, neevidují tedy žádné pohledávky, vše je hrazeno v hotovosti, v modulu Sortiment tedy nemají spuštěné Faktury. Dají se opět samostatně spustit v checkboxu na společnosti. FT poukazy je možno editovat, či mazat pouze ve stavu nový a vystavený z Recepce. Mohou je vystavovat na všechny pracoviště.
