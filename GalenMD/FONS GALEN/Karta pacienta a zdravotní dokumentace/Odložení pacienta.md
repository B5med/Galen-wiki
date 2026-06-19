---
title: "Odložení pacienta"
version: 1
updated_at: 2026-06-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/462028809
---

# Odložení pacienta

Funkce **Odložení pacienta** umožňuje dočasně přerušit práci s aktuálně otevřeným pacientem a uložit ho do schránky, aniž by se ztratil rozpracovaný kontext. Kdykoli se uživatel potřebuje věnovat jinému pacientovi nebo úkonu, může se k odloženému pacientovi jednoduše vrátit a pokračovat přesně tam, kde přestal.

## Jak funkce funguje

Tlačítko schránky je zobrazeno v horním panelu modulu.

![image-20260618-131936.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Odložení pacienta/assets/image-20260618-131936.png>)
Jeho dostupnost závisí na aktuálně otevřeném pohledu:

- **Uložení pacienta do schránky** – pokud je aktivní pacient a uživatel dosud žádného nemá uloženého, kliknutí na tlačítko přesune aktuálního pacienta do schránky. Zobrazení se přepne zpět na kartotéku, takže je možné vyhledat a otevřít jiného pacienta. Název uloženého pacienta je zobrazen v tooltipu tlačítka.
- **Návrat k odloženému pacientovi** – pokud je ve schránce uložen pacient, kliknutí na tlačítko obnoví jeho kontext – systém nastaví daného pacienta jako aktivního a vrátí se na detail (záložku), který byl otevřen v okamžiku odložení.

## Kde je funkce dostupná

- **Ordinace** – funkce je dostupná v modulu Ordinace (např. při psaní dekurzu)
- **Objednávání** – funkce je dostupná v modulu Objednávání (recepce)

## Aktivace

Jedná se o nadstandardní placenou funkcionalitu. Po objednání ze strany zákazníka je funkcionalita zpřístupněna.

Zákazník si následně sám v administraci Galenu v nastavení společnosti (záložka **Konfigurace**, sekce **Odložení pacienta**) zvolí, ve kterých modulech funkci využívá – zaškrtnutím příslušných checkboxů **Ordinace** a **Objednávání**.

Jakmile je příznak pro daný modul zapnutý, funkce je okamžitě dostupná **všem uživatelům** tohoto modulu – bez jakéhokoli dalšího nastavení na straně lékaře nebo uživatele.
