---
title: "Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)"
version: 1
updated_at: 2025-08-26
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/104824874
---

# Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)

Popis procesu odeslání očkování do ISINv2. Jedná se o všechna očkování kromě očkování proti covid-19, která se původně odesílala do SÚKL.

## Výchozí nastavení

Pro odeslání informací o očkování do ISIN je nutné

- Mít na společnosti aktivní nadstandardní modul Odesílání očkování do ISINv2
- Mít na pracovišti nastavený **platný certifikát SÚKL** (stejný, který se využívá pro odeslání eReceptu a eNeschopenky). Případně na společnosti

![[pages/FONS GALEN/Medikace, očkování a registry/Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)/assets/image-20250826-115234.png]]
- Mít na pracovišti vyplněné **PČZ (pořadové číslo zařízení).**Tento údaj je možné získat [zde](https://nrpzs.uzis.cz/) (detail v záložce Detailní záznamy ÚZIS ČR)

![[pages/FONS GALEN/Medikace, očkování a registry/Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)/assets/image-20250826-115254.png]]
- Mít na uživateli vyplněné pole „**NRZP**“

Číselník Národního registru zdravotnických pracovníků lze stáhnout v modulu Nástroje -> ISIN -> Registr zdravotnických pracovníků

Po stažení certifikátu uživatel s rolí Správce přiřadí položku z číselníku v detailu uživatele Správa organizace -> Uživatelé

![[pages/FONS GALEN/Medikace, očkování a registry/Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)/assets/image-20250826-115315.png]]
Poznámka: pro odeslání očkování není nutné vyplňovat podpisový certifikát. Očkování do ISINv2 tedy odesílá z FONS Galen každý zdravotnický pracovník, který očkování ukládá.

- Mít **stažené potřebné číselníky v modulu Nástroje -> ISIN**. Konkrétně se jedná o číselníky:

1. Očkovací látky (Ostatní očkování)
2. Pojišťovny
3. Typy vakcinancí

## Odeslání očkování

Záznamy o všech provedených očkování je dle legislativy povinné odeslat do ISIN. V rámci FONS Galen budou do ISIN odeslána očkování, u kterých není zaškrtnuto „bez schématu“ nebo „doplnit bez vykázání výkonu“.

V případě, že uživatel zaškrtne „bez schématu“ nebo „doplnit bez vykázání výkonu“, bude upozorněn, že takové očkování nebude možné ani v budoucnu do ISIN odeslat.

Údaje odesílané do ISIN se uživateli zobrazují v okně výběru očk. varianty:

![[pages/FONS GALEN/Medikace, očkování a registry/Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)/assets/image-20250826-115417.png]]
Údaje se automaticky předvyplní na základě vybrané

- Očkovací látky

- Pořadí dávky/přeočkování ve schématu očkování

- Očkovací varianty

**Poznámka**: Pole Pojišťovna se automaticky vyplňuje na základě toho, kdo platí očkovací variantu. Nemusí tedy odpovídat stavu pojištění pacienta. Např. Pacient je pojištěn u poj 111, ale aplikuje se očkování, které hradí pacient. Tím pádem se do pole pojišťovna uvádí „samoplátce“.

Pro odeslání očkování je nutné, aby měl pacient vyplněn RID (resortní identifikátor). Pokud se tento nepodaří získat, očkování bude možné v rámci FONS Galen uložit, ale očkování nebude možné odeslat.

Stiskem tl. Očkovat se očkování zároveň odesílá do ISIN.

Úspěšně odeslané očkování má v přehledu stav Přijato

![[pages/FONS GALEN/Medikace, očkování a registry/Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)/assets/image-20250826-115447.png]]

## Editace očkování

V případě potřeba editace již odeslaného očkování je možné zobrazit detail očkování. Zde je ale možné editovat pouze pole Poznámka, ostatní položky jsou vyplněny na základě výběru výše uvedených položek.

![[pages/FONS GALEN/Medikace, očkování a registry/Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)/assets/image-20250826-115512.png]]
Pokud je nutné změnit pole „očkovací látka“, „typ vakcinace“ nebo „pojišťovna“, pak je nutné celé očkování smazat a zadat znovu.

## Smazání očkování

V případě smazání očkování v rámci FONS Galen, které bylo úspěšně odesláno do ISIN, bude požadavek na smazání zároveň odeslán do ISIN.

## Neodeslaná očkování

Modul Dashboard poskytuje přehled očkování, která byl měla být od eOčkování odeslána, ale nebyla. Očkování může odeslat pouze ten odpovědný lékař, který očkování do FONs Galen zadal, nebo uživatel, který není odpovědným lékařem.

Z dashboardu se uživatel dostane na detail konkrétního neodeslaného očkování.

![[pages/FONS GALEN/Medikace, očkování a registry/Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)/assets/image-20250826-115559.png]]
![[pages/FONS GALEN/Medikace, očkování a registry/Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)/assets/image-20250826-115611.png]]

## Poznámka k modulu eOčkování

Modul eOčkování (k dispozici v horní liště nebo v záložce modulu Očkování) zobrazuje informace, které jsou poskytovány ze strany SÚKL. Tam se původně záznamy o očkování odesílaly. Po změně legislativy se záznamy odesílají do ISIN, ale správcem poskytující informace o provedených očkování je stále SÚKL. Propojení mezi SÚKL a ISIN není v tuto chvíli realizované, a proto očkování odeslaná z FONS Galen do ISIN, nebudou v tuto chvíli v modulu eOčkování viditelná.

![[pages/FONS GALEN/Medikace, očkování a registry/Odeslání očkování do ISINv2 (ostatní očkování, původně SÚKL)/assets/image-20250826-115637.png]]
