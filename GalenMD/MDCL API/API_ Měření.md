---
title: "API: Měření"
version: 1
updated_at: 2026-03-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/310214669
---

# API: Měření

> [!info]
> Toto API umožňuje externímu systému zapisovat a číst záznamy měření (dekurzu) pacienta.

Přístup vyžaduje platný Bearer token v hlavičce `Authorization`.

> [!abstract]
> ```
> Authorization: Bearer <token>
> ```

---

## Přehled endpointů

| Metoda | Endpoint | Popis |
| --- | --- | --- |
| POST | /api/Pacient/{PacientId}/Mereni | Založí nový záznam měření pacienta |
| GET | /api/Pacient/{PacientId}/Mereni/{MereniId} | Vrátí detail konkrétního záznamu měření pacienta |
| GET | /api/Pacient/{PacientId}/Mereni/Historie | Vrátí tabulkový přehled historie měření pacienta |
| DELETE | /api/Pacient/{PacientId}/Mereni/{MereniId} | Smaže měření pacienta |

---

## Obecné informace

**Formát datumu**

Pole `Datum` používá formát ISO 8601: `yyyy-MM-ddTHH:mm:ss`

Příklad: `2025-12-19T10:49:00`

**Pole**`PacientId`

ID pacienta v systému FONS Galen (**int32**). Povinný parametr URL u všech endpointů.

**Pole**`OdpovednyLekarId`

ID lékaře v systému FONS Galen (int32). Povinné pole při zápisu. Lékař musí existovat a mít oprávnění k zápisu.

**Soft-delete**

Smazání měření je vždy soft-delete – nastaví se `Deleted` (datum) a `DeletedBy` (uživatel z tokenu). Záznam zůstává v databázi.

---

## POST /api/Pacient/{PacientId}/Mereni

Založí nový záznam měření pacienta v tabulce `[Galen].[Mereni]`.

---

### Parametry URL

| Parametr | Typ | Popis |
| --- | --- | --- |
| `PacientId` | int32 | ID pacienta v systému FONS Galen |

---

### Tělo požadavku

Model: **MereniModelBase**

> [!abstract]
> ```
> {
>   "Datum": "2025-12-19T10:49:00",
>   "OdpovednyLekarId": 4989,
>
>   "Vyska": 150.00,
>   "Vaha": 50.000,
>   "Teplota": 37.0,
>
>   "TlakSystola": 120,
>   "TlakDiastola": 80,
>   "Puls": 55,
>   "Saturace": 98,
>
>   "Moc": true,
>   "Bilkovina": false,
>   "Cukr": false,
>   "Krev": false,
>   "Ketony": false,
>   "Urobilinogen": false,
>
>   "TukNadBicepsem": 50.00,
>   "TukPodLopatkou": 40.00,
>   "TukNadKostiKycelni": 30.00,
>   "TukNadTricepsem": 20.00,
>
>   "Sluch": "bez obtíží",
>   "Zrak": "bez korekce",
>   "Barvocit": "OK",
>
>   "Cholesterol": 4.800,
>   "LdlCholesterol": 2.10,
>   "CholesterolNonHdl": 3.20,
>   "Glykemie": 5.600,
>   "Hba1c": 5.40,
>   "Crp": 1.20,
>
>   "ScreeningZraku": true,
>   "Psa": 0.60,
>   "TSkore": -1.20
> }
> ```

**Povinná pole:**

| Pole | Typ | Popis |
| --- | --- | --- |
| `Datum` | string (date-time) | Datum a čas měření (ISO 8601) |
| `OdpovednyLekarId` | int32 | ID odpovědného lékaře |

**Volitelná pole:**

| Pole | Typ | Jednotka / poznámka |
| --- | --- | --- |
| `Puls` | int32, nullable | /min |
| `Vaha` | double, nullable | kg |
| `Vyska` | double, nullable | cm |
| `TlakDiastola` | int32, nullable | mmHg |
| `TlakSystola` | int32, nullable | mmHg |
| `Saturace` | int32, nullable | % |
| `Teplota` | double, nullable | °C |
| `ObvodPaze` | double, nullable | cm |
| `ObvodBricha` | double, nullable | cm |
| `ObvodBoku` | double, nullable | cm |
| `ObvodPasu` | double, nullable | cm |
| `ObvodHlavy` | double, nullable | cm |
| `ObvodHrudi` | double, nullable | cm |
| `VyskaOtce` | double, nullable | cm |
| `VyskaMatky` | double, nullable | cm |
| `Warfar` | double, nullable |  |
| `Cholesterol` | double, nullable | mmol/l |
| `Glykemie` | double, nullable | mmol/l |
| `LdlCholesterol` | double, nullable | mmol/l |
| `CholesterolNonHdl` | double, nullable | mmol/l |
| `Hba1c` | double, nullable | mmol/mol |
| `Crp` | double, nullable | mg/l |
| `Psa` | double, nullable | µg/l |
| `TSkore` | double, nullable |  |
| `ScreeningZraku` | boolean, nullable |  |
| `Moc` | boolean, nullable | NULL = nevyšetřeno |
| `Bilkovina` | boolean, nullable |  |
| `Cukr` | boolean, nullable |  |
| `Krev` | boolean, nullable |  |
| `Ketony` | boolean, nullable |  |
| `Urobilinogen` | boolean, nullable |  |
| `NitroocniTlakPraveOko` | int32, nullable | mmHg |
| `NitroocniTlakLeveOko` | int32, nullable | mmHg |
| `TukNadBicepsem` | double, nullable | mm |
| `TukPodLopatkou` | double, nullable | mm |
| `TukNadKostiKycelni` | double, nullable | mm |
| `TukNadTricepsem` | double, nullable | mm |
| `TlakPHKSystola` | int32, nullable | mmHg (pravá horní končetina) |
| `TlakPHKDiastola` | int32, nullable | mmHg (pravá horní končetina) |
| `TlakLHKSystola` | int32, nullable | mmHg (levá horní končetina) |
| `TlakLHKDiastola` | int32, nullable | mmHg (levá horní končetina) |
| `Sluch` | string, nullable | max. 255 znaků |
| `Zrak` | string, nullable | max. 255 znaků |
| `Barvocit` | string, nullable | max. 255 znaků |
| `Score` | double, nullable | Score 1 KVO – viz poznámka níže |
| `KvoScore2` | int32, nullable | Score 2 KVO – viz poznámka níže |
| `KvoScore2Riziko` | string, nullable | Nizke / Vysoke / VelmiVysoke – viz poznámka níže |

> **Poznámka k automatickému výpočtu KVO skóre:**
> Pokud request obsahuje pole `Cholesterol` nebo `CholesterolNonHdl`, server automaticky přepočítá hodnoty `Score` (Score 1 KVO), `KvoScore2` a `KvoScore2Riziko` ze serverových lookup tabulek – hodnoty případně zadané v requestu mohou být přepsány.
> Výpočet závisí na souborech `ServerResources/KVScore.csv` a `ServerResources/KvoScore2.csv` na serveru. Pokud tyto soubory nejsou nasazeny, volání vrátí **HTTP 500**.

---

### Příklad volání (curl)

> [!abstract]
> ```
> curl -X POST "https://<host>/api/Pacient/123/Mereni" \
>   -H "Authorization: Bearer <token>" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "Datum": "2025-12-19T10:49:00",
>     "OdpovednyLekarId": 4989,
>     "Vyska": 150.00,
>     "Vaha": 50.000,
>     "TlakSystola": 120,
>     "TlakDiastola": 80,
>     "Puls": 55,
>     "Saturace": 98
>   }'
> ```

---

### Odpověď

**HTTP 200 OK** – vrací kompletní **MereniModel** nově vytvořeného záznamu (viz model níže v sekci GET /Mereni/{MereniId}).

---

### Kódy odpovědí

| Kód | Popis |
| --- | --- |
| 200 | Záznam úspěšně vytvořen – vrací MereniModel |
| 400 | Chyba vstupních parametrů |
| 401 | Neautorizovaný požadavek |
| 404 | Data nebyla nalezena (pacient neexistuje) |

---

## GET /api/Pacient/{PacientId}/Mereni/{MereniId}

Vrátí detail konkrétního záznamu měření pacienta (1 záznam = 1 řádek v `[Galen].[Mereni]`).

---

### Parametry URL

| Parametr | Typ | Popis |
| --- | --- | --- |
| `PacientId` | int32 | ID pacienta v systému FONS Galen |
| `MereniId` | int64 | ID záznamu měření |

---

### Příklad volání (curl)

> [!abstract]
> ```
> curl -X GET "https://<host>/api/Pacient/123/Mereni/223339685746" \
>   -H "Authorization: Bearer <token>"
> ```

---

### Odpověď

**HTTP 200 OK** – model: **MereniModel**

> [!abstract]
> ```
> {
>   "ID": 223339685746,
>   "PacientId": 123,
>   "Datum": "2025-12-16T10:12:12",
>   "OdpovednyLekarId": 4989,
>
>   "Puls": 72,
>   "TlakSystola": 125,
>   "TlakDiastola": 80,
>   "Vyska": 180.00,
>   "Vaha": 82.500,
>   "Bmi": 25.460,
>   "Teplota": 37.0,
>   "Saturace": 98,
>
>   "Moc": true,
>   "Bilkovina": false,
>   "Cukr": false,
>   "Krev": false,
>   "Ketony": false,
>   "Urobilinogen": null,
>
>   "Cholesterol": 4.800,
>   "LdlCholesterol": 2.10,
>   "CholesterolNonHdl": 3.20,
>   "Glykemie": 5.600,
>   "Hba1c": 5.40,
>   "Crp": 1.20,
>
>   "ScreeningZraku": true,
>   "Psa": 0.60,
>   "TSkore": -1.20,
>
>   "Sluch": "bez obtíží",
>   "Zrak": "bez korekce",
>   "Barvocit": "OK",
>
>   "Popis": "Puls:72,00  Tlak:125/80  Hmotnost:82,500  Výška:180,00  BMI:25,460",
>   "Deleted": null
> }
> ```

> **Poznámka k boolean polím v odpovědi:** Pole `Bilkovina`, `Cukr`, `Krev`, `Ketony`, `Urobilinogen` se v odpovědi nevracejí, pokud je jejich hodnota `false`. Absence pole v odpovědi znamená `false` (nikoliv `null` = nevyšetřeno).

MereniModel obsahuje všechna pole MereniModelBase (viz POST endpoint) plus:

| Pole | Typ | Popis |
| --- | --- | --- |
| `ID` | int64 | ID záznamu měření |
| `PacientId` | int32 | ID pacienta |
| `Bmi` | double, nullable | Počítané pole (server) |
| `Popis` | string, nullable | Textový souhrn generovaný serverem |
| `Deleted` | boolean, nullable | Příznak smazání (false nebo null = aktivní) |

---

### Kódy odpovědí

| Kód | Popis |
| --- | --- |
| 200 | OK – vrací MereniModel |
| 400 | Chyba vstupních parametrů |
| 401 | Neautorizovaný požadavek |
| 404 | Data nebyla nalezena (pacient nebo měření neexistuje, nebo měření nepatří pacientovi) |

---

## GET /api/Pacient/{PacientId}/Mereni/Historie

Vrátí seznam záznamů měření pacienta. Každý prvek pole odpovídá jednomu záznamu v `[Galen].[Mereni]`.

---

### Parametry URL

| Parametr | Typ | Popis |
| --- | --- | --- |
| `PacientId` | int32 | ID pacienta v systému FONS Galen |

### Query parametry

| Parametr | Typ | Výchozí | Popis |
| --- | --- | --- | --- |
| `PocetDnu` | int32 | – | Počet dnů zpětně od dnešního dne (např. 365) |
| `IncludeDeleted` | boolean | false | Vrátit i smazané záznamy |
| `Mereni` | string (CSV) | – | CSV seznam položek měření pro projekci sloupců (odpovídá checkboxům v UI) |

---

### Příklad volání (curl)

> [!abstract]
> ```
> curl -X GET "https://<host>/api/Pacient/123/Mereni/Historie?PocetDnu=365&IncludeDeleted=false&Mereni=Vyska,Vaha,Teplota,Bmi,TlakSystola,TlakDiastola,Puls,Saturace" \
>   -H "Authorization: Bearer <token>"
> ```

---

### Odpověď

**HTTP 200 OK** – pole objektů **MereniModel[]**

> [!abstract]
> ```
> [
>   {
>     "ID": 223339685746,
>     "PacientId": 123,
>     "Datum": "2025-12-16T10:12:12",
>     "OdpovednyLekarId": 4989,
>     "Vyska": 180.00,
>     "Vaha": 82.500,
>     "Bmi": 25.460,
>     "Teplota": 37.0,
>     "TlakSystola": 125,
>     "TlakDiastola": 80,
>     "Puls": 72,
>     "Saturace": 98,
>     "Popis": "Puls:72,00  Tlak:125/80  Hmotnost:82,500  Výška:180,00  BMI:25,460",
>     "Deleted": null
>   }
> ]
> ```

Vrácená pole v každém záznamu odpovídají modelu **MereniModel**. Položky, které nebyly zahrnuty v parametru `Mereni`, mohou být `null`.

---

### Kódy odpovědí

| Kód | Popis |
| --- | --- |
| 200 | OK – vrací MereniModel[] |
| 400 | Chyba vstupních parametrů |
| 401 | Neautorizovaný požadavek |
| 404 | Data nebyla nalezena (pacient neexistuje) |

---

## DELETE /api/Pacient/{PacientId}/Mereni/{MereniId}

Smaže záznam měření pacienta (soft-delete – nastaví `Deleted` a `DeletedBy` v tabulce `[Galen].[Mereni]`).

---

### Parametry URL

| Parametr | Typ | Popis |
| --- | --- | --- |
| `PacientId` | int32 | ID pacienta v systému FONS Galen |
| `MereniId` | int64 | ID záznamu měření (`[Galen].[Mereni].ID`) |

---

### Příklad volání (curl)

> [!abstract]
> ```
> curl -X DELETE "https://<host>/api/Pacient/123/Mereni/223339685746" \
>   -H "Authorization: Bearer <token>"
> ```

---

### Odpověď

**HTTP 204 No Content** – žádné tělo odpovědi.

---

### Kódy odpovědí

| Kód | Popis |
| --- | --- |
| 204 | Záznam úspěšně smazán |
| 400 | Chyba vstupních parametrů |
| 401 | Neautorizovaný požadavek |
| 404 | Data nebyla nalezena (pacient nebo měření neexistuje, nebo měření nepatří pacientovi) |
| 409 | Dokumentace je uzamčena |
