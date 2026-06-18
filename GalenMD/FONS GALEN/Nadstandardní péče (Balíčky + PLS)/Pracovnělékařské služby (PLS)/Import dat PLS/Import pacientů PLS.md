---
title: "Import pacientů PLS"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/435617798
---

# Import pacientů PLS

Slouží k hromadnému přiřazení zaměstnanců firem do modulu PLS — vytvoří nebo aktualizuje záznamy zaměstnání (PacientZamestnani) včetně přiřazení skupiny PLS, osobního čísla, střediska a dalších pracovních údajů. Pacient musí v systému existovat, nebo je při importu automaticky vytvořen dle RČ.

> [!info]
> Krok 3 z pořadí importů: **skupiny PLS → smlouvy PLS → pacienti PLS**. Skupiny i smlouvy musí existovat před importem pacientů.

## Předpoklady

- Firma musí být v systému **již založena** (včetně IČO).
- Firma musí mít **alespoň jednu pobočku**.
- **Skupiny PLS** musí být v systému již založeny.
- Import pacientů se provádí **po importu skupin a smluv PLS**.

## Dva režimy importu

| Režim | Popis | Počet sloupců |
| --- | --- | --- |
| **Pouze doplňení** | Soubor obsahuje IČO a Pobočka název (sloupce 1–2). Importuje pacienty ke kterékoli firmě v souboru. Existující záznamy pouze aktualizuje, nic neodstraní. | 25 |
| **Doplňení i odstranění** | Soubor neobsahuje IČO ani Pobočka název. Firma se vybere v UI před importem. Pacienty chybějící v souboru ukončí (nastaví ZaměstnánDo). | 23 |

> [!danger]
> Režim **Doplňení i odstranění** automaticky ukončí zaměstnání všech pacientů firmy, kteří nejsou v importním souboru. Používej jej jen tehdy, když soubor obsahuje *kompletní* aktuální seznam zaměstnanců.

## Sloupce — Pouze doplňení (25 sloupců)

| # | Název sloupce | Povinnost | Popis / povolené hodnoty |
| --- | --- | --- | --- |
| 1 | IČO | **povinný** (jen tento režim) | IČO firmy (bez mezer, bez teček) |
| 2 | Pobočka název | **povinný** (jen tento režim) | Přesný název pobočky firmy v systému |
| 3 | Příjmení | **povinný** | Příjmení pacienta |
| 4 | Jméno | **povinný** | Jméno pacienta |
| 5 | Pohlaví | **povinný** | M — muž · Z — žena · N — neuvedeno |
| 6 | Datum narození RČ | **povinný** | Formát dd.MM.yyyy |
| 7 | RČ | **povinný** | Rodné číslo (číslice, bez lomítka, 9 nebo 10 znaků) — klíč pro identifikaci/párování pacienta |
| 8 | stávající skupina PLS | volitelný | Název skupiny PLS, ve které je pacient aktuálně zařazen — pro identifikaci záznamu při aktualizaci |
| 9 | Nová Skupina PLS | volitelný | Cílová skupina PLS po importu. Pro nové pacienty uveď skupinu zde. Musí existovat v systému. |
| 10 | Pozice | volitelný | Volný text — pracovní pozice zaměstnance (nezávislá na skupině PLS) |
| 11 | Zaměstnán od | **povinný** | Formát dd.MM.yyyy |
| 12 | Zaměstnán do | volitelný | Formát dd.MM.yyyy. Prázdné = aktivní. |
| 13 | Výsledek poslední prohlídky | volitelný | Z způsobilý · N nezpůsobilý · K způsobilý s podmínkou s kompenzací · M způsobilý s podmínkou mimo kompenzaci · D pozbyl způsobilost dlouhodobě · B uzavřeno bez posudku · X nedostavil se |
| 14 | Datum platnosti posudku | volitelný | Formát dd.MM.yyyy |
| 15 | Osobní číslo | volitelný | Max 30 znaků |
| 16 | Středisko | volitelný | Název nebo kód střediska (max 255 znaků) |
| 17 | Mobil | volitelný | Telefonní číslo |
| 18 | e-Mail | volitelný | E-mailová adresa |
| 19 | Ulice | volitelný | Ulice bydliště |
| 20 | Č. popisné | volitelný | Číslo popisné |
| 21 | Č. orientační | volitelný | Číslo orientační |
| 22 | PSČ | volitelný | Poštovní směrovací číslo |
| 23 | Obec | volitelný | Název obce bydliště |
| 24 | Pozastaveno | volitelný | Ne — aktivní · MdRd — MD+RD · Dpn — DPN · Jine — jiný důvod. Prázdné = Ne. |
| 25 | Hodnost | volitelný | Z číselníku Hodnost PLS |

> [!warning]
> **Sloupce 8 a 9 — zařazení do skupiny PLS:**
>
> - **Nový pacient:** sloupec 8 prázdný, do sloupce 9 uveď cílovou skupinu.
> - **Přesun do jiné skupiny:** sloupec 8 = stávající skupina (identifikace záznamu), sloupec 9 = nová skupina.
> - **Aktualizace dat bez změny skupiny:** sloupec 8 = stávající skupina, sloupec 9 prázdný.

## Vzor souboru — Pouze doplňení (25 sloupců)

> [!abstract]
> ```
> IČO;Pobočka název;Příjmení;Jméno;Pohlaví;Datum narození RČ;RČ;stávající skupina PLS;Nová Skupina PLS;Pozice;Zaměstnán od;Zaměstnán do;Výsledek poslední prohlídky;Datum platnosti posudku;Osobní číslo;Středisko;Mobil;e-Mail;Ulice;Č. popisné;Č. orientační;PSČ;Obec;Pozastaveno;Hodnost
> 00637327;Obec Kotvrdovice;Novák;Josef;M;15.03.1985;8503151234;;Skladník;Skladník;01.01.2026;;;31.12.2027;OC001;Sklad;;;;;;;;Ne;
> 00637327;Obec Kotvrdovice;Kovářová;Jana;Z;22.07.1990;9057222345;;Řidič;Řidička;01.01.2026;;;31.12.2027;OC002;Doprava;;;;;;;;Ne;
> 00637327;Obec Kotvrdovice;Svoboda;Martin;M;08.11.1978;7811082468;;Administrativa;Administrátor;01.01.2026;31.12.2026;;31.12.2027;OC003;Kancelář;;;;;;;;Ne;
> ```

## Vzor souboru — Doplňení i odstranění (23 sloupců)

> [!abstract]
> ```
> Příjmení;Jméno;Pohlaví;Datum narození RČ;RČ;stávající skupina PLS;Nová Skupina PLS;Pozice;Zaměstnán od;Zaměstnán do;Výsledek poslední prohlídky;Datum platnosti posudku;Osobní číslo;Středisko;Mobil;e-Mail;Ulice;Č. popisné;Č. orientační;PSČ;Obec;Pozastaveno;Hodnost
> Novák;Josef;M;15.03.1985;8503151234;Skladník;;Skladník;01.01.2026;;;31.12.2027;OC001;Sklad;;;;;;;;Ne;
> Kovářová;Jana;Z;22.07.1990;9057222345;Řidič;;Řidička;01.01.2026;;;31.12.2027;OC002;Doprava;;;;;;;;Ne;
> ```

## Postup importu v aplikaci

1. Otevři modul **Import** (záložka v horním menu PLS).
2. Zvol typ importu: **Import pacientů PLS**.
3. Klikni na **„…“** a vyber připravený CSV soubor.
4. Zvol **Režim**:

   - **Pouze doplňení** — bezpečnější, soubor obsahuje IČO a Pobočku (25 sloupců)
   - **Doplňení i odstranění** — soubor musí být kompletní seznam; pacienti chybějící v souboru budou ukončeni
5. Stiskni **Importovat**.
6. Zkontroluj výsledek — systém zobrazí počty: **Nových / Aktualizováno / Ukončeno**, nebo seznam chyb.

## Chování systému

| Situace | Co systém udělá |
| --- | --- |
| Pacient s daným RČ **neexistuje** | Vytvoří novou kartu pacienta a záznam zaměstnání. Počítáno jako Nových. |
| Pacient existuje, zaměstnání u firmy **neexistuje** | Vytvoří nový záznam zaměstnání. Počítáno jako Nových. |
| Pacient existuje, zaměstnání **existuje** | Aktualizuje data zaměstnání. Počítáno jako Aktualizováno. |
| Pacient **chybí v souboru** (jen Doplňení i odstranění) | Nastaví ZaměstnánDo = datum importu. Počítáno jako Ukončeno. |
| Skupina PLS v sl. 9 **nenalezena** | Chyba importu — zobrazí číslo řádku. |
| Pobočka **nenalezena** | Chyba importu — zkontroluj přesný název pobočky. |

## Časté chyby

| Chybová hláška | Příčina | Řešení |
| --- | --- | --- |
| Řádek obsahuje nesprávný počet sloupců | Soubor nemá přesně 25 (nebo 23) sloupců. Typicky: chybějící středník v sekci adresních polí (sloupce 19–23 jsou prázdná, ale oddělovače musí být zachovány). | Každý řádek musí mít přesně 24 středníků (= 25 polí) pro Pouze doplňení. |
| Skupina PLS nenalezena | Hodnota ve sloupci 9 neodpovídá žádné skupině PLS firmy. | Ověř přesný název skupiny v systému. |
| Pobočka nenalezena | Hodnota ve sloupci 2 neodpovídá žádné pobočce firmy. | Ověř přesný název pobočky v systému. |
| Soubor nelze načíst / znaky jsou rozházené | Nesprávné kódování (UTF-8 místo Windows-1250). | Ulož v kódování Windows-1250. V Excelu: Uložit jako → CSV (MS-DOS). |

> [!tip]
> Úspěšný import zobrazí hlášení **„Import úspěšně dokončen“** s počty: **Nových / Aktualizováno / Ukončeno**.
