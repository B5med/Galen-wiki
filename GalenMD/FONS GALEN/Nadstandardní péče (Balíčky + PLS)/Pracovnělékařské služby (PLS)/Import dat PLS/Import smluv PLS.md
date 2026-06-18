---
title: "Import smluv PLS"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/436535298
---

# Import smluv PLS

Slouží k hromadnému zakládání PLS smluv včetně položek ceníku pro jednotlivé skupiny (pozice). Jeden CSV soubor může obsahovat více smluv pro různé pobočky.

> [!info]
> Krok 2 z pořadí importů: **skupiny PLS → smlouvy PLS → pacienti PLS**. Skupiny musí existovat před importem smluv.

## Předpoklady

- Firma a pobočky musí být v systému **již založeny**.
- **Skupiny PLS** (pozice) musí existovat — importují se v předchozím kroku.
- **Sortimentní kódy** v položkách musí existovat v číselníku Sortiment.
- `Platnost od` nové smlouvy musí být **alespoň o 1 den pozdější** než nejnovější existující smlouva pro danou pobočku.

## Formát souboru

| Parametr | Hodnota |
| --- | --- |
| Přípona | .csv |
| Kódování | Windows-1250 |
| Oddělovač | středník ; |
| Hlavičkový řádek | povinný (přesně dle vzoru) |
| Počet sloupců | 34 (každý řádek musí mít přesně 34 polí) |
| Jeden řádek | jedna položka smlouvy — smlouva s více položkami má více řádků se stejnými daty smlouvy |

## Sloupce (34)

> [!warning]
> **S = data smlouvy** — opakují se na každém řádku. **P = data položky** — liší se na každém řádku. **Pov.: P** = povinný, **V** = volitelný.

| # | Název sloupce | Typ | Pov. | Hodnoty / poznámka |
| --- | --- | --- | --- | --- |
| 1 | ICO | S | P | IČO firmy (bez mezer) |
| 2 | Pobocka nazev | S | P | Přesný název pobočky v systému |
| 3 | Smluva kod | S | P | Kód smlouvy (max 10 znaků), unikátní v rámci pobočky |
| 4 | Smluva nazev | S | P | Název smlouvy (max 100 znaků) |
| 5 | Nefakturovat (1-ano, 0-ne) | S | P | 1 nebo 0 |
| 6 | Platnost od | S | P | Formát dd.MM.yyyy. Musí být alespoň 1 den po nejnovější existující smlouvě pobočky. |
| 7 | Platnost do | S | V | Formát dd.MM.yyyy, nebo prázdné |
| 8 | Zpusob platby | S | P | P = paušál · V = výkony · K = kombinovaně |
| 9 | Typ pausalu | S | P | J = jednorázový · P = za 1 pacienta |
| 10 | Rezim platby | S | P | Dopredu nebo Zpetne |
| 11 | Pocet mesice pausalu | S | V | Celé číslo, nebo prázdné |
| 12 | Cena bez DPH | S | V | Cena smlouvy (paušál). Pro výkonovou smlouvu ponech prázdné nebo 0. |
| 13 | Cena s DPH | S | V | Prázdné pokud sazba DPH = 0 |
| 14 | Sazba DPH | S | P | Číslo (např. 0, 10, 21) |
| 15 | Sleva | S | P | Procento slevy, celé číslo (např. 0) |
| 16 | Fakturovat nedostavil se (1-ano, 0-ne) | S | P | 1 nebo 0 |
| 17 | Procento ceny za nedostavil se | S | V | 0–100, nebo prázdné |
| 18 | Cena za nedostavil se | S | V | Pevná částka bez DPH, nebo 0 |
| 19 | Polozka sortiment kod | P | P | Kód ze Sortimentu — musí existovat v systému |
| 20 | Polozka pozice PLS | P | V | Název skupiny PLS — musí existovat pro danou firmu |
| 21 | Polozka cena bez DPH | P | P | Cena položky bez DPH |
| 22 | Polozka cena s DPH | P | V | Prázdné pokud sazba DPH = 0 |
| 23 | Polozka sazba DPH | P | P | Číslo (např. 0) |
| 24 | Polozka sleva | P | P | Procento slevy, celé číslo |
| 25 | Polozka zpusob uhrady | P | P | Hotovost nebo Faktura |
| 26 | Polozka vazba | P | P | Vykon nebo PSmlouva (v paušálu smlouvy) |
| 27 | Polozka limit | P | P | Celé číslo, 0 = bez limitu |
| 28 | Polozka rozsiruje prohlidku sortiment kod | P | V | Kód sortimentu rozšiřující prohlídky, nebo prázdné |
| 29 | Polozka poznamka | P | V | Volný text, nebo prázdné |
| 30 | Polozka vek od | P | V | Celé číslo (věk v letech), nebo prázdné |
| 31 | Polozka vek do | P | V | Celé číslo (věk v letech), nebo prázdné |
| 32 | Polozka pohlavi | P | V | muz · zena · neuvedeno, nebo prázdné |
| 33 | Smlouva fakturovat nedostavil se vcetne rozsirujucich polozek (1-ano, 0-ne) | S | P | 1 nebo 0 — nesmí být prázdné! |
| 34 | Zpusob fakturace nedostavil se | S | P | ProcentoZCeny nebo PevnaCastka |

> [!danger]
> **Pozor na počet středníků!** Každý řádek musí mít přesně 34 polí (33 středníků). Sloupce 28–32 jsou volitelné, ale musí být přítomny jako prázdná pole — středníky vynechat nelze.
>
> Kontrola konce řádku: `limit;;;;;;fakturovat_vcetne;zpusob_fakturace` — mezi limitem a koncem musí být přesně 7 středníků.

## Vzor souboru

> [!abstract]
> ```
> ICO;Pobocka nazev;Smluva kod;Smluva nazev;Nefakturovat (1-ano, 0-ne);Platnost od;Platnost do; Zpusob platby (P-pausal, V-vykony, K-kombinovane);Typ pausalu (J-jednorazovy, P-za 1 pacienta);Rezim platby (Dopredu, Zpetne);Pocet mesice pausalu;Cena bez DPH;Cena s DPH;Sazba DPH; Sleva;Fakturovat nedostavil se (1-ano, 0-ne);Procento ceny za nedostavil se;Cena za nedostavil se;Polozka sortiment kod;Polozka pozice PLS;Polozka cena bez DPH;Polozka cena s DPH;Polozka sazba DPH;Polozka sleva;Polozka zpusob uhrady (Hotovost, Faktura);Polozka vazba (Vykon, PSmlouva - v pausalu smlouvy);Polozka limit;Polozka rozsiruje prohlidku sortiment kod;Polozka poznamka;Polozka vek od;Polozka vek do;Polozka pohlavi (muz, zena, neuvedeno);Smlouva fakturovat nedostavil se vcetne rozsirujucich polozek (1-ano, 0-ne);Zpusob fakturace nedostavil se (ProcentoZCeny, PevnaCastka)
> 00637327;Obec Kotvrdovice;TEST01;Testovaci smlouva 01;0;02.01.2026;;V;J;Zpetne;;0;;0;0;0;;0;PLS001;Skladník;1000;;0;0;Faktura;Vykon;0;;;;;;0;ProcentoZCeny
> 00637327;Obec Kotvrdovice;TEST01;Testovaci smlouva 01;0;02.01.2026;;V;J;Zpetne;;0;;0;0;0;;0;PLS002;Řidič;1000;;0;0;Faktura;Vykon;0;;;;;;0;ProcentoZCeny
> 00637327;Obec Kotvrdovice;TEST01;Testovaci smlouva 01;0;02.01.2026;;V;J;Zpetne;;0;;0;0;0;;0;PLS003;Administrativa;1100;;0;0;Faktura;Vykon;0;;;;;muz;0;ProcentoZCeny
> ```

## Postup importu v aplikaci

1. Otevři detail firmy → tlačítko **Import**.
2. Zvol typ importu: **Import smluv PLS**.
3. Klikni na **„…“** a vyber připravený CSV soubor.
4. Stiskni **Importovat**.
5. Zkontroluj výsledek — systém zobrazí potvrzení nebo seznam chyb s číslem řádku.

## Časté chyby

| Chybová hláška | Příčina | Řešení |
| --- | --- | --- |
| Soubor/řádek obsahuje nesprávný počet sloupců | Řádek nemá přesně 34 polí | Ověř počet středníků (musí být 33). Volitelné sloupce 28–32 musí být přítomny jako prázdná pole. |
| Chybí hodnota pole Fakturovat „Nedostavil se“ vč. rozšiřujících položek | Sloupec 33 je prázdný — chyba v počtu středníků za sloupcem 27 | Zkontroluj: sloupce 27–34 musí mít 7 středníků: limit;;;;;;fakturovat_vcetne;zpusob_fakturace |
| Smlouva s kódem X má stejné nebo novější datum platnosti | Existující smlouva pobočky má PlatnostOd stejné nebo pozdější | Nastav Platnost od alespoň o 1 den pozdější než nejnovější existující smlouva. |
| Sortimentní kód nenalezen | Hodnota v sloupci 19 nebo 28 neexistuje v číselníku Sortiment | Ověř kód v číselníku Sortiment v systému. |
| Pozice PLS nenalezena | Hodnota v sloupci 20 neexistuje jako skupina PLS pro danou firmu | Nejprve proveď import skupin PLS, nebo zkontroluj název skupiny v systému. |

> [!tip]
> Úspěšný import zobrazí hlášení **„Import úspěšně dokončen“** bez seznamu chyb.
