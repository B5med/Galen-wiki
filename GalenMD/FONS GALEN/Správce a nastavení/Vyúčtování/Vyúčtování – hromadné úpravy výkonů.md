---
title: "Vyúčtování – hromadné úpravy výkonů"
version: 1
updated_at: 2025-07-21
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/75792551
---

# Vyúčtování – hromadné úpravy výkonů

V modulu Vyúčtování lze také provádět hromadné úpravy výkonů, které uživatelům ulehčí práci při nutnosti změny u více výkonů současně. Správce -> Vyúčtování -> Hromadné úpravy

Ve třech základních záložkách

1. Vytvoření výkonů
2. Úprava a odstranění výkonů
3. Přehled operací

![image-20250618-132106.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132106.png>)
lze dle zadaných kritérií ve filtru hromadně vytvořit výkony nové, nebo je možné u stávajících výkonů provést úpravy ve smyslu změny výkonů na výkony jiné, lze také změnit počet vykázaných výkonů, hlavní nebo řádkovou diagnózu nebo navázat či smazat ZUM s možností použití pomocného výkonu. Změny výkonů se zde řídí stejnými pravidly jako v editoru výkonů v kartotéce, tzn. Jsou dodržena platná pravidla, která platí pro svázané výkony, zakázané výkony, zakázané kombinace, frekvenční omezení.

Dodržení zmíněných pravidel lze zkontrolovat v záložce kontrola Výkonů:

![image-20250618-132134.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132134.png>)
V záložce Přehled operací vidíme provedené změny s určením přesného data a času operace, názvu operace a s určením Stavu. Nechybí ani popis průběhu operace a případný popis s přesným určením, proč operace neproběhla dle zadání.

## **Hromadné vykazování**

Funkcionalita, která slouží k hromadnému vytváření, upravování či odstraňování výkonů pro uživatelem definovanou skupiny pacientů, se nachází v modulu Vyúčtování.

![image-20250618-132212.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132212.png>)

### **Definice skupiny pacientů (výkonů)**

V prvním kroku je nezbytné definovat skupinu uživatelů, popřípadě jejich výkonů, nad nimiž budou provedeny požadované operace. Skupina je definovaná pomocí filtrů, který jsou děleny do kategorií - Základní, Registrace, Výkony a Dg. Pro zobrazení výsledků filtrování je nutné kliknout na tlačítko Aplikovat.

![image-20250618-132238.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132238.png>)

### **Vytvoření výkonů**

Uživatel po kliknutí na tlačítko Vytvořit nebo Vytvořit u všech a následném výběru pracoviště, pod které budou výkony vykázány, přejde do okna, kde definuje datum vykázání, výkon, hlavní a řádkovou diagnózu, pracoviště a odpovědného lékaře.

![image-20250618-132302.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132302.png>)
Tlačítkem Z+ lze k příslušným výkonům připojit ZUM. Při výběru ZUMu se uživateli zobrazuje položka Množství pro jednoho pacienta, která je editovatelná. Dále potom Počet pacientů, což odpovídá vzorku, nad kterým provádíme danou operaci. Položka Celkové množství je následně součinem dvou předchozích položek.

![image-20250618-132316.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132316.png>)
Jestliže vybírám ZUM, který má vazbu na sklad, nemůže být celkové množství vyšší než množství, které je skladem. Při hromadné zadání ZUM nelze kombinovat sortimenty z více skladů.

![image-20250618-132348.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132348.png>)
Zaškrtnutím checkboxu povolit pomocný výkon se zajistí, že v situacích, kdy je pro vytvoření ZUM nutné dle metodiky vytvořit pomocný výkon 01999 nebo 09215, se tento výkon automaticky vykáže.

### **Úprava výkonů**

Uživatel se po kliknutí na tlačítko Upravit nebo Upravit všechny u všech dostane do okna, kde zaškrtnutím příslušného checkboxu volí jednu či více úprav, které chce provést.

![image-20250618-132413.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132413.png>)

Po zatrhnutí checkboxu se objeví pole, kam uživatel zadá hodnotu, na kterou chce danou položku změnit.

### **Odstranění výkonů**

Odstranění výkonů lze spustit pomocí tlačítek Odstranit nebo Odstranit všechny. Před samotným odstraněním ovšem musí ještě uživatel určit, zda v případě, že některý z odstraňovaných výkonů obsahuje ZUM s vazbou na sklad, má být tato látka nebo prostředek po odstranění příslušného výkonu vrácena na sklad.

![image-20250618-132742.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132742.png>)

### **Přehled operací**

Jelikož se zadané operace zpracovávají na serveru, může uživatel během zpracování vykonávat kteroukoliv jinou činnost v Galenu nebo dokonce může Galen vypnout. K zjištění podrobností o dané úloze se následně lze vrátit v záložce Přehled operací. Jednotlivé záznamy se zde uchovávají vždy 7 dní od ukončení dané operace. V levé části obrazovky se objevuje přehled operací:

![image-20250618-132828.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132828.png>)
V pravé části se poté zobrazuje detail vybrané operace:

![image-20250618-132841.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132841.png>)
1. Tento ukazatel indikuje, v jakém stavu se daná operace nachází.

2. Jestliže daná operace stále běží, je možné ji pomocí tlačítka Zastavit ukončit. Opětovné spuštění ovšem není již možné.

3. V této části uživatel definuje, jaké typy zpráv chce v detailním přehled zobrazovat.

4. Detailní přehled uživatele informuje o jednotlivých dílčích krocích operace. Tento přehled se v průběhu běhu operace pravidelně aktualizuje. Přehled lze i exportovat do požadovaného formátu stisknutím ikonky: ![image-20250618-132904.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250618-132904.png>)

### **Vygenerování zprávy o chybných výkonech**

Byla vytvořena nová funkcionalita pro předávání informací k opravám výkonů, která slouží k vygenerování zprávy o zadání chybných výkonů a její automatické zobrazení uživatelům na příslušném IČP, kde byl původní chybný výkon zadán.

Funkcionalitu lze zapnout na parametru společnosti (checkbox „Předávat informace k opravám výkonů“).

V modulu Vyúčtování – záložka Doklady lze nyní při novém vyúčtování specifikovat chybu a uvést poznámku, která se zobrazí lékaři.

![image-20250619-072550.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250619-072550.png>)
Na existenci položky k opravě je poté lékař upozorněn pomocí standardního oznámení při přihlášení do aplikace:

![image-20250619-072606.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250619-072606.png>)
Všechny položky vyúčtování k opravě lze zobrazit v Dashboardu, odkud je možné přímým proklikem ze seznamu pacientů vstoupit do výkonů:

![image-20250619-072638.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250619-072638.png>)
Ve výkonech jsou tyto položky k opravě označeny stavem opravy "Předáno k opravě":

![image-20250619-072657.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250619-072657.png>)
Jakmile lékař provede požadovanou opravu, změní stav opravy na "Opraveno":

![image-20250619-072721.png](<../../../../pages/FONS GALEN/Správce a nastavení/Vyúčtování/Vyúčtování – hromadné úpravy výkonů/assets/image-20250619-072721.png>)
Tímto způsobem jsou výkony předány k novému vyúčtování.

### **Nová uživatelská role Specialista vyúčtování**

Na základě požadavku byla vytvořena nová role Specialista vyúčtování. Jde opět jen o zpřístupnění stávající funkcionality týkající se konfigurace smluv se ZP. Konfigurace tohoto pracovníka je na uživateli ve zvláštních oprávněních checkbox – Specialista vyúčtování. Uživateli potom v modulu Vyúčtování přibude v horním modrém menu tlačítko Smlouvy. Pod tímto tlačítkem se nacházejí funkce konfigurace smluv se ZP. Jedná se opět o již hojně využívanou funkcionalitu, která byla dostupná v modulu Správa organizace.
