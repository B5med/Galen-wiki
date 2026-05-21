---
title: "Smlouvy"
version: 4
updated_at: 2025-10-31
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/48922625
---

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124256.png]]
V sekci Smlouvy lze provádět hromadné změny týkající se nasmlouvaných výkonů a parametrů smlouvy. Nejčastěji uživatelé potřebují přidat výkon do více pojišťoven či na více pracovišť současně.

## **Hromadné přidání nasmlouvaného výkonu, parametru smlouvy a jejich aktualizace**

Správce -> Správa organizace -> Smlouvy

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124325.png]]
V levém sloupci je nutné označit pojišťovny, do kterých lze přidat výkon ve středním sloupci označíme všechna pracoviště, u kterých je výkon nasmlouván. Poté stiskem Přidat výkon otevřeme v pravé části okno pro přidání výkonu. Označení všech položek v jednom sloupci po označení jednoho řádku provedeme stiskem kláves CTRL+A.

### **V sekci Smlouvy lze**:

- Přidat výkon a jeho parametry

- Přidat parametry smlouvy

- Aktualizovat parametry výkonu

- Aktualizovat parametry smlouvy

#### **Přidat výkon a jeho parametry**

Správce -> Správa organizace -> Smlouvy

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124416.png]]
![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124430.png]]
Do položky **Typ výkonu** napíšeme kód výkonu (např. 09543) a poté se stiskem tlačítka Provést výkon přiřadí do všech zvolených pojišťoven a pracovišť. Ostatní položky není nutné vyplňovat, ty budou načteny z číselníku výkonů. ` `
Pokud má uživatel s pojišťovnou smluvené jiné než „číselníkové“ parametry smluvy, je možné tato nastavení také definovat v okně Přidat výkon.

**Typ výkonu** - kód výkonu (např. 02125). Chceme-li zadat více výkonů, je nutné jednotlivé výkony oddělit čárkou, poté po stisku tlačítka Provést je výkon přidán k nasmlouvaným výkonům.

**Hodnota bodu** – umožňuje k zadanému výkonu či více výkonům zadat jinou než „číselníkovou“ hodnotu bodu

**Hodnota bodu NP** - umožňuje zvolit hodnotu bodu u pacienta v nepravidelné péči

**Fixní částka** – umožňuje zadat jednoznačnou fixní částku výkonu, která ruší platnost hodnoty bodu

**Cesty** – odškrtnutím checkboxu lze (u výkonů s možností spojení s cestou lékaře k pacientovi, např. 01150) zakázat možnost vykazování cesty svázané s těmito výkony.

**Kapitace**– umožňuje volbu zahrnout či vyloučit výkony do/z kapitační platby

**Platí od, Platí do** – umožňuje stanovit období platnosti uvedených výkonů

Smazat výkon nelze, lze ukončit platnost výkonu.

#### **Přidat parametr smlouvy**

Správce -> Správa organizace -> Smlouvy

Slouží k možnosti hromadného přidání parametrů smlouvy. Stejně jako u možnosti „Přidat výkon“ je nejdříve nutný výběr alespoň jedné pojišťovny a alespoň jednoho pracoviště. Po otevření tabulky „Přidat parametr smlouvy“ je možné hromadně přidat zobrazené položky, např. max. počet km, které lze vykazovat na doklady cest. Systém poté hlídá stanovený limit kilometrů.

Zvolení pojištoven a pracovišt pro provedení změn:

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124523.png]]
Volba operace, kterou chceme na označených pracovištích a pojišťovnách provést:

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124535.png]]
![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124546.png]]
**Od období** – stanovení začátku období platnosti uvedených parametrů smlouvy

**Hodnota bodu** – stanoví hodnotu bodu bez ohledu na údaj z číselníku výkonů

**Hodnota bodu zahr.** – stanoví hodnotu bodu zahraničních pacientů

**Degresní koeficient** – možnost stanovení vlastního degresního koeficientu dle smlouvy s pojišťovnou/ pojišťovnami.

**Kapitační paušál** – možnost stanovení vlastního kapitačního paušálu dle smlouvy s pojišťovnou/ pojišťovnami.

**Kód dopravy** – dle metodiky lze zvolit kód dopravy:

- 06 – paušál na jednu návštěvu u pacienta

- 08 – paušál na měsíc

- 10 – dle kilometrů

**Max.počet km** – možnost stanovení max. počtu km, které lze vykazovat na doklady cest. Systém poté hlídá stanovený limit kilometrů.

**Náhradní IČP** – lze nastavit IČP, které se bude objevovat ve vyúčtovacích dokladech namísto IČP, na kterém byly vyúčtované výkony původně zadané

**Náhradní odbornost** - lze nastavit odbornost, která se bude objevovat ve vyúčtovacích dokladech namísto odbornosti pracoviště, na kterém byly vyúčtované výkony původně zadané

**Nejpřesnější dg** – možnost stanovení kontroly nejpřesnější dg dle metodiky zadávání výkonů. Existuje-li v číselníku čtyřmístná diagnóza, systém hlídá zadání této čtyřmístné = nejpřesnější diagnózy. Např. nelze zdat Dg.M54, je nutno doplnit Dg např M543.

#### **Aktualizovat parametr výkonu**

Správce -> Správa organizace -> Smlouvy

Slouží k možnosti hromadné aktualizace parametrů výkonu pro více pracovišt i pojišťoven. Stejně jako u možnosti „Přidat výkon“ je nejdříve nutný výběr alespoň jedné pojišťovny a alespoň jednoho pracoviště. Po otevření tabulky „Aktualizovat parametr výkonu“ je možné hromadně aktualizovat zobrazené položky.

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124625.png]]
![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124635.png]]
Postup aktualizace jednotlivých položek je stejný jako v případě přidání výkonu a jeho parametrů.

Novinkou je zde možnost **Vynulovat**stávající parametr výkonu. Je-li např. stanovena hodnota bodu NP (pro označené/á pracoviště a označenou/é pojišťovnu/y) např. 2,5, po zaškrtnutí pole Vynulovat dojde na zvolených pracovištích u zvolených pojišťoven ke smazání nastavené hodnoty, která nadále zůstane nevyplněna. Viz příklad dále.

Původní hodnota nastavení Hodnoty bodu NP výkonu 21225:

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124720.png]]
Provedení hromadného vynulování nastavené Hodnoty bodu NP výkonu 21225:

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124737.png]]
Vynulovaná Hodnota bodu NP výkonu 21225 po provedení Aktualizace parametru výkonu:

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124802.png]]
Smazání výkonu se neprovádí, lze provést ukončení platnosti výkonu.Veškeré úpravy výkonu do minulosti se poté budou vázat k nastavení parametrů k datu vykázání výkonu.

#### **Aktualizovat parametr smlouvy**

Správce -> Správa organizace -> Smlouvy

Slouží k možnosti hromadné aktualizace parametrů smlouvy pro více pracovišt i pojišťoven. Stejně jako u možnosti „Přidat parametr smlouvy“ je nejdříve nutný výběr alespoň jedné pojišťovny a alespoň jednoho pracoviště. Po otevření tabulky „Aktualizovat parametr smlouvy“ je možné hromadně aktualizovat zobrazené položky.

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124840.png]]
Postup aktualizace jednotlivých položek je stejný jako v případě přidání parametrů smlouvy.

Novinkou je zde možnost **Vynulovat**stávající parametr smlouvy. Je-li např. stanovena hodnota pole „Max. počet km“(pro označené/á pracoviště a označenou/é pojišťovnu/y) např. 10, po zaškrtnutí pole Vynulovat dojde na zvolených pracovištích u zvolených pojišťoven ke smazání nastavené hodnoty, která nadále zůstane nevyplněna. Nastavení se takto změní u všech zvolených pracovišť a pojišťoven.

### **Kopírování smluvních výkonů**

Poskytuje možnost kopírování smluvních výkonů mezi jednotlivými pojišťovnami nebo pracovišti.

Možnost kopírovat smluvní výkony se nachází ve správě organizace, ve struktuře na úrovni pracoviště.

Při výběru konkrétní pojišťovny klikneme na tlačítko Kopírovat smluvní výkony.

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124906.png]]

#### **Kopírovat smluvní výkony na pracovišti:**

Vybereme cílové smlouvy s pojišťovnami, kam chci smluvní výkony nakopírovat.

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124930.png]]
Po Potvrzení se nám zobrazí výsledek kopírování smluvních výkonů. Info okno obsahuje počet přidaných výkonů, počet přeskočených výkonů, které již na pracovišti existují případně výkony, které již nejsou v platném číselníku.

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-124949.png]]

#### **Kopírovat smluvní výkony mezi pracovišti:**

Při možnosti kopírovat smluvně výkony mezi pracovišti bude uživateli nabídnut číselník všech smluv s pojišťovnami na všech pracovištích společnosti.

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Smlouvy/assets/image-20250618-125019.png]]
