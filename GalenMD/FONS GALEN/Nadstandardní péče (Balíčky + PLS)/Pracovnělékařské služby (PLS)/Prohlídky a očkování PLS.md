---
title: "Prohlídky a očkování PLS"
version: 1
updated_at: 2026-06-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/461012994
---

# Prohlídky a očkování PLS

Tato stránka popisuje, jak v ordinaci provádět a zaznamenávat PLS prohlídky a PLS očkování, a jak je předem nakonfigurovat v modulu Designér.

---

## 1. Konfigurace v modulu Designér

Než lze PLS prohlídky nebo očkování zakládat v Ordinaci, musí je správce propojit s definicemi z modulu **Designér**. Bez tohoto propojení se příslušná prohlídka nebo očkovací látka v Ordinaci nenabídne.

### 1.1 Propojení PLS prohlídky

Cesta: **Designér → Prohlídky → záložka PLS → tlačítko +**

| Pole | Popis |
| --- | --- |
| **Prohlídka** | Výběr z aktivních prohlídek z Designéru (uživatelské i systémové). Bez výběru se prohlídka v Ordinaci → Prohlídky a vyšetření nezobrazí jako hlavní PLS prohlídka. |
| **Typ prohlídky** | Předdefinovaný seznam: Vstupní / Periodická / Výstupní / Mimořádná / Následná. Aktuálně informativní charakter. |
| **Ovlivňuje lhůtu** | Určuje vliv prohlídky na výpočet data příští prohlídky. Hodnoty: *null / Ne / Ano / Podmíněně / Vždy*. Hodnota null se chová jako Ne. Při volbě **Podmíněně** je povinné pole Název položky — prohlídka je označena zkratkou PPOL (viz sekce 2.4). |

### 1.2 Konfigurace PLS očkování

Cesta: **Designér → Prohlídky → záložka PLS Očkování**

| Pole | Popis |
| --- | --- |
| **Látka** | Výběr ze všech aktivních očkovacích látek. Bez výběru OL se v modulu Očkování nezobrazí Očkovací varianta. |
| **Očkovací varianta** | Je-li vybrána, bude tato varianta při očkování předem označena (lze zvolit jinou). |
| **Služby** | Položky, které lze přiřadit aktivní prohlídce. |
| **Balíčky** | Položky, které lze přiřadit stávajícím vytvořeným balíčkům nadstandardní péče. |

---

## 2. PLS prohlídky — práce v Ordinaci

### 2.1 Vytvoření PLS prohlídky

PLS prohlídku zakládáte v okně **Prohlídky a vyšetření** kliknutím na ikonu PLS a výběrem příslušné prohlídky přiřazené firmě.

Ve výběru se zobrazují všechny prohlídky definované na smlouvě (včetně těch z rozšiřujících položek), za těchto podmínek:

- Pacient musí být ve stejné skupině PLS jako je prohlídka na smlouvě.
- Prohlídka musí být zařazena do sortimentu skupiny **Prohlídka**.
- Je-li prohlídka na smlouvě vícekrát, zobrazí se ve výběru odpovídající počet možností.

> [!info]
> **Objednávka z kalendáře:** Je-li pacient s PLS prohlídkou objednán v kalendáři, zobrazí se na prohlídce ikona s hodinami. Po vytvoření prohlídky se automaticky načtou všechny položky přidané při vytváření objednávky a přenese se reference pracoviště objednávky (na hlavní položku toto neplatí — ta přebírá pracoviště, kde je prohlídka vytvářena). Ikona s hodinami zmizí po vytvoření prohlídky nebo po odebrání objednávky z kalendáře.

### 2.2 Práce s položkami na prohlídce

Na prohlídku lze přidávat nové položky ze smlouvy za těchto podmínek:

- Musí se jednat o hlavní položky smlouvy.
- Musí vyhovovat filtru věku a pohlaví nastavenému na položce smlouvy.
- Navázaný sortiment musí být aktivní a nesmí být ze sortimentu skupiny Prohlídka nebo Služba.
- Položka nemusí být ze stejné skupiny PLS jako pacient.
- Jsou-li dvě položky shodné (stejný kód sortimentu, cena bez DPH a DPH), nezobrazují se duplicitně.
- Defaultně se zobrazují položky bez přiřazené kategorie. Po rozdělení do kategorií lze přidávat i výkony.

**Datum návštěvy** nemůže být v budoucnosti. Nelze uzavřít položky prohlídky do období, pro které již existuje vystavená výkonová faktura. Hlavní položka musí být uzavřena jako poslední — jak pořadím, tak datumem.

**Platba za jednotlivé položky:** Označte jednu nebo více položek (Ctrl+klik nebo Shift+klik) a použijte tlačítko **Platba výběr**. Systém nabídne výběr platby kartou nebo hotovostí, s volbou tisku příjmového dokladu.

### 2.3 Přiřazení prohlídky jiné ordinaci (IČP)

Prohlídku lze přidělit k provedení externím poskytovatelem pomocí tlačítka s ikonou lékaře (vedle tlačítka Uzavřít). Po výběru ordinace se nabídnou kalendáře navázané na dané IČP a lze vytvořit objednávku s přiřazením na konkrétní PLS prohlídku a položku smlouvy. Akce PLS přejde do stavu **Přiděleno dalšími IČP**.

### 2.4 Prohlídky podmíněně ovlivňující lhůtu (PPOL)

Pokud má prohlídka v Designéru nastaveno **Ovlivňuje lhůtu = Podmíněně**, zobrazí se na prohlídce pole **DŮVOD** s těmito hodnotami:

- Zdravotní důvod
- Jiný důvod

Hodnota DŮVOD ovlivňuje, zda prohlídka vstoupí do výpočtu intervalu příští prohlídky.

---

## 3. PLS očkování — práce v Ordinaci

### 3.1 Vytvoření PLS očkování

V okně **Očkování** použijte tlačítko **+ PLS** pro zadání očkování vázaného na PLS smlouvu.

Ve výběru se zobrazují všechny očkovací látky definované na smlouvě (včetně rozšiřujících položek) za podmínky, že pacient je ve stejné skupině PLS, ke které je látka na smlouvě přiřazena. Je-li látka na smlouvě vícekrát, zobrazí se odpovídající počet možností.

> [!warning]
> **Omezení:** Nelze vytvořit PLS očkování do období, pro které již existuje vystavená výkonová faktura. Do faktury se přenáší cena i v případě variant, kde očkování nehradí pacient.

Jednotlivá PLS očkování lze v přehledu rozlišit od kurativních pomocí sloupce **Typ dokumentace**.

### 3.2 Doplnění PLS očkování

Vedle standardního PLS očkování existuje funkce **Doplnění PLS očkování**. Toto doplnění:

- Se **nezobrazuje** v přehledu PLS Admin.
- **Nevstupuje** do PLS faktur (nepřenáší se do fakturace).
- Nemá omezení na existenci vystavené výkonové faktury (validace se neuplatní).
