---
id: 25952258
title: "API PacientDataService GET"
version: 4
updated_at: 2025-06-11T08:18:44.028Z
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/25952258
---

# API PacientDataService GET

Toto API zasílá informace o vybraných entitách, které byly vytvořeny v rámci zdravotnické dokumentace pacienta. API úzce souvisí s API StrukturaOrganizaceService.

Metody pro jednotlivé entity jsou v logických dvojících: Jedna z dvojice zasílá všechny údaje týkající se daného pacienta. Druhá z dvojice (*ZaObdobi)* zasílá všechny záznamy, které byly v daném období změněny. Zadané období může být maximálně 24hod.

## Obecné informace

### **DatumCas**

Parametr datum a čas se zadává ve formátu ddMMyyyyTHH:mm:ss

### Datum

Datum se zadává ve formátu ddMMyyyy

### Start

Číslo prvního vráceného záznamu kde první záznam má číslo 0 (nula).

### Pocet

Maximální počet vrácených záznamů

## vykony

## Pacient

Voláním metody je možné získat vybrané informace z karty pacienta.

- datum narození

Ve tvaru DDMMYYYY

- pohlaví

Pole může nabývat hodnot: *Muž, Žena, Neuvedeno.*

- pojišťovna

Jedná se o kódy zdravotních pojišťoven. V případě Pojišťovny VZP, a.s. se jedná o kód 333, samoplátci mají kód 999.

- telefon/email

Zasílá se právě jeden kontakt daného typu a to i v případě, že má pacient zadaných více typů daného kontaktu. V rámci elementu *telefon* se zasílá jak kontakt typu telefon, tak kontakt typu mobil z karty pacienta. Právě jeden kontakt se určí množinou kontaktů daného typu, které nejsou smazané/neuvedené/neplatné. Tyto kontakty se seřadí podle toho, zda mají příznak primární a podle data vytvoření. Z těchto kontaktů se odešle kontakt na prvním místě.

- Karta založena

Ve tvaru DDMMYYYY
