---
id: 56885286
title: "PLS prohlídky"
version: 1
updated_at: 2025-06-26T13:57:40.890Z
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/56885286
---

# PLS prohlídky

PLS prohlídku lze založit v okně Prohlídky a vyšetření, po kliku na ikonu

 a výběru PLS prohlídky, která je přiřazena firmě.

Při **vytváření PLS prohlídky** se zobrazují všechny prohlídky definované na smlouvě (i ty které jsou jen v rozšiřujících položkách, musí však být ve stejné skupině PLS jako je pacient na kartě zaměstnání zařazen), plus musí být tyto prohlídky zařazeny do sortimentu skupiny Prohlídka  
o Pokud je prohlídka na smlouvě vícekrát, zobrazí se tento počet i ve výběru

 Pokud je **pacient s PLS prohlídkou objednán v kalendáři**, při PLS prohlídce se zobrazí ikona s hodinami).

 o Při vytvoření takové prohlídky se automaticky dotáhnou všechny položky přidané na prohlídku během vytváření PLS objednávky.

 o Dotáhne se i reference pracoviště, na které byly položky objednány. Neplatí však na hlavní položku, ta má stále referenci pracoviště, na kterém je prohlídka vytvářena.

 o Ikona s hodinami zmizí, pokud byla vytvořena prohlídka s touto ikonou, (nesmí existovat jiná objednávka na téže prohlídce u pacienta) nebo je tato objednávka z kalendáře odstraněna.

## PLS prohlídka

**Datum návštěvy** na prohlídce nemůže být v budoucnosti. Datum příští prohlídky nemůže být větší než datum návštěvy. Nelze uzavřít žádné položky prohlídky do období, kde již existuje vystavená výkonová faktura. Nelze uzavřít hlavní položku smlouvy s datem menším než začátek prohlídky. Hlavní položka musí být uzavřena jako poslední, a to i pořadím i datumově.

Do prohlídky **lze přidat nové položky –** ze smlouvy. Nemusí být ze stejné PLS skupiny (nezobrazuje se). Pokud jsou dvě položky shodné na základě kódu sortimentu, ceny bez DPH a DPH, nezobrazují se duplicitně. Musí být hlavní položky Musí vyhovovat filtru věku a pohlaví na zadaného na položce. Navázaný sortiment na položku musí být aktivní a nesmí být ze sortimentu prohlídky nebo služby ze sortimentu. Defaultně jsou zobrazeny položky bez zařazení kategorie.

Po rozdělení položek do kategorií, **lze přidávat i výkony.** Ceny v tomto seznamu jsou dotaženy podle cen nastavených sortimentu. Po zaplacení v hotovosti se ikoně s penězi objeví zelené potvrzení („fajfka“). Je možné zaplatit za položky i jednotlivě pomocí tlačítka „**Platba** výběr“, které bude zobrazeno po označení jedné, případně více položek pomocí klávesových zkratek CTRL + C/SHIFT. Následně má možnost uživatel zvolit, zda byla platba provedena kartou nebo hotovostí. Při zvolení s možností vytvoření dokladu se zobrazí po zaplacení tisk s příjmovým dokladem. Při zvolení možnosti nevytvořit pokladní doklad.

Prohlídku **lze přiřadit jiné ordinaci** pomocí tlačítka s ikonou lékaře (vedle tlačítka uzavřít). Po výběru ordinace, se nabídnou kalendáře navázané na toto IČP a můžeme do kalendáře vytvořit objednávku s přiřazením na danou PLS prohlídku a položku smlouvy.

V případě prohlídky, která podmíněně ovlivňuje lhůtu (zkratka PPOL), je na prohlídce zobrazen **DUVOD** s možnostmi výběru hodnot:

o Zdravotní důvod

o Jiný důvod
