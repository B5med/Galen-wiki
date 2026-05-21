---
title: "Vznik nároku"
version: 1
updated_at: 2025-07-10
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/68190229
---

# Vznik nároku

Nárok vzniká způsoby: vykázáním výkonu z prohlídky u registrovaného pacienta, při registraci pacienta, automaticky v noci při dosažení věku, nebo ručním spuštěním generování nad konkrétní definici.

Při vzniku nároku existuje kontrola na duplicitu, která nedovolí, aby měl pacient v 1 okamžik více aktivních nebo budoucích nároků, v rámci stejné definice a v rámci stejné ordinace.

### Vznik nároku vykázáním výkonu z prohlídky

Nárok vznikne vytvořením výkonu pomocí tlačítka *Vytvořit výkon*   v prohlídce. Datum, ke kterému by měla proběhnout další prohlídka definovaná nárokem, není nijak ovlivněno zadaným termínem příští prohlídky.

Vznik nároku probíhá na pozadí, při vykázání výkonu z prohlídky není vznik nároku potvrzován.

Ve chvíli, kdy je výkon vytvořený z vyšetření smazán, je smazán i nárok, který vznikl na základě tohoto výkonu z vyšetření.

Nárok může vzniknout na stejnou definici prohlídky nebo na prohlídku, která je definovaná jako následující.

### Způsob výpočtu platnosti nároku při vykázání výkonu z prohlídky

Datum, do kdy je nárok platný (platnost do) představuje datum, kdy pacient dosáhne horní věkové hranice na definici intervalu.

Datum, od kdy je nárok platný (platnost od) je určen následovně:

- Definice nároku nemá určenou následující prohlídku

o      Platnost od nároku je datum vytvoření vyšetření + hodnota intervalu na definici.

- Definice nároku má určenou následující prohlídku

o      Platnost od nároku je pozdější datum z kombinace, datum vytvoření vyšetření + interval určený na definici a datum, kdy pacient dosáhne spodní hranici věku v následující definici nároku.

### Vznik nároku při registraci pacienta

Ve chvíli, kdy uživatel registruje pacienta pomocí tlačítka *Nová registrace*zobrazí se okno s informací, které nároky pacientovi vzniknou.

Aby se nárok vytvořil, je nutné, aby byly splněny podmínky určené na definici nároku, a

to podmínka na věk pacienta a podmínka splnění rozestupu nároků (podmínka na interval). Rozhodné datum, které je v rámci podmínek zohledňováno, je datum registrace.

(Systém posuzuje věk pacienta k datu registrace, totéž platí i pro podmínku na interval).

Po splnění podmínek se nárok vždy vytváří jako aktivní, s platností, která je rovna datu registrace pacienta.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Generování nároků z vyšetření/Vznik nároku/assets/image-20250710-123014.png]]

### Vznik nároku hromadným generováním

Uživatel s rolí Správce může ručně vygenerovat nároky na zvolenou definici.

Tímto způsobem lze definovat rozsah generování nároků na společnost nebo na konkrétní pracoviště.  Také se definuje, jestli generovat nároky na základě data výkonu vztahující se k vyšetření nebo data realizace výkonu.

Nárok vzniká vždy aktivní, k aktuálnímu datu.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Generování nároků z vyšetření/Vznik nároku/assets/image-20250710-123035.png]]
![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Generování nároků z vyšetření/Vznik nároku/assets/image-20250710-123040.png]]

### Vznik nároku noční úlohou

Po zvolení této možnosti (zatrhnutí na úrovni intervalu definice, viz obrázek), systém bude dle dané definice prohledávat všechny pacienty, kteří splňují podmínky. Po splnění podmínek bude pacientovi vytvořen aktivní nárok s platností od aktuálního dne.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Generování nároků z vyšetření/Vznik nároku/assets/image-20250710-123106.png]]
