---
title: "PACS"
version: 1
updated_at: 2025-07-21
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/75694321
---

# PACS

## **PACS-prohlížeč**

Tato funkcionalita slouží k provolávání systému určenému k prohlížení snímků uložených v systému PACS z AIS Galen.

## **Konfigurace**

Nastavení parametrů může provádět uživatel s oprávněním Správce. K funkcionalitě se dostane následujícím způsobem:

1. Na úrovni Správce otevřít modul **Správa organizace.**

2. Dále je nutné otevřít submodul **Agendy a následně záložku PACS**.

Pro nastavení integrace s prohlížečem PACS snímků jsou klíčové následující položky:

![image-20250701-105711.png](<../../../../../pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/PACS/assets/image-20250701-105711.png>)
1. V položce Aktivační událost je nezbytné zatrhnout checkbox Prohlížeč.

2. **URL prohlížeče:** adresa, na které systém pro prohlížení snímků běží

3. **Parametry-pacient:**uživatel je schopný pomocí této položky definovat, s jakými parametry se bude provolávat prohlížeč z úrovně pacienta. Parametry je doporučené zadat následujícím zápisem: **pid=[@P.CisloPojistence****];****user=[@U.AlternateLogin****]**

- pid a user jsou názvy parametrů, které jsou dané dokumentací prohlížejícího systému

- [@P.CisloPojistence] a [@U.AlternateLogin] jsou zástupné proměnné, pomocí nichž se v okamžiku volání požadavku dotahující požadovaná data. Zástupné proměnné je možné vybrat pomocí následujícího tlačítka: @

- Jednotlivé parametry je nutné oddělovat pomocí středníku

4. **Parametry-žádanka:**uživatel je schopný pomocí této položky definovat, s jakými parametry se bude provolávat prohlížeč z úrovně žádanky. Parametry je doporučené zadat následujícím zápisem: **accno=[@R.RecordCode];user=[@U.AlternateLogin****]**

5. **Certifikát prohlížeče**: do této položky administrátor vloží privátní část certifikátu, pomocí níž se požadavek digitálně podepíše. Do systému určenému k prohlížení PACS snímků je v takovém případě nutné vložit veřejnou část příslušného certifikátu.

6. V dolní části konfiguračního okna následně uživatel volí, z jakých pracovišť je možné volat prohlížeč snímků. Na výběr jsou ale pouze pracoviště radiodiagnostiky.

## **Provolání prohlížeče na úrovni RDG žádanky**

Systém na prohlížení snímků je možné provolat pomocí tlačítka **Zobrazit v PACS**, které je přítomné v modulu RDG žádanek.

![image-20250701-105820.png](<../../../../../pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/PACS/assets/image-20250701-105820.png>)

## **Provolání prohlížeče na úrovni pacienta**

Systém je možné z úrovně pacienta provolat následujícím způsobem:

1. Kliknout pravým tlačítkem myši na kartu vybraného pacienta.

2. Zvolit položku Přístroje.

3. Vybrat položku PACS.

![image-20250701-105847.png](<../../../../../pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/PACS/assets/image-20250701-105847.png>)
