---
title: "API: PLS Pobočky, Skupiny"
version: 2
updated_at: 2025-07-28
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/82214922
---

> [!info]
> Toto API vrací seznam poboček a pracovních skupin PLS evidovaných u dané firmy.
> Slouží jako referenční seznam při zakládání nebo úpravě zaměstnání pacienta – konkrétní pobočka firmy určuje fyzické místo výkonu práce a pracovní skupina PLS definuje specifické rizikové podmínky nebo pracovní zařazení z pohledu pracovně-lékařských služeb.

### GET /api/Firma/{FirmaId}/Pobocky

**Popis:**
Vrací seznam všech poboček firmy.

**Parametry:**

- `FirmaId` – ID firmy

**Odpověď (pole PobockaDetailModel):**

- ICO – IČO firmy
- Nazev – název pobočky
- Adresa – ulice a číslo
- Obec – město
- PSC – poštovní směrovací číslo
- Stat – stát (např. CZ)

**Kódy odpovědi:**

- 200 OK – úspěšné načtení
- 400 Bad Request – firma neexistuje
- 401 Unauthorized – neplatné oprávnění

---

### 🧾 GET /api/Firma/{FirmaId}/Skupiny-pls

**Popis:**
Vrací seznam skupin pracovně-lékařských služeb firmy.

**Parametry:**

- `FirmaId` – ID firmy

**Odpověď (pole SkupinaPlsDetailModel):**

- ID – identifikátor skupiny
- Nazev – název skupiny

**Kódy odpovědi:**

- 200 OK – úspěšné načtení
- 400 Bad Request – firma neexistuje
- 401 Unauthorized – neplatné oprávnění
