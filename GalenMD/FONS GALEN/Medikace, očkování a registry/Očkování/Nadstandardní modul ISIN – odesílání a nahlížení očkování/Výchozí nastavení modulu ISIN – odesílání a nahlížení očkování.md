---
title: "Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování"
version: 7
updated_at: 2026-06-28
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/475627544
---

# Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování

Pro aktivaci modulu **FONS Galen - ISIN odesílání a nahlížení očkování** je potřeba splnit následující podmínky.

## Údaje potřebné pro komunikaci s ISIN

- Mít na **společnosti** aktivní nadstandardní modul **FONS Galen - ISIN odesílání a nahlížení očkování**.
- Mít na **pracovišti** nastavený platný **certifikát SÚKL** (stejný jako pro eRecept a eNeschopenku).

   ![image-20250619-101400.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20250619-101400.png>)
- Mít na **pracovišti** vyplněné **PČZ** (pořadové číslo zařízení). Tento údaj lze zjistit na stránkách UZIS (Detailní záznamy ÚZIS ČR).

   ![image-20250619-101433.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20250619-101433.png>)
- Mít na **uživateli** vyplněné pole **NRZP** (ID zdravotnického pracovníka z Národního registru zdravotnických pracovníků).

   ![image-20260628-125720.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20260628-125720.png>)

> [!info]
> Pro odeslání očkování do ISINv2 není nutné vyplňovat podpisový certifikát. Záznamy odesílá každý zdravotnický pracovník, který očkování v systému ukládá.

## Stažení číselníků

Pro vytvoření uživatelské varianty očkování, kterou je nutné odeslat do ISIN, je nejdříve nutné, aby
uživatel s AIS Galen s rolí Správce stáhnul číselníky, které poskytuje ÚZIS.
Modul Nástroje – ISIN – v jednotlivých záložkách jsou dostupné jednotlivé číselníky.

### Stažení číselníku ručně

V každé ze záložek je nutné stáhnout každý číselník zvlášť pomocí tlačítka aktualizovat.

![image-20260628-132842.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20260628-132842.png>)
Po stisku tlačítka se zobrazí okno pro výběr certifikátu, který se má pro aktualizaci použít. Dostupné
jsou až tyto tři možnosti, které závisí na tom, zda je ve FONS Galen nahrán platný certifikát.

- Společnost – certifikát ÚZIS vložený ve struktuře společnosti
- Podřízená společnost – certifikát ÚZIS vložený ve struktuře podřízené společnosti
- Pracoviště – certifikát SÚKL vložený ve struktuře pracoviště – v případě výběru tohoto
   certifikátu je nutné také vybrat pracoviště.

Každou položku číselníku je možné ručně editovat. Zároveň je možné položky přidat nebo odebrat.

### Automatická aktualizace číselníků

Zároveň je naplánována úloha na automatickou aktualizaci číselníku každou sobotu v 01:00.

## Přiřazení ID zdravotnického pracovníka (NRZP) k uživateli

Uživatel s rolí **Správce** zadá ID zdravotnického pracovníka k uživateli v modulu **Správa organizace – Uživatelé**.

Pokud Správce číslo NRZP nezná, může ho vybrat z číselníku. Číselník je nutné nejprve načíst z NRZP.

### Postup pro získání seznamu pracovníků NRZP společnosti

Uživatel s rolí Správce může stáhnout seznam zdravotnických pracovníků dané společnosti v modulu **Nástroje – Číselníky – ISIN – záložka Registr zdravotnických pracovníků**

![image-20260628-125914.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20260628-125914.png>)
Po kliknutí na tlačítko **Načíst z NRZP** bude zavolána služba ÚZIS, která zašle seznam zdravotnických pracovníků společnosti.

![image-20260628-130059.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20260628-130059.png>)
> [!abstract]
> Volání této služby je časově náročné – získání seznamu může trvat až 10 minut.

Uživatel je vyzván k výběru certifikátu, který se má k volání použít:

- **Pracoviště** – uživatel zvolí certifikát SÚKL přiřazený na pracovišti.

Po stažení seznamu lze zdravotnického pracovníka přiřadit k uživateli ve FONS Galen. Do číselníku je také možné zadat pracovníka ručně přes tlačítko **+**.

## Vytvoření uživatelské varianty očkování

> [!warning]
> Společnost, která chce odesílat informace o očkování proti Covid-19 do ISIN, musí vytvořit **uživatelskou očkovací variantu**.

Uživatelskou variantu vytvoří uživatel s rolí Správce v modulu **Správa organizace – Agendy – Varianty očkování**.

V tomto okně uživatel vidí:

- v **levé části** varianty očkování vytvořené správci AIS Galen na základě platné metodiky (základní varianty),
- v **pravé části** varianty vytvořené správcem dané společnosti (uživatelské varianty).

   ![image-20260628-130457.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20260628-130457.png>)

### Vytvoření uživatelské varianty kopií ze základní varianty

Tento způsob použijte, pokud v základních variantách vidíte variantu, kterou chcete pouze doplnit nebo pozměnit. Z levého sloupce vyberte variantu a stiskněte tlačítko **Kopírovat**. Otevře se okno pro editaci – přenesené položky lze změnit.

![image-20260628-131442.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20260628-131442.png>)

### Vytvoření nové uživatelské varianty

Tento způsob použijte, pokud v základních variantách požadovaná varianta chybí. Novou variantu vytvoříte stisknutím zeleného tlačítka **+** v části uživatelských variant. Vyžaduje vyplnění všech položek.

![image-20260628-131539.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20260628-131539.png>)

### Jednotlivé položky uživatelské varianty

> [!warning]
> Pokud má být očkovací varianta odesílána do ISIN - očkování proti Covid-19, zaškrtněte checkbox **Odesílat do ISIN**.

![image-20260628-131722.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20260628-131722.png>)
V případě, že je potřeba, aby se informace z této očkovací varianty odesílaly do ISIN, zaškrtne uživatel checkbox Odesílat do ISIN **(1.)**.

V první části okna se vyplňují položky, které jsou společné pro všechny očkovací varianty, ať už se odesílají do ISIN, či nikoliv. Specifikují, jakým způsobem se bude dané očkování vykazovat pojišťovně.
Položka název **(2.)** definuje, pod jakým názvem se uživateli bude očkovací varianta nabízet. Záleží tak na uživateli, zda si chce vytvořit jednu obecnou variantu pro každou očkovací látku, např. Hradí stát – ISIN, kterou bude při každém očkování pacienta měnit, nebo zda vytvoří více očkovacích variant pro nejčastější indikace, které zohlední v názvu očkovací varianty.
V druhé části okna **(3.)**je nutné vyplnit informace, které se odesílají do ISIN. Pole očkovací látka a typ očkování je nutné vyplnit.

Další pole (indikace, jiná indikace, aplikační cesta, místo aplikace) uživatel může vyplnit, aby se mu tyto možnosti při zadávání očkování nabízely, ale zároveň bude možné při zadání očkování hodnoty těchto polí změnit.

![image-20260628-133321.png](<../../../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/Nadstandardní modul ISIN – odesílání a nahlížení očkování/Výchozí nastavení modulu ISIN – odesílání a nahlížení očkování/assets/image-20260628-133321.png>)
> [!info]
> Jakmile je očkovací varianta použita pro zadání očkování konkrétnímu pacientovi, všechna pole přestanou být editovatelná. Pokud je nutné variantu změnit, je třeba ji deaktivovat a vytvořit novou.
