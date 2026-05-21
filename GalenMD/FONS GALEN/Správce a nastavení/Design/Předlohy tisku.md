---
title: "Předlohy tisku"
version: 4
updated_at: 2025-06-19
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/49446938
---

# Předlohy tisku

![image-20250618-132039.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-132039.png>)
Záložky Předlohy tisku slouží pro vytváření a editaci předloh tisku formulářů.
Obrazovka je rozdělena na dvé poloviny – Předlohy a Varianty. Logika vychází z předpokladu, že jeden formulář může mít několik variant. Jeden formulář tak má vždy jednu předlohu a alespoň jednu variantu.
Formulář, který se v ordinaci nabízí k vyplnění, je jednotlivou variantou předloh tisku.
Předlohy i varianty jsou rozděleny podle toho, zda byly vytvořeny uživatelem na daném prostředí a společnosti (uživatelské = ano) nebo správce FG (uživatelské = ne).
Uživatelské předlohy i varianty jsou plně ve správě Správce na daném prostředí a společnosti. Předlohy a varianty, které nejsou uživatelské, jsou ve správě FG.

## Předlohy

Uživatelé mohou předlohy pouze přidávat. Po stisknutí zeleného tlačítka Plus v části Předlohy se zobrazí okno na přidání nové předlohy.

![image-20250618-132109.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-132109.png>)
Zde je potřeba zadat mj. **Druh formuláře**. Jedná se o číselník kategorií formulářů, podle kterých jsou formuláře tříděny v kartě pacienta.

![image-20250618-132121.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-132121.png>)
Naopak **Oblast**je textovým polem, tzn. tu si uživatelé dané společnosti na daném prostředí definují sami (pro danou uživatelskou předlohu, nikoli pro všechny předlohy). Formuláře se pod danou oblast zařazují pouze na základě přesného názvu oblasti, a proto by se měl uživatel vyvarovat překlepům. Naopak tak lze pod oblast, která byla vytvořena ze strany FG, zařadit i uživatelskou předlohu. Oblasti uvozují jednotlivé sloupce pro třídění formulářů (LK, OSSZ, Ostatní, Pracovní, apod.).

![image-20250618-132154.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-132154.png>)
Danou předlohu lze omezit pouze pro vybranou **Odbornost**. Takto funkcionalita pracuje tak, že pokud má uživatel přístup na pracoviště s uvedenou odborností, uvidí tento formulář na jakémkoli pracovišti.

## Varianty

![image-20250618-132217.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-132217.png>)
Varianty lze vytvořit dvěma způsoby (oba způsoby pracují bez omezení, zda je jedná o předlohu uživatelskou či nikoliv):

- stisknutím zeleného tlačítku Plus v části Varianty - vytvoří novou prázdnou variantu
- tlačítkem Kopie po označení jiné varianty – vytvoří identickou kopii označené varianty (tlačítko Kopie je aktivní pouze ve chvíli, kdy je vytvořena a označena jedna varianta). V případě, kdy je vytvářena kopie el. laboratorní žádanky, zkopírují se také její nastavení (mapovací soubor, cesta pro uložení eŽádanky na serveru).

Po stisku tlačítka kopie se zobrazí okno, ve kterém uživatel definuje, do jaké předlohy tisku se má nově vytvořená kopie varianty zařadit.

![image-20250618-132329.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-132329.png>)
1. Do stejné předlohy
   Nově vytvořená kopie bude zařazena do stejné předlohy, do které patří varianty, ze které se kopie vytváří.
2. Do nové předlohy
   Po stisku tlačítka se zobrazí okno, ve kterém uživatel definuje novou předlohy, do které se následně kopie zařadí.
3. Do jiné existující předlohy
   Po stisku tlačítka dostane uživatel na výběr seznam již existujících předloh, ze které je možné vybrat právě jednu, do které se nově vytvořená kopie varianty zařadí.

Tlačítko Zakázat pro uživatele slouží k tomu, aby mohla varianta, která není uživatelská, být skryta pro uživatele daného prostředí a společnosti.

### Vytváření obsahu varianty

![image-20250618-132512.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-132512.png>)
V tomto okně se vytváří obsah formuláře

- Zveřejnit

   - publikuje formulář na daném prostředí pro danou společnost
   - ke konkrétní variantě je možné přidat komentář (např. v čem spočívá změna oproti předešlé verzi), který se zobrazí v záložce historie
- Historie

   - přehled zveřejněných verzí varianty
   - po označení dané varianty je možné se k ní vrátit po stisknutí příslušného tlačítka
- Obsah a Pozadí

   - slouží pro překlikávání mezi úpravou obsahu a pozadí formuláře
- Checkbox Aktivní
- Název

   - název varianty dokumentu, pod kterým se zobrazuje uživatelům
- Typ dokumentace

   - výběrové pole Typ dokumentace s možnostmi Kurativa a PLS. Vybraný typ dokumentace se uloží jako výchozí hodnota typu dokumentace pro daný formulář. Tuto výchozí hodnotu je v následné práci s formulářem u konkrétního pacienta možno změnit.
- Omezit pro odbornost
- Nekopírovat do jiné varianty

   - dekurzu lze již vystavené formuláře metodou Drag&Drop kopírovat (již vystavený formulář lze přenést do aktuálního data a vytvořit formulář s identickým obsahem k danému dni). Pokud je tento checkbox zaškrtnut, nelze tuto funkcionalitu u daného formuláře použít.
- Vytvářet jen z vyšetření

   - formulář se nebude nabízet uživatelům v oblasti Formuláře, bude dostupný pouze jako výstup konkrétního vyšetření
- Pozadí

   - (…) zde je možné nahrát obrázek, který bude sloužit jako pozadí formuláře

#### Položka typu seznam

Pomocí položky Parametr-seznam ![image-20250618-133433.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-133433.png>)
 lze vytvořit seznam položek, ze kterého je možné vybrat vždy právě jednu možnost. Po dotažení položky metodu Drag&Drop do formuláře se zobrazí okno pro zadání PropertyName. V rámci formuláře se jedná o unikátní označení dané položky. Toto označení se nikde nezveřejňuje, slouží pouze pro vnitřní identifikaci položek v rámci formuláře. Při zadání PropertyName se uživatel řídí uvedenými instrukcemi.
Po zadání PropertyName se do formuláře vloží prázdná položka, kterou je potřeba naplnit možnosti, resp. položkami seznamu. Položky seznamu je potřeba vepsat do kolonky Values v záložce Vlastnosti.

![image-20250618-133102.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-133102.png>)
Takto zadané položky ve formuláři vypadají takto ![image-20250618-133545.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-133545.png>)
. V tisku potom takto ![image-20250618-133606.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250618-133606.png>)
.

Pomocí dalších vlastností lze nastavit:

1. Rozestup mezi položkami – vlastnost Spacing.
2. Orientaci položek – vlastnost Orientation (horizontální nebo vertikální).

#### Položka typu Combobox

Pomocí položky Parametr-Combobox ![image-20250619-060213.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060213.png>)
 lze vytvořit seznam položek, ze kterých uživatel vybírá právě jednu možnost. Metodou Drag&Drop je potřeba položku umístit do formuláře a zadat PropertyName. Hodnoty do takto vytvoření položky fomuláře je potřeba zadat do kolonky Values v záložce Vlastnosti.

![image-20250619-060244.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060244.png>)
Ve formuláři pak vytvořená položka vypadá takto![image-20250619-060309.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060309.png>)
 resp. takto

![image-20250619-060334.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060334.png>)
resp. takto ![image-20250619-060434.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060434.png>)
 . V tisku pak položka vypadá takto ![image-20250619-060500.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060500.png>)
.

#### Položka typu číselník

Pomocí položky Parametr – Číselník ![image-20250619-060535.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060535.png>)
 lze ve formuláři vytvořit položku, která bude pracovat s položkami vybraného číselníku. Po dotažení parametru do formuláře se zobrazí okno pro výběr konkrétního číselníku.

![image-20250619-060558.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060558.png>)
Zde uživatel zadá PropertyName (požadavky na něj jsou specifikovány v tooltipu) a vybere číselník, se kterým má položka/položky ve formuláři pracovat. Po výběru konkrétního číselníku se zobrazí nabídka sloupců daného číselníku, jejichž obsah se bude dotahovat do kolonek formuláře (platí 1 sloupec číselníku = 1 kolonka ve formuláři).

![image-20250619-060612.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060612.png>)
Sloupec (kolonka) Kód je povinný vždy. U této kolonky se ve formuláři zobrazuje šipka pro rozkliknutí a následný výběr položky z číselníku. Tuto kolonku je však možné pro tisk skrýt (tzn. zobrazí se ve formuláři, nikoli však v tisku) ve vlastnostech dané kolonky (HideForPrint = True).

Po výběru sloupců/položek se vybrané položky přidají do formuláře do levého horního roku. Pouze položka kód se zobrazí v místě, kam byl umístěn parametr (ikona).

Po vložení položek z číselníku do formuláře je možné následně přidat další položku ze stejného číselníku. Stačí označit jednu ze stávajících položek ve formuláři, které k danému číselníku, ze kterého chce uživatel přidat další položku, a stisknout zelené tlačítko PLUS ![image-20250619-060650.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060650.png>)
 .

#### Vložení obrázku do předlohy tisku

Do předlohy tisku lze vložit obrázek přetažením ikony ![image-20250619-060727.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060727.png>)
 do předlohy textu. Po umístění ikony se zobrazí okno s nabídkou nahraných obrázků.

V závislosti na tom, jestli se uživatel pohybuje ve vrstvě pro editaci obsahu ![image-20250619-060756.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060756.png>)
 nebo pozadí ![image-20250619-060815.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060815.png>)
 se nabízí obrázky označené typem Obrázek nebo Pozadí. Typ však lze v okně výběru obrázku změnit a je tak možné nahrát jako pozadí obrázek, který je označen typem Obrázek.

Po umístění obrázku do předlohy tisku lze změnit jeho pozici nebo velikost.

#### Funkce zoom (přiblížení)

Upravovanou předlohu tisku je možné přiblížit posuvníkem, případně kolečkem myši. Zpět na hodnotu 100% je možné se vrátit po kliknutí na ikonu ![image-20250619-060909.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060909.png>)
 .

![image-20250619-060930.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-060930.png>)

### Publikování varianty formuláře

Během procesu vytváření daného formuláře bude uživatel mít potřebu ověřovat, jak se daný formulář bude zobrazovat uživatelům. Formulář v tuto chvíli nepublikuje, ale pouze ukládá.

Pro zobrazení nově vytvořeného formuláře mezi formuláři v nabídce pro uživatele je potřeba zaškrtnout checkbox „Načítat testovací definice“.

![image-20250619-061023.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-061023.png>)
Jakmile je daná varianta formuláře připravena k tomu, aby byla používána všemi uživateli, je možné ji publikovat.

- tlačítkem *Zveřejnit*u variant formulářů
- tlačítkem *Zveřejnit*v editačním poli varianty formuláře

## Obrázky

![image-20250619-061345.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-061345.png>)
Záložka Obrázky slouží pro správu obrázků, které slouží jako pozadí formulářů.

### Popis symbolů ve spodní části panelu

- Zelené tlačítko Plus – slouží pro nahrání nového obrázku z disku počítače. Maximální velikost jednoho obrázku je omezena na 2MB.
- Uživatelské

   - Nic – zobrazí všechny obrázky dostupné pro danou společnost na daném prostředí
   - Ano – obrázek byl nahrán uživatelem a je výhradně v jeho správě
   - Ne – obrázek byl nahrán správcem FG
- Jen aktivní – výchozí hodnota je zaškrtnuto, zobrazí pouze obrázky, které jsou označeny jako aktivní
- Typ – slouží pro lepší orientaci v nahraných obrázcích

   - Pozadí – předpokládá, že obrázek bude použit jako pozadí formuláře (ne však výhradně)
   - Obrázek – předpokládá, že obrázek bude použit v obsahu formuláře
- Využitá kapacita – celková kapacita pro nahrané obrázky je pro uživatele na dané společnosti 1GB.

### Práce s obrázky, které byly nahrány uživatelem

![image-20250619-061632.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-061632.png>)
Kromě zeleného tlačítka Plus, pomocí kterého je možné nahrát nový obrázek, je možné obrázky

#### **editovat**

Po vybrání obrázku a stisknutí modrého tlačítka editovat se otevře nové okno, ve kterém je možné změnit to:

![image-20250619-061727.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-061727.png>)
- zda je obrázek aktivní
- název obrázku
- přidat k obrázku poznámku (tato poznámka slouží jen pro toto okno, nikam jinam se nepřenáší)
- změnit obrázek kliknutím na Vybrat soubor… Po kliknutí se zobrazí upozornění bez ohledu na to, zda ej obrázek použit jako podklad formuláře, či nikoli.

![image-20250619-061808.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-061808.png>)

#### **mazat**

Obrázek je možné mazat stisknutím červeného tlačítka Mínus. Pokud obrázek není použit jako podklad formuláře, bude ihned smazán. Pokud je obrázek použit jako podklad formuláře, tak jej není možné mazat a zobrazí se informace:

![image-20250619-061833.png](<../../../../pages/FONS GALEN/Správce a nastavení/Design/Předlohy tisku/assets/image-20250619-061833.png>)
Obrázek se jako podklad do formuláře nahrává do konkrétní varianty formuláře v záložce Předlohy tisku.
