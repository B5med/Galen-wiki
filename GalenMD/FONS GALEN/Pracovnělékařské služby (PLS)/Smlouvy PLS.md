---
title: "Smlouvy PLS"
version: 1
updated_at: 2025-11-07
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/150110227
---

# Smlouvy PLS

> [!info]
> Smlouvy představují klíčovou část modulu **Nadstandardní péče**.
> Definují podmínky spolupráce s konkrétní firmou – tedy jaké služby a vyšetření se budou provádět, jak často a jak budou fakturována.

---

### ➕ Založení nové smlouvy

Novou smlouvu lze vytvořit:

- **od začátku** pomocí tlačítka **„Nová“**, nebo
- **zkopírováním existující smlouvy** z jiné firmy (např. při podobném typu spolupráce).

> ⚠️ Pro vytvoření smlouvy je nutné, aby firma měla alespoň **jednu aktivní pobočku**.

#### Možnosti při kopírování:

- Lze kopírovat libovolnou existující smlouvu ze všech firem.
- Název nové smlouvy se po kopírování automaticky doplní jako *„Kopie“* původní.

---

### ⚙️ Nastavení smlouvy

#### Základní parametry:

- **Platnost od / do** – určuje období, pro které je smlouva aktivní.
- **Nefakturovat** – pokud je zaškrtnuto, ze smlouvy se negenerují žádné faktury (ani výkonové, ani paušální).
- **Způsob platby** – definuje typ fakturace:

   - **Kombinovaně** – generují se jak výkonové, tak paušální faktury,
   - **Paušál** – generují se pouze pravidelné paušální faktury,
   - **Výkony** – generují se pouze faktury za jednotlivé výkony, a to zpětně (za uzavřené položky z předchozího měsíce).

#### Nastavení paušálu:

- **Režim platby paušálu**

   - *Dopředu* – faktura se vytváří za aktuální měsíc,
   - *Zpětně* – faktura se vytváří za předchozí měsíc.
- **Počet měsíců paušálu** – určuje, jak často se faktury generují (např. 1 = měsíčně, 3 = čtvrtletně, 12 = ročně).
- **Typ paušálu**

   - *Jednorázový* – paušál se fakturuje jako jedna částka,
   - *Za 1 pacienta* – faktura obsahuje cenu paušálu × počet uzavřených položek (např. počet provedených prohlídek).

---

### 💰 Fakturace „Nedostavil se“

V rámci smlouvy lze určit, zda se mají fakturovat i případy, kdy se zaměstnanec nedostavil na prohlídku.

- **Fakturovat stav „Nedostavil se“**

   - Pokud je volba aktivní, systém vygeneruje fakturu i za prohlídku, která byla uzavřena tímto výsledkem.
   - Lze nastavit buď **procento z ceny**, nebo **pevnou částku** (bez DPH).
   - Pokud jsou vyplněny obě hodnoty, uplatní se procento.

> 💡 Typický příklad:
> Cena hlavní položky 1000 Kč, smluvně dohodnutý poplatek za nedostavení se = 20 %.
> Do faktury se promítne částka 200 Kč.

---

### 📋 Položky smlouvy

Každá smlouva se skládá z **hlavních položek** (např. prohlídky, očkování) a volitelně také z **rozšiřujících položek** (např. laboratorní testy, doplňková vyšetření).

#### Hlavní položky:

- jsou základními službami poskytovanými v rámci smlouvy,
- vždy mají vazbu na konkrétní **skupinu PLS**,
- mohou být účtovány buď **fakturou**, nebo **v hotovosti**,
- lze omezit jejich použití podle **věku a pohlaví** pacienta.

#### Rozšiřující položky:

- navazují na konkrétní hlavní položku (např. vstupní prohlídku),
- při vytvoření prohlídky se automaticky načtou do formuláře,
- jejich cena se do faktury zahrne společně s hlavní položkou.

> 💡 Doporučení:
> Pokud má firma specifické požadavky (např. povinné testy pro určité profese), přidejte je jako rozšiřující položky k příslušné prohlídce.
