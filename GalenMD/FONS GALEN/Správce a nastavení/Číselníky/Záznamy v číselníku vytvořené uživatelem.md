---
title: "Záznamy v číselníku vytvořené uživatelem"
version: 3
updated_at: 2025-07-21
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/60915714
---

Uživatelé s rolí *Správce* mají možnost přidávat položky do číselníků vydávaných oficiálními institucemi (např. VZP). Správcem přidané položky budou dostupné pro všechny uživatele v dané společnosti.

## **Uživatelské číselníky**

![[pages/FONS GALEN/Správce a nastavení/Číselníky/Záznamy v číselníku vytvořené uživatelem/assets/image-20250701-081525.png]]
Uživatel s rolí Správce má v modulu Číselníky dostupnou záložku Uživatelské číselníky.

## **Přidání nového číselníku**

Pokud uživatel potřebuje do zpřístupněných číselníků přidat záznam, je nutné v uživatelských číselnících přidat číselník. Tento postup se aplikuje pouze ve chvíli, kdy uživatel přidává první záznam do daného číselníku. Pokud bude přidávat další položku do stejného číselníku, celý číselník nepřidává, pracuje v již přidaném číselníku.

Přidání nového číselníku:

![[pages/FONS GALEN/Správce a nastavení/Číselníky/Záznamy v číselníku vytvořené uživatelem/assets/image-20250701-081835.png]]
Z nabídky vybere číselník, do kterého chce přidávat položky.

![[pages/FONS GALEN/Správce a nastavení/Číselníky/Záznamy v číselníku vytvořené uživatelem/assets/image-20250701-081856.png]]
Po přidání číselníku se zobrazí okno přehledu, kam je možné jednotlivé položky přidat.

![[pages/FONS GALEN/Správce a nastavení/Číselníky/Záznamy v číselníku vytvořené uživatelem/assets/image-20250701-081919.png]]

## **Přidání položek do číselníku**

V detailu číselníku uživatel vyplní jednotlivé řádky – co jedna položka v číselníku, to jeden řádek v přehledu. Toto platí pouze v případě, kdy se hodnoty např. jednoho výkonu v čase nemění. Pokud se v čase mění např. cena výkonu, je nutné přidat nový řádek tak, jak je popsáno v další kapitole.

![[pages/FONS GALEN/Správce a nastavení/Číselníky/Záznamy v číselníku vytvořené uživatelem/assets/image-20250701-081945.png]]
Význam jednotlivých sloupců číselníku je popsán v pravé části obrazovky. Je zde uvedeno, jaký je obsah daného sloupce, zda je povinné jeho vyplnění, maximální délka obsahu a formát obsahu (text/číslo).

![[pages/FONS GALEN/Správce a nastavení/Číselníky/Záznamy v číselníku vytvořené uživatelem/assets/image-20250701-082044.png]]

Veškeré změny (vytvoření, editace, smazání, deaktivace) se ostatním uživatelům v aplikaci projeví do 15 minut. Konkrétně: Pokud uživatel vytvoří nový řádek v číselníku Výkony, tak tento výkon bude možné v parametrech smluv na pracovišti přidat do 15 minut.

**Důležité: Změna hodnoty položky v číselníku v čase**

Pokud se hodnoty jedné položky číselníku mění v čase, je nutné zadat nový řádek se stejným kódem a jinými hodnotami. Příkladem takové změny může být změna bodové hodnoty výkonu nebo ceny výkonu. V takovém případě je nutné u první položky zadat datum platnosti, přidat nový řádek a u toho vyplnit datum platnosti od:

![[pages/FONS GALEN/Správce a nastavení/Číselníky/Záznamy v číselníku vytvořené uživatelem/assets/image-20250701-082112.png]]
Není možné původní záznam deaktivovat, nebo přepsat: při přepočtu nevyúčtovaných výkonů by byly změněny hodnoty i tam, kdy platily ty původní.

## **Zobrazení položky v číselníku přidané uživatelem**

Položka v číselníku přidaná uživatelem má vždy přednost před položkou v oficiálním číselníku. Pokud uživatel do číselníku Výkony přidá výkon, který se následně objeví také v oficiálním číselníku, bude AIS Galen pracovat stále s položkou přidanou uživatelem.

Položky přidané uživatelem mají v číselníku v posledním sloupci Zdroj ikonu informující o uživatelském záznamu:

![[pages/FONS GALEN/Správce a nastavení/Číselníky/Záznamy v číselníku vytvořené uživatelem/assets/image-20250701-082153.png]]
