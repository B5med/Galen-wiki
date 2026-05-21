---
title: "Výdej foniatrické pomůcky předepsané na ePoukaz"
version: 10
updated_at: 2026-02-10
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/247857153
---

> [!info]
> Výdej foniatrických pomůcek je součástí modulu **ePoukaz – předpis**. Abyste mohli tyto pomůcky vydávat, je proto nutné mít modul ePoukaz – předpis aktivní.
>
> Ve FONS Galen lze vydat pouze tu foniatrickou pomůcku, která byla předepsána ePoukazem vystaveným pro stejnou společnost ve FONS Galen.
>
> Při výdeji se automaticky odešle informace o vydání do systému SÚKL a zároveň se vydaná pomůcka připraví pro následné vyúčtování.

## Prerekvizity

Pro zprovoznění výdejů foniatrických pomůcek vydaných na ePoukaz je potřeba, aby uživatel s rolí *Správce* nastavil

- na stejné společnosti, kde je pomůcka na ePoukaz předepsána, **pracoviště výdejny** (výdejen) vč. **kódu SÚKL** a **certifikátu SÚKL** (jedná se o identifikaci pracoviště, které má oprávnění vydávat foniatrické pomůcky)
- uživatele na pracoviště výdejny, kteří budou mít možnost pomůcky vydávat
- na IČZ aktivní příznak *Výdejna fon. pom.*

   ![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Výdej foniatrické pomůcky předepsané na ePoukaz/assets/image-20260129-125332.png]]
- na pracovišti výdejny příznak, že se jedná o pracoviště s oprávněním vydávat foniatrické pomůcky předepsané na ePoukaz (příznak zapíná pracovník Stapro)

### Rozšířené nastavení - doporučujeme

Aby bylo možné na stejném pracovišti ePoukaz na foniatrickou pomůcku předepsat i vydat, je nutné, aby uživatel s rolí*Správce* ve struktuře společnosti nastavil vazbu mezi předepisujícím a vydávajícím pracovištěm. Podrobný návod je uveden [zde](https://stapro-galen.atlassian.net/wiki/x/AoC7Dg).

Ve zkratce: Na předepisujícím pracovišti uživatel nastaví využívané pracoviště výdejny:

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Výdej foniatrické pomůcky předepsané na ePoukaz/assets/image-20260129-133335.png]]
Pokud pracoviště využívá pouze jednu výdejnu (i přesto, že je na společnosti více výdejen), zaškrtne pouze jednu výdejnu. Pokud na předepisujícím pracovišti probíhá výdej na více výdejnách, uživatel vybere všechny potřebné výdejny.

> [!warning]
> Mezi předepisujícím pracovištěm a pracovištěm výdejny je nutné nastavit nahlížení [https://stapro-galen.atlassian.net/wiki/x/lQCCB](https://stapro-galen.atlassian.net/wiki/x/lQCCB)

## Výdej na pracovišti, které předepisuje

Pokud jste nastavili využívané pracoviště pro výdej foniatrické pomůcky, jak bylo uvedeno v [[Výdej foniatrické pomůcky předepsané na ePoukaz|předchozí kapitole]], nemusíte se při výdeji přepínat mezi pracovišti.

Na pracovišti, které má oprávnění pro předpis foniatrické pomůcky, uživatel předepíše ePoukaz tak, jak je zvyklý

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Výdej foniatrické pomůcky předepsané na ePoukaz/assets/image-20260129-140050.png]]
Po úspěšném odeslání, kdy je ePoukaz ve stavu *Předepsaný* a zároveň má ID ePoukazu, se zobrazí záložka *Výdej*

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Výdej foniatrické pomůcky předepsané na ePoukaz/assets/image-20260129-140249.png]]
V záložce *Výdej*uživatel vyplní Datum výdeje a v případě, že má nastaveno více výdejen, vybere výdejnu. Pomocí tlačítka Odeslat odesílá výdej.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Výdej foniatrické pomůcky předepsané na ePoukaz/assets/image-20260129-140420.png]]
Úspěšně vydaný ePoukaz

(1) a (2) je automaticky převeden do stavu *Plně vydaný*

(3) je automaticky načten identifikátor výdeje

(4) v části *Komunikace SÚKL* je založení i výdej uveden

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Výdej foniatrické pomůcky předepsané na ePoukaz/assets/image-20260129-140822.png]]

## Výdej na pracovišti výdejny

Je možné provést výdej na pracovišti výdejny. Takový výdej může provádět pracovník, který nemá mít přístup na pracoviště předepisujícího. V takovém případě je nutné mít nastavené nahlížení mezi pracovišti dle tohoto [návodu](https://stapro-galen.atlassian.net/wiki/x/lQCCB). Ve zkratce předepisující pracoviště musí sdílet informace a vydávající bude mít právo na ně nahlížet.

## Zrušení výdeje

Zrušit výdej je možné jak na předepisujícím pracovišti (pokud má nastavené využívané pracoviště výdejny), tak na pracovišti výdejny.

Výdej je možné zrušit klikem pravým tlačítkem myši na řádek plně vydaného ePoukazu.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Výdej foniatrické pomůcky předepsané na ePoukaz/assets/image-20260129-143403.png]]
Ve chvíli, kdy je zrušen výdej, je zároveň (automaticky na pozadí) smazán foniatrický záznam k vyúčtování.

Poté, co uživatel zapíše důvod zrušení, je ePoukaz převeden do stavu *Předepsaný*.

Takový ePoukaz je možné

- opravit - změnit údaje na ePoukazu
- zrušit - zrušit celý ePoukaz
- změnit na připravovaný - viz [[Výdej foniatrické pomůcky předepsané na ePoukaz|kapitola]]
- aktualizovat dle SÚKL

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Výdej foniatrické pomůcky předepsané na ePoukaz/assets/image-20260129-143609.png]]

### Nevidím možnost Zrušit výdej

Pokud potřebujete zrušit výdej pomůcky, ale tuto možnost nevidíte, může to mít dva důvody

1. Výdej pomůcky provedl jiný uživatel. V takovém případě nemáte práva na editaci daného záznamu a výdej musí zrušit ten uživatel, který výdej zadal.
2. Vydaná pomůcka je vyúčtovaná. Informaci, zda je pomůcka vyúčtovaná zjistíme v modulu *Vyúčtování* - záložka *Foniatrické záznamy.*Pokud má foniatrický záznam přiřazeno číslo dokladu a zároveň stav *Vykázaný*, jedná se o vyúčtovanou pomůcku. Pokud se jedná o tento případ, můžete změnit stav dokladu podle toho, jak potřebujete s ePoukazem dále nakládat podle [[Vyúčtování foniatrické pomůcky vydané na ePoukaz|tohoto postupu]].

   ![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/Výdej foniatrické pomůcky předepsané na ePoukaz/assets/image-20260210-091121.png]]

## Změnit na Připravovaný

Předepsaný ePoukaz je možné změnit do stavu *Připravovaný.* Tento stav nastavuje výdejna (pracoviště, které má nastavené využívané pracoviště výdejny nebo přímo výdejna). Výdejna dává ePoukaz do tohoto stavu ve chvíli, kdy byl ePoukaz uplatněn, ale ještě nebyl plně vydán. Používá se např. v situacích výroby pomůcky na zakázku. Výdejna změní stav na *Připravovaný*, což znamená, že  jej není možné využít v jiné výdejně. Jakmile je pomůcka dodána, provede se klasický výdej.
