---
title: "Očkování"
version: 1
updated_at: 2025-06-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/53149737
---

# Očkování

Modul očkování se standardně zobrazuje na pracovištích odbornosti s odborností praktický lékař, pediatr, gynekolog. V případě jiných specialistů je možné tento modul zaktivnit ve Správci - Správa organizace – na vybraném pracovišti v UI konfiguraci.

![image-20250623-102829.png](<../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/assets/image-20250623-102829.png>)
Na kartě očkování zadáme očkování kliknutím na tlačítko vlevo nahoře “+ Očkovat” (očkování v rámci kurativy), příp. “+ PLS” (očkování v rámci PLS). Přes tato tlačítka můžeme zadat očkování včetně vykázání výkonu a látky na pojišťovnu, nebo zadat očkování bez vykázání výkonu.

![image-20250623-102857.png](<../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/assets/image-20250623-102857.png>)
Po stisku tlačítka Očkovat se zobrazí okno s nabídkou očkovacích látek.

![image-20250623-102912.png](<../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/assets/image-20250623-102912.png>)
**Oblíbené** – OL, které uživatel na pracovišti označil hvězdičkou.

Tato záložka může být zaměněna za záložku

**Důležité** – OL, které jsou v aktuální metodice očkování zahrnuty v povinném očkování.

**Aktivní** – OL, které jsou aktuálně dostupné na trhu očkovacích látek (v případě zapnutého nadstandardního modulu “sklady” se jedná o látky, které jsou skladem a zároveň jsou dostupné na trhu)

**Všechny**– aktivní (modré tlačítko) i neaktivní (šedé tlačítko) OL. Pokud uživatel využívá skladů, tak nenaskladněné OL jsou označeny symbolem.

![image-20250623-102946.png](<../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/assets/image-20250623-102946.png>)
Vybereme očkovací látku a necháme se provést celým očkovacích procesem. V AIS Galen jsou přednastaveny očkovací schémata a očkovací varianty.

V případě, že chceme do systému zadat pouze očkování bez vykázání výkonu a očkovací látky na pojišťovnu - označíte pole “Doplnit bez vykázání výkonu”. slouží ke zjednodušenému zápisu očkování, kdy se zadává pouze datum, očkovací látka, pořadí očkování a datum příštího očkování. Slouží víceméně pouze k evidenci termínů očkování a používá se především k zapsání již minulých očkován.

![image-20250623-103004.png](<../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/assets/image-20250623-103004.png>)
Očkovací schéma vychází ze SPC dané OL nebo z metodiky očkování, které definují v kolika dávkách a v jakém rozmezí má být OL podána.

Možnost „Bez schématu“ slouží k zadání očkování, u kterého nebude sledována další možná návaznost.

Černě je vždy zvýrazněna předpokládaná volba, která vychází z očkování zadaných v minulosti, avšak tuto doporučenou volbu může uživatel změnit.

V prostřední části obrazovky se nabízí dávky, které jsou definované ve schématu. V tomto příkladu vidíme, že klasické schéma je tvořeno třemi dávkami a následným přeočkováním.

Zobrazená data vychází z metodiky, která definuje, v jakém rozmezí mají být jednotlivé dávky podána. Datum se zobrazuje vždy pouze u bezprostředně následující dávky. V případě, že se datum nezobrazuje, není v metodice uveden přesný interval mezi jednotlivými dávkami.

Ve spodní části okna se zobrazuje rozhodné datum pro podání zvolené dávky (nastavuje se aktuální datum) a doporučené datum, kdy by měla být podána další dávka.

Checkbox Doplnit bez vykázání výkonu uživatel zaškrtne v případě, že reálně nebyla provedena aplikace OL, ale chce mít dané očkování evidováno v systému.

V dalším kroku se zobrazí okno pro výběr varianty očkování

Po správném výběru přejdeme přes tl. “Dále” k výběru očkovací varianty.

Pokud má dané pracoviště nadstandardní placený modul eOčkování (odesílání očkování do ÚZIS) je tabulka s očkovacích schématem rozšířená o pole “Údaje pro odeslání do ISIN”.

Lékař vybere požadovanou očkovací variantu – ve spodní části se mu zobrazí kod výkonu a kod materiálu, který bude s danou variantou vykázán a uvidí hlavní a řádkovou dg., která se k očkování vztahuje.

V části “Výběr položek ceníku” jsou uvedeny položky, které si lékař nadefinoval sám k danému očkování v modulu nadstandardní péče.

![image-20250623-103057.png](<../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/assets/image-20250623-103057.png>)
Varianta očkování specifikuje, jakým způsobem je aplikace a OL hrazena.

Ve spodní části okna může uživatel definovat sortiment, který chce účtovat přímo pacientovi.

Přes tl. “Dále” se dostane lékař do záložky, kde uvádí šarži a expiraci dané očkovací látky. V případě, že dané pracoviště využívá **nadstandardní placený modul “sklady”** zobrazí se látky, které jsou na skladě dle požadovaného očkovacího schématu a očkovací varianty.

![image-20250623-103113.png](<../../../pages/FONS GALEN/Medikace, očkování a registry/Očkování/assets/image-20250623-103113.png>)
