---
title: "EZD – elektronická zdravotní dokumentace"
version: 5
updated_at: 2026-02-16
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/47546437
---

# EZD – elektronická zdravotní dokumentace

Elektronický archiv slouží pro ukládání dokumentů elektronické zdravotní dokumentace. Elektronický dokument se stává platným až po uložení do archivu, kde je ověřen.

Napojení na el. archiv zdravotnické dokumentace je placenou nadstavbou. V případě zájmu o napojení je potřeba kontaktovat Stapro, které v prvním kroku vytvoří úložiště a nakonfiguruje napojení. Další kroky popsané v tomto dokumentu již provádí sám zákazník.

## **Konfigurace uživatele**

Uživatelé, kteří jsou oprávněni k podpisu dokumentů, odesílají podepsané dokumenty do archivu. Každý uživatel obdrží své přihlašovací údaje do archivu. Takový uživatel musí mít správcem jeho společnosti zapnutý modul EZD.

Správce -> Správa organizace -> záložka Uživatelé, rozkliknout daného uživatele

![image-20250618-083140.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-083140.png>)
Pokud je na společnosti zapnuta úroveň EZD s archivem, zobrazí se aktivaci modulu EZD.

Zároveň uživatel zvolí způsob odeslání dokumentu do archivu:

- Ručně

Dokumenty jsou odeslány až poté, co uživatel označí dokumenty, které se mají do archivu odeslat. Uživatel dokumenty odesílá pomocí tlačítka Odeslat v modulu EZD. Výhodou této volby je to, že uživatel odesílá dokument až ve chvíli, kdy si je jist, že dokument již nebude upravovat.

- Automaticky

Dokument je ihned po podepsání uživatelem v aplikaci odeslán do archivu. Nevýhodou této volby je v možný nárůst počtu dokumentů v archivu v případě, kdy uživatel potřebuje již odeslaný dokument upravit, protože dokumenty v archivu se nestornují, v archivu zůstávají všechny do něj odeslané dokumenty.

Uživatel si taky volí možnost upozorňovat na nepodepsané dokumenty. Zvolený datum určuje, na jak staré nepodepsané dokumenty nás bude systém upozorňovat. Upozornění je ve formě vyskakovacího okna po zapnutí Galenu.

## **Konfigurace společnosti a pracoviště**

Na úrovni společnosti je možné definovat složku, do které se ukládají dokumenty v případě využití EZD bez archívu. V případě využití EZD s archívem, se dokumenty do této složky ukládají jenom dočasně, dokud nejsou odeslané do archivu.

Zároveň lze EZD aktivovat samostatně pro jednotlivá pracoviště. Tuto možnost je nutné před spuštěním funkcionality předem projednat se STAPRO.

![image-20250618-083227.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-083227.png>)

## **Vytvoření podepsaného pdf dokumentu**

Do el. archivu jsou odeslány podepsané pdf dokumenty. V rámci aplikace AIS Galen je potřeba vygenerovat toto pdf a podepsat jej.

**Dokumentace v rámci dekurzu**

1. Zdravotní dokumentace je v dekurzu rozdělená na dokumentaci Kurativa a dokumentaci PLS. V rámci dekurzu je možné vygenerovat, uzamknout a podepsat tyto části zdravotní dokumentace.

![image-20260216-115457.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20260216-115457.png>)
Pozn. pokud se uživateli toto konfigurační okno po stisku tlačítka nezobrazí, je možné tuto konfiguraci zobrazit po stisku tlačítka busty -> záložka Nastavení → tlačítko Konfigurace zamykání dekurzu.

![image-20250618-083431.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-083431.png>)
![image-20250618-083614.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-083614.png>)
V případě vytvoření více dekurzů v daný den (Kurativa, PLS) se podepisuje zdravotní dokumentace za každý typ dekurzu samostatně.

V případě potřeby je možné vyšetření a žádanky vygenerovat do oddělených dokumentů a ty podepsat. Ostatní položky je možné vygenerovat do pdf a podepsat pouze v rámci dekurzu. V případě zapnuté funkcionality auditní stopy se podepsání a stornování podepsaného dokumentu zobrazí v historii změn.

Tlačítko pro vygenerování pdf. (vpravo)

![1ba2ea0d-0d87-45b2-8b69-3d9d7a804d37.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/1ba2ea0d-0d87-45b2-8b69-3d9d7a804d37.png>)
![image-20250618-083638.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-083638.png>)
**A. Anamnéza**

Anamnézu je možné podepsat pouze v okně Anamnéza, ve kterém se anamnéza vytváří. Pomocí tlačítka pečetě nebo EZD  je možné zprávu podepsat.

![image-20260216-115002.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20260216-115002.png>)
**B. Lékařská zpráva**

Lékařskou zprávu je možné podepsat pouze v okně Lékařské zpráva, ve kterém se zprávy vytváří. Pomocí tlačítka EZD  je možné zprávu podepsat.

**C. Přílohy**

Všechny přílohy (ve formátu .docx, .xlsx, .rtf, .txt, .mp3, .mp4) lze odeslat do EZD pouze společně s dekurzem. V dekurzu se po kliknutí na tlačítko pečetě zobrazí okno ”Konfigurace obsahu EZD”, kde uživatel zvolí, které přílohy chce odeslat do EZD (viz obrázek níže).

![image-20250618-084330.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-084330.png>)
Samotné přílohy se nepodepisují, s výjimkou dokumentace převáděné z listinné do elektronické podoby. K tomuto účelu slouží tlačítko Převod listinné ZD. V tomto případě je k nahrávané či skenované příloze automaticky přidána další strana s tzv. doložkou, která obsahuje informace, kdo a kdy daný dokument naskenoval, rozsah dokumentu a další náležitosti. Tento dokument uživatel podepíše kliknutím na tlačítko ”Opatřit podpisem” v okně ”Náhled dokumentu k opatření podpisem“. Dokumentaci převáděnou z listinné podoby není možné z okna konfigurace obsahu EZD odebrat, aby mohl být proces převodu řádně dokončen. O tomto faktu je uživatel informován po najetí myši na ikonu “i” (info).

![image-20250618-084437.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-084437.png>)
**D. RDG žádanky**

RDG žádanky je možné podepsat v okně RDG žádanky na pracovišti žádajícím i provádějícím radiodiagnostiku, ve kterém se žádanky vytváří. Pomocí tlačítka EZD je možné žádanku podepsat.

**E. FT poukazy**

FT poukazy je možné podepsat v okně FT poukazy na pracovišti žádajícím i na pracovišti, které využívá aparát umožňující práci s přijatými poukazy FT. Pomocí tlačítka pečetě EZD je možné poukaz podepsat.

**F. Lékové žádanky**

Informace o vytvoření nové lékové žádanky se automaticky propíše do dekurzu.

![image-20250618-090752.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-090752.png>)
Při vytvoření nové lékové žádanky po kliknutí na tlačítko "Odeslat" nebo "Odeslat a vytisknout" se propíše informace do dekurzu v následujícím formátu: **Odeslána nová léková žádanka č. {číslo_lékové_žádanky}** lék: {lék}, datum indikace: {datum_indikace}, pracoviště: {pracoviště}, pracovník: {pracovník}

**G. Zaměstnání**

Při ukončení zaměstnání dochází po zadání datumu "Do" u pacienta k přepočítání skartačních lhůt veškeré dokumentace:

1. Vybereme požadované zaměstnání + potvrdíme tlačítkem "Ok":

![image-20250618-090923.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-090923.png>)
2. Zobrazí se informace, zda si přejeme informaci o ukončení zaměstnání přenést do dekurzu. Pro provedení zvolíme v dialogovém okně volbu "Ano":

![image-20250618-090947.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-090947.png>)
3. Následně dochází k náhledu dokumentu k podepsání. K podpisu dokumentu a k přenesení informace dochází kliknutím na tlačítko "Podepsat":

![image-20250618-091013.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-091013.png>)
4. V dekurzu následně dochází k zápisu informace o ukončení zaměstnání. Zde je možné také dokument později zobrazit.

![image-20250618-091033.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-091033.png>)

## **Převod podepsaného dokumentu na papírovou autorizovanou konverzi**

Každý dokument, který byl podepsaný a uložený do archivu EZD, lze převést na papírovou autorizovanou konverzi dat. Možnost uložit podepsaný dokument je dostupná na všech místech, kde je možné dokument zobrazit, např. v přílohách vybraného pacienta, v modulu EZD, u lékařských zpráv, dekurzů a dalších dokumentů odeslaných do archivu EZD.

![image-20250618-092909.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-092909.png>)
Po kliknutí na Zobrazit se otevře náhled podepsaného dokumentu s tlačítkem uložit.

![image-20250618-092937.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-092937.png>)
Po kliknutí na Uložit si uživatel může zvolit, kam daný soubor z archivu uloží ve svém počítači, případně na flash disk apod. Po kliknutí jen na Odejít se dokument neuloží.

## **Stornování podepsaného dokumentu**

V případě, že je potřebné dokumentaci po podepsání ještě upravit, musí se záznam znovu otevřít a podepsaný dokument stornovat. Po úpravě je možné znovu dokument podepsat. Stornovat podepsaný dekurz lze dvěma způsoby:

1. Přes pravé tlačítko myši nad lištou se stavem vygenerovaného dokumentu EZD
2. Kliknutím levým tlačítkem myši na modrou ikonu otevřeného zámečku příslušné návštěvy

![image-20250618-093023.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-093023.png>)
Pozn.: Stornovat dokument může pouze uživatel, který daný záznam podepsal (uzamknul). V případě, že bylo společně uzamknuto více návštěv dohromady v daný den, dojde při stornování k odemčení všech těchto spolu uzamknutých návštěv.

## **Nepodepsané dokumenty v Dashboardu**

Přehled nepodepsaných dokumentů je možné vyhledat i v okně Dashboard. Dokumenty jsou zde zobrazeny od data uloženého na konfiguraci uživatele. Z jednotlivých záznamů je možné se prokliknou přímo do dokumentů a následně je podepsat.

![image-20250618-093108.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-093108.png>)

## **Odeslání podepsaného dokumentu do archivu**

V závislosti na konfiguraci uživatele jsou dokumenty odeslány do archivu okamžitě po podepsání nebo až po ručním odeslání uživatelem pomocí tlačítka Odeslat.

Ruční odeslání dokumentu probíhá v modulu EZD – záložka *Dokumenty k odeslání* nebo záložka *Správa dokumentů EZD* – dokumenty ve stavu *Čeká na schválení odeslání do archivu*.

![image-20250618-093143.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-093143.png>)
Dokumenty, které je potřeba odeslat do archivu, je potřeba označit (je možný i multiselect) a stisknout tlačítko Odeslat.

**Po odeslání dokumentů do archivu dokument nabývá těchto stavů**:

- Odesílání do archivu - dokument je odesílán od archivu.
- Odeslán do archivu  - dokument bylo doručen do archivu a čeká, až bude archivem přijat.
- Archivovaný - dokument byl přijat archivem.
- Chyba při odesílání do archivu - podrobnosti k chybě jsou zobrazeny ve sloupci *Chyba.*

## **Popis modulu EZD**

V modulu EZD může uživatel dokument podepsat a odeslat jej do archivu. Následující podkapitoly popisují jednotlivé záložky modulu.

### **Správa dokumentů EZD**

Záložka zobrazuje dokumenty ve všech stavech, kterých může dokument EZD nabýt. Záložka pracuje pouze nad dokumenty v rámci EZD, tzn. podepsanými pdf dokumenty. Dokumenty, které ještě nebyly podepsány, nezobrazuje.

![image-20260216-121702.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20260216-121702.png>)

#### **Filtrace**

- Pracoviště – pokud uživatel přistupuje jako Správce, vidí navíc filtraci podle pracoviště, na kterém dokument vznikl.
- Typ dokumentu – určuje, v rámci kterého modulu byl dokument vygenerován. Pokud bylo vyšetření uzamčeno a vygenerováno do pdf v rámci dekurzu, zobrazí se pdf dokument pouze pod typem dokumentu „dekurz“.
- Pacient – určuje dokumenty EZD pro konkrétního pacienta.
- Datum od, Datum do – filtruje podle data podpisu pdf dokumentu.
- Typ dokumentace – filtruje dokumentaci typu Kurativa či PLS. Nevyplněný parametr zobrazí všechny dokumenty.
- Stav
- Checkbox „Chybový stav“ – zaškrtnutí zobrazí všechny dokumenty, které jsou v jakémkoli chybovém stavu.
- Checkbox „Vč. dokumentů vzniklých před napojením archivu“ – zobrazení defaultně pracuje pouze s dokumenty, které vznikly po napojení společnosti na el. archiv. Po zaškrtnutí checkboxu se zobrazí i dokumenty vzniklé před napojením. Tyto dokumenty však nelze z důvodu chybějících metadat do archivu odeslat.

#### **Filtrování stavů**

1. **Podepsaný** = v aplikaci byl vygenerován pdf dokument, který byl podepsaný. Dokument tento stav nabývá pouze v případě, že společnost v aplikaci nemá aktivován stav EZD s archivem. V tomto stavu jsou tedy všechny dokumenty, které uživatelé vygenerovali a podepsali před napojením společnosti na archiv EZD. Dokumenty vzniklé před napojením společnosti na archiv již není možné do archivu odeslat z důvodu chybějících metadat.
2. **Stornovaný** = jedná se o podepsaný dokument, který byl uživatelem stornován. Uživatel obvykle dokument stornuje ve chvíli, kdy potřebuje upravit záznam, který již byl vygenerován od podepsaného pdf. Stornovat lze pouze podepsaný dokument i dokument, který již byl odeslán do archivu. V archivu dokument stornován není, zůstává tam i nadále, ale v rámci aplikace již dále není stav stornovaného dokumentu vůči archivu ověřován.
3. **Čeká na schválení odeslání do archivu** =  tohoto stavu může nabýt pouze dokument, který vznikl na společnosti po napojení na archiv. Dokument v tomto stavu čeká, až jej uživatel odešle z aplikace do archivu. To znamená, že tohoto stavu nemůže nebýt dokument, který podepsal uživatel, který má nastaveno automatické odesílání do archivu.
4. **Odesílání do archivu**= dokument je odesílán do archivu
5. **Chyba při odeslání do archivu** = dokument se nepodařilo do archivu odeslat
6. **Odeslán do archivu**= dokument byl odeslán do archivu, kde ale čeká na další ověření ze strany archivu. To znamená, že ač byl dokument do archivu doručen, ještě nemusí být archivem přijat.
7. **Zpracováván, čeká v archivu**= dokument je ověřován archivem.
8. **Archivovaný** = dokument byl přijat archivem a je v pořádku archivován.
9. **Určen k trvalé archivaci**= tohoto stavu nabývají pouze dokumenty se skartačním typem V. Po uplynutí doby určené vyhláškou se uživatel rozhoduje, zda je již možné je skartovat, nebo zda ještě musí být v archivu uložené.

   1. Poznámka: V rámci novelizací byl skartační znak zrušen. Jedná se tedy již o historickou záležitost, protože současná legislativa jej nevyžaduje.
10. **V procesu skartačního řízení** = dokument byl archivem navržen ke skartaci.  Uživatel se v tuto chvíli přihlásí do webového rozhraní archivu, kde rozhodne o tom, zda se má dokument skartovat. Pokud ano, je možné jej v archivu skartovat. Pozor! Nikdy se neskartují jednotlivé dokumenty pacienta, ale vždy jeho celá dokumentace. Při skartaci v archivu je vhodné nechat si vygenerovat seznam skartovaných pacientů – pro následnou skartaci dokumentaci v rámci aplikace.
11. **Skartován** = dokument by v archivu uživatelem skartován. V tuto chvíli má uživatel seznam pacientů, jejichž dokumentaci v archivu skartoval. Následně je potřeba skartovat dokumentaci pacientů v rámci aplikace.
12. **Neznámý stav** = nepodařilo se od archivu získat stav dokumentu.
13. **Chyba v archivu** = dokument v archivu nabyl chybového stavu.

### **Dokumenty k odeslání**

![image-20260216-123406.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20260216-123406.png>)
Tato záložka zobrazuje pouze dokumenty, které

- čekají na ruční odeslání uživatelem do archivu (stav Čeká na schválení odeslání do archivu)
- jsou do archivu právě odeslány, ale archiv je zatím nepřijal (stav Odesílání do archivu)
- do archivu nebyly doručeny, např. z důvodu nedostatečného oprávnění uživatele v archivu (stav Chyba při odesílání do archivu).

### **Odeslané dokumenty**

![image-20260216-123441.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20260216-123441.png>)
Zobrazuje pouze dokumenty, které byly do archivu odeslány. Pokud byl dokument do archivu odeslán a následně v aplikaci stornován, v této záložce se již neobjeví.

### **Nepodepsané dokumenty**

![image-20260216-123521.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20260216-123521.png>)
Přehled zobrazuje zdravotnickou dokumentaci vytvořenou v rámci aplikace, která dosud nebyla vygenerovaná do podepsaného pdf dokumentu.

V modulu EZD lze dokument po výběru pracoviště zobrazit a podepsat dvojklikem nebo pomocí tlačítka **Podepsat**. Hromadné podepisování dokumentů není z legislativních důvodů povoleno, je však možné označit více dokumentů najednou a tím postupně spustit proces jejich zobrazení a podepisování.

## **Proces skartace**

Kapitola popisuje proces skartace, kdy je dokument navržen elektronickým archivem ke skartaci, uživatel jej v prostředí webového archivu posoudí a rozhodne, zda se má dokument skartovat. Po posouzení uživatelem uživatel dokument v archivu skartuje. Uživatel následně skartuje záznamy v AIS Galen.

**Důležitá poznámka** - archiv navrhuje ke skartaci jednotlivé dokumenty, kdežto aplikace skartuje pouze pacienty. Aplikace tedy neskartuje jednotlivé záznamy pacienta, ale pouze všechny záznamy daného pacienta.

1. **Možnost exportu seznamů**

Všechny přehledy, resp. seznamy dokumentů archivu je možné exportovat pomocí tlačítka, viz. níže.

![abff32ae-c791-4828-9c0c-527873eb0b39.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/abff32ae-c791-4828-9c0c-527873eb0b39.png>)
Exportovat tedy lze např. seznam dokumentů navržených ke skartaci, ale i seznam skartovaných dokumentů. Vždy se však jedná pouze o popis dokumentů, není přiložen přehled jejich popisných dat (např. jméno pacienta, číslo pojištěnce, atd.)

2. **Skartační třída**

Každý dokument z aplikace AIS Galen (dále jen „aplikace“) zaslán do prostředí elektronického archivu (dále jen „archiv“) zaslán s již zadanou skartační třídou, která je nastavena na základě vyhlášky o zdravotnické dokumentaci.

Každá skartační třída se skládá z číslic vyjadřující dobu v letech a dříve i z písmena S nebo V.

S = označuje zdravotnickou dokumentaci, která se po uplynutí doby uchování navrhne ke zničení.

V = označuje zdravotnickou dokumentaci, jejíž hodnotu nelze v okamžiku vzniku určit.

Jakmile uplyne lhůta definovaná skartační lhůtou, je dokument k 1. 1. následujícímu roku archivem navržen ke skartaci.

Poznámka: V rámci novelizací byl skartační znak (písmeno) zrušen. Jedná se tedy již o historickou záležitost, protože současná legislativa jej nevyžaduje.

3. **Dokumenty ke skartaci**

Archiv automaticky kontroluje dobu skartace každého dokumentu. Jakmile uplyne doba, po kterou musí být dokument uchován, je zařazen archivem do dokumentů ke skartaci. *Záložka Dokumenty  - Dokumenty ke skartaci.*Zde jsou zobrazeny všechny dokumenty, které byly archivem automaticky vyhodnoceny jako vhodné ke skartaci.

![image-20250618-093738.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-093738.png>)
Uživatel každý dokument posoudí (kliknutím na ikonu nastavení může zobrazit popisná data každého dokumentu) a rozhodne, zda jej zařadí do skartačního návrhu. Dokument může zařadit do stávajícího skartačního návrhu, nebo vytvořit nový skartační návrh.

4. **Návrh skartačního řízení**

Následně uživatel zobrazí jednotlivé návrhy skartačního řízení (může existovat jedno, nebo více návrhů skartačního řízení).

*Záložka Dokumenty – Návrhy skartačního řízení*

Zde jsou v jednotlivých návrzích zařazené dokumenty navržené ke skartaci. Pokud má dokument nastaven skartační znak S, je možné jej ihned skartovat. Pokud má dokument skartační znak V, je nutné posoudit, zda se má skartovat. Pokud tomu tak skutečně je, je potřeba změnit jeho skartační znak na S. Pro změnu skartačního znaku z V na S je nutné dokument označit zaškrtnutím checkboxu a v možnostech vybrat *Změnit skartační znak V na S*.

![image-20250618-093826.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/EZD – elektronická zdravotní dokumentace/assets/image-20250618-093826.png>)
Pokud dokument bez ohledu na jeho skartační typ ještě nemá být skartován, je možné jej ve stejném okně za odebrat ze skartačního návrhu. Tím se dokument dostane zpět do Dokumentů ke skartaci.

5. **Skartační řízení**

Po skartaci je dokument z archivu smazán, zůstává pouze záznam o dokumentu
