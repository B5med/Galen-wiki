---
title: "RDG žádanky"
version: 1
updated_at: 2025-07-01
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/60850197
---

# RDG žádanky

## **Obecný popis**

### **Základní konfigurace**

RDG žádanky jsou nadstavbovou funkcionalitou FONS Galen.

V případě zakoupení příslušné licence jsou ze strany Stapro označena pracoviště určená zákazníkem jako pracoviště poskytující radiodiagnostiku.

Následně je možné ze strany zákazníka v modulu *Správa organizace* definovat, která pracoviště mohou na pracoviště radiodiagnostiky zasílat elektronické žádanky.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-085811.png]]
![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-085835.png]]
Chování aplikace se pak liší v závislosti na tom, zda je uživatel přihlášen na pracovišti radiodiagnostiky, nebo na pracovišti, které o radiodiagnostické vyšetření žádá.

## **Konfigurace komunikace s PACS**

Během procesu zpracovávání *RDG žádanky* může probíhat komunikace s PACS. K tomu je zapotřebí na stanici, která má patřičnou konektivitu, nakonfigurovat přístroj typu *Obecný RTG* nebo *Obecné externí zařízení*.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-085913.png]]
![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-085928.png]]
V konfiguraci přístroje je zapotřebí zvolit několik atributů. Zásadním je přiřazení daného přístroje RDG žádankám (šipka 1) a určení spouštěcí události (šipka 2).

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-090002.png]]
Spouštěcí události jsou tři:

1. Žádanka – vyvolává se ve chvíli, kdy je *RDG žádanka* pracovištěm radiodiagnostiky přebrána

2. Nález – vyvolává se ve chvíli, kdy je k *RDG žádance* doplněn popis nálezu

3. Prohlížeč – je-li nastaven, pak se v horní liště *RDG žádanky* zobrazuje tlačítko pro vyvolání prohlížeče snímků

Pro každou událost je možné nakonfigurovat samostatný „přístroj“, nebo je případně možné nastavit jeden „přístroj“ pro více spouštěcích událostí. Která varianta má být použita se liší v závislosti na konkrétní implementaci PACS.

V případě spouštěcích události *Žádanka* a *Nález* se typicky exportují vybrané informace. FONS Galen tyto informace exportuje do souborů na základě definovaných šablon. Šablony jsou textové soubory, které kombinují části napevno určeného textu a zástupné řetězce, které jsou v čase exportu nahrazeny konkrétními hodnotami.

V rámci konfigurace je zapotřebí určit cestu k šabloně, cestu k adresářům, do kterých má být vystupovaný soubor uložen apod.

S konfigurací těchto šablon, stejně jako s dalšími atributy, Vám ochotně pomohou pracovníci Stapro, budou k tomu však potřebovat dokumentaci od Vašeho dodavatele PACS, nebo alespoň kontakt na zodpovědnou osobu dodavatele.

## **Konfigurace infopanelu pacienta**

V sekci *Správa organizace*-> IČP -> *UI konfigurace* je na záložce *Infopanel pacienta* možné zadat počet posledních *RDG žádanek*, které se mají v infopanelu pacienta zobrazovat.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-090051.png]]
V infopanelu pacienta se následně zobrazují nálezy ze zadaného počtu poslední *RDG žádanek*daného pacienta.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-102549.png]]
Jednotlivé nálezy se zobrazují ve sbalené formě, vždy je možné kliknutím rozbalit jeden z nich (obdobný princip, jako při zobrazování dekurzu v infopanelu).

## **Žádanka RDG**

Žádanka RDG je speciální objekt, který se od ostatních objektů ve FONS Galen odlišuje tím, že s ní během jejího životního cyklu mohou pracovat dvě různá pracoviště (žádající pracoviště a pracoviště provádějící radiodiagnostiku).

Žádanka RDG nabývá v průběhu času několika stavů:

- **Nová**

**Jedná se o vytvořenou žádanku, kterou pracoviště provádějící zobrazovací diagnostiku**ještě nepřebralo. Do tohoto stavu se žádanka dostává ve chvíli, kdy je vytvořena (na žádajícím pracovišti, nebo i na pracovišti radiodiagnostiky v případně listinných žádanek).

- **Přijatá** (= přijatá ke zpracování) Do tohoto stavu se žádanka dostává ve chvíli, kdy jí pracovník na pracovišti radiodiagnostiky otevře z fronty nových žádanek a oklasifikuje jí (doplní výkony, doplní klasifikaci ČRK, …). Je možná i ruční změna stavu bez nutnosti uvedené údaje zadávat. Při přechodu do tohoto stavu může být (v závislosti na konfiguraci) odesílána informace do PACS.

- **Zpracovaná**(= bylo provedeno snímkování) Do tohoto stavu se žádanka dostává ve chvíli, kdy jí příslušný pracovník na pracovišti radiodiagnostiky doplní o informace o provedeném měření (zadá údaje o expozici, formáty pořízených snímků, …). Bude možná i ruční změna stavu bez nutnosti zadání údajů o provedeném měření.

- **Popsaná**

**Do tohoto stavu se žádanka**dostává ve chvíli, kdy k ní lékař na pracovišti radiodiagnostiky doplní popis snímku. Při přechodu do tohoto stavu může být (v závislosti na konfiguraci) odesílána informace do PACS.

## **Pracoviště žádající o provedení radiologického vyšetření**

Na pracovišti, které má možnost o provedení radiologického vyšetření požádat, se v horní liště zobrazuje ikona *Žádanky RDG*.

Pozn.: Pokud je pracoviště oprávněné vystavovat také *Poukazy FT* – hledejte Žádanky RDG pod ikonou *Žádanky.*

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-102702.png]]
Pomocí této ikony se zobrazuje seznam žádanek, které byly pro daného pacienta vytvořeny. V tomto seznamu jsou zobrazeny žádanky, které byly vytvořeny na daném pracovišti, nebo které byly vytvořena na pracovišti, na které je definováno nahlížení. Žádanky z ostatních pracovišť jsou zobrazovány šedým písmem.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-102723.png]]
Novou žádanku pro daného pacienta je možné vytvořit pomocí ikony (+) nad seznamem žádanek.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-102743.png]]
Dialog pro vytvoření nové žádanky je rozdělen na dvě části: větší levá část slouží k zadávání samotné žádanky, pravá část zobrazuje žádanky, které jsou k danému pacientovi evidované.

Hlavička žádanky obsahuje:

- Č. žádanky – nelze editovat, bude přiřazeno žádance automaticky

- Platnost do – přednastaveno na 3 měsíce

- Urgentnost – přednastavena Rutina, lze změnit na Statim

- Typ dokumentace – přednastaveno Kurativa, lze změnit na PLS. Při volbě PLS se zobrazí doplňkové pole Zaměstnání, kde je potřeba vybrat z číselníku zaměstnání pacienta.

Identifikační údaje žadatele jsou dotahované kontextově a nelze je měnit. Požadované vyšetření vyplňuje uživatel, který žádanku vytváří. Vybírá mj. i cílové pracoviště radiodiagnostiky – pokud je k dispozici právě jedno, je předvyplněno.

V pravé části je možný dvojí pohled na ostatní žádanky:

1. Seznam vyšetření – tabulka s hlavičkovými údaji

V případě výběru jedné se pod tabulkou zobrazuje popis. Dvojklikem je možné žádanku rozkliknout do náhledu.

2. Seznam nálezů – textový blok vygenerovaný ze všech popisů všech žádanek

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-102814.png]]
Po potvrzení žádanky tlačítkem *Ok* se žádanka ukládá a od tohoto okamžiku je dostupná určenému pracovišti radiodiagnostiky. Případné opravy jsou možné pouze do chvíle, než si pracoviště radiodiagnostiky žádanku přebere.

Až od okamžiku, kdy je žádanka na pracovišti radiodiagnostiky popsaná, se žádajícímu pracovišti nezobrazují žádné další informace k žádance (s výjimkou změn stavů). Po vytvoření popisu je součástí žádanky i blok *Nálezu.*

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-102853.png]]
Pomocí ikony šipky je možné text přenést do dekurzu a zde jej dále upravovat.

V případě RdgDruhu SG (Skiagrafie) a věku pacientky 15 až 50 let, bude povinné zatrhnout možnost Těhotenství viz. obrázek níže.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-102916.png]]

## **Pracoviště provádějící radiodiagnostiku**

### **Vyhledání nebo tvorba RDG žádanky**

Pracoviště provádějící radiodiagnostiku má dvě možnosti, jak s RDG žádankami pracovat:

1. Pracovat se žádankami konkrétního vybraného pacienta

2. Pracovat se všemi žádankami, které jsou směrovány na pracoviště RDG z ostatních pracovišť (napříč různými pacienty). Žádanky, které byly odeslány na dané RDG pracoviště, jsou zobrazeny modře, žádanky odeslaná na ostatní pracoviště, jsou zobrazeny šedou barvou.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103006.png]]
V obou případech je možné využít filtr, který je možné předdefinovat a uložit. V seznamu se zobrazují i žádanky pacientů, které dané pracoviště nemusí mít v kartotéce (pokud organizace nemá sdílenou kartotéku).

Při rozkliku takové žádanky je uživatel informován, že je zapotřebí pacienta nejprve do kartotéky zařadit.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103029.png]]
Pracoviště radiodiagnostiky má rovněž možnost vytvořit žádanku, která přišla v listinné formě. V takovém případě musí nejprve založit kartu pacienta a následně vstoupit do seznamu žádanek tohoto pacienta (nelze přes seznam žádanek nad celým pracovištěm). Zde se zpřístupní tlačítko (+) pro založení nové žádanky.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103049.png]]
Dialog pro vytváření RDG žádanky na pracovišti radiodiagnostiky je obdobný. Rozdíl je v tom, že na pracovišti radiodiagnostiky je možné vyplnit i identifikaci žadatele a že zároveň s vytvořením žádanky je možné provést klasifikaci žádanky, zadat parametry provedeného vyšetření apod.

### **Převzetí RDG žádanky**

Pracoviště radiodiagnostiky v prvním kroku RDG žádanku přijímá. To může provést několik způsoby:

- Tlačítkem *Přijatá* v horní liště žádanky (šipka 1) – tímto tlačítkem je možné přijmout RDG žádanku, která byla původně přiřazena na jiné RDG pracoviště a je ve stavu *Nová*. Tím se přeřadí na aktuální RDG pracoviště.

- Výběrem data převzetí (šipka 2)

- Zadáním klasifikace/výkonů/pohledávky/výšky a hmotnost/těhotenství (šipka 3)

- Pole výška a hmotnost/ těhotenství

- Tyhle hodnoty zadané při vytvoření žádanky, může pracoviště RDG zadáním v sekci klasifikace aktualizovat – do formuláře se budou brát tyhle hodnoty

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103140.png]]
V rámci převzetí je možné žádanku klasifikovat kódy České radiologické klasifikace.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103203.png]]
Zároveň je možné přímo vykázat potřebné výkony.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103225.png]]
Výkony zadané přes RDG žádanku jsou vykázané úplně stejně, jako by byly zadány v editoru výkonů (přes tlačítko *Výkon* v horní liště ordinace). Po vyúčtování jsou tyto výkony přeneseny na záložku *Vyúčtované výkony*.

Obdobným způsobem je možné pacientovi zadat pohledávku – platbu v hotovosti, ať již manuálně nebo výběrem z definovaného sortimentu.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103246.png]]
Samotná platba pohledávky se provádí již v okně pokladny. Po uhrazení se přesouvá ze záložky *Pohledávky* na záložku *Uhrazené pohledávky.*

Ve chvíli, kdy obsluha vyplní klasifikaci, výkon nebo pohledávku, je doplněn *Datum převzetí*automaticky, není-li již zadán.

### **Zpracování žádanky**

Pracoviště radiodiagnostiky v druhém kroku RDG žádanku označuje jako zpracovanou. To může provést několik způsoby:

1. Tlačítkem *Přijatá* v horní liště žádanky (šipka 1)

2. Výběrem data zpracování (šipka 2)

3. Zadáním expozičních hodnot (šipka 3)

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103330.png]]
Expoziční hodnoty jsou aktuálně řešeny jako kombinace dvou textových polí *Metoda* a *Hodnota*. Ve chvíli, kdy obsluha vyplní expoziční hodnoty, je doplněn *Datum provedení* automaticky, není-li již zadán.

### **Popis žádanky**

Žádanka se do stavu *Popsaná* dostává v okamžiku, kdy je k ní uložen *Popis nálezu*.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103418.png]]
Ve chvíli, kdy je žádanka s popisem uložena, přechází do stavu *Popsaná* a nález se začne zobrazovat i na pracovišti, které vyšetření požadovalo.

Je možné žádanku uložit s rozpracovaným popisem, aniž by se tento zpřístupnil pracovišti, které vyšetření požadovalo. To je možné vypnutím škrtátka *Nález dokončen* (ve výchozím stavu je zapnuté), viz Obr.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103438.png]]

### **Podepisování RDG žádanky**

Obě pracoviště, žádající i provádějící radiodiagnostiku, mají možnost RDG žádanku podepsat a následně archivovat. Jelikož během životního cyklu jedné RDG žádanky s žádankou pracují různí uživatelé, není možné při podepisování žádanku uzamknout proti další editaci. Proto se vždy po kliknutí na tlačítko EZD vygeneruje nad danou žádankou PDF dokument obsahující aktuální data RDG žádanky, který následně uživatel podepíše a odesílá do archivu EZD. Samotná RDG žádanka zůstává nadále editovatelná, aby s ní mohli pracovat další uživatelé.

Nad vybranou RDG žádanku lze v modulu *Žádanky RDG* vygenerovat PDF k podpisu přes tlačítko *EZD* na následujících místech:

- v okně editace konkrétní RDG žádanky

- ve formulářích nad danou RDG žádankou

- nad seznamem RDG žádanek

***Podepisování RDG žádanky v okně editace RDG žádanky***

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103514.png]]
Po kliknutí na tlačítko *EZD* se zobrazí náhled PDF dokumentu k podepsání s aktuálními daty RDG žádanky.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103529.png]]
Kliknutím na *Podepsat* se dokument podepíše a je připraven na odeslání do archivu. Po kliknutí na *Odejít* dokument nebude podepsán a okno náhledu se uzavře.

V pravém dolním rohu okna editace RDG žádanky je zobrazen seznam všech podepsaných PDF dokumentů, vygenerovaných nad danou RDG žádankou.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103549.png]]
Kliknutím pravým tlačítkem myši nad konkrétním podepsaným dokumentem lze vyvolat kontextovou nabídku a dokument stornovat.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-103604.png]]
***Podepisování RDG žádanky ve formulářích***

V případě, že uživatel požaduje zobrazit data editované RDG žádanky na podkladu určitého formuláře (tiskopisu), např. Poukaz Z, může tak učinit kliknutím na tlačítko *Formuláře*.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-104525.png]]
V dalším kroku vybere požadovaný formulář, nad kterým chce data RDG žádanky zobrazit. Takto zobrazený formulář lze opět podepsat prostřednictvím tlačítka *EZD*.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-104541.png]]
Po kliknutí na tlačítko *EZD* se zobrazí náhled PDF dokumentu k podepsání s aktuálními daty RDG žádanky na podkladu vybraného formuláře.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-104604.png]]
Kliknutím na *Podepsat* se dokument podepíše a je připraven na odeslání do archivu. Po kliknutí na *Odejít* dokument nebude podepsán a okno náhledu se uzavře.

***Podepisování RDG žádanky nad seznamem RDG žádanek***

Uživatel má možnost podepsat RDG žádanku nad seznamem RDG žádanek, aniž by vstupoval do editace dané žádanky.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-104630.png]]
Kliknutím označíme žádanku, kterou chceme podepsat a následně klikneme na tlačítko EZD. Zobrazí se náhled dokumentu k podepsání, který obsahuje aktuální data RDG žádanky.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-104731.png]]
Kliknutím na *Podepsat* se dokument podepíše a je připraven na odeslání do archivu. Po kliknutí na *Odejít* dokument nebude podepsán a okno náhledu se uzavře.

K lepšímu přehledu, která žádanka byla na daném pracovišti již podepsána a která ještě ne, slouží v seznamu *Žádanky RDG* sloupec *Podepsáno*.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-104749.png]]

## **Komunikace s PACS**

Je-li nakonfigurovaná komunikace s PACS (viz kapitola 1.2), probíhá na pracovišti radiodiagnostiky automaticky odeslání informací ve dvou okamžicích:

1. Při přijetí žádanky – odchází informace o žádance

2. Při uložení popis – odchází popis nálezu

Stav odeslání indikuje signální bod v záhlaví příslušné sekce.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-104917.png]]
Odeslání je možné vyvolat i ručně, a to kliknutím pravým tlačítkem myši na signální bod a výběrem volby *Odeslat do PACS* z kontextového menu.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/RDG žádanky/assets/image-20250701-104946.png]]
