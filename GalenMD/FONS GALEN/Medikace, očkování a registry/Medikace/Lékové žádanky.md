---
title: "Lékové žádanky"
version: 2
updated_at: 2025-06-19
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/48005121
---

# Lékové žádanky

Pro vystavování lékových žádanek je nutné disponovat certifikátem umožňující odesílání žádanek. Pro lékové žádanky jsou definovány 2 role:

- Praktik – role umožňující vystavovat lékové žádanky bez definice konkrétního léku
- Medikace – role umožňující vystavovat lékové žádanky s definicí konkrétního léku a umožňující aplikaci léku

## **Seznam lékových žádanek**

Kartotéka -> výběr konkrétního pacienta -> Medikace -> Žádanky

Zobrazí se seznam všech lékových žádanek pacienta. S žádankami lze dále pracovat:

1. Zobrazit detail (dvojklik)

2. Založit nový záznam (tlačítko Přidat nový záznam)

### Stavy lékových žádanek:

**Aktivní**– nová aktivní žádanka vystavená lékařem

**Vystaven recept**– žádanka byla vytvořena a v rámci vytvoření byl vystaven také recept

**Aplikováno**– potvrzena aplikace léku

**Lék poskytnut**– potvrzeno poskytnutí léku pacientovi

**Po Platnosti**– propadlá žádanka (žádanka má platnost 10 dní od data posledního pozitivního testu, poté je zneplatněna úlohou na pozadí)

**Zrušeno**– aktivní žádanka byla zrušena nově vystavenou žádankou

![léková žádanka.png](<../../../../pages/FONS GALEN/Medikace, očkování a registry/Medikace/Lékové žádanky/assets/léková žádanka.png>)

## **Detail lékové žádanky**

Pro roli praktik slouží detail pouze ke čtení a nabízí možnost vytisknutí lékové žádanky (tlačítko Tisk).

Pro roli medikace lze s detailem dále pracovat. Lze definovat konkrétní lék a jeho aplikaci.

![LŽ2.png](<../../../../pages/FONS GALEN/Medikace, očkování a registry/Medikace/Lékové žádanky/assets/LŽ2.png>)

## **Založení lékové žádanky**

Novou lékovou žádanku lze založit přes tlačítko Přidat nový záznam. Uživatel následně zatrhne dvě potvrzení (povinné) a žádanku odešle tlačítkem Odeslat nebo Odeslat a vytisknout.

Pro roli praktik lze definovat:

- Datum indikace: předdefinováno aktuální datum

![Obrázek3.png](<../../../../pages/FONS GALEN/Medikace, očkování a registry/Medikace/Lékové žádanky/assets/Obrázek3.png>)
Pro roli medikace lze definovat:

- Lék

- Datum indikace: předdefinováno aktuální datum

- Aplikovat

![Obrázek4.png](<../../../../pages/FONS GALEN/Medikace, očkování a registry/Medikace/Lékové žádanky/assets/Obrázek4.png>)
Po stisku tlačítka Přidat nový záznam se může zobrazit informace z UZIS:

- Pacient může mít pouze jednu žádanku ve stavu aktivní. Pokud u pacienta již existuje žádanka ve stavu aktivní, původní žádanku lze založením nové zrušit.

- Pacient nemá pozitivní test COVID-19

- Seznam léků, které byly pacientovy aplikovány

Poznámka: Ani jedna z výše zmiňovaných informací nebrání založení nové žádanky.
