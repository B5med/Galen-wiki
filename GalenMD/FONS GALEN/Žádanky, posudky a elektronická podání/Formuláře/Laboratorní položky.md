---
title: "Laboratorní položky"
version: 1
updated_at: 2025-08-26
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/105086977
---

# Laboratorní položky

Pro vytvoření formuláře typu eŽádanka, tj. laboratorní žádanka, která je elektronicky lab. klientem odeslána do laboratoře, je nutné vytvořit soubor laboratorních metod, které bude žádanka obsahovat.

## Dostupnost souborů lab. položky

Soubory pro jednotlivé žádanky jsou vytvořeny ze strany Stapro, jedná se o tzv. neuživatelské soubory. Uživatel je v přehledu vytvořených souborů vidí, ale nemůže editovat.

![image-20250826-071646.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-071646.png>)
Pomocí tlačítka Zakázat pro uživatele je může zakázat pro uživatele své společnosti (funkcionalita je stejná jako v ostatních entitách: formuláře atd.)

Uživatel může editovat pouze ty soubory lab. položek, které vytvořil sám, tj. jsou uživatelské.

## Import souboru laboratorních položek

Soubor lab. metod, konkrétně názvů položek a jejich NČLP kódů dodá laboratoř. Tento soubor je následně nahrán v modulu Design -> Lab. položky pomocí tlačítka Import z CSV

![image-20250826-071800.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-071800.png>)

![image-20250826-071748.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-071748.png>)

Soubor ve formátu .csv musí mít tuto strukturu, tj. 6 sloupců.

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

Musí být v rámci jedné žádanky unikátní.

Každá metoda má právě jeden kód.

Pokud začíná P_, pak indikuje to, že se bude jednat o textovou položku, která se v rámci žádanky přenáší jiným elementem (lip), než položky typu checkbox (lop).

Pokud je potřeba, aby se obsah textové položky přesto přenášel v elementu lop, pak kód položky (i když je textová) nesmí začínač P_.

### Sloupec NČLP

Musí obsahovat právě 5 číslic.

Řádek označující skupinu nesmí NČLP kód obsahovat.

### Sloupec LCLP

Aktuálně se nevyužívá.

### Sloupec Parametr

Jeho vyplnění indikuje, že se jedná v rámci žádanky o textovou položku. Musí začínat znaky P_.

### Sloupec Název položky

Obsahuje textový název položky.

Muže obsahovat max. 256 znaků.

### Vytvoření nového souboru lab. položek

Po importu dokumentu ve formátu .csv se vytvoří nový soubor lab. metod

## Vytvoření nového souboru lab. položek

Po importu dokumentu ve formátu .csv se vytvoří nový soubor lab. metod

![image-20250826-072218.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072218.png>)
1. Uživatel doplní název souboru. Protože každý soubor odpovídá jedné žádance jedná laboratoře, doporučujeme použít jmennou konvenci *NÁZEV LABORATOŘE Název žádanky*, např. SYNLAB Mikrobiologie. S ohledem na množství metod v jedné žádance, kde každá laboratoř může pro „stejnou“ metodu použít jiný NČLP kód, nedoporučujeme pro různé žádanky používat stejné soubory lab. metod, i když je to samozřejmě možné.
2. Uživatel upraví dostupnost. Nastaví, na kterých společnostech má být daný soubor dostupný.
3. Typ položky se načetl na základě struktury souboru .csv. Uživatel zkontroluje, zda typ položky odpovídá dané metodě.
4. Skupiny se načetly na základě struktury souboru .csv. Uživatel zkontroluje, zda odpovídají požadovanému a zároveň, zda se metody načetly do správné skupiny.

## Další možnosti souboru lab. položek

Položky do souboru lab. položek se načetly na základě struktury souboru .csv, ale v souboru lab. položek je možné doplnit další vlastnosti tohoto souboru ručně.

### Parametry

První sloupec *Parametr* indikuje, že se v rámci žádanky jedná o textovou položku. Druhý sloupec *Parametry* (1.) označuje povinné vyplněný polí v případě požadovaní konkrétní metody.

![image-20250826-072336.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072336.png>)
Pokud lékař požaduje lab. metodu *Kreatinin,*musí v žádance vyplnit pole Výška a Hmotnost (bez jejich vyplnění nebude možné žádanku odeslat). Výška a Hmotnost jsou tedy parametry položky Kreatinin. Výška a hmotnost jsou v uvedeny v žádance jako metody, ale uživatel je také uvede do části Parametry (2.). Kód položky a kód parametru (3.) se musí shodovat.

Následně uživatel přiřadí zadané parametry do řádku konkrétní metody, jak je znázorněno v řádku Kreatinin.

### Odběrový materiál

U každé metody je možné zadat, v jakém typu odběrového materiálu bude vzorek do laboratoře zaslán.

![image-20250826-072405.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072405.png>)
Uživatel zadá odběrový materiál (1.), kde

- Kód je unikátní značení daného materiálu, může obsahovat číslice
- Název odpovídá názvu, který se bude následně tisknout na průvodce
- Barva v tuto chvíli není dále zpracovávána, pole je připraveno pro případné další využití. Zadává se kódem typu hexa bez znaku #, např. EEAA33.

Vytvořený odběrový materiál uživatel přiřadí k jednotlivým metodám (2.). Jedna metoda může 0 – n odběrových materiálů.

## Poznámka k polím Skupina, Parametry a Odběrový materiál

Pokud uživatel zadá nový řádek do částí Skupina, Parametry nebo Odběrový materiál, není už možné tento řádek odstranit. Uživatel je však k metodám nemusí přiřadit.

Skupina, parametry ani odběrový materiál se nepřenáší do laboratoře v rámci xml.

Skupiny slouží ke grafickému rozřazení metod v rámci žádanky a dále k tisku průvodky, kde se metody seskupují do konkrétních skupin.

Parametry slouží k vynucení správného vyplnění žádanky ze strany uživatele před jejím odesláním.

Odběrový materiál slouží k přehledu zaslaného materiálu do laboratoře na průvodce žádanky, kde každý typ použitého odběrového materiálu se uvádí právě jednou.

### Přenášet do textu žádosti

Funguje pouze u formátu dat DASTA4. Je možné zaškrtnout pouze u metody typu text. Pokud je checkbox zaškrtnutý, přenáší se uživatelem vyplnění text nikoli jako metoda v elementu „lop“, ale jako text žádosti (váže se k celé žádance) v elementu „text_zadosti“.

## Ruční vytvoření souboru lab. metod/editace

Soubor lab. metod je samozřejmě možné vytvořit také ručně, bez importu souboru ve formátu xml.

Nový soubor je možné vytvořit pomocí zeleného tlačítka plus . V tom případě uživatel neimportuje soubor .csv, ale ručně vyplňuje skupiny a jednotlivé metody. Import je možný pouze pomocí stejnojmenného tlačítka.

![image-20250826-072521.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072521.png>)

Editace stávajícího souboru lab. metod je možná po otevření detailu konkrétního souboru. V případě editace je nutné mít na paměti, že všechny změny provedené v souboru lab. metod je následně nutné ze strany uživatele provést také v lab. žádance (formuláři), na kterou je daný soubor lab. metod navázán. Např.

- Pokud uživatel změní název skupiny nebo název metody, je následně nutné název skupiny nebo metody také změnit v konkrétní žádance (formuláři).
- Pokud uživatel změní hodnotu v poli kód lab. metody nebo parametru, je nutné tento kód změnit také v property name checkboxu nebo textového pole žádanky, na kterou je soubor lab. metod navázán.

## Použití souboru lab. metod v konkrétní žádance

Žádanku, kterou uživatelé budou vyplňovat v rámci FONS Galen, uživatel vytvoří jako formulář v části *Předlohy tisku*. Může vytvořit novu předlohu, nebo pouze novou variantu formuláře.

V detailu prázdné varianty formuláře zvolí možnost Lab. položky a vybere soubor, který chce do formuláře nahrát.

![image-20250826-072608.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072608.png>)
Po výběru konkrétního souboru lab. položek se zobrazí okno pro možnou specifikaci konkrétních polí, které se do formuláře nahrají.

![image-20250826-072624.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072624.png>)
Po stisku tl. OK se hlavička a metody přenesou do formuláře

![image-20250826-072653.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-072653.png>)

### Hlavička

Položky v hlavičce žádanky není možné přidávat, resp. nepřenesly by se do xml odeslané do laboratoře.

Do xml se v rámci žádanky přenáší

#### *Žádající lékař a pracoviště*

Přenáší se údaje o pracovišti a odpovědném lékaři, který žádanku vystavuje. Tyto údaje se přenáší na pozadí, tzn. bez ohledu na tom co je vyplněno ve formuláři.

#### *Pacient*

Údaje o pacientovi (jméno, příjmení, číslo pojištěnce, pojišťovna) se přenáší také na pozadí z karty pacienta, tzn. bez ohledu na to, co je vyplněno v žádance.

#### *Diagnóza*

Kolonka pro vyplnění první diagnózy musí mít propertyname „Diagnoza“. Druhá diagnóza musí mít propertyname „DalsiDiagnoza“. Je možné přidat třetí diagnózu s propertyname „DalsiDiagnoza2“.

### Seznam metod

Metody na nahrály z připraveného souboru lab. metod. V případě editace je nutné

- Neměnit polohu názvu metody a checkboxu/textového pole. Název metody (položka typu MLabel) a checkbox nebo textové pole pro vyplnění hodnoty metody (MData) spolu nejsou nijak svázané. Jejich vazbu tvoří pouze to, že jsou zobrazeny vedle sebe. Pokud by uživatel polohu těchto dvou checkboxů  změnil bez toho, aby také změnit polohu položek s názvem (Urea, Kreatinin), lékař by při zaškrtnutí checkboxu vedle pole Urea do laboratoře odesílal požadavek na metodu Kreatinin.

![image-20250826-073010.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-073010.png>)

![image-20250826-073019.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-073019.png>)

- V případě změny propertyname checkboxu nebo textového pole pro vyplnění metody musí tuto změnu také promítnout do pole Kód u dané metody v souboru lab. položek.

- V případě změny názvu metody nebo skupiny musí tuto změnu promítnout do názvu metody nebo skupiny metod v souboru lab. položek.

### eKomunikace

Pro vytvoření eŽádanky, tj. zobrazení tlačítka Odeslat v žádance, je nutné nastavit eKomunikaci ve stejnojmenné záložce.

![image-20250826-073137.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/Formuláře/Laboratorní položky/assets/image-20250826-073137.png>)
Typ přenášených dat = laboratorní žádanka, jiná možnost není dostupná

Adresace = Pevná volba, jiná možnost není dostupná

Název laboratoře = textový název, např. Synlab nebo Unilabs

Cesta nebo složka = tvoří prvních pět písmen z názvu laboratoře bez diakritiky \Zadanky. Např. SYNLA\Zadanky nebo AESKU\Zadanky.

Formát dat = DASTA3 nebo DASTA4.

Mapovací soubor = nevyplňuje se

Laboratorní položky = název souboru lab. metod

Kódování = volba dle domluvy s laboratoří
