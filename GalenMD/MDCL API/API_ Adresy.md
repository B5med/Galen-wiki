---
title: "API: Adresy"
version: 1
updated_at: 2025-07-08
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/66093057
---

> [!info]
> Toto API slouží pro správu adres evidovaných u konkrétního pacienta. Umožňuje načíst seznam adres, upravovat jednotlivé adresy a pracovat s jejich typy (např. trvalý pobyt, korespondenční adresa apod.).

### Obecné informace

**Typy adresy (TypAdresy):**
Pole může nabývat hodnot např.:

- `TrvalyPobyt` – adresa trvalého pobytu
- `Kontaktni` – kontaktní adresa

**Stát:**
Hodnoty odpovídají mezinárodním kódům zemí, např. `CZ`, `SK`, `DE`, `AT` apod.

---

## 🧾 GET `/api/Pacient/{PacientId}/Adresy`

**Popis:**
Vrací seznam všech adres evidovaných u daného pacienta.

**Parametry:**

- `PacientId` – ID pacienta

**Odpověď (pole**`AdresaModel`**):**

- `ID` – identifikátor adresy
- `Ulice` – název ulice
- `CisloPopisne` – číslo popisné
- `CisloOrientacni` – číslo orientační (nepovinné)
- `Obec` – název obce
- `PSC` – poštovní směrovací číslo
- `Stat` – stát (např. `CZ`)
- `TypAdresy` – typ adresy (např. `TrvalyPobyt`)
- `CisloEvidencni` – evidenční číslo (volitelné)

**Kódy odpovědi:**

- `200 OK` – úspěšné načtení seznamu
- `400 Bad Request` – nevalidní ID pacienta
- `401 Unauthorized` – chybějící nebo neplatná autorizace

---

## 📝 PUT `/api/Pacient/{PacientId}/Adresa/{AdresaId}`

**Popis:**
Upraví zadanou adresu pacienta.

**Parametry:**

- `PacientId` – ID pacienta (v URL cestě)
- `AdresaId` – ID adresy, která se má upravit
- Tělo požadavku (`InsertUpdateAdresaModel`):

   - `Ulice` – název ulice
   - `CisloPopisne` – číslo popisné
   - `CisloOrientacni` – číslo orientační
   - `Obec` – název obce
   - `PSC` – poštovní směrovací číslo
   - `Stat` – kód státu
   - `TypAdresy` – typ adresy
   - `CisloEvidencni` – evidenční číslo

**Validace:**

- Povinná pole: `Ulice`, `CisloPopisne`, `Obec`, `PSC`, `Stat`, `TypAdresy`
- `PSC` musí odpovídat validnímu formátu (např. 5 číslic pro `CZ`)
- `TypAdresy` musí být z definované množiny (např. `TrvalyPobyt`, `Kontaktni` …)

**Kódy odpovědi:**

- `200 OK` – adresa byla upravena
- `400 Bad Request` – chybná data, adresa neexistuje nebo není svázána s pacientem
- `401 Unauthorized` – chybějící přístupová oprávnění
