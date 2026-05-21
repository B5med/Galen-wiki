---
title: "API: Kontakty pacienta"
version: 1
updated_at: 2025-07-08
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/65306627
---

# API: Kontakty pacienta

> [!info]
> Toto API slouží pro správu kontaktů evidovaných u konkrétního pacienta v systému. Umožňuje načíst seznam kontaktů, přidávat nové, upravovat existující a také je mazat.

Obecné informace

**Typy kontaktů:**
Pole `Typ` nabývá hodnot podle typu kontaktu – např. `mobil`, `telefon`, `email`.

> [!warning]
> Hodnoty je nutné dodržet přesně podle enum definice systému.

**Primární kontakt:**
Každý pacient může mít právě jeden primární kontakt daného typu. Pokud přidáš další a nastavíš ho jako primární, měl by systém ten předchozí upravit na neprimární (není-li řešeno automaticky, je nutné validací ošetřit).

**Neplatný kontakt:**
Kontakty označené jako `Neplatny = true` jsou považovány za neaktivní a nejsou nadále používány (např. při výběru kontaktu pro odeslání notifikací).

## 📥 POST `/api/Pacient/{PacientId}/Kontakt`

**Popis:**
Přidá nový kontakt k danému pacientovi.

**Parametry:**

- `PacientId` – ID pacienta (v URL cestě)
- Tělo požadavku (`InsertUpdateKontaktModel`):

   - `Typ` – typ kontaktu (např. `mobil`, `email`)
   - `Hodnota` – konkrétní údaj (např. číslo, e-mail)
   - `Primarni` – boolean, zda se jedná o hlavní kontakt
   - `Neplatny` – boolean, zda je kontakt neplatný
   - `Poznamka` – doplňkový popis (volitelné)

**Validace:**

- `Typ` a `Hodnota` jsou povinné.
- `Hodnota` nesmí být prázdná.
- V kombinaci s příznakem `Primarni` nesmí existovat jiný aktivní primární kontakt daného typu.

**Kódy odpovědi:**

- `200 OK` – kontakt byl přidán
- `400 Bad Request` – chybný vstup, duplicitní nebo nevalidní kombinace dat
- `401 Unauthorized` – chybějící nebo neplatný přístupový token

## 🧾 GET `/api/Pacient/{PacientId}/Kontakty`

**Popis:**
Vrací seznam všech kontaktů daného pacienta.

**Parametry:**

- `PacientId` – ID pacienta (v URL cestě)

**Odpověď (pole**`KontaktDetailModel`**):**

- `ID` – identifikátor kontaktu
- `Typ` – typ kontaktu (`mobil`, `telefon`, `email`, …)
- `Hodnota` – hodnota kontaktu (např. telefonní číslo, e-mail)
- `Primarni` – zda je kontakt označen jako primární
- `Neplatny` – zda je kontakt označen jako neplatný
- `Poznamka` – doplňková poznámka

**Kódy odpovědi:**

- `200 OK` – úspěšné načtení seznamu
- `400 Bad Request` – nevalidní ID pacienta
- `401 Unauthorized` – chybějící nebo neplatná autorizace

## 📝 PUT `/api/Pacient/{PacientId}/Kontakt/{KontaktId}`

**Popis:**
Upraví existující kontakt pacienta.

**Parametry:**

- `PacientId` – ID pacienta (v URL cestě)
- `KontaktId` – ID kontaktu, který se má upravit
- Tělo požadavku: viz POST

**Validace:**

- Kontakt musí existovat a patřit danému pacientovi.
- Při označení kontaktu jako `Primarni` nesmí být v systému jiný aktivní primární kontakt téhož typu.

**Kódy odpovědi:**

- `200 OK` – kontakt byl upraven
- `400 Bad Request` – chybná data nebo kontakt neexistuje
- `401 Unauthorized` – neautorizovaný požadavek

## ❌ DELETE `/api/Pacient/{PacientId}/Kontakt/{KontaktId}`

**Popis:**
Smaže zadaný kontakt pacienta.

**Parametry:**

- `PacientId` – ID pacienta
- `KontaktId` – ID kontaktu, který se má smazat

**Kódy odpovědi:**

- `204 No Content` – kontakt byl úspěšně odstraněn
- `400 Bad Request` – kontakt neexistuje nebo nepatří zadanému pacientovi
- `401 Unauthorized` – chyba autorizace
