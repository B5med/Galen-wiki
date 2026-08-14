---
title: "ePoukaz – změny platné od 1. 9. 2026"
version: 1
updated_at: 2026-08-13
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/542146561
---

# ePoukaz – změny platné od 1. 9. 2026

Tento dokument shrnuje všechny změny v systému ePoukaz, které vstupují v platnost od 1. 9. 2026. Cílem je poskytnout přehlednou a srozumitelnou informaci o úpravách funkcí, nových polích a doplněných možnostech tak, aby uživatelé mohli systém používat efektivně a v souladu s aktuální legislativou SÚKL.

## Párový orgán u ePoukazu – léčebný, foniatrický a optický

U ePoukazu pro léčebné, foniatrické a optické pomůcky je nově k dispozici pole **„Párový orgán“** s možnostmi **Pravý / Levý / Oba**. Slouží k upřesnění, zda je předepisovaný zdravotnický prostředek určen pro pravou, levou, nebo obě strany párové tělesné části pacienta – typicky například u pooperační nebo odlehčovací obuvi (pro jednu nohu, nebo pro obě), u pomůcek pro koleno, nebo u sluchadel (pro jedno ucho, nebo pro obě).

Pole najdete přímo ve formuláři daného typu poukazu (léčebný/foniatrický/optický) – vyplňuje se jednou za celý poukaz, ne zvlášť pro každou položku v seznamu. U pole je k dispozici nápovědná ikonka s vysvětlením: „Vyplňte, pokud je zdravotnický prostředek určen pro pravou, levou, nebo obě strany párové tělesné části (např. koleno, ucho).“ Vyplnění je dobrovolné – pokud párový orgán u dané pomůcky není potřeba rozlišovat, pole jednoduše necháte prázdné a na vystavení ani odeslání poukazu to nemá žádný vliv. Vyplněná hodnota se odesílá i načítá spolu s ostatními údaji poukazu.

## Šířka a hloubka sedu invalidního vozíku

Na ePoukazu – léčebný přibyla u vozíků dvě nová pole: **„Šířka sedu (cm)“** a **„Hloubka sedu (cm)“**. Týkají se úhradových skupin 07.01.01.* a 07.01.02.* (mechanické a elektrické vozíky) a zadávají se v centimetrech, včetně jednomístných desetinných hodnot (např. 42,5 cm).

Jakmile do poukazu vyberete položku z těchto úhradových skupin, pole se automaticky zobrazí pod tabulkou položek. Na rozdíl od párového orgánu jsou tato pole **povinná** – pokud u relevantní pomůcky šířku a hloubku sedu nevyplníte, tlačítko „Odeslat“ zůstane zašedlé a po najetí myší se zobrazí nápověda, které pole ještě chybí doplnit (např. „Vyplňte prosím Šířka sedu (cm)“). Poukaz tedy nelze odeslat bez těchto údajů.

## Ověření množstevního a úhradového limitu

U položky ePoukazu je nově k dispozici tlačítko **„Ověřit limity“**, umístěné vedle tlačítka pro odebrání položky. Slouží k rychlému ověření, zda vydávané množství nebo výše úhrady zdravotnického prostředku nepřekračuje limit stanovený pro dané období – systém se v takovém případě přímo dotáže SÚKL a zobrazí odpověď.

Aby bylo možné limit ověřit, musí být na položce vyplněné alespoň číslo pojištěnce, datum narození pacienta, SÚKL kód a množství – pokud některý z těchto údajů chybí, je tlačítko neaktivní a po najetí myší se zobrazí nápověda s konkrétním výčtem toho, co je potřeba doplnit (např. „Pro ověření limitu je nutné mít vyplněné: SÚKL kód, Množství.“). Po úspěšném ověření systém zobrazí buď informaci, že limit není překročen, nebo – v případě jeho překročení – chybovou zprávu s popisem a doporučením a přehled předchozích výdejů, které se do limitu započítávají. Jde čistě o informativní dotaz – žádná data se při tomto ověření na naší straně neukládají.
