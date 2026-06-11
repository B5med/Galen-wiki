---
id: 54427649
title: "Notifikace objednávek"
version: 4
updated_at: 2026-04-13T07:39:42.181Z
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/54427649
---

# Notifikace objednávek

none

Pacienta je možné notifikovat o vytvoření a smazání objednávky, také je možné nastavit x dní před samotnou objednávkou automatické připomenutí. Notifikace je možné zasílat prostřednictvím SMS, e-mailu, nebo oboje.

## **Objednávky a notifikace**

1. Objednávku v kalendáři – jedná se o objednávku, která má vazbu na konkrétního pacienta v kartotéce

2. Záznam v kalendáři – jedná se o objednávku, která nemá vazbu na konkrétního pacienta v kartotéce

Na objednávku nebo na záznam v kalendáři je možné nastavit tři typy notifikací:

1. Upozornění – zpráva přijde pacientovi ihned po vytvoření objednávky/záznamu v kalendáři, nebo po změně objednávky/ záznamu v kalendáři

2. Zrušení - zpráva přijde pacientovi ihned po smazání objednávky/záznamu v kalendáři

3. Připomenutí – zpráva přijde pacientovi definovaný počet dní před datem objednávky/záznamu v kalendáři. Zprávy se generují a odesílají hromadně jednou denně.

## **Nastavení šablony notifikace**

Aby bylo možné odeslat notifikaci, je nutné na objednávku nebo na záznam v kalendáři a na každý druh notifikace vytvořit šablonu. Celkem se tedy jedná o 6 druhů notifikací. Pokud je potřeba odesílat notifikace jak skrze SMS, tak e-mailem, bude potřeba nastavit celkem 12 druhů notifikací.

Šablony se nastavují v modulu Správce -> Nástroje ->  Šablony -> Notifikace

V šabloně je možné definovat text a zároveň proměnné položky

Šablonu je možné definovat obecně pro všechny pacienty, nebo rozlišovat dle pohlaví pacienta. V tom případě je nutné nastavit šablonu pro muže, ženy a pro pacienty, kteří neuvedli pohlaví.

## **Použití šablony v nastavení kalendáře**

V nastavení kalendáře (Správce -> Správa organizace -> Agendy -> Kalendáře -> Nastavení -> Notifikace a připomínání) je možné u každého kalendáře nastavit, aby se určitý druh notifikace odesílal.

V horní polovině okna (A) se nastavují notifikace týkající se objednávky (tj. záznam v kalendáři s vazbou na konkrétního pacienta v kartotéce).

Ve spodní polovině okna (B) se nastavují notifikace týkající se záznamu v kalendáři (tj. záznam v kalendáři bez vazby na pacienta v kartotéce).

Pro každý druh notifikace se nastavuje šablona pro komunikaci e-mailem (C) a SMS (D).

Pro připomínání (E) je možné nastavit až n zpráv jak pro SMS, tak e-maily.

U každé šablony je možné nastavit stav Odesílat, Neodesílat, Zakázat:

- **Odesílat** = při založení objednávky bude odesílání této šablony defaultně zaškrtnuto

- **Neodesílat** = při založení této objednávky bude odesílání této šablony defaultně vypnuto, uživatel může odesílání aktivovat

- **Zakázat** = tento typ šablony se nebude při vytvoření objednávky nabízet, tento typ notifikace nebude možné aktivovat

Výchozí nastavení se takto promítne při do nastavení při vytvoření objednávky.

SMS upozornění na objednávku úplně chybí, protože je nastaveno na „zakázat“.

SMS zrušená objednávka není aktivní, protože je nastaveno na „neodesílat“.

SMS připomenutí objednávky je aktivní, protože je nastaveno „odesílat“.

## **Použití šablony v nastavení ordinačních hodin**

Nastavené notifikace je možné používat stejně pro všechny objednávky v daném kalendáři, nebo je možné nastavit na vybrané ordinační doby jiné notifikace. Tento postup se používá např. ve chvíli, kdy má být připomenutí na objednávky na úterý, středu, čtvrtek a na pátek odesláno den předem, ale upozornění na objednávku na pondělí má být odesláno už v pátek.

Na každé ordinační době je defaultně přeneseno nastavení notifikací z kalendáře.

Nastavení kalendáře -> dvojklik na konkrétní ordinační dobu -> Notifikace a připomínání

Toto nastavení je možné změnit pouze pro daný konkrétní blok ordinačních hodin.
