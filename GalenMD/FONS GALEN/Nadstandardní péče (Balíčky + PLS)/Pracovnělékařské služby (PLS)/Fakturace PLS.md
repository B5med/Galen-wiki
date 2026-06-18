---
title: "Fakturace PLS"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/435945474
---

# Fakturace PLS

> [!info]
> Fakturaci PLS provádí uživatel s rolí **správce**. Zahrnuje kontrolu stavů uzavřených akcí v PLS Adminu, generování faktur a správu číselné řady.

---

## 📊 PLS Admin — přehled akcí před fakturací

Okno **PLS Admin** slouží k celkovému přehledu všech PLS akcí (prohlídky a očkování). Záznamy lze filtrovat a připravit k fakturaci.

| **Stav akce** | **Význam** |
| --- | --- |
| **Nová naplánovaná akce** | Nově založená PLS prohlídka nebo očkování, dosud neuzavřená |
| **Přiděleno dalšími IČP** | Nastává pouze u nehlavních položek smlouvy |
| **Vráceno** | Nastává pouze u nehlavních položek smlouvy |
| **Uzavřena, fakturovat** | Uzavřená akce, fakturace dosud neproběhla — **připraveno k fakturaci** |
| **Uzavřena, nefakturovat** | Výsledek prohlídky je „Nedostavil/a se“ a smlouva nemá zapnuté fakturování tohoto stavu |
| **Faktura vystavena** | Fakturace proběhla |

### Další možnosti v PLS Adminu

- Uzavřené položky lze **znovu otevřít**.
- U neuzavřených položek lze měnit **způsob úhrady** (hotovost ↔ faktura).
- Dodatečně přidané položky na prohlídce (mimo smlouvu) lze **odstranit**.
- Přes kontextové menu (pravé tlačítko myši) lze určit **datum příští prohlídky** i s poznámkou. Změna je viditelná v recepci a PLS aplikaci (za datem se zobrazí „určeno správcem“).

---

## 📄 PLS Admin Služby — přehled služeb

Okno **PLS Admin Služby** zobrazuje přehled vytvořených PLS služeb. Služby lze filtrovat, uzavřené znovu otevřít a u neuzavřených měnit způsob úhrady. Stavy odpovídají stavům z PLS Adminu (stavy Přiděleno dalšími IČP, Vráceno a Uzavřena, nefakturovat u služeb nenastávají).

---

## 🧾 Generování PLS faktur

Faktury se generují v okně **Vyúčtování PLS faktur** (sekce PLS Faktury).

| **Prvek** | **Funkce** |
| --- | --- |
| **Období** | Filtr ve formátu RRMM (např. 2506 = červen 2025). Určuje, které faktury se zobrazí nebo smají. |
| **Datum vystavení** | Určuje, od jakého data mají být faktury vystaveny. Akce vytvořené po tomto datu do faktur nevstoupí. |
| **Tlačítko Nové** | Vygeneruje nové faktury pro uzavřené akce se stavem „Uzavřena, fakturovat“. |
| **Tlačítko Smazat** | Odstraňuje stávající faktury podle zadaného období (na základě data jejich vytvoření). |
| **Hlavní prohlídky** | Checkbox — zobrazí v přehledu položek pouze prohlídky definované jako hlavní položky smlouvy. |

---

## 🔢 Číselná řada PLS faktur

Fakturace PLS používá automaticky generovanou **desetimístné číselné označení**:

| **Pozice** | **Význam** |
| --- | --- |
| 1. číslice | Vždy **1** |
| 2.–3. číslice | Rok minus 2000 (např. rok 2025 → **25**) |
| 4.–5. číslice | Vždy **00** |
| 6.–10. číslice | Pořadové číslo od **00001**, zvyšuje se o 1 u každé nové faktury |

**Příklad:** 1250000001, 1250000002, …, 1250000014
