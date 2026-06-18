---
title: "Průvodce: Od založení firmy k první faktuře PLS"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/435290119
---

# Průvodce: Od založení firmy k první faktuře PLS

> [!info]
> Tento průvodce ukazuje **kompletní průchod** modulem PLS — od založení firmy až po vystavení první faktury. Všechny kroky jsou ilustrovány na fiktivní firmě **AutoServis Novák s.r.o.** s jedním zaměstnancem.
>
> Pokud zastáváte místo správce nebo zavádíte PLS v nové ordinaci, začněte zde.

## Předpoklady

Před započetím musí být v systému:

- Aktivní modul **Nadstandardní péče** (licence PLS)
- Alespoň jedna položka **sortimentu** s nastaveným ceníkem (viz [Ceník a sortiment](https://stapro-galen.atlassian.net/wiki/pages/createpage.action?spaceKey=fg&title=Cen%C3%ADk%20a%20sortiment&linkCreation=true&fromPageId=435290119))
- Oprávnění role **Správce**

---

## Scénář

| **Firma** | AutoServis Novák s.r.o., IČO 12345678 |
| --- | --- |
| **Pobočka** | Praha — Hlavní provozovna |
| **Skupina PLS** | Automechanik — riziko: hluk, vibrace, chemikálie |
| **Smlouva** | Výkonová, platnost 1. 1. 2026 – 31. 12. 2026 |
| **Zaměstnanec** | Jan Procházka, periodická prohlídka |

---

## Fáze 1 — Nastavení (jednorázové)

> [!warning]
> Tuto fázi provádíte jen jednou při zavádění nového zaměstnavatele do systému.

### Krok 1 — Založení firmy

1. Otevřete modul **Nadstandardní péče** → klikněte na **+** (Nová firma).
2. Do pole **IČO** zadejte `12345678` — údaje se doplní z ARES automaticky.
3. Ověřte Název, adresu a klikněte **Uložit**.

*Viz také:*[*Nastavení PLS — smlouvy a skupiny*](https://stapro-galen.atlassian.net/wiki/pages/createpage.action?spaceKey=fg&title=Nastaven%C3%AD%20PLS%20%E2%80%94%20smlouvy%20a%20skupiny&linkCreation=true&fromPageId=435290119)*— sekce Založení firmy.*

### Krok 2 — Editace pobočky

1. V detailu firmy přejděte na záložku **Pobočky** a dvojklikem otevřete detail.
2. Zadejte Název: *Praha — Hlavní provozovna*.
3. Nastavte **Období vedení lhůtníku** (např. od 1. 1. 2026).
4. Přidejte pracoviště ze seznamu (tomuto pracovišti umožníte provádět PLS).
5. Uložte.

### Krok 3 — Vytvoření skupiny PLS

1. Přejděte do sekce **Skupiny PLS** → **Nová skupina**.
2. Vyberte firmu *AutoServis Novák s.r.o.*, zadejte Název:
3. Přidejte rizika pro sledování lhůt.
4. Uložte.

*Interval prohlídek se vypočte automaticky jako minimum z intervalů přiřazených rizik.*

### Krok 4 — Vytvoření smlouvy PLS

1. V základních údajích firmy označte příznak **PLS**, vyberte pobočku.
2. V sekci **Smlouvy PLS** klikněte **+**.
3. Vyplnte: Kód *AS2026*, Název *AutoServis Novák 2026*, Platnost od *1. 1. 2026*.
4. Způsob platby: *Výkony*.
5. Přejděte na sekci **Hlavní položky smlouvy** a klikněte **+**.
6. Vyberte sortiment *Periodická prohlídka*, nastavte Skupinu PLS: *Automechanik*, Vazbu: *Výkon*a nastavte cenu. Uložte.

> [!tip]
> Bez položky smlouvy vázané na skupinu PLS systém prohlídku nevyúčtuje.

## Fáze 2 — Registrace zaměstnance

### Krok 5 — Zaevidování pacienta (zaměstnance)

1. Ověřte, že Jan Procházka je evidován jako pacient v FONS Galen.
2. Na kartě pacienta přejděte na záložku **PLS**.
3. Přiřaďte pacienta k firmě *AutoServis Novák s.r.o.* a skupině PLS *Automechanik*.
4. Zadejte **datum nástupu** do zaměstnání.

Systém automaticky vypočte datum příští povinné prohlídky na základě rizik skupiny.

---

## Fáze 3 — Objednávka a prohlídka

### Krok 6 — Vytvoření objednávky PLS

1. Přejděte do **Pracovnelékařské služby → Objednávky PLS** → **Nová objednávka**.
2. Vyberte pacienta *Jan Procházka*, firmu *AutoServis Novák*, skupinu *Automechanik*.
3. Typ prohlídky: *Periodická*, plánované datum: např. *15. 6. 2026*.
4. Uložte — vzniká akce PLS ve stavu *Nová plánovaná akce*.

### Krok 7 — Provedení a zapsání výsledku

1. Lékař provede prohlídku a otevře akci PLS z karty pacienta (záložka PLS → Akce PLS).
2. V poli **Výsledek posudku** vybere hodnotu — např. *Z* (Způsobilý bez omezení).
3. Uloží.

---

## Fáze 4 — Uzavření a fakturace

### Krok 8 — Uzavření akce PLS

1. V detailu akce PLS klikněte **Uzavřít akci**.
2. Zvolte stav: *Uzavřena, fakturovat*.
3. Zkontrolujte cenu a způsob úhrady (*Faktura*). Potvrdte.

### Krok 9 — Generování faktury

1. Přejděte do **Pracovnelékařské služby → Vyúčtování PLS**.
2. Nastavte období (např. červen 2026) a vyberte firmu *AutoServis Novák s.r.o.*
3. Klikněte **Vystavit fakturu PLS**.
4. Vyplnte číslo faktury, datum vystavení, datum plnění a klikněte **OK**.
5. Fakturu vytiskněte přes **Tisk vyúčtování PLS**.

> [!tip]
> Faktury můžete generovat hromadně pro všechny firmy najednou — nemusíte opakovat krok 9 pro každou firmu zvlášť.

---

## Přehled celého workflow

| Fáze | Co se děje | Kdo | Stav akce PLS |
| --- | --- | --- | --- |
| Nastavení | Firma, pobočka, skupina, smlouva | Správce | — |
| Registrace | Přiřazení zaměstnance ke skupině | Správce / koordinátor | — |
| Objednávka | Nenaplánování prohlídky | Koordinátor PLS | Nová plánovaná akce |
| Prohlídka | Realizace + zapsání výsledku | Lékař | Nová plánovaná akce |
| Uzavření | Změna stavu na „fakturovat“ | Koordinátor / správce | Uzavřena, fakturovat |
| Fakturace | Vystavení faktury zaměstnavateli | Správce / účetnictví | Faktura vystavena |

> [!warning]
> **Opakování:** Pro každou další prohlídku začněte od **Kroku 6** — nastavení (fáze 1–2) se nedělá znovu.
