---
title: "Oprávnění"
version: 4
updated_at: 2026-02-04
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/75628693
---

# Oprávnění

## Nahlížení

![image-20250618-113044.png](<../../../../pages/FONS GALEN/Správce a nastavení/Správa organizace/Oprávnění/assets/image-20250618-113044.png>)
Ikona Oprávnění (Správce -> Správa organizace -> Oprávnění) umožňuje nastavit možnost nahlížení na dokumentaci mezi pracovišti. Nastavení tak umožní, aby uživatel na jednom pracovišti viděl (v režimu pro čtení) záznamy z jiného pracoviště.

Pokud chceme, aby lékař mohl s kartotékou pracovat, musíme v Konfiguraci společnosti zaškrtnout možnost Sdílená kartotéka.

Uživatel zvolí pracoviště, mezi kterými chce nastavit nahlížení na dokumentaci.

![image-20260204-143814.png](<../../../../pages/FONS GALEN/Správce a nastavení/Správa organizace/Oprávnění/assets/image-20260204-143814.png>)
V tomto konkrétní příkladě pracoviště Gynekologie poskytuje svoje data pracovišti Diabetologie, tzn. Diabetologie uvidí záznamy z pracoviště Gynekologie.

Avšak Gynekologie neuvidí záznamy z pracoviště Diabetologie, protože Diabetologie neposkytuje data.

##### V rámci nahlížení jsou sdíleny záznamy tohoto typu:

- Anamnéza–EZD – kurativa
- Anamnéza–EZD – PLS
- ČSSZ – kurativa ČSSZ – PLS Dekurz – kurativa
- Dekurz – PLS
- ePoukaz – kurativa
- ePoukaz – PLS
- Externí zpráva – kurativa
- Externí zpráva – PLS
- Foniatrie
- Formulář – kurativa
- Formulář – PLS
- Laboratorní výsledky – kurativa
- Laboratorní výsledky – PLS
- Lékařská zpráva – kurativa
- Lékařská zpráva – PLS
- Medikace – kurativa
- Medikace – PLS
- Očkování – kurativa
- Očkování – PLS
- Příloha – kurativa
- Příloha – PLS
- Vyšetření – kurativa
- Vyšetření – PLS
- Žádanka zobrazovacích metod

> [!info]
> Pokud uživatel na pracovišti nastavil [[Anamnéza|*Zákaz nahlížení*]], tak dokumentace daného pacienta pro dané pracoviště není sdílena i přesto, že je zde dokumentace pracoviště nastavena jako sdílená.

### Definovat jednotlivé moduly zvlášť

Pokud uživatel zaškrtne checkbox *Definovat jednotlivé moduly zvlášť*, může specifikovat která dokumentace bude mezi pracovišti sdílena.

![image-20260204-144210.png](<../../../../pages/FONS GALEN/Správce a nastavení/Správa organizace/Oprávnění/assets/image-20260204-144210.png>)
V tomto případě bude pracoviště Gynekologie poskytovat pouze záznamy o vystavených dávkách ČSSZ a ePoukazech. Ostatní záznamy, jako např. dekurz, medikace a další poskytovány nebudou.
