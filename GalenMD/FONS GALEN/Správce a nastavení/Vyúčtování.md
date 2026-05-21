---
title: "Vyúčtování"
version: 1
updated_at: 2025-07-21
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/75792385
---

Aby mohl uživatel IS Galen provádět pravidelné vyúčtování zdravotní péče a vzniklé dávky odeslat zdravotním pojišťovnám k proplacení, je nutné mít v tabulce v Uživateli (Správce -> Správa společnosti -> záložka Uživatelé -> rozkliknout dvojklikem příslušného uživatele) zaškrtnuté zpřístupnění modulu Vyúčtování. Takový uživatel za použití několika kliknutí velmi jednoduše vytvoří dávky, které je možno poté přímo z IS Galen odeslat zdravotním pojišťovnám. Pověřený uživatel provádí úkony vyúčtování v modulu Správce -> Vyúčtování

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-130607.png]]
Samotné vyúčtování začneme stiskem ikony **Vyúčtovat.**  Do vyúčtování se zahrnou všechny výkony zadané u pacientů za zvolený měsíc, které ještě nebyly vyúčtovány.

Správce -> Vyúčtování -> Vyúčtovat

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-130630.png]]
Otevře se tabulka, ze které vybereme účtované období (na příkladu červen 2022)

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-130646.png]]
Poté zvolíme za jaká IČZ chceme vyúčtovat (na příkladu za celou polikliniku, pokud mám pouze jednu ambulanci – uvidím pouze jednu ambulanci) a jednoduchým zakřížkováním si vyberu požadované a klikneme vpravo nahoře na ikonu **Kontrola**

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-130702.png]]
Zaškrtáme si vše, co chceme zahrnout do vyúčtování a klikneme na Vyúčtovat (pokud neúčtujeme dávky foniatrických pomůcek). Ve stejném okně se pro informaci zobrazují starší nevyúčtované výkony, tzn. Výkony za minulá období, které nejsou zahrnuty v žádném vyúčtování, a tudíž nebyly pojišťovnám odeslány a proplaceny. Jedná se pouze o informaci, proto záleží na uživateli, jestli bude starší nevyúčtované výkony dále zpracovávat nebo ne.

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-130730.png]]
Vytvoří se F-dávka i K-dávka, číslo faktury aj. (z Externích žádanek, u kterých zadáváme IČP žadatele (např. FT poukaz) se do K-Dávek ve vyúčtování načítají kromě hlavní diagnózy až 4 diagnózy vedlejší) Stačí pak kliknout na Uložit vše. Jakmile jsou soubory uloženy, aktivuje se tlačítko Odeslat podání.

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-130746.png]]

## **Odeslání vyúčtování do ZP**

Po volbě pole Odeslat podání a budeme vyzváni k výběru odeslat podání na Portál ZP. Odeslat na portál lze buď všechna nově vytvořená podání současně, k tomu slouží tlačítko Odeslat podání v pravé dolní části daného okna. Je také možné odeslat pouze některá podání, Která jednotlivě označíme v levé horní části obrazovky zaškrtnutím příslušných políček křížkem. Nad těmito označenými podáními poté najdeme tlačítko Odeslat vybraná podání. Pak budeme vyzváni programem k výběru a podpisu certifikátem (Galen si automaticky najde certifikáty nainstalované v počítači). Výsledek -> máme vyúčtováno.

**K odesílání** dávek do zdravotních pojišťoven jsou potřeba **2 certifikáty**. Jedná se o komerční (public) a kvalifikovaný certifikát vydávaný certifikační autoritou. Odesílání na portál VZP (111) zpravidla vyžaduje certifikát komerční. Ostatní pojišťovny vyžadují k odesílání vyúčtování certifikát kvalifikovaný. Zdravotní pojišťovna ZPMV (211) vyžaduje k odesílání vyúčtování autentizaci pomocí hesla.

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-130841.png]]

**Nastavení certifikátu**lze z pozice správce v modulu Správa organizace v záložce Uživatelé, kde je nutné vyhledat příslušného uživatele a otevřít jeho nastavení dvojklikem.

## **Výsledek vyúčtování**

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-130906.png]]
U praktických lékařů se typ dokladu váže na registraci pacienta, tj. pokud je výkon vykazován u registrovaného pacienta, výkon se při vyúčtování automaticky dosadí na ambulantní doklad, v případě neregistrovaného pacienta na doklad nepravidelné péče. Uživatel tedy nemusí volit typ dokladu, ten se zvolí automaticky.

#### **Zrušit vyúčtování**

Správce -> modul Vyúčtování -> v horní liště tlačítko Zrušit vyúčtování

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-130958.png]]
Tlačítko „Zrušit vyúčtování“ umožňuje správci společnosti s přístupem do modulu Vyúčtování hromadně zrušit vyúčtování za vybrané období a vybranou pojišťovnu.

Lze například smazat všechna vytvoření podání (pro všechna IČZ) za 12. měsíc roku 2024 (prosinec 2024) u pojišťovny 209.

Po stisku tlačítka Zrušit vyúčtování je nutné vybrat z nabídky požadované období a následně požadovanou pojišťovnu. Tlačítkem OK uživatel provede zrušení vyúčtování dle zvolených parametrů.

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-131036.png]]
![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-131045.png]]
Po zrušení vyúčtování **se nesmažou vykázané výkony** v ordinaci za dané období a pojišťovnu, ale zruší se vytvořené doklady, dávky (výkonové dávky, faktury, kapitační dávky, doklady cest, registrační dávky...), které se běžně odesílají do zdravotních pojišťoven.

Za dané období lze poté vyúčtovat znovu běžným způsobem.

## **Vyúčtování – opravy**

Opravy dokladů provádíme na základě zúčtovacích zpráv ze zdravotních pojišťoven, ve kterých najdeme konkrétní údaje o dokladech, které je nutné opravit.

V záložce doklady najdeme doklad (např. podle čísla dokladu; je možné využít filtry v levém postranním panelu), který chceme opravit, a kliknutím ho označíme („zmodrá“). Číslo dokladu musí být pro správné vyhledání zadané na všech sedm míst. Pokud je v zúčtovací zprávě uvedeno kratší číslo např. 356, je nutné jej doplnit zleva nulami na sedm míst, např. 0000356.

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-131119.png]]

## ***Funkce tlačítek:***

### **Změnit stav dokladu**

- označí doklad stavem CHYBNÝ nebo ODMÍTNUTÝ a vyřadí ho z dalšího účtování. Nadále zůstává doklad v evidenci, ale není s ním dále pracováno např. při kontrolách frekvenčních omezení apod.

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-131142.png]]

### **Opravit doklad**

– tlačítkem opravit doklad zajistíme odeslání dokladů pojišťovnám ve stejném stavu bez provedených změn. Doklady se odesílají se stejným číslem dokladů. Tento postup doporučujeme pouze po výslovné domluvě s danou pojišťovnou, aby nedocházelo k duplicitám čísel dokladů a opětovnému nepřijetí vyúčtování. Běžné opravy výkonů a jejich položek v dokladech se provádí tlačítkem Nově vyúčtovat.

### **Nově vyúčtovat**

– lze změnit různé údaje, např. přidat výkon, zaměnit výkon za jiný, vyjmout výkon, změnit diagnózu, upravit datum, změnit v kartě pacienta údaje pacienta, atd. Po kliknutí na tlačítko *Nově vyúčtovat* se původní doklad označí jako OPRAVENÝ a vytvoří se kopie výkonů z daného dokladu.

Doklad po volbě Nově vyúčtovat:

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-131216.png]]
Výkony po volbě Nově vyúčtovat:

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-131234.png]]
Tyto kopie výkonů pak vstupují do nového vyúčtování (nemají čísla původních dokladu, v rámci nového vyúčtování jim jsou pak přidělena nová čísla dokladů). U těchto výkonů lze v modulu *Vyúčtování* – záložka *Výkony* změnit požadované údaje. Chceme-li měnit jakékoliv parametry výkonů, dvojklikem na řádek příslušného výkonu (který nemá číslo dokladu!) otevřeme editor výkonů umožňující provedení změn. Změny potvrdíme tlačítkem OK. Takto upravené výkony jsou připraveny k dalšímu vyúčtování.

Poté je potřeba běžným způsobem vyúčtovat za daný měsíc. Pokud odesíláme do zdravotní pojišťovny výkony za předešlé měsíce (pokud se nejedná o řádné vyúčtování na konci měsíce za jeden minulý měsíc), je nutné zvolit **řadu faktur*****“Doúčtování”***.  Ostatní úkony se dějí totožně s běžným měsíčním vyúčtováním. Nově vzniklé doklady s upravenými výkony se odesílají do portálu Zdravotních pojišťoven stejným způsobem jako běžné vyúčtování.

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-131251.png]]

## **Změna pojišťovny u pacienta:**

Změna údajů pojišťovny pacienta je nutné provést následujícím postupem:

1. Najít odmítnutý doklad/y a stisknout tlačítko „Nově vyúčtovat“ - tím se vytvoří kopie původních výkonů k novému vyúčtování.

1. Změnit zdravotní pojišťovnu v kartě pacienta, nová pojišťovna se přenese do všech otevřených výkonů

1. Vyúčtovat za daný měsíc běžným způsobem

Pozor, pořadí provedených kroků je důležité. Pokud nejdříve změníme pojišťovnu v kartě pacienta a poté opravujeme doklady, změna pojišťovny se do dokladů nenačte. V takovém je nutno vstoupit do karty pacienta a znovu změnit pojišťovnu na již vloženou správnou pojišťovnu (např. u pojištěnce 111 změnit údaj znovu na 111).

Poté je potřeba opět běžně vyúčtovat za daný měsíc.

## **Zrušení podání**

V případech, že je z nějakého důvodu nutné celé vyúčtování zrušit a udělat znovu, je možné využít funkce *Zrušit podání*. Toto tlačítko způsobí smazání všech hlaviček dávek vygenerovaných v daném podání (podání ≈ jeden textový soubor) a všech hlaviček dokladů z těchto dávek. Smaže se rovněž související faktura. Výkony, ZUMy, cesty, …, zůstanou zachovány a je možné je znovu vyúčtovat.

Pozor, tato funkce je nevratná a měla by být využívána ve zcela výjimečných případech. Údaje ze zrušeného (smazaného) vyúčtování nezůstávají v IS Galen v žádné evidenci. Zrušení podání provádí odmazání pouze v databázi FONS Galen, pokud bylo již podání odesláno na ZP, není toto podání na ZP automaticky stornováno. V takovém případě je vždy zapotřebí kontaktovat ZP a domluvit s ní další postup.

Při následném opětovném vyúčtování není zaručeno, že nově vytvořeným hlavičkám dokladů a dávek budou přidělena stejná čísla, jako v případě původního podání.

## **Nastavení verzí datového rozhraní vyúčtování**

Oprávnění ke změně verze datového rozhraní zapíná správce ve správě organizace na úrovni uživatele v kategorii Zvláštní oprávnění.

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-131353.png]]
Uživateli s oprávněním pro změnu verze datového rozhraní se vždy při ukládání, kopírování a podání zobrazí možnost vybrat verzi datového rozhraní.

![[pages/FONS GALEN/Správce a nastavení/Vyúčtování/assets/image-20250618-131429.png]]
Automatickou možností je vždy možnost s datovým rozhráním náležejícím k datu vytvoření.
