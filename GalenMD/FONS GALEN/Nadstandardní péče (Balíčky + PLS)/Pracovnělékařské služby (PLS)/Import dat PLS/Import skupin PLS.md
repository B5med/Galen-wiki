---
title: "Import skupin PLS"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/435912707
---

# Import skupin PLS

Slouží k hromadnému zakládání pracovních pozic (skupin) pro danou firmu včetně přiřazení rizik. Alternativou je ruční zadání přímo v detailu firmy.

## Předpoklady

- Firma musí být v systému **již založena** (včetně IČO).
- Firma musí mít **alespoň jednu pobočku**.
- Import skupin se provádí **vždy před importem smluv** a pacientů.

## Formát souboru

| Parametr | Hodnota |
| --- | --- |
| Přípona | .csv |
| Kódování | Windows-1250 |
| Oddělovač | středník ; |
| Hlavičkový řádek | povinný (přesně dle vzoru) |
| Počet sloupců | 6 |
| Jeden řádek | jedna pracovní pozice (skupina) |

## Sloupce

| # | Název sloupce v hlavičce | Povinnost | Popis |
| --- | --- | --- | --- |
| 1 | `ICO` | **povinný** | IČO firmy v systému (bez mezer, bez teček) |
| 2 | `Pozice` | **povinný** | Název skupiny PLS / pracovní pozice (max 100 znaků) |
| 3 | `Kategorie název` | **povinný** | Přesný název kategorie z číselníku Rizika → záložka Kategorie |
| 4 | `Rizikový faktor pracovních podmínek název (volitelné)` | volitelný | Přesný název z číselníku Rizika → záložka Rizikové faktory pracovních podmínek |
| 5 | `Profesní riziko název (volitelné)` | volitelný | Přesný název z číselníku Rizika → záložka Profesní rizika |
| 6 | `Speciální název (volitelné)` | volitelný | Přesný název z číselníku Rizika → záložka Speciální |

> [!warning]
> Volitelné sloupce se vyplníují pouze tehdy, je-li riziko relevantní. Pokud ne, pole se ponechá prázdné — středníky zůstávají.

## Vzor souboru

> [!abstract]
> ```
> ICO;Pozice;Kategorie název;Rizikový faktor pracovních podmínek název (volitelné);Profesní riziko název (volitelné);Speciální název (volitelné)
> 00637327;Skladník;Kategorie II;Prašné prostředí;Práce ve výškách;
> 00637327;Řidič;Kategorie III;Hluk;Řidič referent;
> 00637327;Administrativa;Kategorie I;;;
> 00637327;Svářeč;Kategorie III;Ionizující záření;Nakládání s výbušninami;
> 00637327;Technik;Kategorie II;Zraková zátěž;;
> ```

## Postup importu v aplikaci

1. Otevři detail firmy → záložka nebo sekce **Import**.
2. Zvol typ importu: **Import skupin PLS**.
3. Klikni na **„…“** a vyber připravený CSV soubor.
4. Zkontroluj, že je zvolen správný **Režim** (standardně „Pouze doplňení“).
5. Stiskni **Importovat**.
6. Zkontroluj výsledek — systém zobrazí potvrzení nebo seznam chyb s číslem řádku.

## Chování systému

| Situace | Co systém udělá |
| --- | --- |
| Pozice se stejným názvem **neexistuje** | Založí novou skupinu PLS a přiřadí jí rizika z CSV. |
| Pozice se stejným názvem **existuje** | Název ponechá beze změny. Rizika **přepíše** — odstraní stávající a zapíše nová dle CSV. |
| Shoda názvu se vyhodnocuje | Case-insensitive, diakritika se ignoruje (např. „skladnik“ = „Skladník“). |
| Název rizika **nenalezen** v číselníku | Chyba importu — zobrazí se číslo řádku a popis chyby. |

> [!danger]
> Rizika existující skupiny jsou při reimportu **celá přepsána**. Před reimportem zkontroluj, zda CSV obsahuje kompletní sadu rizik pro danou pozici.

## Platné hodnoty rizik

Hodnoty musí přesně odpovídat názvům v číselníku **Rizika práce** v systému. Níže jsou hodnoty z testovacího prostředí — v produkci ověř aktuální číselník.

**Kategorie (povinná):** Kategorie I · Kategorie II · Kategorie III · Kategorie IV · Kategorie IIR · Kat I · Kat II · Kat. 2R · J_Kategorie_I · Největší

**Rizikový faktor pracovních podmínek (volitelný):** Atmosférický přetlak · Hluk · Ionizující záření · Prašné prostředí · Prašnost · Zraková zátěž

**Profesní riziko (volitelné):** Nakládání s výbšninami · Obsluha nebo opravy tlakových nádob · Obsluha řídících center a velínů · Práce ve výškách · Řidič referent

**Speciální (volitelné):** V testovacím prostředí bez aktivních hodnot. Ověř aktuální číselník v produkci.

## Časté chyby

| Chybová hláška | Příčina | Řešení |
| --- | --- | --- |
| Soubor obsahuje nesprávný počet sloupců | Chybí nebo přebývá sloupec, chybí hlavičkový řádek, špatný oddělovăč | Zkontroluj, zda soubor má přesně 6 sloupců oddělených ; a hlavičkový řádek. |
| Chyba na řádku X — riziko nenalezeno | Název kategorie, FP nebo OZ neodpovídá žádné hodnotě v číselníku | Ověř přesný název v Rizika práce a oprav CSV. |

> [!tip]
> Úspěšný import zobrazí hlášení **„Import úspěšně dokončen“** bez seznamu chyb.
