---
title: "Ceník a sortiment"
version: 2
updated_at: 2026-06-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/436699137
---

# Ceník a sortiment

## Přehled polí sortimentní položky

Tato sekce popisuje všechna dostupná pole při vytváření nebo editaci položky sortimentu, včetně méně zřejmých chování.

| Pole | Popis a chování |
| --- | --- |
| **Aktivní** | Může nabývat tří stavů: *Aktivní* — položka je funkční. *Neaktivní* — nezobrazuje se při vytváření položek smlouvy ani v nabídce sortimentu v okně Stav účtu. *Neexistuje* — logika chování identická jako Neaktivní, pouze informativní rozlišení (např. pro položky, které byly odstraněny z nabídky trvale). |
| **Kód** | Povinné pole. Unikátní identifikátor položky. |
| **Název** | Povinné pole. |
| **Doplněk** | Volitelný popis položky — zobrazuje se např. na faktuře. |
| **Pořadí** | Určuje pořadí zobrazení při **tisku a exportu PLS faktur**. Výchozí hodnota 10 000. |
| **Variabilní cena** | Při zaškrtnutí lze cenu této položky v okně **Stav účtu** (modul Ordinace) ručně upravit. |
| **Sazba DPH** | Povolené hodnoty: 0 %, 10 %, 15 %, 21 %. |
| **Cena / Cena vč. DPH** | Zadáním jedné hodnoty se druhá dopočítá automaticky. |
| **Platnost od–do** | Definuje období platnosti ceny. Pokud pro aktuální datum neexistuje platná cena, systém odmítne vyúčtování. |
| **Odbornost** | Omezuje platnost ceny na danou odbornost. **Nelze kombinovat s polem Pracoviště** — je-li zadána odbornost, pracoviště musí zůstat prázdné. |
| **Pracoviště** | Omezuje platnost ceny na konkrétní pracoviště. **Nelze kombinovat s polem Odbornost** — je-li zadáno pracoviště, odbornost musí zůstat prázdná. Bez vyplnění platí cena pro celou ordinaci. |

> [!info]
> Cena z ceníku sortimentu se zobrazuje při výběru v okně **Stav účtu**. Výjimka: u firem bez příznaku PLS a bez smlouvy se tato cena přenáší i při vytváření PLS prohlídky v modulu Ordinace — pokud není zadána odbornost ani pracoviště, zobrazuje se všem takovým firmám.

---

## Návody krok za krokem

### 4.3 Nastavení ceníku pro sortiment

**Cíl:** Přiřadit cenu konkrétní sortimentní položce s platností od–do a sazbou DPH.

**Kdo:** Správce

**Předpoklady:** Existující sortiment, oprávnění ke správě ceníků.

1. Otevřete modul Nadstandardní péče (viz kapitola 2.2).
2. Klikněte na ikonu „Ceníky".
3. Vyberte požadovaný typ položky ceníku ① a přejděte na požadovanou položku ②.
4. Lze také vytvořit zcela nový záznam ceníku ③.
5. Zadejte Platnost od ④ (povinné) a volitelně Platnost do ⑤.
6. Zadejte Cenu bez DPH ⑥ a Sazbu DPH ⑦ v procentech (např. 21 pro 21 %).
7. Pole Cena vč. DPH ⑧ se vypočítá automaticky.
8. Volitelně přiřaďte Pracoviště ⑨ — bez přiřazení platí cena pro celou ordinaci.
9. Klikněte na Uložit.

**Výsledek:** Pro daný sortiment je evidována cena s platností. Při vyúčtování bude systém automaticky dohledávat aktuálně platnou cenu.

> [!warning]
> Pokud pro aktuální datum neexistuje platná cena, systém odmítne vyúčtování a zobrazí chybové hlášení.

---

### 4.4 Deaktivace sortimentní položky

**Cíl:** Vyřadit položku sortimentu z aktivní nabídky bez nutnosti jejího smazání (zachování historických dat).

**Kdo:** Správce ordinace.

1. Přejděte do Ceníky → Sortiment.
2. Vyberte položku, v detailu změňte pole Aktivní ① z hodnoty Aktivní na Neaktivní.
3. Klikněte na OK ②.

**Výsledek:** Položka zůstane v systému (historická data zachována), ale nebude se nabízet při nových vyúčtováních.

> [!info]
> Smazání položky zahrnuté v existujícím balíčku nebo závazku systém neumožní, pokud k ní již existují navázané položky. Použijte deaktivaci místo mazání.

---

### 4.10 Přidání nové položky sortimentu

**Cíl:** Zaregistrovat novou položku (zboží, výkon nebo očkování) do číselníku sortimentu.

**Kdo:** Správce ordinace / správce systému.

**Předpoklady:** Oprávnění ke správě sortimentu.

1. Přejděte do sekce Nastavení → Sortiment ①.
2. Klikněte na Nová položka ② (nebo Ins).
3. Zadejte Kód ③ (max. 50 znaků, unikátní), např. VITA-C, PRAC-PRO.
4. Zadejte Název ④ (max. 255 znaků), např. Vitamín C 1000 mg, Pracovní prohlídka – řidiči.
5. Vyberte Typ sortimentu ⑤: Sortiment (S), Prohlídka (P) nebo Očkování (O).
6. Nastavte Aktivní ⑥ na hodnotu Aktivní.
7. Volitelně doplňte Pořadí ⑦ (výchozí 10 000) — ovlivňuje pořadí při tisku PLS faktur.
8. Klikněte na Uložit ⑧.
9. Přejděte na záložku Ceník ⑨ a zadejte cenu (viz kapitola 4.3).

**Výsledek:** Nová položka sortimentu je dostupná pro přiřazení do balíčků nebo do položek smlouvy PLS.

> [!warning]
> Bez záznamu ceníku nelze položku vyúčtovat — systém zobrazí chybu „Nenalezena platná cena".
