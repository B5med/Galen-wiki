---
title: "Definice nároku"
version: 1
updated_at: 2025-07-10
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/68517899
---

# Definice nároku

V modulu Nároky je třeba definovat nad kterou prohlídkou budou nároky vznikat.

Definici zadává uživatel s oprávněním Správce v modulu *Nároky*.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Generování nároků z vyšetření/Definice nároku/assets/image-20250710-122731.png]]
Po kliknutí na tlačítko **+**se objeví okno, kde uživatel nadefinuje, jaké podmínky platí pro generovaní nároků na danou prohlídku a jejich splnění.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Generování nároků z vyšetření/Definice nároku/assets/image-20250710-122747.png]]
Definice nároku se skládá z hlavičky definice a intervalu definice. Počet intervalů může být pod jednou hlavičkou více.

V rámci hlavičky definice je nutné určit:

- Definici prohlídky, z které se mají nároky generovat.

- Název definice – přednastaví se název prohlídky.

- Následná prohlídka – když je definována, po vytvoření aktuální prohlídky (a splnění podmínek), je vytvořen nový nárok na následnou prohlídku.

V rámci intervalu definice je nutné určit:

- Odbornost – nároky se budou tvořit jenom pro pacienty s danou odborností.

Nemusí být vyplněno.

- Věk od – minimální věk pacienta, aby mohl být nárok v rámci daného intervalu definice vytvořen/splněn.

- Věk do – maximální věk pacienta, aby mohl být nárok v rámci daného intervalu definice vytvořen/splněn.

- Interval

o      Určuje minimální počet dní, který musí uběhnout mezi dvěma vytvořenými nároky v rámci stejné prohlídky.

o      Když má definice určenou následnou prohlídku, určuje minimální počet dní, který musí uběhnout mezi dvěma vytvořenými nároky v rámci aktuální prohlídky a následné prohlídky.

- Tolerance splnění – určuje kolik dní předem je možné nárok splnit, před dosáhnutím jeho platnosti (splnění budoucího nároku).

- Záměna za prohlídku – definuje která jiná prohlídka zastupuje aktuální prohlídku.

(zaměněná prohlídka vytváří a splní nároky podle aktuální definice).

Generování dosažením věku – když je zatrhnuté, budou se nároky pacientům generovat 1x v noci, při splnění podmínek v intervalu.
