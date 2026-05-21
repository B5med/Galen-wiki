---
title: "Modul sklad"
version: 3
updated_at: 2025-12-05
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/48136251
---

# Modul sklad

## Sklad

Modul Sklad je určen pro evidenci vakcín. Při očkování automaticky odepisuje vybranou vakcínu, do záznamu o očkování doplňuje šarži a datum expirace.

Nejdříve je však nutné vyplnit skladovou kartu této očkovací látky.

![image-20250618-105509.png](<../pages/Modul sklad/assets/image-20250618-105509.png>)
Pro přidání nové očkovací látky je třeba kliknout na zelené plus. Objeví se formulář pro zadání očkovací látky:

![image-20250618-105527.png](<../pages/Modul sklad/assets/image-20250618-105527.png>)
![image-20250618-105612.png](<../pages/Modul sklad/assets/image-20250618-105612.png>)

Očkovací látku lze vybrat ze seznamu, který se otevře po kliknutí do žlutého políčka. Ještě je nutné zadat počet dávek v balení a min. počet dávek. Tento počet udává, kdy má začít program upozorňovat, že je na skladě málo očkovací látky.

Poté, co je založená karta očkovací látky, je možné zadávat její jednotlivá balení kliknutím na tlačítko „Naskladnit – nová šarže“. Objeví se okno pro zadávání nového balení očkovací látky. Je nutné vyplnit kód SÚKL, šarži očkovací látky, typ, datum expirace (popř. upravit datum naskladnění) a počet balení.

![image-20250618-105630.png](<../pages/Modul sklad/assets/image-20250618-105630.png>)
> [!info]
> Typ
>
> **Volný prodej**jsou očkovací látky, které nespadají do povinného očkování. Jedná se o volitelné očkování, které ale může pojišťovna plně nebo částečně hradit.
>
> **Látky hrazení státem (clearingové centrum)** zahrnuje očkovací látky, které metodika označuje jako povinné, resp. pravidelné očkování.
>
> **Zvláštní látky** zahrnují očkování proti hepatitidě A, hepatitidě B, proti vzteklině a proti Covid-19 tak je je specifikuje *Vyhláška o očkování proti infekčním nemocem*
>
> č. 537/2006 Sb., konkrétně §9, §10 a §11.

V případě, že není naskladňován celý balíček očkovací látky, je možné zadat i jiný počet dávek, než jsou v originálním balení. Políčko typ udává, zda je očkovací látka vykazována standardně na pojišťovnu nebo je hrazena mandatorně (státem). V případě, že se lékař překlepne v šarži látky nebo udělá nějakou jinou chybu, je možné očkovací látku smazat tlačítkem „Smazat nepoužitou šarži“. Toto tlačítko bude neaktivní ve chvíli, kdy již nějaká vakcína této šarže byla aplikována. Pokud bude třeba naskladnit další vakcíny stejné šarže, stačí kliknout na tlačítko „Naskladnit“ vedle názvu šarže. Naopak, pokud bude třeba z nějakého důvodu (např. prošlá expirace, rozbitá lednice,…) odstranit ze skladu vakcíny nějaké šarže, je třeba kliknout na tlačítko „Vyskladnit“. Toto tlačítko slouží k hromadnému vyskladnění očkovací látky. Po aplikaci očkovací látky pacientovi a zadání očkování do programu je příslušná vakcína rovnou ze skladu odepsána. Při kliknutí na danou šarži je vidět pohyb na její skladové kartě.

**Pozn. Aby bylo možné využívat sklad, je nutné ho mít povolen u uživatele v Organizační struktuře a nadefinován na pracovišti.**

## **Příklad naskladnění Tetavaxu:**

- jako látku hrazenou státem

- jako látku na volný prodej

![image-20250618-105717.png](<../pages/Modul sklad/assets/image-20250618-105717.png>)
![image-20250618-105822.png](<../pages/Modul sklad/assets/image-20250618-105822.png>)
![image-20250618-105911.png](<../pages/Modul sklad/assets/image-20250618-105911.png>)

Máme-li naskladněnou očkovací látku na skladové kartě, lze s použitím této očkovací látky očkovat pacienty v kartotéce ve funkcionalitě Očkování na dolní modré liště. Během zadávání konkrétního očkování do záznamu pacienta se nabízí očkovací látka s označením počtu dávek naskladněné očkovací látky. Po dokončení evidence očkování pacienta v IS Galen se použitá dávka očkovací látky automaticky ze skladové karty odečte. Pokud lékař očkování u pacienta z nějakého důvodu smaže, očkovací látka se opět na skladovou kartu vrátí.

![image-20250618-105959.png](<../pages/Modul sklad/assets/image-20250618-105959.png>)
