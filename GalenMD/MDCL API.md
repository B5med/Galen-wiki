---
title: "MDCL API"
version: 2
updated_at: 2025-07-08
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/66093066
---

# MDCL API

REST API pro práci s pacientem, jeho kontakty a adresami v systému Galen. API obsahuje validace vůči číselníkům a povinným hodnotám. Všechny požadavky (POST/PUT/DELETE) vyžadují autorizaci typu:

> [!abstract]
> ```
> Authorization: Bearer {token}
> Content-Type: application/json
> ```
