---
title: "Novinky ve verzi k 25. 8. 2026"
version: 1
updated_at: 2026-08-24
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/556826629
---

# Novinky ve verzi k 25. 8. 2026

# Novinky a vylepšení

---

## ePoukaz

### ePoukaz – nová verze rozhraní

Od 1. 9. 2026 FONS Galen komunikuje se SÚKL v nové verzi datového rozhraní ePoukaz. Nové rozhraní zahrnuje tyto změny:

***Párový orgán***

Na položce ePoukazu přibyla nová možnost „Párový orgán“ (Pravý/Levý/Oba) – vyplňuje se u úhradových skupin, kde to vyžaduje legislativa (např. 04.07.01.01 – Obuv pooperační a odlehčovací).

***Šířka a hloubka sedu invalidního vozíku***

Na ePoukazu – léčebný lze pro úhradové skupiny 07.01.01.* a 07.01.02.* nově zadat šířku a hloubku sedu v cm; bez vyplnění nelze ePoukaz odeslat.

***Ověření množstevního/úhradového limitu***

U položky ePoukazu přibylo tlačítko „Ověřit limity“ – zavolá novou službu SÚKL a zobrazí odpověď (upozornění na překročení limitu i seznam předchozích výdejů).

Více informací: [[ePoukaz – změny platné od 1. 9. 2026]]

## Vyúčtování a fakturace

### Zobrazení názvu banky a předvyplnění bankovního účtu při vystavování externí faktury

V dialogu pro vystavení externí faktury se nyní u výběru bankovního spojení v rozbalovacím seznamu zobrazuje i název banky, nejen číslo účtu – díky tomu lze účet bezpečně rozpoznat na první pohled, aniž by bylo nutné ho dohledávat podle čísla.

Pole s bankovním účtem se navíc automaticky předvyplní podle následující priority:

1. účet naposledy použitý přihlášeným pracovníkem na daném pracovišti,
2. pokud takový není, účet naposledy použitý kýmkoli na daném pracovišti,
3. jinak se předvyplní první aktivní bankovní účet společnosti ze seznamu bankovních spojení.

Výběr účtu zůstává i nadále zcela volný – předvyplněná hodnota slouží jen jako usnadnění, uživatel si může vybrat kterýkoli jiný účet ze seznamu.

## Stav účtu pacienta

### Celkový součet útraty pacienta

Na kartě Stav účtu pacienta se v seznamech **Příjmové doklady** a **Faktury** nově v hlavičce sloupce **Částka** zobrazuje součet všech nestornovaných dokladů. Celkovou útratu pacienta tak vidíte na první pohled, bez ručního sčítání jednotlivých dokladů.
