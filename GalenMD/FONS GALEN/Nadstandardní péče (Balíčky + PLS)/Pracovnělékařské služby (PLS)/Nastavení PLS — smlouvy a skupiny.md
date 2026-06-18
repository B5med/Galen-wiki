---
title: "Nastavení PLS — smlouvy a skupiny"
version: 2
updated_at: 2026-06-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/436305934
---

# Nastavení PLS — smlouvy a skupiny

Tato stránka popisuje jednorázové nastavení, které provádí uživatel s rolí **správce** před započetím práce s PLS. Zahrnuje správu firem, skupin zaměstnanců, rizik, smluv a pracovního zařazení pacientů.

---

## Správa firem a poboček

### Založení firmy

Novou firmu přidáte v modulu **Nadstandardní péče** tlačítkem **„+"**. Údaje se automaticky doplní z databáze **ARES** na základě IČO.

Lze ukládat pouze **české firmy** registrované v ARES. Zahraniční firmy nejsou podporovány.

| Pole | Popis |
| --- | --- |
| **Název, IČO, adresa** | Doplní se z ARES automaticky |
| **Prohlídka předem (dny)** | Kolik dní před nástupem lze provést vstupní prohlídku |
| **Aktivní stav** | Aktivní firma je dostupná při zadávání pacientů a smluv |

Odstranit firmu lze pouze tehdy, pokud na ni nejsou navázány žádné záznamy (pobočky, smlouvy, skupiny PLS). Jinak lze jen změnit stav na **neaktivní**.

### Pobočky

Každá firma může mít více poboček. Zakládají se v detailu firmy.

| Pole | Popis |
| --- | --- |
| **Typ pobočky** | Informativní údaj (Provozovna / Jednotka) |
| **Fakturovat samostatně** | Pobočka bude mít vlastní fakturu při generování |
| **Období vedení lhůtníku (od–do)** | Definuje, pro jaké období se vypočítává interval prohlídek. Prohlídky mimo toto období nevstupují do výpočtu lhůt. |
| **Pracoviště** | Umožní uživatelům daného pracoviště zobrazit informace o firmě a jejích smlouvách |
| **Hodnosti** | Doplňkový informativní údaj zobrazovaný na kartě pacienta |

### Kontakty

K firmě nebo pobočce lze přidat kontaktní osoby (např. personalisty nebo bezpečnostní techniky).

- Kontakt lze přiřadit konkrétnímu aktivnímu uživateli systému Galen, který má příznak **PLS**. Přiřazením kontaktu se firmě a jejím smlouvám zpřístupní daný uživatel v PLS aplikaci.
- Pokud uživatel není vybrán, má kontakt pouze informativní funkci na kartě firmy.
- **Typ kontaktu** (informativní): HR / Fakturace / Obchod / Provoz.

### Nákladová střediska

Nákladová střediska umožňují rozdělit náklady v rámci jedné firmy na více celků pro účely fakturace a reportingu. Podrobný popis viz stránku [[Nákladová střediska]].

---

## Skupiny PLS a rizika

### Skupiny PLS (pozice zaměstnanců)

Skupiny PLS slouží k rozdělení zaměstnanců podle pracovních pozic nebo rizikovosti práce. Každá skupina je přiřazena konkrétní firmě a může mít definována tři typy rizik:

1. **Kategorie**
2. **Faktory prostředí**
3. **Ohrožení zdraví**

**Princip výpočtu intervalu:** Interval mezi prohlídkami se určuje jako **nejkratší (MIN)** z intervalů všech přiřazených rizik. Nastavení skupin PLS má přímý vliv na výpočet data příští prohlídky a plánování v kalendáři.

### Rizika

Rizika určují frekvenci pracovnělékařských prohlídek podle druhu práce a expozice. Spravují se v sekci **Rizika** v modulu Nadstandardní péče.

| Typ rizika | Příklady |
| --- | --- |
| **Kategorie** | Práce ve výškách, práce s chemikáliemi |
| **Faktory prostředí** | Hluk, prach, vibrace, teplota |
| **Ohrožení zdraví** | Ergonomie, stres, zraková zátěž |

- **Periodické prohlídky:** Interval lze vztahovat na věk pacientů (zadáním věku od–do). Věk se zjišťuje **zpětně** při uzavření prohlídky.
- **Mimořádná prohlídka** a **Následná prohlídka**: aktuálně pouze informativní charakter, nepoužívají se v žádné jiné logice.
- Riziko lze smazat pouze tehdy, pokud nebylo použito ve skupinách PLS.
- Interval prohlídky lze smazat i v případě, že již byl použit — pokud se datum příští prohlídky počítalo z tohoto intervalu, datum se smaže.

Po změně rizik stiskněte tlačítko **„Přepočti všechny intervaly všech pacientů"** — aktualizují se lhůty všech zaměstnanců dané firmy.

---

## Smlouvy PLS

### Založení nové smlouvy

Novou smlouvu lze vytvořit:

- **od začátku** pomocí tlačítka **„Nová"**, nebo
- **zkopírováním existující smlouvy** z jiné firmy (např. při podobném typu spolupráce).

Pro vytvoření smlouvy je nutné, aby firma měla alespoň **jednu aktivní pobočku**.

### Nastavení smlouvy

| Parametr | Popis |
| --- | --- |
| **Platnost od / do** | Určuje období, pro které je smlouva aktivní |
| **Nefakturovat** | Pokud zaškrtnuto, ze smlouvy se negenerují žádné faktury (ani výkonové, ani paušální) |
| **Způsob platby: Kombinovaně** | Generují se jak výkonové, tak paušální faktury |
| **Způsob platby: Paušál** | Generují se pouze pravidelné paušální faktury |
| **Způsob platby: Výkony** | Generují se pouze faktury za jednotlivé výkony. **Pozor: výkonové faktury se generují výhradně zpětně** — pouze za položky uzavřené v předchozím měsíci a dříve. |

### Nastavení paušálu

| Parametr | Popis |
| --- | --- |
| **Režim platby paušálu** | *Dopředu* — faktura za aktuální měsíc; *Zpětně* — faktura za předchozí měsíc |
| **Počet měsíců paušálu** | Frekvence generování faktur (1 = měsíčně, 3 = čtvrtletně, 12 = ročně). Pokud nezadáno, bere se 1 měsíc. |
| **Typ paušálu: Jednorázový** | Faktura obsahuje cenu paušálu 1× |
| **Typ paušálu: Za 1 pacienta** | Faktura obsahuje cenu paušálu × počet uzavřených hlavních položek (bez ohledu na vazbu). Příklad: Cena paušálu 1 000 Kč. Pacient 1 má jednu PLS prohlídku. Pacient 2 má jednu prohlídku a jedno PLS očkování. Faktura paušálu = 3 000 Kč (3 hlavní položky). |

### Fakturace „Nedostavil se"

V rámci smlouvy lze určit, zda se mají fakturovat i případy, kdy se zaměstnanec nedostavil na prohlídku. Lze nastavit buď **procento z ceny**, nebo **pevnou částku** (bez DPH). Pokud jsou vyplněny obě hodnoty, uplatní se procento.

Procento se vztahuje **pouze na cenu hlavní položky smlouvy** — rozšiřující položky se do výpočtu nezahrnují.

Příklad: Cena hlavní položky 1 000 Kč, smluvně dohodnutý poplatek za nedostavení = 20 %. Do faktury se promítne částka 200 Kč.

### Položky smlouvy

Každá smlouva se skládá z **hlavních položek** a volitelně také z **rozšiřujících položek**.

| Typ položky | Charakteristika |
| --- | --- |
| **Hlavní položky** | Základní služby (prohlídky, očkování); vždy vázané na skupinu PLS; lze omezit věkem a pohlavím; účtování fakturou nebo hotově. **Cena se při výběru sortimentu nepřenáší z ceníku** — je nutné ji zadat ručně. Limit je aktuálně pouze informativní. Pole Poznámka je viditelné pouze v editaci položky smlouvy. |
| **Rozšiřující položky** | Navázány na konkrétní hlavní položku (musí být ze sortimentu skupiny Prohlídky); načtou se automaticky při vytváření PLS prohlídky; cena se zahrne společně s hlavní položkou do faktury. |

**Vazba položky**: *Výkon* — položka vstupuje do výkonových faktur. *V paušálu smlouvy* — položka nevstupuje do žádné faktury, cena má pouze informativní charakter.

**Způsob úhrady**: *Hotově* — položky s tímto typem se nezobrazují ve fakturách. *Faktura* — položky vstupují do faktur.

---

## Zaměstnání pacienta

Na kartě pacienta lze přiřadit zaměstnavatele. Firma s příznakem PLS lze uložit pouze tehdy, pokud má **aktivní smlouvu** a na smlouvě alespoň **jednu hlavní položku se zařazenou skupinou PLS**.

| Pole | Popis |
| --- | --- |
| **PLS Poznámka** | Zobrazuje se červeně v PLS Adminu a na prohlídce — slouží k upozornění personálu na specifika zaměstnance. |
| **Středisko** | Informativní charakter; slouží jako filtr v PLS aplikaci. |
| **Platnost posudku** | Údaj dotažený z modulu Recepce nebo Objednávání. Používá se pro výpočet data příští prohlídky, pokud dosud neproběhla žádná PLS prohlídka. |
| **Plánovaná prohlídka** | Datum poslední plánované prohlídky. |
| **Pozastavení** | Informativní charakter; používá se jako filtr v PLS aplikaci. Hodnoty: *Ne / MD + RD / DPN / Jiný důvod*. |

---

## Návody krok za krokem

### 4.5 Vytvoření smlouvy PLS

**Cíl:** Uzavřít smluvní vztah se zaměstnavatelem a nastavit podmínky fakturace.

**Kdo:** Správce

**Předpoklady:** Firma (zaměstnavatel) je evidována v systému Galen.

1. Vyberte firmu ze seznamu a otevřete detail firmy dvojklikem.
2. Označte příznak „PLS" v levé části „Základní údaje".
3. Označte pobočku pro tvorbu smlouvy PLS v sekci „Pobočky" nebo vytvořte novou pobočku.
4. Klikněte na + v sekci „Smlouvy PLS".
5. Vyplňte Kód (max. 10 znaků) a Název (max. 100 znaků).
6. Nastavte Platnost od a volitelně Platnost do.
7. Zvolte Způsob platby: Paušál, Výkony nebo Kombinovaně.
8. Vyplňte Cenu a Sazbu DPH (cena vč. DPH se dopočítá automaticky).
9. Nastavte Slevu (%) (0 = bez slevy).
10. Volitelně nakonfigurujte fakturaci stavu „Nedostavil se" (procentem z ceny nebo pevnou částkou).
11. Klikněte na OK.
12. Po uložení přejděte na záložku **Položky smlouvy**.
13. Klikněte na **Nová položka** (+) a vyplňte: Cena a Sazba DPH, Sleva (%), Limit, Vazba (Výkon / V paušálu smlouvy), Skupina PLS, volitelně Omezení věku/pohlaví a Fakturovat samostatně.
14. Klikněte na OK.

**Výsledek:** Smlouva PLS je evidována v systému a připravena k naplnění položkami.

### 4.9 Vytvoření skupiny (pozice) PLS

**Cíl:** Vytvořit pracovní skupinu zaměstnanců pro danou firmu a přiřadit jí odpovídající druhy rizik.

**Kdo:** Správce ordinace / správce systému.

1. Přejděte do sekce Pracovnělékařské služby → Skupiny PLS.
2. Klikněte na Nová skupina (nebo Ins).
3. Vyberte Firmu, pro kterou skupinu zakládáte.
4. Zadejte Název skupiny (max. 100 znaků), např. Skladník, Řidič referentský.
5. Zkontrolujte, že je přepínač Aktivní nastaven na Aktivní.
6. Klikněte na Uložit.
7. Přejděte na záložku Rizika skupiny a přidejte druhy rizik (dle § 37 zák. 373/2011 Sb.).
8. Uložte záznamy rizik.

**Výsledek:** Skupina PLS je evidována a připravena k přiřazení zaměstnanců a k propojení s položkami smlouvy PLS.

Tip: Jedna skupina PLS je sdílená napříč smlouvami — „Skladník" lze propojit s položkami z více smluv různých zaměstnavatelů.
