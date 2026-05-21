---
title: "ePosudek – Řidičské oprávnění (ŘP)"
version: 1
updated_at: 2026-04-29
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/360710145
---

# ePosudek – Řidičské oprávnění (ŘP)

Tato stránka popisuje specifika posudků **Zdravotní způsobilost k řízení motorových vozidel** v modulu ePosudek. Obecné nastavení (certifikát PZS, číslo KRZP) a popis okna najdete na nadřazené stránce **ePosudek – Elektronické lékařské posudky**.

## Formulář posudku

Formulář je členěn do pěti bloků:

### 1. Údaje pacienta

Vyplní se automaticky z karty pacienta (jméno, příjmení, datum narození, rodné číslo, adresa). Pole nejsou editovatelná.

### 2. Základní údaje posudku

| Pole | Popis |
| --- | --- |
| **Datum vystavení** | Datum vydání posudku |
| **Platnost do** | Datum, do kdy je posudek platný |
| **Druh prohlídky** | Výběr druhu prohlídky (vstupní, periodická, mimořádná…) |
| **Druh posudku** | Výběr druhu posudku (prvořidič, senioři…) |

### 3. Způsobilost

#### Skupiny ŘP

| Skupina | Zahrnuté kategorie |
| --- | --- |
| **Skupina 1** | A, A1, A2, AM, B, B1, BE |
| **Skupina 2** | A, A1, A2, AM, B, B1, BE, C, C1, CE, C1E, D, D1, DE, D1E, T |

#### Výsledek způsobilosti

Pro každou vybranou skupinu se zadává jeden z těchto výsledků: Způsobilý / Způsobilý s podmínkou / Nezpůsobilý.

#### Podmínky

Tabulka podmínek se zobrazí při výsledku *Způsobilý s podmínkou*. Každý řádek obsahuje typ podmínky, kód a doplňující informace.

> [!warning]
> Maximální délka doplňujícího textu je**300 znaků**.

### 4. Výsledek podání

| Pole | Popis |
| --- | --- |
| **Název** | Název podání |
| **Stav** | Stav posudku v ELP |
| **ID posudku** | ID posudku (obdrženo z ELP po vytvoření posudku) |

### 5. Komunikace s ELP

| Pole | Popis |
| --- | --- |
| **Popis** | Textový popis / poznámka k odeslání |
| **Čas odeslání** | Datum a čas odeslání do ELP (vyplní se automaticky po odeslání) |
| **Poznámka** | Interní poznámka (nezasílá se do ELP) |

## Kontextové menu (pravé tlačítko myši)

Kliknutím pravým tlačítkem myši na záznam v přehledu se zobrazí kontextové menu s dostupnými akcemi pro daný stav posudku:

| Stav posudku | Dostupné akce |
| --- | --- |
| **Připravovaný** | Smazat posudek |
| **Platný** | Zneplatnit posudek, Zobrazit historii, Export |
| **Zneplatněný** | Zobrazit historii |

## Jak vytvořit posudek

1. Otevřete kartu pacienta a klikněte na ikonu **eFormulář → ePosudek**.
2. Klikněte na tlačítko **Nový**.
3. V dialogu vyberte typ posudku a potvrďte.
4. Vyplňte základní údaje posudku, způsobilost, skupiny ŘP a doplňte případné podmínky.
5. Klikněte na **Uložit** – posudek se uloží lokálně ve stavu **Připravovaný**.

## Jak uložit posudek

1. Vyplňte požadované údaje ve formuláři.
2. Klikněte na tlačítko **Uložit** v nástrojové liště.
3. Posudek se uloží lokálně v IS Galen ve stavu **Připravovaný**.
4. K posudku se lze kdykoli vrátit, pokračovat v jeho vyplnění nebo jej odeslat do ELP.

## Jak odeslat posudek do ELP

1. Vyberte posudek ve stavu **Připravovaný**.
2. Zkontrolujte vyplněné údaje.
3. Klikněte na tlačítko **Odeslat**.
4. Systém odešle posudek do registru ELP přes zabezpečené spojení.
5. Po úspěšném odeslání a potvrzení registrem se stav změní na **Platný**.

## Jak exportovat a vytisknout posudek

Tlačítko **Export** je dostupné pro posudky ve stavu **Platný**. Otevře dialog *Vyberte způsob exportu*:

| Možnost | Popis |
| --- | --- |
| **Otevřít soubor** | Otevře PDF posudku v externím prohlížeči – odtud lze posudek vytisknout |
| **Uložit soubor** | Uloží PDF posudku na disk počítače |
| **Poslat soubor e-mailem** | Odešle PDF jako přílohu e-mailu |
| **Poslat soubor zabezpečeně pacientovi** | Odešle PDF zabezpečeně pacientovi |
| **Poslat soubor zabezpečeně spolupracujícímu lékaři** | Odešle PDF zabezpečeně spolupracujícímu lékaři |
| **Poslat soubor prostřednictvím Portálu pacienta** | Odešle PDF přes Portál pacienta |
| **Poslat soubor do spisové služby** | Odešle PDF do spisové služby |

**Postup pro tisk:**

1. Vyberte posudek ve stavu **Platný**.
2. Klikněte na tlačítko **Export**.
3. V dialogu vyberte **Otevřít soubor** a klikněte na **OK**.
4. PDF posudku se otevře v externím prohlížeči.
5. Vytiskněte prostřednictvím funkce tisku prohlížeče (Ctrl+P nebo ikona tisku).

## Jak zneplatnit posudek

1. V záložce *Vedené v IS Galen* klikněte **pravým tlačítkem myši** na posudek ve stavu **Platný**.
2. V kontextovém menu vyberte **Zneplatnit posudek**.
3. Potvrďte zneplatnění.
4. Systém odešle požadavek na zneplatnění do ELP.
5. Stav posudku se změní na **Zneplatněný**.

> [!danger]
> Zneplatnit lze pouze posudky vystavené vlastním PZS (stejné IČO). Posudky jiného PZS nelze zneplatnit. Zneplatnit lze pouze posudky ve stavu **Platný**.

## Jak zobrazit historii posudku

1. V záložce *Vedené v IS Galen* klikněte **pravým tlačítkem myši** na posudek ve stavu **Platný**.
2. V kontextovém menu vyberte **Zobrazit historii**.
3. Zobrazí se historie změn daného posudku.

## Jak kopírovat posudek (opakovaný posudek)

1. Vyberte existující posudek ve stavu **Platný**.
2. Klikněte na tlačítko **Kopie**.
3. Systém předvyplní formulář nového posudku dle vybraného záznamu.
4. Upravte potřebné údaje a pokračujte: **Uložit → Odeslat**.

## Jak smazat posudek

1. V záložce *Vedené v IS Galen* klikněte **pravým tlačítkem myši** na posudek ve stavu **Připravovaný**.
2. V kontextovém menu vyberte **Smazat posudek**.
3. Potvrďte smazání.
4. Posudek bude odstraněn z IS Galen.

> [!danger]
> Smazat lze pouze posudky ve stavu **Připravovaný**. Odeslané a platné posudky nelze smazat – ty lze pouze zneplatnit.
