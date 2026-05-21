---
title: "API: Zaměstnání"
version: 1
updated_at: 2025-07-28
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/82214913
---

> [!info]
> Toto API slouží pro správu zaměstnání evidovaných u konkrétního pacienta. Umožňuje načíst seznam aktuálních zaměstnání, založit nové a upravit stávající záznamy. Záznamy jsou navázány na společnosti (firmy), jejich pobočky a případně na pracovní skupinu PLS.

### Obecné informace

**Pozice (Pozice):**
Textový popis pracovní pozice, např. *technik*, *asistent*, *řidič*.

**Společnost (Firma):**
Identifikována pomocí IČO a názvu. Pokud firma ještě neexistuje, je automaticky založena.

**Pobočka (PobockaId):**
Odkaz na konkrétní provozovnu firmy. Pokud není uvedena, použije se centrála.

**Skupina PLS (SkupinaPlsId):**
Volitelný odkaz na evidovanou skupinu pracovně-lékařských služeb.

**Datumy:**

- *ZamestnanOd* – datum nástupu ve formátu DDMMYYYY
- *ZamestnanDo* – datum ukončení, volitelné

---

### 🧾 GET /api/Pacient/{PacientId}/Zamestnani

**Popis:**
Vrací seznam všech aktuálních zaměstnání daného pacienta.

**Parametry:**

- `PacientId` – ID pacienta

**Odpověď (pole ZamestnaniDetailModel):**

- ID – identifikátor záznamu
- Pozice – název pracovní pozice
- SpolecnostICO – IČO firmy
- SpolecnostNazev – název firmy
- ZamestnanOd – datum nástupu (DDMMYYYY)
- ZamestnanDo – datum ukončení (nepovinné)
- Poznamka – poznámka k pracovnímu poměru
- PobockaId – ID pobočky
- SkupinaPlsId – ID skupiny PLS (nepovinné)

**Kódy odpovědi:**

- 200 OK – úspěšné načtení
- 400 Bad Request – nevalidní ID pacienta
- 401 Unauthorized – chybějící nebo neplatná autorizace

---

### 📝 POST /api/Pacient/{PacientId}/Zamestnani

**Popis:**
Založí nové zaměstnání pacienta. Firma i pobočka se případně založí automaticky.

**Parametry:**

- `PacientId` – ID pacienta

**Tělo požadavku (InsertZamestnaniModel):**

- SpolecnostICO – IČO firmy
- SpolecnostNazev – název firmy
- PobockaId – ID pobočky
- SkupinaPlsId – ID skupiny PLS
- Pozice – pracovní pozice
- ZamestnanOd – datum nástupu
- ZamestnanDo – datum ukončení
- Poznamka – poznámka

**Validace:**

- Povinná pole: SpolecnostICO, SpolecnostNazev, ZamestnanOd, Pozice
- Datum ve formátu DDMMYYYY
- Pokud firma existuje a není uvedeno `PobockaId`, musí být zadáno

**Kódy odpovědi:**

- 200 OK – úspěšné založení
- 400 Bad Request – neplatná data
- 401 Unauthorized – chybějící oprávnění

---

### 📝 PUT /api/Pacient/{PacientId}/Zamestnani/{ZamestnaniId}

**Popis:**
Upraví existující zaměstnání pacienta.

**Parametry:**

- `PacientId` – ID pacienta
- `ZamestnaniId` – ID zaměstnání

**Tělo požadavku (UpdateZamestnaniModel):**

- SkupinaPlsId – ID skupiny PLS
- Pozice – upravená pozice
- ZamestnanDo – datum ukončení
- Poznamka – poznámka

**Validace:**

- Datum ve formátu DDMMYYYY
- Pokud je zadaný `SkupinaPlsId`, musí existovat v systému

**Kódy odpovědi:**

- 200 OK – úspěšná aktualizace
- 400 Bad Request – chybná data nebo neexistující záznam
- 401 Unauthorized – chybějící oprávnění
