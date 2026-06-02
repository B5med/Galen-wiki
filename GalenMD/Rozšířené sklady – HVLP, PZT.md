---
title: "Rozšířené sklady – HVLP, PZT"
version: 2
updated_at: 2026-06-01
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/108494849
---

# Rozšířené sklady – HVLP, PZT

## Základní popis

FONS Galen v základní verzi umožňuje evidovat skladové zásoby očkovacích látek. Coby nadstavbovou funkcionalitu je možné zapnout rozšíření skladů o další typy evidovaných komodit.

V rámci rozšířených typů skladů je možné evidovat následující typy zboží:

- HVLP
- PZT
- MTZ
- Ostatní

V případě HVLP a PZT je realizováno provázání na vykazování ZUM/ZULP v editoru výkonů.

## Konfigurace systému

### Zapnutí rozšířených skladů

Rozšířené typy skladů se zapínají na konkrétních pracovištích.

Zapnutí funkcionality na konkrétních pracovištích mohou provádět pouze pracovníci Stapro.

### Skladový sortiment

Je-li alespoň na jednom pracovišti organizace zapnuto rozšíření skladů, je v modulu *Správce -> Správa organizace -> Agendy* doplněna záložka *Skladový sortiment*.

![image-20250901-073146.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073146.png>)
Definují se zde skladové položky, které má být možné na skladech dané společnosti evidovat. Skladové karty na jednotlivých skladech následně vznikají ve vazbě na skladový sortiment a na základě jeho definice je následně definován způsob práce se skladovou kartou.

Základními atributy skladové sortimentu jsou:

- **Název, doplněk názvu**
   Uživatelsky (správcovsky) zadané textové hodnoty popisující dané zboží.
- **Typ zboží**
   Typ rozdělující sortiment na léky, zdravotnické prostředky a ostatní.
- **Jednotka příjmu, jednotka výdeje**
   Popisuje, v jakých jednotkách je dané zboží přijímáno a vydáváno (např. příjem v baleních, výdej v tabletách). Samotná skladová evidence je následně realizována ve výdejových jednotkách.
- **Přepočet příjmu na výdej**
   Popisuje, kolik „výdejových jednotek“ odpovídá jedné „příjmové jednotce“.  Např. jedno balení obsahuje 10 tablet.
- **Povinné zadávání kódu při příjmu**
   Příznak popisující, zda je nutné při příjmu uvádět kód zboží. Pokud je zapnut, musí být při příjmu uveden alespoň jeden identifikátor zboží (viz dále).

![image-20250901-073230.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073230.png>)
Pro potřeby další funkcionality (např. v budoucnu plánovaného příjmu elektronických dodacích listů) je k sortimentu možné definovat seznam kódů, které zboží identifikují. Každý kód je definován pomocí těchto atributů:

- **Druh kódu**
   Jedná se o atribut popisující, o jaký kód se jedná (kdo jej vydává). Nabývá hodnot SÚKL, EAN, PDK, REF. Specifický je REF (katalogové číslo), který sám o sobě není jednoznačně identifikující – tím se stává až v kombinaci s identifikací dodavatele, která se uvádí do atributu **IČO dodavatele**.

- **Kód**
   Hodnota kódu pro daný sortiment

- **Přepočet příjmu na výdej**
   Jakým poměrem mají být v případě tohoto kódu přepočteny příjmové jednotky na výdejové.

Není možné zadat kódy SÚKL, které odpovídají kódům přiřazeným očkovacím látkám, pro skladovou evidenci těchto látek jsou určeny sklady očkovacích látek ze základní funkcionality programu.

## Práce s rozšířenými sklady

Práce s rozšířenými sklady probíhá ve stejném okně, jako práce s očkovacími látkami. Základní rozvržení okna je shodné s rozvržením okna u skladů očkovacích látek.

![image-20250901-073329.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073329.png>)
Jsou-li na daném pracovišti zapnuty rozšířené sklady, zobrazuje se nad seznamem skladových karet přepínač *Typ skladu*.

![image-20250901-073349.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073349.png>)

### Založení skladové karty

Skladová karta se zakládá pomocí tlačítka (+) nad seznamem skladových karet. Při zakládání je nutné určit, podle jakého skladového sortimentu má být skladová karta vytvořena.

![image-20250901-073416.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073416.png>)
V rámci definice skladové karty se uvádí také minimální množství dané komodity ve výdejových jednotkách. Systém následně upozorňuje, pokud množství na skladě klesne pod tuto hodnotu.

![image-20250901-073436.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073436.png>)
Skladová karta je podle definice sortimentu zařazena na sklad správného typu.

V rámci editace skladové karty je možné skladovou kartu deaktivovat (pokud již nadále nemá být zboží na daném skladu evidováno).

### Příjem zboží

Příjem zboží na danou skladovou kartu je možné provést dvojím způsobem:

- Tlačítkem *Naskladnit* nad seznamem šarží

- Tlačítkem *Naskladnit*na řádku konkrétní šarže

Rozdíl mezi oběma způsoby spočívá v tom, že při příjmu z konkrétní šarže je předvyplněný kód šarže, exspirace a případně vybraný kód, kterým je zboží identifikováno.

![image-20250901-073518.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073518.png>)
![image-20250901-073532.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073532.png>)
![image-20250901-073550.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073550.png>)
Mezi základní informace, které je nutné zadat, patří datum a čas příjmu (automaticky se nastavuje aktuální datum a čas, ale je možné provést změnu), šarže a datum exspirace.

Podle nastavení skladového sortimentu může být možné nebo povinné kliknutím vybrat kód zboží, které je přijímáno.

Dále je nutné zadat množství, které je naskladňováno. Toto množství se zadává v příjmových jednotkách definovaných na skladovém sortimentu a systém toto množství automaticky přepočítává na výdejové jednotky (ty nelze zadat ručně).

Zadání cenových informací je volitelné, zadávají se nákupní ceny pro danou příjmovou jednotku. Po potvrzení tlačítkem *OK* je příjem dokončen.

### Přehled pohybů dané šarže

V základním stavu se v přehledu šarží zobrazují všechny šarže, které jsou aktivně skladem. To indikuje stav rozbalovacích seznamu *Stavy skladu – Všechny šarže*.

![image-20250901-073622.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073622.png>)
Při výběru (jeden klik myši) konkrétní šarže v seznamu šarží se ve spodní části okna zobrazuje informace o realizovaných pohybech (příjmech, výdejích, …) této šarže.

![image-20250901-073737.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073737.png>)
Systém si pro každou šarži pamatuje příjem a ceny, se kterými byl tento příjem realizován. Výdej (viz dále) pak realizuje s vazbou na příjem.

Při dvojkliku na konkrétní šarži dojde k zobrazení jednotlivých *cenových vět*. *Cenovou větou* se rozumí jeden kód šarže přípravku, přijatý v jeden konkrétní okamžiku s konkrétní cenou.

- Jedna šarže za stejnou cenu přijatá dopoledne a odpoledne představuje dvě samostatné cenové věty.

- Jedna šarže dodaná na jednom dodacím listu se dvěma různými cenami představuje dvě samostatné cenové věty.

Při výběr konkrétní cenové věty se následně v okně pohyby zobrazují pouze pohyby dané cenové věty

![image-20250901-073811.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073811.png>)
Rozbalovací seznam *Stavy skladu* v takovém případě obsahuje konkrétní šarži. Přepnutí zobrazení z přehledu cenových vět konkrétní šarže na všechny šarže se provede pomocí tlačítka *Všechny šarže* vedle seznamu *Stav skladu.*

### Výdej ze skladu

Výdej ze skladu je možné realizovat třemi způsoby

- Ze skladové šarže

- Z cenové věty

- Z editoru výkonů v modulu *Ordinace*

#### Výdej ze skladové šarže

Jsou-li v seznamu šarží zobrazeny všechny šarže, je možné vyskladnění provést kliknutím na tlačítko *Vyskladnit* z řádku dané šarže.

![image-20250901-073855.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073855.png>)
Informace k výdeji zahrnují především datum výdeje (přednastavený je aktuální okamžik) a množství, které má být vydáno (ve výdejových jednotkách).

![image-20250901-073911.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073911.png>)
Cenová věta, ze které má být zboží vyskladněno, je určena principem FIFO (dříve naskladněná cenová věta se odepisuje dříve). Pokud je požadováno vyskladnění většího množství, může být výdej realizován z více cenových vět zároveň. Pokud je požadováno vyskladnění většího množství, než kolik je dané šarže na skladě, není vyskladnění realizováno a uživatel je vyzván ke změně množství.

#### Výdej z cenové věty

Pokud není žádoucí realizovat výdej s využitím principu FIFO, je možné „rozkliknutím“ šarže zobrazit konkrétní cenové věty, které tuto šarži tvoří. Na každé z nich je následně možné využít tlačítko *Vyskladnit*.

![image-20250901-073955.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-073955.png>)
Z hlediska zadávaných informací se již výdej dále neodlišuje od výdeje šarže.

#### Výdej z editoru výkonů

Výdej ze skladu je možný i v rámci zadání ZUM/ZULP v editoru výkonů.

Editor výkonů je transakční dialog, tzn. až do chvíle, než je definitivně potvrzen (a projdou všechny kontroly), se nic neukládá. Může tak dojít k situaci, že mezi zadáním ZUM a skutečným odpisem ze skladu uplyne určitá chvíle, během které se může stav skladu změnit, apod.

Výdej je proto realizován dvoufázově. V okamžiku zadání ZUM si systém pouze zapamatuje, kterou šarži bude vyskladňovat, a teprve v okamžiku skutečného uložení provede vyskladnění.

Při zadávání ZUM (přes tlačítko Z+ vedle výkonu) se zobrazuje stejný dialog, jako obvykle, pouze je tento dialog rozšířen o sloupec *Skladem*. Zde se zobrazuje v zásadě trojí informace:

- **Ano**, zboží je k dispozici na některém skladě
   Zadání ZUM je vždy doprovázeno současným odepsáním ze skladu

- **Ne**, zboží není k dispozici na žádném dostupném skladě
   Zadání ZUM je možné, ale systém žádá potvrzení, že má být ZUM vykázán bez vazby na skladové hospodářství.

- **--**, k danému zboží neexistuje žádná skladová karta
   Zadání ZUM je možné bez jakýchkoli omezení.

V případě zadání ZUM spojeného s výdejem ze skladu je dialog pro zadání ZUM mírně upraven.

![image-20250901-074043.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-074043.png>)
Uživatel zde má k dispozici několik přepínačů, pomocí kterých může výdej ovlivnit:

1. **Výběr sortimentu**
   Pokud je u vícero skladového sortimentu uveden daný kód pro vykázání, má uživatel možnost zvolit, ze kterého sortimentu chce vybírat.

2. **Výběr skladu**
   Je-li daná položka na vícero skladech, má uživatel možnost určit, ze kterého skladu chce vybírat. Je-li skladů více než jeden, zobrazuje se v kulatých závorkách jejich počet.

3. **Výběr šarže**
   Je-li daná položka na daném skladu ve vícero šaržích, má uživatel možnost určit, kterou šarži chce vydat. Je-li šarží více než jedna, zobrazuje v kulatých závorkách jejich počet.

4. **Počet**
   Jaké množství chce uživatel vyskladnit. Udává se ve výdejových jednotkách, pro vykázání se množství přepočte podle hodnoty *Množství ZUM* uvedené ve skladovém sortimentu.

Po potvrzení dialogu je vedle řádku se ZUM uvedena informace o tom, že položka je připravena pro výdej ze skladu.

![image-20250901-074113.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-074113.png>)
![image-20250901-074113.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-074113.png>)
K samotnému výdeji dojde až po uložení celého dialogu. Při vyskladnění se vybere cenová věta s využitím principu FIFO.

Informace vedle ZUM následně potvrzuje, že k výdeji již došlo.

![image-20250901-074136.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-074136.png>)
Pokud by mezitím došlo z jiného PC k odepsání zboží ze skladu, bude při ukládání uživatel upozorněn a rovněž informace vedle ZUMu se změní.

![image-20250901-074157.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-074157.png>)
![image-20250901-074213.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-074213.png>)
V takovém případě musí uživatel rozkliknut název ZUM a v dialogu vybrat jinou šarži pro odepsání.

Při použití šablony výkonů se v případě, že definovaný ZUM má vazbu na skladu, zobrazí po aplikaci šablony informace, že je nutné určit šarži, která má být ze skladu odepsána.

![image-20250901-074301.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-074301.png>)
V takovém případě musí uživatel rozkliknut název ZUM a v dialogu vybrat šarži pro odepsání.

##### *Mazání ZUM v editoru výkonů*

Případné mazání ZUM je možné provést standardně pomocí pravého tlačítka myši a volbou *Smazat ZUM*.

![image-20250901-074340.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-074340.png>)
Při mazání má uživatel možnost rozhodnout, zda má být zboží vráceno na skladu, nebo zda má zůstat již odepsáno. Pokud zvolí možnost, že má zůstat odepsáno, je u daného výdeje na skladě evidována informace, že k výdeji došlo na základě vydaného ZUM.

![image-20250901-074359.png](<../pages/Rozšířené sklady – HVLP, PZT/assets/image-20250901-074359.png>)
