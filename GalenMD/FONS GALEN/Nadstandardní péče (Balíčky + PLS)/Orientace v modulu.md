---
title: "Orientace v modulu"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/435486723
---

# Orientace v modulu

## 1. Úvod

### 1.1 K čemu modul slouží

Modul Nadstandardní péče pokrývá dvě hlavní oblasti:

1. **Nadstandardní péče (balíčky)** — správa a účtování služeb a zboží, které nejsou hrazeny zdravotní pojišťovnou. Pracuje se systémem balíčků — pojmenovaných skupin položek (sortimentu, prohlídek a očkování), které lze přiřadit pacientovi a vyúčtovat.
2. **Pracovnělékařské služby (PLS)** — evidence a fakturace pracovnělékařských prohlídek a služeb pro zaměstnavatele na základě smluvního vztahu. Zahrnuje správu smluv s firmami, skupin zaměstnanců, objednávek prohlídek a vystavování faktur.

*📋 Legislativní rámec: Povinnost zajistit pracovnělékařské prohlídky pro zaměstnance vyplývá ze zákona č. 373/2011 Sb. o specifických zdravotních službách a z prováděcí vyhlášky č. 79/2013 Sb. Zaměstnavatel je povinen hradit náklady na pracovnělékařské prohlídky.*

Modul podporuje:

- Definici balíčků nadstandardní péče s libovolným počtem položek.
- Přiřazení sortimentu (zboží, materiál, administrativa), prohlídek a očkování do balíčků.
- Správu ceníku s platností od/do, sazbou DPH a vazbou na pracoviště.
- Evidenci závazků pacientů (platba hotově nebo fakturou).
- Nastavení slev a hromadného výdeje na úrovni jednotlivých položek.
- Vedení smluv PLS se zaměstnavateli (způsoby platby: paušál, výkony, kombinovaně).
- Správu skupin (pozic) PLS a přiřazení zaměstnanců k prohlídkovým povinnostem.
- Evidenci akcí PLS (konkrétních prohlídek) s workflow stavů od plánování po fakturaci.
- Vystavování faktur PLS firmám za realizované prohlídky a služby.

### 1.2 Komu je modul určen

| **Role** | **Oprávnění v modulu** |
| --- | --- |
| Zdravotnický personál (sestra, lékař) | Prohlížení balíčků, přiřazení balíčku pacientovi, evidování platby, uzavírání a předávání akcí PLS k fakturaci |
| Koordinátor PLS / recepce | Správa objednávek PLS, komunikace se zaměstnavateli |
| Správce ordinace | Vytváření a úprava balíčků, správa sortimentu a ceníku, zakládání smluv PLS a skupin PLS, import dat PLS |
| Správce systému | Veškerá nastavení, konfigurace kategorií ceníku, import dat PLS, správa uživatelů |

*Pro zdravotníky: Části dokumentu označené symbolem 🔧 jsou určeny správcům systému a nemusí být pro každodenní práci relevantní.*

### 1.3 Předpoklady použití

1. Přihlášení do aplikace Galen — platné uživatelské jméno a heslo.
2. Oprávnění k modulu — přístup musí být povolen správcem systému v nastavení rolí uživatelů.
3. Nastavená společnost — každý balíček a sortiment je vázán na konkrétní společnost (ordinaci).
4. 🔧 Definovaný sortiment — před vytvořením balíčků musí být v systému evidovány položky sortimentu.
5. 🔧 Nastavené kategorie ceníku — pro přiřazení cen k položkám jsou potřeba kategorie ceníku.

Další předpoklady pro část Pracovnělékařské služby (PLS):

6. 🔧 Evidovaná firma (zaměstnavatel) — smlouva PLS se vždy váže na konkrétní firmu a její pobočku. Firma musí být v systému předem založena.
7. 🔧 Definované skupiny PLS — pracovní skupiny/pozice zaměstnanců u firmy, ke kterým se přiřazují příslušné typy prohlídek ze smlouvy.
8. 🔧 Sortiment typu Prohlídka — pro PLS akce je vyžadován sortiment s typem „Prohlídka" (P) přiřazený jako položka smlouvy.

🔧 Hromadný import PLS dat: Při prvním nasazení PLS nebo při přechodu od jiného systému je možné hromadně importovat zaměstnance, skupiny pozic a smlouvy pomocí csv souborů.

---

## 2. První kroky

### 2.1 Spuštění modulu Nadstandardní péče

![obrazek-20260526-063802.png](<../../../pages/FONS GALEN/Nadstandardní péče (Balíčky + PLS)/Orientace v modulu/assets/obrazek-20260526-063802.png>)
1. V nabídce vyhledejte a klikněte na dlaždici Nadstandardní péče.
2. Otevře se hlavní okno modulu.

### 2.2 Orientace v hlavním okně

![obrazek-20260601-071153.png](<../../../pages/FONS GALEN/Nadstandardní péče (Balíčky + PLS)/Orientace v modulu/assets/obrazek-20260601-071153.png>)

| **Oblast** | **Popis** |
| --- | --- |
| Firmy | Obecná evidence firem ve FONS Galen. Příznak PLS označuje firmu jako odběratele péče pro zaměstnance. K firmě se váže smlouva PLS, pobočky, kontaktní osoby a faktury. |
| Ceníky | Definice cen pro jednotlivé typy služeb (sortiment) s vazbou na pracoviště. Podporují časovou platnost (platnost od/do) a sazbu DPH. Smluvní ceny pro konkrétní firmu se nastavují v položkách smlouvy PLS. |
| Balíčky | Číselník balíčků, do kterých se sdružují položky sortimentu (typy služeb). Balíček slouží jako logická skupina sortimentu pro přehledné nabízení a objednávání péče. |
| Kategorie | Kategorie pro třídění položek sortimentu (typů služeb). Slouží k přehledné organizaci nabídky a filtrování v seznamech. |
| PLS Admin | Přehled provedených prohlídek a očkování s možností rozšířeného filtrování. |
| PLS Admin služby | Přehled provedených služeb s možností rozšířeného filtrování. |
| PLS Faktury | Evidence a generování faktur za nadstandardní péči. Propojení s firmami, balíčky a odčerpaným plněním. |
| Rizika | Přiřazení rizikových faktorů (DruhRizika) ke skupinám zaměstnanců (Skupina PLS / PozicePLS). Definuje, s jakými pracovními riziky daná skupina pracuje, a ovlivňuje výběr sortimentu při vytváření smluv. |
| Import | Hromadný import skupin zaměstnanců, smluv a pacientů do modulu PLS — načítání ze vstupního souboru (CSV) s validací dat, mapováním na existující firmu/pobočku a protokolem o výsledku. |
| Služby | Přehled a zadávání provedené PLS služby správcem. |

---
