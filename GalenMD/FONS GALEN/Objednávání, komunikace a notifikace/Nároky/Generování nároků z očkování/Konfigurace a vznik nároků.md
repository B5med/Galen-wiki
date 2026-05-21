---
title: "Konfigurace a vznik nároků"
version: 1
updated_at: 2025-07-10
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/68419606
---

Konfigurace se nachází pod správcovským účtem v module Nároky, v okně Očkování.

Zdravotník tuto konfigurací vidí jenom jako náhled, nemůže ji upravovat.

Základnou konfigurací pro nároky z očkování je konfigurace onemocnění, kde si správce určí, pro jaké onemocnění se nároky budou vytvářet. V rámci onemocnění lze následně konfigurovat, pro jaký věk pacienta a jakou odbornost se budou vytvářet. Těchhle konfigurací v rámci onemocnění může být vícero.

Příklad: Správce si nastaví, že nároky z očkování se budou vytvářet jenom v rámci onemocnění Chřipka. V rámci onemocnění dále nastaví, aby se nároky vytvářeli jenom dětem od 4 do 14 let pro odbornost 002 a dále pro seniory od 65 let.

V rámci generování nároků lze taky na úrovni onemocnění nastavit, aby se nárok generoval jenom po zočkovaní.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Generování nároků z očkování/Konfigurace a vznik nároků/assets/image-20250710-124601.png]]
- Jakmile jsou na onemocnění vytvořené nároky, definici onemocnění nelze smazat, lze pouze zneaktivnit.

o Při zneaktivnění definice onemocnění se všechny aktívní nebo budoucí nároky převedou do stavu pozastavený, kde při opětovném zaktivnění onemocnění se tyhle nároky znovu zaktivní, v případě že budou stále spadat do věkových intervalů na onemocnění.

- Věkové intervaly na onemocnění lze upravovat bez následků na aktivní nároky, avšak platí podmínka, že intervaly se nesmí přetínat.

## Vznik nároku

Nárokymohou vznikat po očkovaní pacienta, automatickou kontrolou věku, při registraci nebo ručním vygenerováním. Každý vznik nároku se váže na konfiguraci viz předešlá kapitola.

### Vznik nároku po očkovaní pacienta

Nový nárok na očkovaní vznikne v případě naočkovaní pacienta očkovací látkou, která spadá pod aktivní definici onemocnění (očkovací látky definice je vidět při konfiguraci definice onemocnění), zároveň věk pacienta odpovídá věkovému intervalu v definici a na očkování je zadán datum příštího očkování. Protože datum příštího očkování musí být v budoucnosti, takto vzniklý nárok je vždy budoucí.

### Vznik nároku automatickou kontrolou věku

Systém automaticky 1x v noci kontroluje registrované pacienty, které spadají do věkového intervalu jedné z aktivních definic**í** onemocnění. Pokud ano, vytvoří se jim aktivní nárok.

### Vznik nároku při registraci

Při registraci nejdříve proběhne kontrola, jestli pacient nemá pozastavené nároky (například při od-registraci pacienta, nebo zneaktivnění definice onemocnění), následně proběhne kontrola, jestli pacient nebyl naočkovaný (kontrola očkovaní napříč společností) během doby, kdy nebyl registrován a nakonec proběhne kontrola věku pacienta v době registrace, kde se vše porovnává s věkovými intervaly na aktivních definicích onemocnění.

### Vznik nároku ručním vygenerováním

Administrátor má možnost po nakonfigurovaní nebo změně definice onemocnění spustit algoritmus na generaci nároků. Algoritmus a jeho podmínky je stejný jako při registraci.

## Smazání nároku

Uživatel s rolí Správce může ručně smazat nároky nad zvolenou definici. Pro smazání nároků nad očkování platí stejný postup jako pro smazání nároků z vyšetření.

## Realizace nároku

Standardní cesta jak realizovat nárok je po naočkovaní pacienta. Nárok změní stav na realizovaný v případě, že má aktuálně nárok ve stavu aktivní nebo budoucí a očkovací látka kterou byl naočkován spadala pod onemocnění, z kterého byli aktuální nároky pacienta vygenerovány.

Nárok lze realizovat taky jako administrátor v module Nároky. Administrátor pro realizaci zvoleného nároku, musí tuhle realizaci přiradit reálnému očkování pacienta.

## Exspirace nároku

Nárok z očkování exspiruje v případě, že jeho platnost do vyprší. Platnost do se u nároků z očkovaní doplní v případě naočkovaní pacienta pomocí předvolených schémat, a to v případě, že očkovací schéma obsahuje následnou dávku, jejíž platnost je časově omezená nebo když je interval definice onemocnění omezen taky věkem do.

## Základní omezení při práci s nároky z onemocnění

- Nárok může vzniknout jen registrovanému pacientovi.

- Pacient může mít v jednu chvíli jen 1 nárok ve stavu aktivní nebo budoucí v rámci 1 onemocnění.

- Nároky se vztahují na ordinaci (IČP).
