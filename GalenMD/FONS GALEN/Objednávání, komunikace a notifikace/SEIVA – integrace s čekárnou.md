---
title: "SEIVA – integrace s čekárnou"
version: 1
updated_at: 2026-06-22
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/466747393
---

# SEIVA – integrace s čekárnou

**SEIVA** je externí čekárenský systém (samoobslužný kiosk), který umožňuje pacientům zaregistrovat se do čekárny přiložením kartičky pojištěnce. Přístroj načte identifikační údaje pacienta (jméno, příjmení, číslo pojištěnce) a uloží je do souboru ve formátu **GDT**.

Integrace zajišťuje, že FONS Galen automaticky sleduje tyto soubory a zobrazuje přihlášené pacienty přímo v modulu **Čekárna**. Recepce tak vidí příchozí pacienty bez nutnosti ručního zadávání.

> [!info]
> Integrace je jednosměrná — SEIVA posílá data do Galenu (přes soubory GDT). Galen na přístroj žádná data neposílá zpět.

## Jak integrace funguje – princip

Celý tok od příchodu pacienta po zobrazení v čekárně:

1. Pacient přiloží kartičku pojištěnce k přístroji SEIVA v čekárně.
2. SEIVA vytvoří GDT soubor s údaji pacienta do nastavené sdílené složky.
3. Galen sleduje složku pomocí **FileSystemWatcher** — zachytí každý nový soubor okamžitě (i při startu aplikace zpracuje soubory, které přišly mezidobí).
4. Galen se pokusí najít pacienta v databázi podle **čísla pojištěnce**.
5. Výsledek se zobrazí v modulu Čekárna — spárovaný nebo nespárovaný záznam.

### Přiřazení pacienta ke kalendáři

Každý záznam ze SEIVY musí být přiřazen ke konkrétnímu kalendáři. Galen to určí podle těchto pravidel:

1. **Jedinečná cesta:** pokud má daný kalendář nastavenou cestu, která nepatří žádnému jinému kalendáři, pacient je přiřazen automaticky.
2. **Sdílená cesta + Důvod příchodu:** pokud více kalendářů sdílí stejnou složku, Galen porovná pole *Důvod příchodu* (nastavené v přístroji SEIVA) s **přesným názvem kalendáře** v Galenu (včetně diakritiky a velikosti písmen).
3. **Více informací v Důvodu:** pokud přístroj vyplní do důvodu i další text (např. `MUDr. Novák|Odběr`), hodnoty jsou odděleny znakem `|` — první část je název kalendáře. Díky tomu lze více kiosků nebo vstupů směrovat do jedné fronty.

> [!danger]
> **Neshoda názvů = ztráta záznamu.** Pokud se název tlačítka na SEIVA kiosku neshoduje s názvem kalendáře v Galenu a jsou současně otevřeny dva nebo více kalendářů se SEIVA, záznam pacienta je zahozen — pacient se nikde v čekárně nezobrazí. Při jediném otevřeném kalendáři se pacient přiřadí zdánlivě správně, ale chyba se projeví hned jak se přihlásí druhý uživatel. Toto je nejčastější příčina hlášení „pacient se v čekárně nezobrazil".

## Konfigurace

> [!abstract]
> **Předpoklad:** Technická podpora musí mít předem aktivovánu integraci SEIVA na úrovni společnosti (*Čekárenský systém = SEIVA*). Bez tohoto nastavení kroky níže nemají efekt. Pokud integrace nefunguje, ověřte s technickou podporou, zda bylo toto provedeno.

Po aktivaci technickou podporou nastavte v Galenu každý zapojený kalendář ve dvou krocích.

### Krok 1 – Správa čekárny na každém zapojeném kalendáři

Na každém kalendáři, který má být součástí SEIVA fronty, nastavte pole:

- **Správa čekárny** = `Evidence stavů`

| Hodnota | Popis | Kdy použít |
| --- | --- | --- |
| Ruční odstranění VÝCHOZÍ | Záznamy se mažou ručně | Bez čekárny nebo bez SEIVA |
| Evidence stavů PRO SEIVA | Sledování stavů, záznamy zůstávají | Vždy při SEIVA integraci |
| Automatické odstranění | Záznamy mizí automaticky po vyřízení | Jen pokud zákazník explicitně chce |

### Krok 2 – Cesta ke složce GDT souborů

Na jednom z zapojených kalendářů (zpravidla hlavním) vyplňte pole:

- **Čekárna SEIVA – cesta** — lokální nebo síťová cesta ke složce, kde SEIVA ukládá GDT soubory (max. 255 znaků)

Ostatní zapojené kalendáře mají nastavenu *Evidenci stavů*, ale pole cesty mohou mít prázdné. Více kalendářů může sdílet stejnou cestu.

| Příklad cesty | Typ |
| --- | --- |
| `C:\SEIVA\Sdilena` | Lokální disk (jen jeden PC) |
| `\\server01\seiva` | UNC — doporučeno pro více stanic |
| `Z:\SEIVA` | Mapovaný síťový disk |

> [!warning]
> **Více kalendářů se sdílenou cestou:** v přístroji SEIVA musí být nastaven *Důvod příchodu*, jehož hodnota přesně odpovídá názvu kalendáře v Galenu (velikost písmen se počítá). Před nasazením ověřte přesné znění tlačítek na kiosku.

## Čekárna – zobrazení v Galenu

Pacienti přihlášení přes SEIVA se zobrazují v modulu **Čekárna** spolu s pacienty přidanými ručně. Každý záznam ze SEIVY je označen ikonou párování:

| Ikona | Stav | Zobrazené údaje |
| --- | --- | --- |
| ✔ zelená | Pacient byl úspěšně spárován s kartou v Galenu | Údaje z karty pacienta (pole *Pacient* je vyplněno) |
| ! oranžová | Pacient nebyl automaticky spárován | Jméno, příjmení a číslo pojištěnce převzaty přímo z GDT souboru (pole *Pacient* je prázdné) |

## Párování pacienta

Pokud pacient nebyl spárován automaticky, lze ho spárovat ručně.

1. V čekárně najděte záznam s **oranžovou ikonou** (nespárovaný).
2. **Poklepejte** na záznam — otevře se okno *Párování pacienta s objednávacím systémem*.
3. Zadejte do pole hledání jméno, příjmení nebo číslo pojištěnce. Seznam níže se průběžně filtruje.
4. Najdete-li shodu, označte pacienta a klikněte na **Spárovat**.
5. Nenajdete-li pacienta v databázi, klikněte na **Založit novou kartu pacienta** — Galen otevře formulář nové karty a předvyplní dostupné údaje z GDT souboru.

> [!abstract]
> Tlačítko **Založit novou kartu pacienta** se zpřístupní až po zadání alespoň 1 znaku do pole vyhledávání.

### Proč pacient není spárovaný – to nemusí být chyba

Nespárování (oranžová ikona) je normální stav v těchto případech:

- **Nový nebo cizí pacient** — není v kartotéce, spárovat nelze; použijte *Založit novou kartu pacienta*.
- **Nesoulad čísla pojištěnce** — pacient zadal na kiosku jiné RČ než je v kartotéce.
- **Neúplná data z kiosku** — čtečka karet nenačetla všechny údaje (prázdné jméno nebo RČ).

> [!info]
> Nespárování není chyba integrace — je to datový problém na straně pacienta nebo kartotéky. Řeší se ručním párováním nebo založením nové karty.

## Stavy pacienta v čekárně

| Stav | Popis |
| --- | --- |
| NOVÝ | Pacient právě dorazil — dosud ho nikdo nezpracoval. |
| V ŘEŠENÍ | Recepce nebo lékař záznam otevřeli a pracují s ním. |
| VYŘEŠENÝ | Pacient byl vyšetřen, návštěva ukončena. |
| PŘEŘAZEN | Pacient byl přesunut na jiný kalendář. |
| PŘEDČASNÝ ODCHOD | Pacient odešel ještě před vyšetřením. |
| ODSTRANĚNÝ | Záznam byl ručně odstraněn z čekárny. |

## Signalizace nových pacientů

Pokud se v čekárně nachází alespoň jeden pacient se stavem NOVÝ, zobrazí se nad ikonou Čekárna v hlavním panelu Galenu **červené kolečko s počtem** takových pacientů.

> [!info]
> Podmínka zobrazení: pacient musí být přiřazen ke kalendáři vašeho aktuálního pracoviště, nebo ke kalendáři, ke kterému máte právo přístupu.

## Ověření funkčnosti

Po konfiguraci lze ověřit, že integrace běží správně, přímým pohledem do sdílené složky:

| Co vidím ve složce | Co to znamená |
| --- | --- |
| Soubory `!CEKAJICI_*.csv` s dnešním datem | SEIVA funguje a zapisuje snapshoty čekárny — integrace na straně SEIVA je v pořádku |
| Žádné CSV soubory | SEIVA nepíše — problém na straně SEIVA nebo špatná cesta v nastavení kalendáře |
| Soubory `AMB_CEK*.001` (nebo .002, .003…) | **Galen soubor přečetl, ale zpracování selhalo.** Zkontrolovat `Seiva.log` pro důvod odmítnutí (nejčastěji neshoda názvu kalendáře nebo prázdné jméno pacienta) |
| Soubory `AMB_CEK*.GDT` zůstávají déle než minutu | Galen soubory nečte — pravděpodobně neběží nebo nemá práva ke čtení složky |

## Chybový log

Pokud při zpracování GDT souborů dojde k chybě (soubor nelze přečíst, neplatný formát, neshoda názvu kalendáře apod.), Galen zapíše chybu do lokálního logu:

> [!abstract]
> ```
> C:\ProgramData\Galen\Seiva.log
> ```

Log je uložen na každé Galen stanici zvlášť. Je to první místo k prozkoumání, pokud pacienti ze SEIVY přestali přicházet do čekárny.

> [!warning]
> V případě opakovaných problémů s párováním zkontrolujte, zda hodnota *Důvod příchodu* nastavená v přístroji SEIVA přesně odpovídá názvu kalendáře v Galenu (včetně diakritiky a velikosti písmen).
