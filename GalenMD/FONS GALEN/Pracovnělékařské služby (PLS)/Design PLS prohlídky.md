---
title: "Design PLS prohlídky"
version: 1
updated_at: 2025-06-26
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/56918054
---

Modulu Designér lze vytvářet uživatelské PLS prohlídky. Cesta: Design -> okno Prohlídky -> záložka PLS -> Tlačítko +

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-140330.png]]
**Ovlivňuje lhůtu**

Má vliv na výpočet lhůty, a tedy tato hodnota přímo ovlivňuje datum následující prohlídky (přesný popis je v kapitole 7 – Výpočet lhůty) může získat 5 stavů

o Hodnota null (bez určení) – chová se stejně jako ne

o Ne

o ano

o Podmíněně – při tomto stavu je povinné pole Název položky

o Vždy

# Záznamy v číselníku vytvořené uživatelem

Uživatelé s rolí *Správce* mají možnost přidávat položky do číselníků vydávaných oficiálními institucemi (např. VZP). Správcem přidané položky budou dostupné pro všechny uživatele v dané společnosti.

## Uživatelské číselníky

Uživatel s rolí Správce má v modulu Číselníky dostupnou záložku Uživatelské číselníky

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-140355.png]]
Zde jsou zpřístupněny oficiální číselníky, do kterých je možné uživatelsky přidávat záznam. V tuto chvíli se jedná o číselníky Výkony a Žadatelé VZP. Číselníky, do kterých je možné vložit záznam uživatelem, jsou zpřístupňovány ze strany správců AIS Galen.

### Přidání nového číselníku

Pokud uživatel potřebuje do zpřístupněných číselníků přidat záznam, je nutné v uživatelských číselnících přidat číselník. Tento postup se aplikuje pouze ve chvíli, kdy uživatel přidává první záznam do daného číselníku. Pokud bude přidávat další položku do stejného číselníku, celý číselník nepřidává, pracuje v již přidaném číselníku.

Přidání nového číselníku:

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-140408.png]]
Z nabídky vybere číselník, do kterého chce přidávat položky.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-140419.png]]
Po přidání číselníku se zobrazí okno přehledu, kam je možné jednotlivé položky přidat.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-140448.png]]

### Přidání položek do číselníku

V detailu číselníku uživatel vyplní jednotlivé řádky – co jedna položka v číselníku, to jeden řádek v přehledu. Toto platí pouze v případě, kdy se hodnoty např. jednoho výkonu v čase nemění. Pokud se v čase mění např. cena výkonu, je nutné přidat nový řádek tak, jak je popsáno v další kapitole.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-140510.png]]
Význam jednotlivých sloupců číselníku je popsán v pravé části obrazovky. Je zde uvedeno, jaký je obsah daného sloupce, zda je povinné jeho vyplnění, maximální délka obsahu a formát obsahu (text/číslo).

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-140521.png]]
Veškeré změny (vytvoření, editace, smazání, deaktivace) se ostatním uživatelům v aplikaci projeví do 15 minut. Konkrétně: Pokud uživatel vytvoří nový řádek v číselníku Výkony, tak tento výkon bude možné v parametrech smluv na pracovišti přidat do 15 minut.

**Důležité: Změna hodnoty položky v číselníku v čase**

Pokud se hodnoty jedné položky číselníku mění v čase, je nutné zadat nový řádek se stejným kódem a jinými hodnotami. Příkladem takové změny může být změna bodové hodnoty výkonu nebo ceny výkonu. V takovém případě je nutné u první položky zadat datum platnosti, přidat nový řádek a u toho vyplnit datum platnosti od:

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-140954.png]]
Není možné původní záznam deaktivovat, nebo přepsat: při přepočtu nevyúčtovaných výkonů by byly změněny hodnoty i tam, kdy platily ty původní.

## Zobrazení položky v číselníku přidané uživatelem

Položka v číselníku přidaná uživatelem má vždy přednost před položkou v oficiálním číselníku. Pokud uživatel do číselníku Výkony přidá výkon, který se následně objeví také v oficiálním číselníku, bude AIS Galen pracovat stále s položkou přidanou uživatelem.

Položky přidané uživatelem mají v číselníku v posledním sloupci Zdroj ikonu informující o uživatelském záznamu:

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-141011.png]]
**Automatické doplnění nákladového střediska na žádance**

Pokud je na společnosti aktivní nadstandardní modul „Nákladová střediska“, je možné na jednotlivých firmách nákladová střediska definovat a ty následně přednastavovat ve formuláři žádanky.

## Přiřazení nákladového střediska na firmě

Uživatel s rolí Správce v modulu Nadstandardní péče -> detail konkrétní firmy -> záložka Nákladová střediska přiřazuje k firmě nákladová střediska.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-141024.png]]
Nákladová střediska jsou třech typů:

1. PLS – indikuje vyšetření v rámci PLS

1. Vstupní prohlídka – indikuje vstupní prohlídku

1. Spalničky – indikuje, že v žádance je požadováno pouze vyšetření spalniček

Ke každé firmě je možné přiřadit více nákladových středisek stejného typu, ale pouze jedno z nich je možné označit příznakem „Primární“.

V detailu firmy uživatel zároveň definuje počet dní před nástupem a po nástupu do zaměstnání, kdy se ještě vystavuje vstupní prohlídka.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-141036.png]]

## Přiřazení alternativního nákladového střediska

Nákladové středisko se v žádance vyplňuje podle pravidel uvedených v následující kapitole. Uživatel má však možnost přednastavit jiné nákladové středisko v kartě zaměstnání pacienta.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Design PLS prohlídky/assets/image-20250626-141053.png]]

## Vyplnění nákladového střediska v žádance

V žádance se automaticky vyplňuje pole Nákladové středisko dle následujících pravidel:

1. Pokud je zaškrtnut pouze konkrétní NČLP kód v žádance (Morbilli (Spalničky) (IgG)), tak se automaticky vyplní nákladové středisko s příznakem "spalničky", které je nastavené u daného zaměstnavatele (Nadstandardní péče – detail firmy). Pokud daný zaměstnavatel nebude mít definovanou položku s příznakem "Spalničky NS", pokračuje krokem 2). Vyplňuje se NS s příznakem spalničky a příznakem primární. Pokud neexistuje příznak primární a existuje právě jedno „spalničky“, vyplní se toto.

1. Pokud má pacient v kartě zaměstnání vyplněné pole „Alternativní nákladové středisko“, doplní se automaticky tato hodnota.

1. Pokud má zadané datum začátku zaměstnání, které odpovídá intervalu definovaným správcem na firmě na počet dní před a počet dní po nástupu do, pak se automaticky v žádance vyplní nákladové středisko s příznakem "Vstupní prohlídka NS" a příznakem primární. Pokud neexistuje příznak primární a existuje právě jedno vstupní, vyplní se toto. Jinak: se automaticky vyplní nákladové středisko s příznakem "PLS NS" a „primární“, Pokud neexistuje příznak primární a existuje právě jedno „PLS NS“, vyplní se toto.
