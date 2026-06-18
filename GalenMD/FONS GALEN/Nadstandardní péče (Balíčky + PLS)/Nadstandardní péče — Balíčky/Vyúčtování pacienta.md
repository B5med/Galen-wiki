---
title: "Vyúčtování pacienta"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/434798596
---

# Vyúčtování pacienta

## 4.6 Vyúčtování pacienta — tvorba závazku NP

Tato kapitola popisuje, jak vyučtovat pacientovi položky z balíčku nadstandardní péče a vytvořit závazek. Závazek je finanční pohledávka vůči pacientovi evidovaná v entitě `Galen.Zavazek`.

### 4.6.1 Vytvoření nového závazku

1. Otevřete **kartu pacienta**.
2. Přejděte na záložku **Závazky**.
3. Klikněte na **Nový**.
4. V dialogu vyberte **balíček NP**, ze kterého chcete položky vyučtovat.
5. Systém automaticky načte položky balíčku s cenami z platného ceníku (ke dni vyučtování). U položek s příznakem **Plně hrazeno** je cena pro pacienta nulová.
6. Zkontrolujte seznam položek, jejich počty a ceny.
7. Zvolte **způsob platby**: *Hotově* nebo *Bezhotovostně*.
8. Klikněte na **Uložit**.

> [!info]
> Při platbě **Hotově** systém automaticky nabídne tisk **pokladního dokladu (stvrzenky)**. Tisk lze opakovat kdykoliv ze záložky Závazky pomocí tlačítka **Tisk**.

### 4.6.2 Storno závazku

1. Na záložce **Závazky** vyberte závazek, který chcete stornovat.
2. Klikněte na tlačítko **Storno**.
3. Systém vytvoří opravný záznam s účelem „Storno“. Původní záznam zůstane v historii zachován.

### 4.6.3 Tisk přehledu závazků

Plný přehled závazků pacienta (včetně plateb) exportujte ze záložky **Závazky** tlačítkem **Tisk přehledu**.

> [!danger]
> Pokud se při ukládání závazku zobrazí chyba **„Nenalezena platná cena“**, ověřte, zda má sortiment zadanou cenu s platností pokrývající aktuální datum (**Nastavení → Sortiment → Ceník**). Podrobnosti viz kapitola 4.3.
