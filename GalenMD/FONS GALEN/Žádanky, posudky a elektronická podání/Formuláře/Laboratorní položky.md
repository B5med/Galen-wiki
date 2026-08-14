---
title: "Laboratorní položky"
version: 2
updated_at: 2026-08-13
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/105086977
---

# Laboratorní položky

Pro vytvoření formuláře typu eŽádanka, tj. laboratorní žádanka, která je elektronicky lab. klientem odeslána do laboratoře, je nutné vytvořit soubor laboratorních metod, které bude žádanka obsahovat.

## Dostupnost souborů lab. položky

Soubory pro jednotlivé žádanky jsou vytvořeny ze strany Stapro, jedná se o tzv. neuživatelské soubory. Uživatel je v přehledu vytvořených souborů vidí, ale nemůže editovat.

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-071646.png>)
Pomocí tlačítka Zakázat pro uživatele je může zakázat pro uživatele své společnosti (funkcionalita je stejná jako v ostatních entitách: formuláře atd.)

Uživatel může editovat pouze ty soubory lab. položek, které vytvořil sám, tj. jsou uživatelské.

## Import souboru laboratorních položek

Soubor lab. metod, konkrétně názvů položek a jejich NČLP kódů dodá laboratoř. Tento soubor se nahrává v modulu Design -> Lab. položky pomocí tlačítka **Import**, které podporuje jak soubory .csv, tak soubory Excel (.xls, .xlsx, .xlsm).

### Mezikrok importu – definice listů a sloupců

Po výběru souboru se zobrazí mezikrok, ve kterém uživatel určí:

- Který list obsahuje **laboratorní metody** – tento výběr je povinný, bez něj nelze import dokončit.
- Který list obsahuje **parametry** – volitelné. Pokud list není určen, u laboratorních metod pak nelze žádné parametry nastavit ani zobrazit.
- Který list obsahuje **odběrový materiál** – volitelné, analogicky jako u parametrů.
- Přiřazení **názvu žádanky** k jednotlivým listům s metodami – jeden soubor tak může obsahovat metody pro víc žádanek najednou (např. list Biochemie a list Mikrobiologie ve stejném souboru).

U listu s laboratorními metodami uživatel dále namapuje jednotlivé sloupce na: název skupiny, název metody, NČLP kód, kód(y) parametrů, kód(y) odběrového materiálu a volitelně kód položky (property name). U listu s parametry se mapuje NČLP kód, název parametru a jednotka, u listu s materiálem kód, název a barva.

Pokud import obsahuje chyby na více listech současně (např. neplatný NČLP kód na jednom listu a neplatný kód položky na jiném), zobrazí se chybové hlášení seskupené podle jednotlivých listů.

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-071800.png>)

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-071748.png>)

Struktura listu s laboratorními metodami (příklad se 6 sloupci):

| #Skupina | KOD | NCLP | LCLP | Parametr | Nazevpolozky |
| --- | --- | --- | --- | --- | --- |
| #LESO | LESO |  |  |  | Ledvinový soubor |
| LESO | UREA | 03086 |  |  | Urea |
| LESO | KREA | 01512 |  |  | Kreatinin |
| LESO | KMOC | 03078 |  |  | Kys. močová |
| LESO | CYSC | 12137 |  |  | Cystatin C |
| LESO | MDRD | 17341 |  |  | MDRD |
| #MOC | MOC |  |  |  | Screening drog |
| MOC | MEFE | 11577 |  |  | Metamfetamin |
| MOC | AMFE | 11450 |  |  | Amfetamin |
| MOC | KOK | 11541 |  |  | Kokain |
| MOC | MOHE | 11583 |  |  | Morfin/Heroin |
| MOC | MARI | 11535 |  |  | Marihuana |
| MOC | META | 11579 |  |  | Metadon |
| MOC | BEDI | 11526 |  |  | Benzodiazepiny |
| MOC | P_CAS | 02994 | 2004 | P_CAS | Doba sběru |
| MOC | P_OBJEM | 03142 | 2003 | P_OBJEM | Objem/ml |
| MOC | P_VAHA | 12429 | 2002 | P_VAHA | Hmotnost/kg |
| MOC | P_VYSKA | 12422 | 2001 | P_VYSKA | Výka/cmva |

### Sloupec Skupina

Vytváří vazby mezi názvem skupiny a jednotlivými položkami/metodami.

Může obsahovat pouze písmena a číslice, nesmí začínat číslicí.

Pokud řádek označuje název skupiny metod, obsah sloupce Skupina začíná znakem #.

Pokud řádek označuje název skupiny metod, nesmí obsahovat NČLP, LCLP kód nebo parametr.

Každá metoda musí být zařazena do právě jedné skupiny.

### Sloupec Kód

Může obsahovat pouze písmena, číslice a znak „_“, nesmí začínat číslicí.

Musí být v rámci jedné žádanky unikátní.

Každá metoda má právě jeden kód.

Pokud začíná P_, pak indikuje to, že se bude jednat o textovou položku, která se v rámci žádanky přenáší jiným elementem (lip), než položky typu checkbox (lop).

Pokud je potřeba, aby se obsah textové položky přesto přenášel v elementu lop, pak kód položky (i když je textová) nesmí začínač P_.

#### Import kódu položky vs. automatické vygenerování

Pokud je v souboru sloupec s kódem položky vyplněný a v mezikroku namapovaný, položky po importu převezmou kódy přímo ze souboru.

Pokud tento sloupec vyplněný/namapovaný není, Galen kód vygeneruje automaticky (10 znaků, první znak písmeno, zbývající znaky písmena nebo číslice).

### Sloupec NČLP

Musí obsahovat právě 5 číslic.

Řádek označující skupinu nesmí NČLP kód obsahovat.

V rámci jedné žádanky musí být NČLP kód unikátní.

### Sloupec LCLP

Aktuálně se nevyužívá.

### Sloupec Parametr

Jeho vyplnění indikuje, že se jedná v rámci žádanky o textovou položku. Musí začínat znaky P_.

### Sloupec Název položky

Obsahuje textový název položky.

Muže obsahovat max. 256 znaků.

## Vytvoření nového souboru lab. položek

Po importu dokumentu se vytvoří nový soubor lab. metod

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072218.png>)
1. Uživatel doplní název souboru. Protože každý soubor odpovídá jedné žádance jedná laboratoře, doporučujeme použít jmennou konvenci *NÁZEV LABORATOŘE Název žádanky*, např. SYNLAB Mikrobiologie. S ohledem na množství metod v jedné žádance, kde každá laboratoř může pro „stejnou“ metodu použít jiný NČLP kód, nedoporučujeme pro různé žádanky používat stejné soubory lab. metod, i když je to samozřejmě možné.
2. Uživatel upraví dostupnost. Nastaví, na kterých společnostech má být daný soubor dostupný.
3. Typ položky se načetl na základě struktury importovaného souboru. Uživatel zkontroluje, zda typ položky odpovídá dané metodě.
4. Skupiny se načetly na základě struktury importovaného souboru. Uživatel zkontroluje, zda odpovídají požadovanému a zároveň, zda se metody načetly do správné skupiny.

## Další možnosti souboru lab. položek

Parametry a odběrový materiál je možné namapovat přímo při importu (viz mezikrok importu výše). Pokud nebyly importem nastaveny, je možné je v souboru lab. položek doplnit i ručně.

### Parametry

První sloupec *Parametr* indikuje, že se v rámci žádanky jedná o textovou položku. Druhý sloupec *Parametry* (1.) označuje povinné vyplněný polí v případě požadovaní konkrétní metody.

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072336.png>)
Pokud lékař požaduje lab. metodu *Kreatinin,*musí v žádance vyplnit pole Výška a Hmotnost (bez jejich vyplnění nebude možné žádanku odeslat). Výška a Hmotnost jsou tedy parametry položky Kreatinin. Výška a hmotnost jsou v uvedeny v žádance jako metody, ale uživatel je také uvede do části Parametry (2.). Kód položky a kód parametru (3.) se musí shodovat.

Následně uživatel přiřadí zadané parametry do řádku konkrétní metody, jak je znázorněno v řádku Kreatinin.

### Odběrový materiál

U každé metody je možné zadat, v jakém typu odběrového materiálu bude vzorek do laboratoře zaslán.

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072405.png>)
Uživatel zadá odběrový materiál (1.), kde

- Kód je unikátní značení daného materiálu, může obsahovat číslice
- Název odpovídá názvu, který se bude následně tisknout na průvodce
- Barva v tuto chvíli není dále zpracovávána, pole je připraveno pro případné další využití. Zadává se kódem typu hexa bez znaku #, např. EEAA33.

Vytvořený odběrový materiál uživatel přiřadí k jednotlivým metodám (2.). Jedna metoda může 0 – n odběrových materiálů.

## Poznámka k polím Skupina, Parametry a Odběrový materiál

Pokud uživatel zadá nový řádek do částí Skupina, Parametry nebo Odběrový materiál, není už možné tento řádek odstranit. Uživatel je však k metodám nemusí přiřadit.

Skupina, parametry ani odběrový materiál se nepřenáší do laboratoře v rámci xml.

Skupiny slouží ke grafickému rozřazení metod v rámci žádanky a dále k tisku průvodky, kde se metody seskupují do konkrétních skupin.

Parametry slouží k vynucení správného vyplnění žádanky ze strany uživatele před jejím odesláním.

Odběrový materiál slouží k přehledu zaslaného materiálu do laboratoře na průvodce žádanky, kde každý typ použitého odběrového materiálu se uvádí právě jednou.

### Přenášet do textu žádosti

Funguje pouze u formátu dat DASTA4. Je možné zaškrtnout pouze u metody typu text. Pokud je checkbox zaškrtnutý, přenáší se uživatelem vyplnění text nikoli jako metoda v elementu „lop“, ale jako text žádosti (váže se k celé žádance) v elementu „text_zadosti“.

## Aktualizace souboru importem (nová verze)

Existující soubor lab. položek je možné aktualizovat opětovným importem – tlačítkem **Aktualizovat importem** u vybrané položky. Postup mezikroku (výběr listů, mapování sloupců) je stejný jako u prvního importu.

- Aktualizovat importem lze najednou pouze jednu vybranou položku.
- Pokud má metoda ve zdrojovém souboru stejný NČLP kód jako v předchozí verzi, zachová se stejný kód položky (property name) – šablony v žádankách, které na položku odkazují, tak zůstanou funkční. Pokud je NČLP kód nový, vytvoří/přiřadí se nový kód položky.
- Datum platnosti nové verze odpovídá datu, kdy byla aktualizace importem provedena.
- Pokud uživatel při aktualizaci importem znovu nenastaví listy s parametry nebo odběrovým materiálem, hodnoty z předchozí verze se automaticky nepřenesou – je potřeba je nastavit znovu.

## Vyhledávání v přehledu laboratorních položek

V přehledu souborů/položek je možné vyhledávat:

- Podle NČLP kódu.
- Podle názvu, včetně použití znaku % jako zástupného znaku (např. „%glukóza%“).

V detailu konkrétní laboratorní položky je navíc k dispozici filtr pro vyhledávání souvisejících metod podle NČLP kódu i podle názvu metody.

## Ruční vytvoření souboru lab. metod/editace

Soubor lab. metod je samozřejmě možné vytvořit také ručně, bez importu souboru.

Nový soubor je možné vytvořit pomocí zeleného tlačítka plus . V tom případě uživatel neimportuje soubor, ale ručně vyplňuje skupiny a jednotlivé metody. Import je možný pouze pomocí stejnojmenného tlačítka.

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072521.png>)

Editace stávajícího souboru lab. metod je možná po otevření detailu konkrétního souboru. V případě editace je nutné mít na paměti, že všechny změny provedené v souboru lab. metod je následně nutné ze strany uživatele provést také v lab. žádance (formuláři), na kterou je daný soubor lab. metod navázán. Např.

- Pokud uživatel změní název skupiny nebo název metody, je následně nutné název skupiny nebo metody také změnit v konkrétní žádance (formuláři).
- Pokud uživatel změní hodnotu v poli kód lab. metody nebo parametru, je nutné tento kód změnit také v property name checkboxu nebo textového pole žádanky, na kterou je soubor lab. metod navázán.

## Použití souboru lab. metod v konkrétní žádance

Žádanku, kterou uživatelé budou vyplňovat v rámci FONS Galen, uživatel vytvoří jako formulář v části *Předlohy tisku*. Může vytvořit novu předlohu, nebo pouze novou variantu formuláře.

V detailu prázdné varianty formuláře zvolí možnost Lab. položky a vybere soubor, který chce do formuláře nahrát. Pokud má soubor lab. položek víc verzí, uživatel zvolí konkrétní verzi, kterou chce do formuláře nahrát – nemusí jít vždy o poslední verzi.

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072608.png>)
Po výběru konkrétního souboru lab. položek se zobrazí okno pro možnou specifikaci konkrétních polí, které se do formuláře nahrají.

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072624.png>)
Po stisku tl. OK se hlavička a metody přenesou do formuláře

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072653.png>)

### Hlavička

Položky v hlavičce žádanky není možné přidávat, resp. nepřenesly by se do xml odeslané do laboratoře.

Do xml se v rámci žádanky přenáší

#### *Žádající lékař a pracoviště*

Přenáší se údaje o pracovišti a odpovědném lékaři, který žádanku vystavuje. Tyto údaje se přenáší na pozadí, tzn. bez ohledu na tom co je vyplněno ve formuláři.

#### *Pacient*

Údaje o pacientovi (jméno, příjmení, číslo pojištěnce, pojišťovna) se přenáší také na pozadí z karty pacienta, tzn. bez ohledu na to, co je vyplněno v žádance.

#### *Diagnóza*

Kolonka pro vyplnění první diagnózy musí mít propertyname „Diagnoza“. Druhá diagnóza musí mít propertyname „DalsiDiagnoza“. Je možné přidat třetí diagnózu s propertyname „DalsiDiagnoza2“.

### Seznam metod

Metody na nahrály z připraveného souboru lab. metod. V případě editace je nutné

- Neměnit polohu názvu metody a checkboxu/textového pole. Název metody (položka typu MLabel) a checkbox nebo textové pole pro vyplnění hodnoty metody (MData) spolu nejsou nijak svázané. Jejich vazbu tvoří pouze to, že jsou zobrazeny vedle sebe. Pokud by uživatel polohu těchto dvou checkboxů  změnil bez toho, aby také změnit polohu položek s názvem (Urea, Kreatinin), lékař by při zaškrtnutí checkboxu vedle pole Urea do laboratoře odesílal požadavek na metodu Kreatinin.

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-073010.png>)

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-073019.png>)

- V případě změny propertyname checkboxu nebo textového pole pro vyplnění metody musí tuto změnu také promítnout do pole Kód u dané metody v souboru lab. položek.

- V případě změny názvu metody nebo skupiny musí tuto změnu promítnout do názvu metody nebo skupiny metod v souboru lab. položek.

### Parametry a odběrový materiál ve formuláři

Pokud má načtená laboratorní položka přiřazené parametry, zobrazí se na konci žádanky jako název (včetně jednotky v závorce) a textové pole pro vyplnění.

Odběrový materiál se na konci žádanky zobrazí souhrnně jako přehled (název + barevný panýlek) a zároveň u jednotlivé metody jako barevný panýlek. Pokud má metoda přiřazeno více druhů odběrového materiálu, barvy jednotlivých materiálů se u metody skládají nad sebou.

### Import z jednoho souboru s více žádankami

Pokud zdrojový soubor obsahoval více listů s přiřazenými různými názvy žádanek (viz mezikrok importu), metody se po nahrání do formuláře zařadí pod odpovídající žádanku – pro každý název žádanky vznikne samostatná položka a pod ní příslušné metody.

### eKomunikace

Pro vytvoření eŽádanky, tj. zobrazení tlačítka Odeslat v žádance, je nutné nastavit eKomunikaci ve stejnojmenné záložce.

![](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-073137.png>)
Typ přenášených dat = laboratorní žádanka, jiná možnost není dostupná

Adresace = Pevná volba, jiná možnost není dostupná

Název laboratoře = textový název, např. Synlab nebo Unilabs

Cesta nebo složka = tvoří prvních pět písmen z názvu laboratoře bez diakritiky \Zadanky. Např. SYNLA\Zadanky nebo AESKU\Zadanky.

Formát dat = DASTA3 nebo DASTA4.

Mapovací soubor = nevyplňuje se

Laboratorní položky = název souboru lab. metod

Kódování = volba dle domluvy s laboratoří
