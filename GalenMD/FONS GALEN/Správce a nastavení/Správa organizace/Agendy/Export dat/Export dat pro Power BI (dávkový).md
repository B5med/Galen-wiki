---
title: "Export dat pro Power BI (dávkový)"
version: 2
updated_at: 2026-06-19
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/463699974
---

# Export dat pro Power BI (dávkový)

## Co je dávkový export dat

Dávkový export dat je placená funkce IS FONS Galen, která umožňuje automaticky přenášet vybrané záznamy do externího systému zákazníka. Na rozdíl od průběžného exportu, který reaguje na každou jednotlivou změnu v reálném čase, dávkový export přenáší vždy kompletní aktuální data hromadně – každou noc ve **3:00 ráno**.

Přenos probíhá prostřednictvím FTP, SFTP nebo přímým zápisem do databáze SQL Server zákazníka. Exportovaná data slouží typicky jako zdroj pro vytváření reportů a dashboardů v nástroji Microsoft Power BI nebo jiném analytickém prostředí zákazníka.

## K čemu slouží

Funkce je určena zákazníkům, kteří potřebují pravidelně synchronizovat data z Galenu do vlastního analytického prostředí nebo datového skladu. Typické využití zahrnuje:

- pravidelný přenos klinických a provozních dat do Power BI pro manažerské reporty,
- plnění vlastního datového skladu zákazníka pro potřeby statistik a analýz,
- export dat do externího SQL Serveru zákazníka pro další zpracování.

## Exportované agendy

Konkrétní obsah exportu je stanoven při aktivaci funkcionality dodavatelem systému na základě potřeb zákazníka. Standardně export zahrnuje tyto agendy:

| **Agenda** | **Popis** |
| --- | --- |
| Pacienti | Základní demografické údaje pacientů – jméno, příjmení, číslo pojištěnce, pojišťovna, pohlaví. |
| Pracoviště / Zařízení | Seznam pracovišť – IČP, odbornost, adresa. |
| Návštěvy | Záznamy návštěv členěné po rocích – datum, diagnózy, nález. |
| Výkony | Vykázané výkony členěné po rocích – kód výkonu, počet, body, cena, stav, diagnóza. |
| Vyšetření | Záznamy vyšetření členěné po rocích – druh, diagnóza, datum příští prohlídky. |
| Medikace | Předepsané léky – přípravek, dávkování, diagnóza, datum. |
| Anamnéza | Anamnestické záznamy pacientů – alergologická, osobní, profesní anamnéza, CAVE. |
| Dávky | Vyúčtovací dávky odesílané pojišťovnám. |
| Objednávky | Kalendářní záznamy objednávek pacientů. |
| Fronta | Záznamy čekárny. |
| Pracovníci | Seznam pracovníků (uživatelů) ordinace. |
| Číselníky | Referenční číselníky – HVLP, výkony, léčivé přípravky, zdravotnické prostředky. |

## Jak přenos funguje

Každou noc ve 3:00 ráno Galen spustí export a přenese kompletní aktuální data do cílového úložiště zákazníka. Při každém spuštění se přenášejí vždy **všechna data**, nikoli pouze změny od posledního exportu.

V případě přenosu přes FTP nebo SFTP jsou data odesílána jako soubory do vzdáleného adresáře na serveru zákazníka. V případě přenosu přes SQL Server jsou data zapsána přímo do tabulek v databázi zákazníka – stávající tabulky jsou před zápisem vždy smazány a znovu vytvořeny.

## Nastavení ve FONS Galen

Dávkový export se nastavuje ve dvou krocích: nejprve je nutné funkci zapnout na úrovni společnosti, poté vytvořit konfiguraci exportu.

### Krok 1 – Zapnutí funkce na společnosti

Funkci dávkového exportu zapíná na společnosti dodavatel systému (STAPRO). Bez tohoto nastavení není konfigurace exportu dostupná.

---

### Krok 2 – Konfigurace exportu

Po zapnutí funkce je v administraci Galenu dostupná sekce konfigurace exportu dat (**Správce → Správa organizace → Agendy → Export dat**). Zde se vytvoří nový záznam konfigurace s následujícími parametry:

| **Pole** | **Popis / hodnota** |
| --- | --- |
| Označení exportu | Libovolný název konfigurace (max. 30 znaků), slouží k identifikaci záznamu. |
| Aktivní | Určuje, zda je konfigurace aktivní. Může existovat pouze jedna aktivní konfigurace dávkového exportu na společnost. |
| Typ přenosu dat | Volba způsobu přenosu: **FTP**, **S-FTP** nebo **SQL Server**. |

**Pro typ přenosu FTP nebo S-FTP:**

| **Pole** | **Popis / hodnota** |
| --- | --- |
| Název serveru FTP | Hostname nebo IP adresa FTP/SFTP serveru. |
| Port FTP | Port serveru. |
| Vzdálený adresář FTP | Cesta k adresáři na serveru, kam se soubory ukládají. |
| Uživatelské jméno FTP | Přihlašovací jméno pro připojení k serveru. Hodnota je v systému šifrována. |
| Heslo FTP | Heslo pro připojení k serveru. Hodnota je v systému šifrována. |

**Pro typ přenosu SQL Server:**

| **Pole** | **Popis / hodnota** |
| --- | --- |
| Připojovací řetězec | Connection string pro připojení k databázi SQL Server zákazníka. Hodnota je v systému šifrována. |

### Důležité poznámky

- Na jednu společnost může být aktivní vždy jen jedna konfigurace dávkového exportu. Při pokusu o aktivaci druhé konfigurace Galen nabídne deaktivaci té stávající.
- Při každém spuštění jsou přenášena vždy kompletní data – nedochází k přenosu pouze změn.
- Funkci dávkového exportu (příznak na společnosti) aktivuje dodavatel systému STAPRO – zákazník nemůže toto nastavení provést sám.
- Samotnou konfiguraci exportu (typ přenosu, přihlašovací údaje) spravuje zákazník v administraci Galenu.
