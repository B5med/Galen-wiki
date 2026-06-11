---
id: 67993602
title: "Výpočet percentilu BMI s vazbou na výkony"
version: 2
updated_at: 2025-07-16T08:30:12.779Z
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/67993602
---

# Výpočet percentilu BMI s vazbou na výkony

Tento manuál popisuje kroky potřebné pro konfiguraci a použití nové funkce pro výpočet percentilu BMI u dětských pacientů v rámci vybraných preventivních prohlídek.

Funkcionalita „**Výpočet percentilu BMI**“ je **placenou službou** a je dostupná pouze pro **odbornost 002**.  
Pro aktivaci služby prosím kontaktujte svého obchodního zástupce.

## Výpočet v rámci měření

Výpočet percentilu BMI probíhá automaticky na základě údajů zadaných do měření.

**Cesta**: modul **Ordinace** → vybrat pacienta → přejít do **Dekurzu** → tlačítko **Zadat měření**

1. V měření v sekci „**Výška, hmotnost, teplota**“ uživatel vyplní položky:

**a.       Výška (cm)**

**b.      Hmotnost (kg)**

2. Na základě těchto údajů se automaticky vypočítá hodnota v položce **BMI** a následně **Percentil BMI**.

## Výpočet v rámci prohlídky

**Cesta**: modul **Ordinace** → vybrat pacienta → záložka **Prohlídky a vyšetření** → **Nová prohlídka** → vybrat odpovídající preventivní prohlídku

Funkcionalita je dostupná pro všechny typy preventivních prohlídek určených pro děti a dorost.

1. V sekci **Měření** uživatel vyplní položky:

**a.       Výška (cm)**

**b.      Hmotnost (kg)**

2. Na základě těchto údajů se automaticky dopočítají hodnoty v polích **BMI** a **Percentil BMI.**
3. Po stisknutí tlačítka **Vytvořit výkony** se v části **Volitelné výkony** automaticky nabídne ten výkon, který odpovídá vypočítanému percentilu.

**Automaticky nabízené výkony dle výsledku percentilu BMI:**

·       **Výkon 02325** – percentil BMI ≤ 20

·       **Výkon 02326** – 20 < percentil BMI ≤ 90

·       **Výkon 02327** – 90 < percentil BMI ≤ 97

·       **Výkon 02328** – percentil BMI > 97
