---
title: "Průběžný export dat (RabbitMQ)"
version: 3
updated_at: 2026-06-19
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/421396481
---

# Průběžný export dat (RabbitMQ)

## Co je průběžný export dat

Průběžný export dat je funkce IS Galen, která umožňuje automaticky odesílat vybrané záznamy do externího systému zákazníka v reálném čase – ihned v okamžiku, kdy dojde ke změně dat v Galenu. Na rozdíl od dávkového exportu, který data přenáší hromadně v naplánovaných intervalech, průběžný export reaguje na každou jednotlivou událost (vytvoření, změnu nebo smazání záznamu) a přenáší ji okamžitě.

Přenos probíhá prostřednictvím message brokeru RabbitMQ. Galen publikuje zprávy ve formátu JSON na definovaný RabbitMQ Exchange, odkud si je přebírá systém zákazníka.

## K čemu slouží

Funkce je určena zákazníkům, kteří potřebují data z Galenu průběžně synchronizovat s jiným systémem – například s vlastním informačním systémem, BI platformou, CRM nebo jiným softwarem třetí strany. Typické využití zahrnuje:

- okamžitou synchronizaci eReceptů do externího systému po jejich vystavení nebo změně,

- průběžný přenos objednávek a kalendářních záznamů pro potřeby plánování nebo zákaznických portálů,

- automatický přenos příloh (dokumentů) přidaných k záznamu pacienta.

## Exportované agendy

V rámci průběžného exportu lze nakonfigurovat export těchto agend:

| **Pole** | **Popis / hodnota** |
| --- | --- |
| eRecept | Exportují se eRecepty – každé vytvoření, změna nebo smazání eReceptu. |
| Objednávka | Exportují se objednávky a kalendářní záznamy. |
| Příloha | Exportují se přílohy přidané k záznamu pacienta. |

Je možné aktivovat export jedné nebo více agend současně. Alespoň jedna agenda musí být vybrána.

## Jak přenos funguje

Při každé změně exportovaného záznamu Galen sestaví zprávu ve formátu JSON a odešle ji na nakonfigurovaný RabbitMQ Exchange. Zpráva obsahuje informaci o tom, zda byl záznam vytvořen, změněn nebo smazán, a příslušná data záznamu.

Zprávy jsou odesílány s potvrzením doručení (publisher confirms). Pokud RabbitMQ zprávu nepotvrdit ve stanoveném čase, Galen zaznamená chybu přenosu.

Routing key zprávy má formát galen.{agenda}, například galen.erecept nebo galen.objednavka. Přijímající systém zákazníka si nastaví odběr zpráv z příslušné fronty navázané na tento Exchange.

## Nastavení ve FONS Galen

Průběžný export se nastavuje ve dvou krocích: nejprve je nutné funkci zapnout na úrovni společnosti, poté vytvořit konfiguraci exportu.

## Krok 1 – Zapnutí funkce na společnosti

Funkci průběžného exportu zapíná na společnosti dodavatel systému (Stapro). Na záznamu společnosti musí být nastaven příznak Průběžný export dat. Bez tohoto nastavení není konfigurace exportu dostupná.

## Krok 2 – Konfigurace exportu

Po zapnutí funkce je v administraci Galenu dostupná sekce Konfigurace exportu dat (správce - Správa organice - Agendy - Export dat). Zde se vytvoří nový záznam konfigurace typu Průběžný s následujícími parametry:

| **Pole** | **Popis / hodnota** |
| --- | --- |
| Označení exportu | Libovolný název konfigurace (max. 30 znaků), slouží k identifikaci záznamu. |
| Aktivní | Určuje, zda je konfigurace aktivní. Může existovat pouze jedna aktivní konfigurace průběžného exportu na společnost. |
| Typ přenosu dat | Pro průběžný export se vybere hodnota RabbitMQ. |
| Průběžně exportované agendy | Výběr agend určených k exportu: eRecept, Objednávka, Příloha. Musí být vybrána alespoň jedna. |
| Adresa | Hostname nebo IP adresa RabbitMQ serveru. |
| Port | Port RabbitMQ serveru. Výchozí hodnota: 5671 (SSL). |
| Virtual host | Virtual host na RabbitMQ serveru. |
| Exchange název | Název Exchange, na který Galen publikuje zprávy. |
| Exchange durable | Určuje, zda je Exchange trvalý (přežije restart RabbitMQ). Výchozí hodnota: ne. |
| Exchange auto delete | Určuje, zda se Exchange automaticky smaže, když nemá žádné odběratele. Výchozí hodnota: ne. |
| Uživatelské jméno | Přihlašovací jméno pro připojení k RabbitMQ. |
| Heslo | Heslo pro připojení k RabbitMQ. Hodnota je v systému šifrována. |

## Volitelné: Notifikace při selhání přenosu

Je možné zapnout automatické upozornění při opakovaném selhání přenosu dat. Upozornění se odesílá prostřednictvím Telegram Bota. Pro aktivaci je nutné vyplnit:

| **Pole** | **Popis / hodnota** |
| --- | --- |
| Notifikace selhání přenosu dat | Zapíná odesílání upozornění při selhání. |
| Interval (min) | Časový interval sledování selhání v minutách. Výchozí hodnota: 10. Hodnota 0 znamená okamžité odeslání při každém selhání. |
| Počet neprovedených pokusů | Počet selhání v intervalu, po kterém se odešle upozornění. Výchozí hodnota: 5. |
| Telegram Bot Token | Token Telegram Bota, přes který se odesílá upozornění. |
| Chat Id | ID Telegram chatu nebo skupiny, do které se upozornění odesílá. |

Správnost nastavení Telegram upozornění lze ověřit tlačítkem Odeslat testovací notifikaci přímo v administraci.

## Důležité poznámky

- Na jednu společnost může být aktivní vždy jen jedna konfigurace průběžného exportu. Při pokusu o aktivaci druhé konfigurace Galen nabídne deaktivaci té stávající.

- Komunikace s RabbitMQ probíhá vždy přes SSL (šifrované připojení).

- Funkci průběžného exportu (příznak na společnosti) aktivuje dodavatel systému Stapro – zákazník nemůže toto nastavení provést sám.

- Samotnou konfiguraci exportu (přihlašovací údaje, exchange, agendy) spravuje zákazník v administraci Galenu.
