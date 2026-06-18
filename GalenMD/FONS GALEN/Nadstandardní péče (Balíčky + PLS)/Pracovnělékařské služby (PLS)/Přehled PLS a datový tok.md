---
title: "Přehled PLS a datový tok"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/435126277
---

# Přehled PLS a datový tok

### *Přehled datového toku PLS*

*Pořadí kroků při práci s pracovnělékařskými službami — od nastavení až po fakturaci:*

> [!abstract]
> ```
> 1. Firma (zaměstnavatel) + Pobočka        ← předpoklad, zakládá správce
>   2. Skupiny PLS (pozice zaměstnanců)
>        └─ Rizika skupiny (druhy rizik)
>   3. Smlouva PLS  ─────────────────────────  platnost, způsob platby
>        └─ Položky smlouvy PLS              ← typ prohlídky/sortimentu,
>             └─ Skupina PLS                   cena, limit, vazba (výkon/paušál)
>   4. Objednávka PLS (od zaměstnavatele)
>        └─ Položky objednávky + Přílohy
>   5. Akce PLS (plánovaná prohlídka)         ← stav: Nová plánovaná akce
>        └─ Pacient + Pracoviště
>        └─ Vyšetření (po provedení)          ← stav: → Uzavřena, fakturovat
>        └─ Výsledek posudku (PLSResult)
>   6. Vyúčtování PLS (hromadná příprava)
>        └─ Faktura PLS                       ← číslo, období, typ, identifikace pac.
>             └─ Položky faktury PLS
> ```

---

### Výsledky pracovnělékařského posudku

Po provedení prohlídky lékař zaznamená výsledek posudku. Systém nabízí tyto hodnoty:

| **Kód** | **Výsledek posudku** |
| --- | --- |
| Z | Zdravotně způsobilý/á |
| N | Zdravotně nezpůsobilý/á |
| K | Zdravotně způsobilý/á s podmínkou s kompenzací |
| M | Zdravotně způsobilý/á s podmínkou mimo kompenzaci |
| D | Pozbyl/a dlouhodobě zdravotní způsobilost |
| B | Prohlídka uzavřena bez vydání posudku |
| X | Nedostavil/a se |

*📌 Poznámka: Výsledek X — Nedostavil/a se je klíčový pro fakturaci: pokud má smlouva PLS nastaveno „Fakturovat stav Nedostavil se", bude i tato akce zahrnuta do faktury pro zaměstnavatele (viz nastavení smlouvy, kapitola 4.5).*

---
