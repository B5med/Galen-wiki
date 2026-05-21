---
title: "API: Pacient"
version: 1
updated_at: 2025-07-08
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/65994755
---

> [!info]
> Toto API slouží pro správu základních údajů o pacientech. Umožňuje načítat, zakládat a upravovat kartu pacienta na základě čísla pojištěnce nebo ID pacienta.

### Obecné informace

**Formát data narození:**
`ddMMyyyy` (např. `08102005`)

**Pohlaví:**

- `Muz`
- `Zena`
- `Neuvedeno`

**DruhPojištění (DruhPojisteni):**
Typ pojištění, obvykle:

- `1` – veřejné
- `2` – komerční
- `3` – samoplátce

**Pojišťovna:**
Kód pojišťovny – např.

- `111` – VZP
- `201`, `205`, ... dle seznamu pojišťoven
- `999` – samoplátce

**Stát:**
Dle mezinárodních kódů: `CZ`, `SK`, `DE`, `UA`, …

---

### POST `/api/Pacient/Pacient`

**Popis:**
Založí novou kartu pacienta.

**Tělo požadavku (JSON):**

> [!abstract]
> ```
> {
>   "CisloPojistence": "string",
>   "Prijmeni": "string",
>   "Jmeno": "string",
>   "TitulPred": "string",
>   "TitulZa": "string",
>   "DatumNarozeni": "string",
>   "Pohlavi": "string",
>   "DruhPojisteni": "string",
>   "Pojistovna": "string",
>   "Stat": "string",
>   "RodnePrijmeni": "string",
>   "ObcanskyPrukaz": "string",
>   "HesloProKomunikaci": "string"
> }
> ```

**Validace:**

- Povinná pole: `CisloPojistence`, `Prijmeni`, `Jmeno`, `DatumNarozeni`, `Pohlavi`, `Pojistovna`, `Stat`
- `CisloPojistence`: rodné číslo bez lomítka (např. `"0510087336"`)
- `DatumNarozeni`: formát `ddMMyyyy`
- `Pohlavi`: `"Muz"`, `"Zena"`, `"Neuvedeno"`

**Kódy odpovědi:**

- `200 OK` – pacient úspěšně založen
- `400 Bad Request` – chyba ve vstupních datech
- `401 Unauthorized` – přístup zamítnut

### GET `/api/Pacient/Pacient?CisloPojistence={cislo}`

**Popis:**
Vrací údaje o pacientovi podle zadaného čísla pojištěnce.

**Parametry:**

- `CisloPojistence` (string) – rodné číslo bez lomítka

**Model odpovědi:**

> [!abstract]
> ```
> {
>   "ID": 0,
>   "CisloPojistence": "string",
>   "Prijmeni": "string",
>   "Jmeno": "string",
>   "TitulPred": "string",
>   "TitulZa": "string",
>   "DatumNarozeni": "string",
>   "Pohlavi": "string",
>   "DruhPojisteni": "string",
>   "Pojistovna": "string",
>   "Stat": "string",
>   "RodnePrijmeni": "string",
>   "ObcanskyPrukaz": "string",
>   "HesloProKomunikaci": "string"
> }
> ```

## **Kódy odpovědi:**

- `200 OK` – pacient nalezen
- `400 Bad Request` – chybné parametry
- `401 Unauthorized` – přístup zamítnut

### PUT `/api/Pacient/Pacient/{Id}`

**Popis:**
Aktualizuje údaje pacienta podle ID.

**Parametry:**

- `Id` (integer) – ID pacienta

**Tělo požadavku:**
Stejné jako u POST.

**Kódy odpovědi:**

- `200 OK` – aktualizace proběhla úspěšně
- `400 Bad Request` – chyba ve vstupních datech
- `401 Unauthorized` – přístup zamítnut
