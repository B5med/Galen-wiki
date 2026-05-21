---
title: "Notifikace pacientů ohledně zpracování laboratorních výsledků"
version: 1
updated_at: 2025-08-26
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/104759320
---

# Notifikace pacientů ohledně zpracování laboratorních výsledků

Cílem funkcionality je omezit volání pacientů do ordinací s dotazy ohledně stavu zpracování jejich laboratorních výsledků. Tohoto cíle bude dosaženo ručním odesíláním notifikací pacientovi o stavu lab. výsledku jednotlivě, nebo hromadně.

## Konfigurace funkcionality

Po zpřístupnění administrátory ze strany podpory AIS Galen, je možné funkcionalitu okamžitě používat.

Doporučujeme si však nejdříve nastavit šablony notifikací, které budeme pacientům odesílat.

Šablony najdeme v modulu Nástroje, okno Šablony, záložka Notifikace. Na tento účel nám poslouží šablony s použitím:

- ***Notifikace laboratorního výsledku – bez konzultace***(šablona určená pro pacienty s lab. výsledkem ve stavu *,,V pořádku“*) – pacienti kteří již nemusí lab. výsledek konzultovat s lékařem.
- ***Notifikace laboratorního výsledku – potřebná konzultace***(šablona určená pro pacienty s lab. výsledkem ve stavu *,,Nutná konzultace“, nebo „Ostatní“*) – pacienti u kterých je konzultace s lékařem potřebná.

U obou typů notifikací je možné zatrhnout možnost ,,*Zahrnout komentář lékaře*“. Po zatrhnutí této možnosti se při odeslání notifikace automaticky doplní komentář lékaře k danému lab. výsledku. Komentář se doplní na konec zprávy.

![image-20250826-080917.png](<../../../pages/FONS GALEN/Objednávání, komunikace a notifikace/Notifikace pacientů ohledně zpracování laboratorních výsledků/assets/image-20250826-080917.png>)
![image-20250826-081045.png](<../../../pages/FONS GALEN/Objednávání, komunikace a notifikace/Notifikace pacientů ohledně zpracování laboratorních výsledků/assets/image-20250826-081045.png>)

### **Odeslání notifikace**

Odeslání notifikace bude možné jen pro zpracované lab. výsledky. Lab. výsledkem ve stavu *,,Nový“* nebude možné notifikaci odeslat.

Odeslání notifikace bude možné ze dvou míst v AIS Galen a to individuálně pro každého pacienta z **dekurzu**, nebo hromadně z **modulu** **Komunikace**.

#### **Notifikace z dekurzu**

Po rozkliknutí detailu lab. výsledku přibude nové tlačítko *,,Notifikovat“*. Uživatel bude mít možnost zvolit, jestli chce notifikaci odeslat i se samotným lab. výsledkem ve formátu PDF.

![image-20250826-081205.png](<../../../pages/FONS GALEN/Objednávání, komunikace a notifikace/Notifikace pacientů ohledně zpracování laboratorních výsledků/assets/image-20250826-081205.png>)
![image-20250826-081215.png](<../../../pages/FONS GALEN/Objednávání, komunikace a notifikace/Notifikace pacientů ohledně zpracování laboratorních výsledků/assets/image-20250826-081215.png>)
Po kliku na tlačítko *,,Notifikovat“* se uživateli objeví okno pro odeslání notifikace.

- Okno obsahuje na začátku informaci, jaká informace bude pacientovi odeslána. V případě který je na screenshotu je to informace, která obsahuje šablonu s nutností další konzultace. Je to z důvodu že stav lab. výsledku byl *,,Nutná konzultace“.*
- Uživatel si může zvolit, jestli chce odeslat SMS, E-mail, nebo obojí.
- Na screenshotu na konci notifikace se automaticky zkopíroval komentář lékaře k danému lab. výsledku (možnost nastavení na šabloně notifikace, popsána výše).

![image-20250826-083459.png](<../../../pages/FONS GALEN/Objednávání, komunikace a notifikace/Notifikace pacientů ohledně zpracování laboratorních výsledků/assets/image-20250826-083459.png>)

## **Notifikace z modulu komunikace**

Z modulu komunikace, v okně Lab. výsledky, je možné odeslat notifikace k vícero lab. výsledkům naráz.

Do okna byly přidané nové prvky:

- Možnost rozdělit si poměrově obrazovku dle potřeby (potáhnutím myši na rozdělovací čáře obrazovky, znázorněné šipkou v screenshotu).

- Možnost označit vícero lab. výsledků naráz (klávesové zkratky CTRL + levý klik myší, nebo SHIFT + levý klik myší).

- V okně bude možnost filtrovat jenom lab. výsledky bez notifikace.

- Přibyla tři nová tlačítka:

- Notifikovat – primární tlačítko na odeslání notifikací.

- Již nenotifikovat – přidá k laboratornímu výsledku příznak *,,Nenotifikovat“.*Tomuto lab. výsledku nebude možné odeslat notifikaci.

- Povolit notifikaci – Zpětně odstraní příznak *,,Nenotifikovat“.*

- Sloupce v zobrazení byly rozšířeny o nové, poskytující informace o odeslání/neodeslání notifikací.

![image-20250826-083626.png](<../../../pages/FONS GALEN/Objednávání, komunikace a notifikace/Notifikace pacientů ohledně zpracování laboratorních výsledků/assets/image-20250826-083626.png>)
Při zvolení vícero výsledků s různými stavy zpracování (například: 1. výsledek ve stavu v pořádku, 2. se stavem nutná konzultace), je nutné každému pacientovi odeslat jinou informaci. Z toho důvodu po kliknutí na tlačítko Notifikovat, uživatel nejdříve odešle notifikace pro pacienty s informací, že konzultace není nutná a následně notifikaci pro pacienty s informací, že konzultace je potřebná (**okno z obrázku č. 3 se objeví 2x**, pro každou informaci zvlášť).

V případě že má pacient vícero lab. výsledků kterým odesíláme notifikaci, odešleme mu vždy maximálně 1 SMS a 1 email.

V případě že má rozdílné stavy zpracování lab. výsledků, vyhrává odesílání informace o tom, že je potřebná konzultace.
