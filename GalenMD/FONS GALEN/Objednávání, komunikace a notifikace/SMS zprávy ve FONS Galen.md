---
title: "SMS zprávy ve FONS Galen"
version: 2
updated_at: 2026-04-13
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/341704706
---

> [!info]
> Napojení na SMS bránu je **nadstandardní placená funkcionalita** – pro její aktivaci kontaktujte tým podpory STAPRO.

## 1. Odeslání SMS jednotlivému pacientovi z kartotéky

SMS lze odeslat přímo z kartotéky kliknutím **pravým tlačítkem myši** na pacienta. Z kontextového menu zvolte **Poslat zprávu → Napsat SMS** (nebo **Napsat e-mail i SMS**). Zobrazí se okno pro sestavení zprávy, kde lze napsat vlastní text nebo vybrat přednastavenou šablonu.

## 2. Hromadné odeslání SMS z kartotéky

V kartotéce lze označit více pacientů najednou a odeslat jim SMS hromadně.

1. V kartotéce označte požadované pacienty pomocí **Ctrl + klik** nebo **Shift + klik**.
2. Klikněte **pravým tlačítkem myši** na výběr a zvolte **Poslat zprávu → Napsat SMS**.
3. Sestavte zprávu nebo vyberte šablonu a potvrďte odeslání.

## 3. SMS notifikace objednávek

Systém umí automaticky odesílat SMS pacientům v návaznosti na události v kalendáři objednávek. Jedná se o tři typy notifikací:

- **Potvrzení objednávky** – SMS se odešle ihned po vytvoření objednávky v kalendáři.
- **Připomenutí termínu** – SMS se odešle definovaný počet dní před termínem. Lze nastavit více připomínek najednou (např. 3 dny předem i 1 den předem). Zprávy se generují a odesílají hromadně jednou denně.
- **Zrušení objednávky** – SMS se odešle ihned po smazání objednávky z kalendáře.

### Nastavení notifikací objednávek

Nastavení probíhá na třech místech:

- **Šablony zpráv** – texty SMS se definují v **Správce → Nástroje → Šablony → Notifikace**. Šablonu lze nastavit obecně pro všechny pacienty nebo rozlišovat dle pohlaví. Pro každý typ notifikace (potvrzení, připomenutí, zrušení) a každý typ záznamu v kalendáři je potřeba vytvořit samostatnou šablonu.
- **Nastavení na úrovni kalendáře** – **Správce → Správa organizace → Agendy → Kalendáře → Nastavení → Notifikace a připomínání**. Pro každou šablonu lze nastavit stav: **Odesílat** (výchozně zapnuto), **Neodesílat** (výchozně vypnuto, lze ručně aktivovat), **Zakázat** (nelze aktivovat).
- **Nastavení na úrovni ordinačních hodin** – pro konkrétní bloky ordinačních hodin lze nastavit odlišné notifikace než jsou výchozí pro celý kalendář. Přístup: dvojklik na konkrétní ordinační dobu → **Notifikace a připomínání**.

### Příklady šablon SMS zpráv

Následující šablony lze využít jako výchozí bod v **Správce → Nástroje → Šablony → Notifikace**.

**Potvrzení objednávky:**

> [!abstract]
> ```
> Dobrý den, [@P.Jmeno] [@P.Prijmeni], Vaše objednávka na [@ObjednavkaRef.RecordName] dne [@Objednavka.Datum] v [@Objednavka.Time] hod. byla přijata. Těšíme se na Vás. [@Z.RecordName]
> ```

**Připomenutí termínu:**

> [!abstract]
> ```
> Dobrý den, [@P.Jmeno] [@P.Prijmeni], připomínáme Vám termín [@ObjednavkaRef.RecordName] dne [@Objednavka.Datum] v [@Objednavka.Time] hod. V případě potřeby nás kontaktujte. [@Z.RecordName]
> ```

**Zrušení objednávky:**

> [!abstract]
> ```
> Dobrý den, [@P.Jmeno] [@P.Prijmeni], Vaše objednávka na [@ObjednavkaRef.RecordName] dne [@Objednavka.Datum] v [@Objednavka.Time] hod. byla zrušena. Pro nový termín nás prosím kontaktujte. [@Z.RecordName]
> ```

## Předpoklady pro fungování SMS

- Aktivní napojení na SMS bránu (nadstandardní placená funkcionalita – zajišťuje tým podpory STAPRO)
- Vyplněné mobilní číslo pacienta v kartě pacienta
- Vytvořená šablona notifikace pro daný typ zprávy
- Aktivovaná notifikace v nastavení daného kalendáře

## Související stránky

- [[Notifikace objednávek]]
