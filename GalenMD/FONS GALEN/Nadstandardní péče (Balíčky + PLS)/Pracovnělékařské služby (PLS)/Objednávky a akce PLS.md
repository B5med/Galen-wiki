---
title: "Objednávky a akce PLS"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/436666381
---

# Objednávky a akce PLS

### 4.6 Vytvoření objednávky PLS

*Cíl: Naplánovat pracovnelékařskou prohlídku pro konkrétního zaměstnance a vložit ji do systému jako nové PLS akce.*
*Kdo: Koordinátor PLS, správce ordinace.*
*Předpoklady: Pacient (zaměstnanec) je zaevidován v systému, existuje platná smlouva PLS s příslušnou skupinou PLS.*

1. Přejděte do sekce **Pracovnelékařské služby → Objednávky PLS**.
2. Klikněte na **Nová objednávka** (+).
3. Vyberte **Pacienta** (zaměstnance) ze seznamu.
4. Vyberte **Firmu** a **Pobocku** zaměstnavatele.
5. Vyberte **Skupinu PLS** odpovídající pracovní pozici zaměstnance.
6. Zvolte **Typ prohlídky** (Vstupní, Periodická, Výstupní, Mimoperiodická nebo jiná dle smlouvy).
7. Zadejte **Plánované datum** prohlídky.
8. Volitelně doplňte **Poznámku** (max. 1024 znaků).
9. Klikněte na **Uložit** — systém vytvoří novou akci PLS ve stavu *Nová plánovaná akce*.

*Výsledek: V systému je vytvořena objednávka PLS, která se zobrazí v seznamu Akcí PLS a v lhůtníku.*

> [!tip]
> Objednávky lze hromadně generovat přímo z **Lhůtníku** (sekce Pracovnelékařské služby → Lhůtník) — systém zobrazí všechny zaměstnance, kteří mají prohlídku po lhůtě nebo se blíží termín jejich periodické prohlídky.

---

### 4.7 Uzavření akce PLS a příprava k fakturaci

*Cíl: Po realizaci pracovnelékařské prohlídky správně uzavřít akci PLS a připravit ji k fakturaci zaměstnavateli.*
*Kdo: Koordinátor PLS, zdravotnický personál.*
*Předpoklady: Prohlídka pacienta byla provedena a zapsána v systému, akce PLS je ve stavu „Nová plánovaná akce“ nebo „Přiděleno dalšími IČP“.*

1. Přejděte do části Pracovnelékařské služby → Akce PLS.
2. Vyhledejte příslušnou akci pacienta (filtr podle firmy, data nebo stavu).
3. V detailu akce zkontrolujte pole Vyšetření a Datum návštěvy.
4. Zkontrolujte Cenu a Způsob úhrady (Hotově / Faktura).
5. Volitelně doplňte Poznámku (max. 1024 znaků).
6. Klikněte na Uzavřít akci — zvolte stav Uzavřena, fakturovat nebo Uzavřena, nefakturovat.
7. Spusťte funkci Vyúčtování PLS pro hromadnou přípravu faktur za dané období.
8. Klikněte na Vystavit fakturu PLS a vyplňte: číslo faktury, datum vystavení, datum plnění, období od/do, typ faktury (Paušál nebo Výkony), identifikaci pacientů, popis.
9. Fakturu vytiskněte přes Tisk vyúčtování PLS.

*Stavy akce PLS — přehled workflow:*

| Stav | Popis | Přechod do |
| --- | --- | --- |
| Nová plánovaná akce | Akce je naplánována, prohlídka dosud neproběhla | Přiděleno dalšími IČP / uzavřena |
| Přiděleno dalšími IČP | Prohlídka přidělena k provedení externím poskytovatelem | Vráceno / uzavřena |
| Vráceno | Akce vrácena k přepracování | Nová plánovaná akce |
| Uzavřena, fakturovat | Prohlídka proběhla, bude zahrnuta do faktury | Faktura vystavena |
| Uzavřena, nefakturovat | Prohlídka uzavřena bez nároku na fakturaci | — |
| Faktura vystavena | Faktura pro zaměstnavatele byla vystavena | — |

*Výsledek: Akce PLS je uzavřena a faktura vystavena zaměstnavateli.*

*⚠️ Upozornění: Uzavřenou akci ve stavu „Faktura vystavena“ nelze zpětně editovat. Pokud je nutná oprava, kontaktujte správce systému — faktura musí být nejprve stornována funkcí „Smazat fakturu PLS“.*

---

### 4.8 Zapsání výsledku pracovnelékařského posudku

*Cíl: Po provedení pracovnelékařské prohlídky zapsat výsledek posudku do systému.*
*Kdo: Lékař.*
*Předpoklady: V systému existuje akce PLS ve stavu „Nová plánovaná akce“ nebo „Přiděleno dalšími IČP“.*

1. Na kartě pacienta přejděte na záložku PLS → Akce PLS a vyhledejte příslušnou akci.
2. Otevřete detail akce a zkontrolujte propojení s Vyšetřením.
3. V poli Výsledek posudku vyberte odpovídající hodnotu (Z / N / K / M / D / B / X).
4. Doplňte Poznámku (max. 1024 znaků) a klikněte na Uložit.
5. Pokud má být prohlídka fakturována, změňte stav na Uzavřena, fakturovat (podrobný postup viz kapitola 4.7).

*Výsledek: Výsledek posudku je zapsán a propojen s akcí PLS a vyšetřením pacienta.*

*⚠️ Upozornění: Výsledek X — Nedostavil/a se nevyžaduje propojení s vyšetřením. Zkontrolujte nastavení smlouvy ohledně fakturace tohoto stavu.*

---
