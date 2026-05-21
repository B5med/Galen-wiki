---
title: "Nadstandardní modul eOčkování"
version: 1
updated_at: 2025-06-19
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/50298914
---

# Nadstandardní modul eOčkování

Nyní mají lékaři povinnost bezodkladně učinit elektronický záznam o očkování, který bude odeslán do ISIN (Informační systém infekčních nemocí).

Lékaři mají možnost **nahlížet na informace** nebo **informace do ISIN odesílat** prostřednictvím webové aplikace nebo je možné očkování odesílat do ISIN prostřednictvím nadstandardního modulu. Obě varianty mají možnost nahlížet na očkování, která má pacient v ISIN zadaná.

#### **Výchozí nastavení**

Pro odeslání informací o očkování do ISIN je nutné

- Mít na společnosti aktivní nadstandardní modul Odesílání očkování do ISIN
- Mít na pracovišti nastavený platný certifikát SÚKL (stejný, který se využívá pro odeslání eReceptu a eNeschopenky).

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-101400.png]]
- Mít na pracovišti vyplněné PČZ (pořadové číslo zařízení). Tento údaj je možné získat na stránkách UZIS (Detailní záznamy ÚZIS ČR)

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-101433.png]]
- Mít na uživateli vyplněné pole „NRZP“

Číselník Národního registru zdravotnických pracovníků lze stáhnout v modulu Nástroje -> ISIN -> Registr zdravotnických pracovníků. Přesný popis v kategorii níže - Očkování Covid. Po stažení certifikátu uživatel s rolí Správce přiřadí položku z číselníku v detailu uživatele Správa organizace -> Uživatelé

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-101523.png]]
**Poznámka**: pro odeslání očkování není nutné vyplňovat podpisový certifikát. Očkování do ISINv2 tedy odesílá z FONS Galen každý zdravotnický pracovník, který očkování ukládá.

#### **VARIANTA 1: Nahlížení do výpisu provedeného očkování lékařem**

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-101842.png]]
Přístup k informacím se nachází v modulu Ordinace pod ikonou eOčkování.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-101907.png]]
Uživatel dle potřeby vyplní filtr (onemocnění, datum od, datum do) a stiskne tlačítko Aplikovat (Poznámka: tlačítko Aplikovat je nutné stisknout vždy, i bez vyplněného filtru).

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-101924.png]]
Po stisknutí tlačítka aplikovat se zobrazí všechna zadaná očkování.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-101942.png]]
V případě potřeby je možné kliknout na jednotlivé řádky v přehledu a zobrazit tak podrobnosti dané vakcinace.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102001.png]]
![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102011.png]]

#### **Výpis provedeného očkování**

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102031.png]]
Po kliku na tlačítko Export se nabídne export výpisu očkování, který je právě uživatelem zobrazen. Např. pokud uživatel filtruje pouze očkování proti tetanu, budou ve výpisu provedených očkování uvedena pouze tato očkování. Pokud mají být ve výpisu všechna očkování, je nutné zrušit všechny filtry.

#### **VARIANTA 2: Pro uživatele, kteří očkování aktivně aplikují**

Zaznamenání provedeného očkování ke konkrétnímu pacientovi

Změna a rušení záznamu o očkování

Nahlížení do výpisu provedeného očkování lékařem

Generování PDF o záznamu o očkování a generování PDF výpisu záznamu o očková

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102146.png]]
![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102202.png]]

#### **Skladová evidence očkovacích látek**

- **platí pro uživatele, kteří využívají nadstandardní modul “sklad”.**Stávající proces naskladnění očkovacích látek je rozšířen o položku **kód SÚKL** dané očkovací látky, protože tento kód je pro odeslání do ISIN povinný. Doporučujeme tak kód SÚKL při naskladnění očkovací látky uvést, uživateli to ušetří další práci při zadávání vlastního očkování. Pokud při naskladnění SÚKL kód očkovací látky nebyl vyplněn, musí uživatel kód zadat při každém očkování.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102326.png]]

Uživatel vybere kód SÚKL z číselníku. Je nutné zvolit správný kód, který rozlišuje velikost balení nebo sílu léčivého přípravku. Při odeslání do ISIN je uvedený kód SÚKL porovnáván s uvedenou šarží – **tyto údaje musí souhlasit s číselníkem.**

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102510.png]]

#### **Odeslání záznamu očkování do ISIN**

- Výběr schématu

Pokud uživatel v okně pro výběr schématu zaškrtne checkbox „Bez schématu“ nebo „Doplnit bez vykázání výkonu“, tak nebude možné toto očkování do ISIN odeslat, protože v něm nebudou vyplněné údaje povinné pro očkování.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102543.png]]
- Výběr varianty

V okně pro výběr varianty se nic nemění.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102606.png]]

#### **Výběr šarže**

V okně pro výběr šarže probíhá kontrola, zda zadaná šarže odpovídá kódu SÚKL dané očkovací látky. Toto ověření probíhá oproti číselníku SÚKL. Pokud se zde šarže očkovací látky neověří, je možné ověřit šarži online. Pokud ani po tomto kroku není šarže ověřena, není možné očkování do ISIN odeslat. Pokud si je uživatel jist, že zadal správný kód SÚKL očkovací látky a správnou šarži, musí kontaktovat SÚKL, aby jeho šarži přidal do číselníku.

- Výběr šarže **pro naskladněné očkovací látky** (pro uživatele využívající nadstandardní modul “sklad”)

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102710.png]]
Šarže na prvním řádku obrázku **nemá zadaný kód SÚKL při naskladnění**(obr. níže)

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102728.png]]
Šarže na druhém řádku **má zadaný správný kód SÚKL** při naskladnění, a tak **není potřeba nic ověřovat** a je možné pokračovat na další okno. (obr. níže)

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102744.png]]
Pokud při naskladnění SÚKL kód očkovací látky nebyl vyplněn, musí uživatel kód zadat při každém očkování.

- Výběr šarže pro očkovací látky **bez skladové evidence**

SÚKL kód očkovací látky uživatel vybere při zadávání očkování. Vybraný kód se předvyplní při dalším očkování stejně jako šarže a exspirace.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102856.png]]

#### **Důležité - Tlačítko Očkovat/Dále**

V případě, že byla ověřena šarže a kód SÚKL, zobrazí se uživateli tlačítko Dále pro zobrazení dalšího okna pro kontrolu údajů, které budou odeslány do ISIN.

V případě, že se šarže a kód SÚKL neověří, zobrazí se uživateli tlačítko Očkovat. Takové očkování se uloží do databáze, ale neodešle se (ani v budoucnu) do ISIN, protože kódu SÚKL je údaj povinný pro odeslání.

**Informace k odeslání do ISIN**

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-102949.png]]
**Očkovací látka** – název se dotahuje z číselníku Léčivé přípravky na základě zadaného kódu SÚKL očkovací látky

**Typ vakcinace**– automaticky se doplňuje dle vybraného pořadí dávky v okně výběru očkovacího schematu. Nabývá hodnot Primovakcinace nebo Přeočkování.

**RID** - rezortní identifikátor pacienta. Je-li RID v kartě pacienta vyplněný, automaticky se při očkování do příslušného pole doplňuje. Pokud v kartě pacienta RID vyplněný není, vpravo za polem RID lze stiskem tlačítka se zahnutými šipkami tento rezortní identifikátor Autentizovat (dotáhnout).

**Pojišťovna** – údaj povinně zadaný v kartě pacienta se zde automaticky vyplňuje.

**Kód výkonu a materiálu i diagnóza** se dotahuje z očkovacího schematu. Diagnózu lze změnit.

V posledním okně jsou zobrazené informace o naskladněné OL. Nyní lze odeslat do ISIN.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103012.png]]

#### **Stav odeslání ISIN**

Po stisku tlačítka Očkovat se záznam uloží a zároveň odešle do ISIN.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103039.png]]
Úspěšně odeslané očkování bude potvrzeno hláškou. Očkování může být přijato, ale zároveň se uživateli zobrazí informace upozorňující na nějakou nesrovnalost, která je v příslušném okně popsána.

Očkování, které bylo přijato, se v Přehledu očkování zobrazuje ve stavu Přijato.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103055.png]]
V případě, že je ve sloupci Stav ISIN uvedeno Chyba nebo není stav uveden, je nutné očkování zaslat do ISIN znovu.

Pokud uživatel odesílá očkování s jiným datem, než je ten dnešní, vrátí se chyba, ve které je popis problému.

#### **Přehled očkování**

Přehled očkování byla rozšířen o sloupec „Stav ISIN“.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103129.png]]
Pokud je očkování ve stavu Přijato, bylo takové očkování akceptováno.

Pokud je očkování ve stavu Chyba – je nutné upravit údaje podle pokynů a odeslat znovu.

#### **Detail provedeného očkování**

Detail provedeného očkování získáme rozkliknutím příslušného řádku očkování dvojklikem.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103159.png]]
Očkování zadané po zapnutí funkcionality eOčkování obsahuje údaje potřebné pro odeslání do ISIN. Očkování zadaná před zapnutím funkcionality není možné zpětně odeslat.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103213.png]]
V případě potřeby editace údajů, které nejsou editovatelné, je nutné celé očkování smazat a zadat znovu.

Pro zprovoznění funkcionality eOčkování v AIS Galen je potřeba mít stávající nezbytnosti pro odeslání eReceptu, tzn.

- Certifikát SÚKL na pracovišti
- Kód SÚKL
- Identitu uživatele SÚKL
- Podpisový certifikát

Uživatelé, kteří již z AIS Galen odesílají eRecept, nebudou potřebovat nic dalšího kromě toho, co používají nyní.

#### **Editace očkování**

V případě potřeba editace již odeslaného očkování je možné zobrazit detail očkování. Zde je ale možné editovat pouze pole Poznámka, ostatní položky jsou vyplněny na základě výběru výše uvedených položek.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103240.png]]
Pokud je nutné změnit pole „očkovací látka“, „typ vakcinace“ nebo „pojišťovna“, pak je nutné celé očkování smazat a zadat znovu.

#### **Smazání očkování**

V případě smazání očkování v rámci FONS Galen, které bylo úspěšně odesláno do ISIN, bude požadavek na smazání zároveň odeslán do ISIN.

#### **Neodeslaná očkování**

Modul Dashboard poskytuje přehled očkování, která byl měla být od ISIN odeslána, ale nebyla. Očkování může odeslat pouze ten odpovědný lékař, který očkování do FONs Galen zadal, nebo uživatel, který není odpovědným lékařem.

Z dashboardu se uživatel dostane na detail konkrétního neodeslaného očkování.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103351.png]]

#### **Poznámka k modulu eOčkování**

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103413.png]]
Modul eOčkování (k dispozici v horní liště nebo v záložce modulu Očkování) zobrazuje informace, které jsou poskytovány ze strany SÚKL. Tam se původně záznamy o očkování odesílaly. Po změně legislativy se záznamy odesílají do ISIN, ale správcem poskytující informace o provedených očkování je stále SÚKL. Propojení mezi SÚKL a ISIN není v tuto chvíli realizované, a proto očkování odeslaná z FONS Galen do ISIN, nebudou v tuto chvíli v modulu eOčkování viditelná.

Poznámka: *Pediatři mají zadávání očkování obdobné, systém je však doplněn o očkovací kalendář.*

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103445.png]]

#### **Očkování COVID**

Informace o očkování pacienta do ISIN probíhá v rámci zadání očkování. Je však nutné, aby bylo provedeno správné nastavení - viz. Níže.

**Nastavení:**

- Pro odesílání a získávání informace z ISIN je nutné **identifikovat zdravotnického pracovníka**, který informaci z ISIN získává/odesílá pomocí ID zdravotnického pracovníka z Národního registru zdravotnických pracovníků (dále jako NRZP).Jako druhou možnost pro komunikaci zdr. pracovníka s ISIN je možné zaslat rodné číslo pracovníka, avšak tento způsob identifikace je označen ze strany ÚZIS jako nedoporučovaný.
- Pro odeslání informace o provedeném očkování do ISIN je nutné, aby uživatel AIS Galen s rolí Správce **vytvořil**v AIS Galen **uživatelskou variantu očkování**, ve které použije číselníky poskytované ÚZIS.

#### **Přiřazení ID zdravotnického pracovníka (čísla NRZP) k uživateli AIS Galen**

Uživatel s rolí Správce zadá ID zdravotnického pracovníka k uživateli v modulu Správa organizace –Uživatelé, viz Obrázek

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103600.png]]
Tento postup předpokládá, že Správce číslo NRZP uživatele zná. Pokud číslo NRZP nezná, číslo NRZP může vybrat z číselníku. Číselník je nutné nejprve načíst z NRZP,viz další kapitoly.

**Nutné předpoklady pro získání ID zdravotnického pracovníka**

Certifikát vydaný SÚKL, jedná se o stejný certifikát společnosti, který je nutný pro odeslání eReceptu.

**Postup pro získání seznamu pracovníků NRZP společnosti**

Pokud Správce ID zdravotnického pracovníka nezná, může si za pomocí certifikátu zavolat službu pro získání seznamu zdravotnických pracovníků dané společnosti. Položky z tohoto seznamu pak lze přiřadit k uživateli v AIS Galen.

**Stažení seznamu zdravotnických pracovníků společnosti**

Uživatel s rolí Správce může stáhnout seznam zdravotnických pracovníků dané společnosti. Modul Nástroje – Číselníky – ISIN - záložka Registr zdr. Prac.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103647.png]]
Po kliku na tlačítko Načíst z NRZP bude zavolána služba ÚZIS, která zašle seznam zdravotnických pracovníků společnosti. Upozornění: Volání této služby je časově náročné, získání seznamu může trvat až 10 minut.

Uživatel je vyzván pro výběr certifikátu, který se má k volání seznamu použít.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103702.png]]
**Společnost**– pro volání se použije certifikát ÚZIS, který je přiřazen na společnosti.

**Podřízená společnost** – uživatel zvolí, který z certifikátů ÚZIS přiřazených na podřízených společnostech, se pro volání má použít.

**Pracoviště** – uživatel zvolí, který z certifikátů SÚKL přiřazených na pracovištích, se pro volání má použít.

Následně bude stažen seznam zdravotnických pracovníků. Do tohoto číselníku je také možné zadat zdravotnického pracovníka ručně - přes tlačítko +.

#### V**ytvoření uživatelské varianty očkování**

Společnost, která chce odesílat informace o očkování do ISIN, si musí vytvořit uživatelskou očkovací variantu, kterou se budou informace do ISIN odesílat. Uživatelskou očkovací variantu vytvoří uživatel AIS Galen s rolí Správce v modulu Správa organizace – Agendy – Varianty očkování

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103732.png]]
V tomto okně uživatel vidí v levé části varianty očkování vytvořené Správci AIS Galen na základě platné metodiky. V pravé části okna jsou vidět varianty očkování, které vytvořil uživatel s rolí Správce dané společnosti.

**Vytvoření uživatelské varianty je možné dvěma způsoby:**

- **Vytvořením uživatelské varianty kopií ze základní očkovací varianty** – tento způsob použijte v případě, kdy v základních očkovacích variantách vidíte očkovací variantu, kterou pouze chce doplnit nebo pozměnit.
- **Vytvořením vlastní uživatelské varianty** – tento způsob použijte v případě, kdy v základních očkovacích variantách nevidíte variantu, kterou potřebujete doplnit nebo pozměnit. Tento způsob vyžaduje vyplnění všech položek.

#### **Vytvoření uživatelské varianty kopií ze základní očkovací varianty**

Uživatel z levého sloupce přehledu očkovacích variant s názvem Varianty očkování základní vybere variantu, kterou chce kopírovat a stiskne tlačítko Kopírovat ![[pages/Nadstandardní modul eOčkování/assets/image-20250619-104432.png]]

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-103822.png]]
Otevře se okno pro editaci očkovací varianty. Položky, které byly vyplněny v základní očkovací variantě jsou přeneseny, ale zároveň je možné je změnit.

#### **Vytvoření nové uživatelské varianty**

Novou uživatelskou variantu je možné vytvořit stisknutím zeleného tlačítka PLUS  v části uživatelské varianty.

#### **Jednotlivé položky uživatelské varianty**

V případě, že je potřeba, aby se informace z této očkovací varianty odesílaly do ISIN, zaškrtne uživatel checkbox Odesílat do ISIN (1.).

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-104642.png]]

V první části okna se vyplňují položky, které jsou společné pro všechny očkovací varianty, ať už se odesílají do ISIN, či nikoliv. Specifikují, jakým způsobem se bude dané očkování vykazovat pojišťovně.

Položka název (2.) definuje, pod jakým názvem se uživateli bude očkovací varianta nabízet. Záleží tak na uživateli, zda si chce vytvořit jednu obecnou variantu pro každou očkovací látku, např. Hradí stát – ISIN, kterou bude při každém očkování pacienta měnit, nebo zda vytvoří více očkovacích variant pro nejčastější indikace, které zohlední v názvu očkovací varianty.

V druhé části okna (3.) je nutné vyplnit informace, které se odesílají do ISIN.

Pole očkovací látka a typ očkování je nutné vyplnit.

Další pole (indikace, jiná indikace, aplikační cesta, místo aplikace) uživatel může vyplnit, aby se mu tyto možnosti při zadávání očkování nabízely, ale zároveň bude možné při zadání očkování hodnoty těchto polí změnit.

**Důležité**: Jakmile je očkovací varianta použita pro zadání očkování konkrétnímu pacientovi, všechna pole očkovací varianty přestanou být editovatelná. V případě, že po naočkování uživatel vyhodnotí, že je nutné ve variantě něco změnit, je nutné danou očkovací variantu deaktivovat a vytvořit novou.

#### **Odeslání informace o očkování do ISIN**

Do ISIN je možné odeslat informaci o očkování pouze ve chvíli, kdy je očkování zadáno do Galenu pomocí tlačítka**Očkovat**. Očkování do ISIN nelze odeslat pouze při doplnění.

**V prvním kroku** uživatel vybere očkovací látku

**V druhém kroku** uživatel musí zvolit očkovací schéma

V tomto kroku je možné zaškrtnout další možnosti:

**Ve třetím kroku** – výběr varianty zvolí uživatelsky vytvořenou variantu, která má příznak „Odesílat do ISIN“. Uživateli se přednastaví položky, které vyplnil při vytváření varianty. Položky Indikace, Jiná indikace, Poznámka, Aplikační cesta, Místo aplikace je možné změnit nebo doplnit. Hodnota pole Typ výkonu se přednastavuje na základě toho, zda byla v předchozím kroku vybrána první nebo druhá dávka očkování.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-104921.png]]
![[pages/Nadstandardní modul eOčkování/assets/image-20250619-105025.png]]
![[pages/Nadstandardní modul eOčkování/assets/image-20250619-105052.png]]
![[pages/Nadstandardní modul eOčkování/assets/image-20250619-105118.png]]

**Ve čtvrtém kroku** uživatel buď vybere šarží ze skladu, nebo v případě, že sklady nepoužívá, zadá šarži a expiraci ručně. Po stisknutí tlačítka očkovat se očkování uloží a zároveň odešle do ISIN.

#### **Zobrazení informací v okně očkování**

#### **Přehled očkování**

Okno přehled očkování bylo rozšířeno o položky, které jsou odesílány do ISIN.

Jedná se o sloupce

- Stav ISIN – pokud byla podána první dávka ze dvou, vakcinace je ve stavu probíhající. Pokud byla podána druhá dávka ze dvou, vakcinace je ve stavu ukončená.

- Typ očkování ISIN

- Indikace ISIN

- Jiná indikace ISIN

- Aplikační cesta ISIN

- Místo aplikace ISIN

- Typ výkonu ISIN

- Poznámka ISIN

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-105215.png]]

**Poznámka**: Pro přehlednější zobrazení informaci v jednotlivých sloupcích lze celé okno posunout. Po najetí myší na středovou vertikální čáru, která odděluje pravou a levou část okna, se zobrazí dvojitá šipka, pomocí které je možné toto rozdělení posunout.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-105232.png]]

#### **Záložka Seznam očkování ISIN**

V záložce Seznam očkování ISIN jsou k dispozici tlačítka pro zařazení, vyřazení nebo ověření, zda je možné pacienta zařadit do očkovacího seznamu. Také je zde zobrazen přehled očkování, která má pacient již zadaná v ISIN.

**Oprava údajů zaslaných do ISIN**

Údaje zaslané do ISIN je možné upravit a zaslat znovu do ISIN. V přehledu očkování je potřeba rozkliknut řádek s dávkou, kterou je potřeba upravit.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-105531.png]]
Po editaci příslušného pole se spolu se stisknutím tlačítka OK odešlou informace do ISIN. **Důležité**: Pole Typ výkonu nelze editovat. Pokud uživatel zadal špatné pořadí dávky vakcinace, je nutné řádek očkování smazat a zadat znovu.

#### **Stažení certifikátu o provedeném očkování**

V případě, že je očkování ukončeno, tzn. jsou do ISIN odeslány všechny dávky dle očkovacího schématu, tak je možné z ISIN stáhnout certifikát pro pacienta o provedeném očkování. Je potřeba označit řádek, ve kterém je uvedená vakcinace ve stavu „ukončená“. Následně se v Přehledu očkování zobrazí tlačítko pro stažení certifikátu.

![[pages/Nadstandardní modul eOčkování/assets/image-20250619-105605.png]]
Následně se zobrazí okno, ve kterém si uživatel vybere způsob exportu certifikátu.
