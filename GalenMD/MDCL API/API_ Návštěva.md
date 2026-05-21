---
title: "API: Návštěva"
version: 1
updated_at: 2026-03-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/309657607
---

> [!info]
> Toto API umožňuje externímu systému zapsat záznam návštěvy přímo do dekurzu pacienta.

Přístup vyžaduje platný Bearer token v hlavičce `Authorization`.

> [!abstract]
> ```
> Authorization: Bearer <token>
> ```

---

## Obecné informace

**Formát datumu**

Pole `datumCas` používá formát ISO 8601:

> [!abstract]
> ```
> yyyy-MM-ddTHH:mm:ss
> ```

Příklad: `2025-03-18T09:00:00`

---

**Hodnoty pole**`typNavstevy`

| Hodnota | Popis |
| --- | --- |
| `Navsteva` | Standardní lékařská návštěva |
| `Pristroj` | Návštěva zaznamenaná přístrojem |

---

**Pole**`diagnozy`

Pole `diagnozy` je nepovinné pole kódů diagnóz (např. `["J069", "Z000"]`).

---

**Pole**`odpovednyLekarId`

ID lékaře v systému FONS Galen. Povinné pole.

---

## POST /api/Pacient/{PacientId}/Navsteva

Zapíše nový záznam návštěvy do dekurzu pacienta.

**Autorizace:** `PacientSpravaAPI`

---

### Parametry URL

| Parametr | Typ | Popis |
| --- | --- | --- |
| `PacientId` | int64 | ID pacienta v systému FONS Galen |

---

### Tělo požadavku

> [!abstract]
> ```
> {
>   "datumCas": "2025-03-18T09:00:00",
>   "typNavstevy": "Navsteva",
>   "diagnozy": ["J069"],
>   "nalez": "Pacient bez obtíží.",
>   "mereniId": null,
>   "poznamka": "Kontrolní návštěva.",
>   "odpovednyLekarId": 42
> }
> ```

| Pole | Typ | Povinné | Popis |
| --- | --- | --- | --- |
| `datumCas` | datetime | ano | Datum a čas návštěvy (ISO 8601) |
| `typNavstevy` | string | ano | Typ záznamu: `Navsteva`  nebo `Pristroj` |
| `diagnozy` | string[] | ne | Pole kódů diagnóz |
| `nalez` | string | ano | Textový nález |
| `mereniId` | int64 | ne | ID záznamu měření; vyplnit, pokud je návštěva provázána s konkrétním měřením |
| `poznamka` | string | ne | Volná poznámka |
| `odpovednyLekarId` | int32 | ano | ID odpovědného lékaře |

---

### Příklad volání (curl)

> [!abstract]
> ```
> curl -X POST "https://<host>/api/Pacient/123/Navsteva" \
>   -H "Authorization: Bearer <token>" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "datumCas": "2025-03-18T09:00:00",
>     "typNavstevy": "Navsteva",
>     "diagnozy": ["J069"],
>     "nalez": "Pacient bez obtíží.",
>     "odpovednyLekarId": 42
>   }'
> ```

---

### Odpověď

**HTTP 200 OK**

> [!abstract]
> ```
> {
>   "id": 98765,
>   "datumCas": "2025-03-18T09:00:00",
>   "typNavstevy": "Navsteva",
>   "diagnozy": ["J069"],
>   "nalez": "Pacient bez obtíží.",
>   "mereniId": null,
>   "poznamka": null,
>   "odpovednyLekarId": 42
> }
> ```

| Pole | Typ | Popis |
| --- | --- | --- |
| `id` | int64 | ID nově vytvořeného záznamu návštěvy |

---

### Kódy odpovědí

| Kód | Popis | Příklad těla odpovědi |
| --- | --- | --- |
| 200 | Záznam úspěšně vytvořen | Viz model výše |
| 400 | Chybí nebo je neplatné povinné pole | `{ "errors": { "typNavstevy": ["The typNavstevy field is required."] } }` |
| 401 | Neplatný nebo chybějící Bearer token | *(prázdné tělo)* |
| 404 | Pacient s daným PacientId neexistuje | `{ "message": "Pacient nenalezen." }` |
