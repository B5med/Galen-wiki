---
title: "Import PLS"
version: 1
updated_at: 2025-06-26
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/57180205
---

# Import PLS

V rámci importu PLS lze importovat PLS smlouvy, PLS skupiny a importovat samotné pacienty. Všechny importy se nacházejí v okně s detailem firmy.

![image-20250626-135312.png](<../../../pages/FONS GALEN/Pracovnělékařské služby (PLS)/Import PLS/assets/image-20250626-135312.png>)

### Založení a import dat smlouvy PLS do LS Galen

Cílem této definice je zpracování obecného a universálního skriptu pro založení smlouvy a import nezbytného rozsahu dat pro zajištění pracovně-lékařských či obdobných služeb smluvnímu partnerovi prostřednictvím lékařského systému Galen.

Pojmy:

**smlouva** – soubor všech parametrů, atributů a sjednaných podmínek pro úplné a správné nastavení zpracování agendy PLS ve vztahu ke konkrétnímu smluvnímu partnerovi

**firma** – název a soubor základní údajů k právní entitě, ke které se vztahuje další nastavení (pobočky, smlouvy, skupiny PLS/pozice)

**pobočka** – entita v rámci firmy, na kterou je zavedena konkrétní smlouva; jedna smlouva resp. soubor parametrů smlouvy může být shodný pro všechny pobočky

**datum importu – datum**, ke kterému je spuštěn administrátorem import

**datum smlouvy-**"platnost od“ tzn. datum, od kterého nastává platnost údajů nově importované smlouvy

**Vzniknou 2 typy importů**.

1. založení Skupiny PLS – pozice a hodnosti

2. založení parametrů smlouvy

**Obecné předpoklady**

Samotnému importu smlouvy vždy předchází založení firmy a poboček administrátorem LSG. V prvním kroku je vždy importován přehled skupin PLS, pak teprve následuje import smlouvy. Povinností administrátora je zajistit správnost a úplnost údajů k firmě a pobočce.

Import / založení skupiny PLS– principy a předpoklady

**Založení položky**

Tlačítko import pod danou firmou ale importujeme na jednotlivou pobočku, formát .csv

Import zakládá položku skupiny PLS tzn. pozice (hodnosti ne). Pakliže systém najde shodu stávajícího údaje s položkou importu – ponechá původní, nová položka není založena. Ověření probíhá dle názvu tzn. vazba import x systém = „název skupiny PLS (pozice). V případě, že shoda názvu není nalezena. Založí položku z importu a doplní tak seznam s názvem položky tak, jak je uveden v importním souboru

**Atributy položky – rizika**

V rámci importu je možné založit či upravit atributy skupiny PLS v rozsahu „Kategorie“ (K), „Faktor prostředí“ (FP) a „Ohrožení zdraví“ (OZ). Názvy rizik v importe se musí shodovat s názvy rizik v systému. V případě shody položky, systém „od-označí rizika a faktory a zapíše nově dle CSV. Pokud není shoda (položka dle názvu nenalezena), systém založí novou skupinu PLS (pozici) a k ní kombinaci rizik a faktorů dle CSV. Při ověření dat importu ignorovat diakritiku a velká/malá písmena.

Riziko (kategorie) je povinný údaj (vycházíme z nastavení GUI systému); údaje FP a OZ nepovinné.

V GUI při vytváření Skupiny PLS kategorie není povinná.

K dané pozici v importu bude n řádků s ohledem na počet záznamů k riziku, co řádek, to záznam o riziku k dané pozici (viz vzor xls). Pokud není nalezena shoda u faktorů rizika tzn. u K, FP a OZ systém vrací hlášení o chybě. Chybová hláška totožná s hláškou u importu zaměstnanců (souřadnice importu)
