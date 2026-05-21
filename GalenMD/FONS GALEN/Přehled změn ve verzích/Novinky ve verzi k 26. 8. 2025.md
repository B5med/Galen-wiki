---
title: "Novinky ve verzi k 26. 8. 2025"
version: 2
updated_at: 2025-09-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/103219202
---

# Novinky ve verzi k 26. 8. 2025

# 💊 Změna preskripčních omezení u léků se symbolem **„L“**

Galen zohledňuje novelu vyhlášky č. 376/2011 Sb. platnou od 1. 7. 2024.

---

## 🔹 Co se mění

- **Praktičtí lékaři (001) a pediatři (002)**

   - Pokud lék se symbolem **„L“** **nemá další omezení v příbalové informaci**, lze jej předepsat **přímo s úhradou pojišťovny**.
   - Pokud lék **další omezení má**, Galen:

      1. zobrazí **okno pro výběr doporučujícího lékaře**,
      2. následně upozorní na preskripční omezení.
- **Ostatní odbornosti**

   - Chování zůstává beze změny – platí původní pravidla.
- **Samoplátci**

   - Léky se symbolem **„L“** se jim vždy předepisují s úhradou **Pacient**.

---

## 📋 Praktické příklady

| Léčivý přípravek | Odbornost | Omezení | Chování v Galenu |
| --- | --- | --- | --- |
| **VESSEL DUE F (0225450)** | Praktik / Pediatr | Bez dalšího omezení | Předepíše se přímo s úhradou pojišťovny, **bez dialogu** |
| **jiný lék se symbolem „L“ + omezení** | Praktik / Pediatr | Omezení v příbalové informaci | Zobrazí se dialog „Spolupracující lékař“ + upozornění |
| **libovolný lék se symbolem „L“** | Ostatní odbornost | libovolné | Chování beze změny – kontrola jako dosud |
| **libovolný lék se symbolem „L“** | Samoplátce | libovolné | Úhrada vždy „Pacient“ |

## Opravy chyb

- **Oprava podrobného filtru**
   Opravili jsme chování tisku a exportu v kartotéce, kdy se na některých instalacích ignoroval podrobný filtr a tiskla se celá kartotéka. Nově se při tisku i exportu vždy správně uplatní nastavený filtr a do výstupu se dostanou pouze vybraní pacienti.
- **Oprava chyby u biometrického podpisu**

   Chyba týkající se biometrického podpisu byla opravena a funkčnost je nyní obnovena. K chybě došlo na straně dodavatele.
- **Oprava API**
   Hodnoty vrácené v datech nyní používají stejnou časovou zónu (Europe/Prague). Díky tomu jsou výsledky konzistentní a odpovídají skutečnému času provedené změny.
