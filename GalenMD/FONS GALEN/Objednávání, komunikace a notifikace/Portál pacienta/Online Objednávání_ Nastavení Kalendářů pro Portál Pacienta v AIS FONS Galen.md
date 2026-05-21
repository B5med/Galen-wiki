---
title: "Online Objednávání: Nastavení Kalendářů pro Portál Pacienta v AIS FONS Galen"
version: 3
updated_at: 2026-01-19
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/233504769
---

> [!info]
> Tento text popisuje, jak správně nastavit kalendáře v AIS FONS Galen tak, aby se pacienti mohli **objednávat online prostřednictvím Portálu pacienta**.

Dokument je určen pro:

- správce ordinace
- administrativní pracovníky
- odpovědné osoby za nastavení objednávání

---

## Základní princip online objednávání

Portál pacienta pouze **zobrazuje a zpracovává data z IS Galen**.
Pokud není nastavení v Galenu správné, pacient se nemůže objednat.

Aby bylo online objednávání funkční, musí být splněny všechny následující podmínky:

- existuje **pracoviště (provozovna)**
- existuje **kalendář**
- kalendář je **aktivní a veřejný**
- kalendář má přiřazené **odpovědné pracoviště**
- jsou nastavené **veřejné ordinační hodiny**
- ordinační hodiny mají povolené **typy objednávek**

---

## 1️⃣ Kontrola pracoviště (provozovny)

**Cesta v Galenu:**
`Správce → Správa organizace → Pracoviště`

Zkontrolujte, že:

- pracoviště je **aktivní**
- má správně vyplněný **název**
- název je srozumitelný pro pacienty

> ℹ️ Název pracoviště se zobrazuje pacientům při výběru místa objednání.

**Doporučení:**
Nepoužívejte interní nebo technické názvy, které pacientům nic neříkají.

---

## 2️⃣ Nastavení kalendáře

**Cesta v Galenu:**
`Správce → Správa organizace → Agendy → Kalendáře`

V detailu kalendáře nastavte následující položky:

### Povinné nastavení

- **Název kalendáře**
   (např. „Gynekologie – MUDr. Nováková“)
- **Odpovědné pracoviště** ❗
   Bez této položky nelze kalendář označit jako veřejný.
- **Veřejný** = zapnuto ❗
   Pouze veřejné kalendáře se zobrazují v Portálu pacienta.
- **Aktivní** = zapnuto

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Portál pacienta/Online Objednávání_ Nastavení Kalendářů pro Portál Pacienta v AIS FONS Galen/assets/obrazek-20260119-125505.png]]

### Doporučené nastavení

- **Minutový interval** (např. 10 nebo 15 minut)
- **Pořadí** – určuje pořadí kalendářů v Portálu pacienta
- **Omezení rezervací** (např. uzavření objednávání 24 hodin předem)

---

## 3️⃣ Typy objednávek (úkonů)

Typy objednávek určují, **na jaký úkon se pacient může objednat** prostřednictvím Portálu pacienta.

**Cesta v Galenu:**
`Správce → Správa organizace → Agendy → Kalendáře → Typy objednávek`

U každého typu objednávky, který má být dostupný pacientům, je nutné nastavit:

- **Název typu objednávky**
   (zobrazuje se pacientům)
- **Délku trvání**
   (např. 20, 30 nebo 60 minut)
- **Veřejný = zapnuto** ❗
   Pouze veřejné typy objednávek se zobrazují v Portálu pacienta.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Portál pacienta/Online Objednávání_ Nastavení Kalendářů pro Portál Pacienta v AIS FONS Galen/assets/obrazek-20260119-130725.png]]
> ⚠️ Typ objednávky, který není označen jako **veřejný**, se pacientům **nikdy nezobrazí**, ani pokud je přiřazen ke kalendáři.

---

## 4️⃣ Ordinační hodiny

Ordinační hodiny určují, **kdy** se pacient může objednat.

**Postup:**

1. Otevřete detail kalendáře, bublina Ordinační hodiny
2. Dvojklikem vytvořte nebo upravte blok ordinačních hodin

U každého bloku zkontrolujte:

- **Veřejný** = zapnuto ❗
- povolené **typy objednávek**
- správný **časový rozsah**

> ℹ️ Kalendář může být veřejný, ale pokud ordinační hodiny veřejné nejsou, pacient neuvidí žádné termíny.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Portál pacienta/Online Objednávání_ Nastavení Kalendářů pro Portál Pacienta v AIS FONS Galen/assets/obrazek-20260119-135114.png]]

---

## 5️⃣ Omezení objednávání (doporučeno)

V nastavení Typu objednávky lze konfigurovat

- jak dlouho dopředu se lze objednat
- nejpozdější čas pro změnu nebo zrušení rezervace
- minimální časový odstup před termínem

Doporučujeme tato omezení používat, aby se předešlo rušení termínů na poslední chvíli.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Portál pacienta/Online Objednávání_ Nastavení Kalendářů pro Portál Pacienta v AIS FONS Galen/assets/obrazek-20260119-135400.png]]

---

## 6️⃣ Notifikace pacientům

Pro zvýšení komfortu pacientů doporučujeme zapnout notifikace:

- potvrzení objednávky
- zrušení objednávky
- připomenutí termínu

**Cesta v Galenu:**
`Kalendář → Notifikace a připomínání`

---

# 🧪 Test nastavení online objednávání – krok za krokem

Tato část slouží k ověření, že je online objednávání správně nastavené a funkční.

Doporučujeme test provést:

- po každé změně kalendáře
- po změně ordinačních hodin
- při zavádění online objednávání

---

## Krok 1 – Ověření kalendáře

1. Otevřete:
   `Správce → Správa organizace → Agendy → Kalendáře`
2. Otevřete kalendář určený pro online objednávání

Zkontrolujte:

- ☐ kalendář je **aktivní**
- ☐ je označen jako **veřejný**
- ☐ má vyplněné **odpovědné pracoviště**
- ☐ název je srozumitelný pro pacienta

---

## Krok 2 – Ověření ordinačních hodin

1. V detailu kalendáře otevřete **Ordinační hodiny**
2. Otevřete konkrétní časový blok

Zkontrolujte:

- ☐ blok je **veřejný**
- ☐ má povolené typy objednávek
- ☐ čas odpovídá realitě

---

## Krok 3 – Ověření typů objednávek

1. Otevřete:
   `Správce → Správa organizace → Agendy → Kalendáře → Typy objednávek`

Zkontrolujte:

- ☐ typ objednávky existuje
- ☐ má nastavenou délku trvání
- ☐ je povolen v kalendáři
- ☐ je povolen v ordinačních hodinách

---

## Krok 4 – Test z pohledu pacienta

1. Otevřete Portál pacienta
2. Zvolte **Objednání k lékaři**
3. Postupně vyberte:

   - pracoviště
   - kalendář
   - typ objednávky

Ověřte:

- ☐ pracoviště se zobrazuje
- ☐ kalendář se zobrazuje
- ☐ typ objednávky se zobrazuje
- ☐ jsou vidět volné termíny
- ☐ objednávku lze dokončit

---

## Krok 5 – Kontrola notifikací (volitelné)

Po vytvoření testovací objednávky zkontrolujte:

- ☐ dorazilo potvrzení e-mailem nebo SMS
- ☐ při zrušení dorazí notifikace
- ☐ dorazí připomenutí termínu

---

## ❌ Nejčastější problémy

| Problém | Pravděpodobná příčina |
| --- | --- |
| Kalendář se nezobrazuje | Není veřejný nebo nemá pracoviště |
| Nejsou vidět termíny | Ordinační hodiny nejsou veřejné |
| Nezobrazuje se typ objednávky | Typ není povolen v bloku |
| Nelze dokončit objednávku | Nastavené omezení rezervací |
