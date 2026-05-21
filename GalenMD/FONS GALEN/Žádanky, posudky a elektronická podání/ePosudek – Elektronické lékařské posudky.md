---
title: "ePosudek – Elektronické lékařské posudky"
version: 1
updated_at: 2026-04-29
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/359006213
---

# ePosudek – Elektronické lékařské posudky

Modul **ePosudek** umožňuje vystavovat, odesílat a spravovat elektronické lékařské posudky v souladu s požadavky systému **ELP** (Elektronické lékařské posudky) provozovaného NCEZ / MZ ČR. Odesílání posudků probíhá přes zabezpečené spojení (HTTPS/TLS, OAuth 2.0) s použitím systémového certifikátu PZS.

## Přehled typů posudků

Každý typ posudku je popsán v samostatné podstránce:

- [[Certifikát PZS]]
- [[ePosudek – Řidičské oprávnění (ŘP)]]

## Nastavení před prvním použitím

Toto nastavení platí pro **všechny typy posudků**.

### 1. Certifikát PZS

PZS musí mít platný systémový autentizační certifikát vydaný Certifikační autoritou MZ ČR (**EZCA II**, `ezca-ez.csez.cz`). Více informací zde: [https://stapro-galen.atlassian.net/wiki/pages/resumedraft.action?draftId=377421825&draftShareId=e6682cc9-dd8d-4164-affe-78efdbf32414&atlOrigin=eyJpIjoiNjFiNmY0Njc1M2NjNGJjZWIxZDhmMjliZmFlNGE2ZTUiLCJwIjoiYyJ9](https://stapro-galen.atlassian.net/wiki/pages/resumedraft.action?draftId=377421825&draftShareId=e6682cc9-dd8d-4164-affe-78efdbf32414&atlOrigin=eyJpIjoiNjFiNmY0Njc1M2NjNGJjZWIxZDhmMjliZmFlNGE2ZTUiLCJwIjoiYyJ9)

**Správa → Struktura → [název organizace] → Certifikát PZS → Nastavit**

> [!warning]
> Bez platného certifikátu PZS není možné posudky odesílat do registru ELP. Podrobnosti o získání certifikátu EZCA II najdete v dokumentaci na stránkách MZ ČR.

### 2. Číslo KRZP (alternativně NRZP) lékaře

Každý lékař vystavující posudky musí mít v systému vyplněné číslo KRZP(NRZP) – identifikátor v Registru zdravotnických pracovníků.

**Správa → Uživatelé → [detail uživatele] → Číslo KRZP → Ověřit**

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/assets/image-20260424-090251.png]]

## Přístup k modulu

**Karta pacienta → ikona eFormulář → ePosudek**

## Popis okna ePosudku

### Nástrojová lišta

| Tlačítko | Popis |
| --- | --- |
| **Nový** | Otevře dialog pro vytvoření nového posudku |
| **Kopie** | Vytvoří opakovaný posudek na základě vybraného záznamu |
| **Uložit** | Uloží posudek lokálně v IS Galen |
| **Odeslat** | Odešle posudek do systému ELP |
| **Export** | Exportuje PDF posudku – nabízí možnosti odeslání, uložení nebo otevření |
| **Zpět** | Zavře formulář |

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/assets/image-20260424-090859.png]]

### Záložky přehledu

| Záložka | Obsah | Sloupce |
| --- | --- | --- |
| **Vedené v IS Galen** | Posudky vystavené tímto IS | Datum vystavení, Typ posudku, Stav, Typ dokumentace |
| **Vedené mimo IS Galen** | Posudky z ELP registru od jiného PZS – pouze ke čtení | Datum, Typ posudku, Stav, Název PZS |

Volba **Zobrazit zneplatněné záznamy** zahrne do přehledu i zneplatněné posudky.

## Stavy posudku

Platí pro všechny typy posudků:

| Stav | Popis |
| --- | --- |
| **Připravovaný** | Uložen lokálně v IS Galen, nebyl dosud odeslán do ELP |
| **Platný** | ELP potvrdil; posudek je platný, lze zobrazit a exportovat PDF |
| **Částečně znepl.** | V rámci jednoho podání byly vytovřeny posudky pro skupinu 1 a skupinu 2. Zneplatněn byl pouze jeden posudek. |
| **Zneplatněný** | Zneplatněn v ELP |
| **Neplatný** | Zamítnut nebo jinak neplatný |

> [!warning]
> PDF posudku lze zobrazit a exportovat pouze pro posudky ve stavu **Platný** s platným datem platnosti.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/assets/obrazek-20260427-063725.png]]
