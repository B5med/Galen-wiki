---
title: "Pracovnělékařské služby (PLS)"
version: 5
updated_at: 2026-05-14
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/150339588
---

> [!info]
> Modul **Nadstandardní péče** slouží k evidenci a správě pracovnělékařských prohlídek, očkování a služeb poskytovaných zaměstnancům firemních klientů.
> Umožňuje kompletní zpracování agendy pracovnělékařské péče — od správy firem a smluv až po fakturaci a sledování lhůtníku prohlídek.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/assets/image-20250626-132147.png]]

---

**Hlavní přínosy modulu**

- přehledná evidence firem, poboček a jejich smluvních vztahů,
- automatické načítání údajů z ARES,
- propojení s kalendářem a kartou pacienta,
- automatický výpočet lhůtníku podle rizik,
- podpora výkonové i paušální fakturace,
- možnost importu zaměstnanců z CSV souboru,
- přehled uzavřených i plánovaných prohlídek v PLS Adminu.

---

**Komu je modul určen**

- **lékařům a sestrám** pracovnělékařských služeb,
- **administrátorům** spravujícím firemní smlouvy,
- **recepci**, která zajišťuje objednávání a evidenci návštěv,
- **vedení**, které sleduje přehled fakturace a vykázaných služeb.

---

## 🏢Správa firem a poboček

---

### 🔸

Novou firmu přidáte v modulu **Nadstandardní péče** pomocí tlačítka **„+“**.
V současnosti lze ukládat pouze české firmy z databáze **ARES**.

> [!warning]
> Odstranit firmu je možné pouze tehdy, pokud na ni nejsou navázány jiné záznamy (např. pobočky, smlouvy nebo skupiny PLS).
> Pokud již existují vazby, lze pouze změnit stav firmy na neaktivní.

**Pole a nastavení:**

- **Název firmy**, **IČO**, **adresa** – údaje se doplňují automaticky z ARES,
- **Prohlídka předem (dny)** – určuje, kolik dní před začátkem zaměstnání je možné provést vstupní prohlídku,
- **Aktivní stav** – určuje, zda je firma dostupná při zadávání pacientů a smluv.

---

### 🔸 Pobočky

Každá firma může mít více poboček. Ty se zakládají v detailu firmy.

**Možnosti nastavení:**

- **Typ pobočky** – informativní údaj (*Provozovna* / *Jednotka*),
- **Fakturovat samostatně** – pokud je zaškrtnuto, pobočka bude mít při generování faktur vlastní fakturu,
- **Období vedení lhůtníku (od–do)** – určuje, pro jaké období se vypočítává interval prohlídek,
- **Pracoviště** – přidáním pracoviště umožníte jeho uživatelům (s povoleným modulem Nadstandardní péče) zobrazit informace o firmě a jejích smlouvách,
- **Hodnosti** – doplňkový informativní údaj, zobrazovaný na kartě pacienta při zadávání zaměstnavatele.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/assets/image-20250626-132627.png]]
> 💡 **Doporučení:**
> Nastavte pro každou pobočku jasné období vedení lhůtníku. Prohlídky založené mimo toto období se do výpočtu lhůt nezahrnují.

---

## 👥 Skupiny PLS a rizika

---

### 🔸

Skupiny PLS slouží k rozdělení zaměstnanců podle pracovních pozic nebo rizikovosti práce.
Každá skupina je přiřazena konkrétní firmě a může mít definována tři typy rizik:

1. **Kategorie**,
2. **Faktory prostředí**,
3. **Ohrožení zdraví**.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/assets/image-20250626-132754.png]]
**Princip výpočtu intervalu:**

Interval mezi prohlídkami se určuje jako **nejkratší (MIN)** z intervalů všech zvolených rizik.
Tím je zajištěno, že zaměstnanci s vyšším rizikem mají kratší periodu kontrol.

> [!info]
> Nastavení skupin PLS má přímý vliv na výpočet data příští prohlídky a plánování v kalendáři.

---

### 🔸

Rizika určují frekvenci pracovnělékařských prohlídek podle druhu práce a expozice.

**Typy rizik:**

- **Kategorie** (např. práce ve výškách, práce s chemikáliemi),
- **Faktory prostředí** (hluk, prach, vibrace, teplota),
- **Ohrožení zdraví** (ergonomie, stres, zraková zátěž).

**Správa rizik:**

- Rizika se vytvářejí a upravují v sekci **Rizika** v modulu Nadstandardní péče,
- Lze je upravovat, mazat nebo přidávat nové, pokud nejsou již použita ve skupinách,
- Po změně rizik je nutné stisknout tlačítko **„Přepočti všechny intervaly všech pacientů“** — aktualizují se tím lhůty všech zaměstnanců dané firmy.

---
