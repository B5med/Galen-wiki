---
title: "Novinky ve verzi k 21. 4. 2026"
version: 7
updated_at: 2026-04-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/359661570
---

# Novinky a vylepšení

---

### Pole pro řádkovou diagnózu ve zúčtovacích zprávách

V modulu **Vyúčtování** bylo doplněno pole **Řádková diagnóza** při zpracování měsíční zúčtovací zprávy. Pole je dostupné na záložce **ZUM** u konkrétního dokladu a také při akci **KNV**.

### PLS – výběr střediska z číselníku

V modulu PLS bylo pole pro zadání střediska přepracováno z volného textového pole na **výběr z číselníku**. Uživatelé nyní vybírají středisko ze standardizovaného seznamu předdefinovaných hodnot, čímž se eliminují překlepy a nekonzistentní záznamy a usnadňuje se filtrování a reporting podle střediska.

### Rozšíření API notifikací o IČP a provozovny

Bylo rozšířeno API pro správu notifikací (Vytvoř, Zobraz, Uprav). Pole **ICP** nově umožňuje zadání více hodnot — notifikace se zobrazí pro všechna zadaná IČP. Nově bylo přidáno pole **Provozovna**, do kterého lze uvést jedno nebo více ID provozoven; notifikace se zobrazí pro všechny uvedené provozovny.

## Vyúčtování

### Pravidlo pro zakázané kombinace výkonů s diagnózou

Bylo upraveno pravidlo pro zakázanou kombinaci výkonů **01204 + 09532**. Tato kombinace je přípustná v případě, že jsou výkony vykázány s **odlišnými diagnózami**. Pravidlo bylo rozšířeno tak, aby tuto situaci správně vyhodnotilo.

## Prohlídky a vyšetření

### Podmínka pohlaví v Designeru

Do Designeru prohlídek (sekce Prohlídky – Výkony) byla přidána nová podmínka **Pohlaví** (muž/žena). Správci nyní mohou u výkonů v šablonách nastavit, zda se výkon týká pouze mužů, pouze žen, nebo obou pohlaví.

# Opravy chyb

---

## Opravy příloh – nelze otevřít starší nebo cloudové přílohy

Po aktualizaci ze dne 31. 3. 2026 nebylo možné otevírat přílohy vložené před touto verzí. Chyba se projevila u více zákazníků. Přílohy uložené před nasazením i nově vložené přílohy jsou nyní opět plně přístupné.

## Oprava příloh se speciálními znaky v názvu

Přílohy nahrané s názvy obsahujícími speciální znaky (zejména otazník) nebylo možné otevřít ani stahovat prostřednictvím API. Systém nyní při uložení automaticky odstraňuje nebo nahrazuje problematické znaky a při přejmenování přílohy informuje uživatele o provedené změně.

## Dávka na zdravotní pojišťovnu obsahuje doklady z více let

Bylo opraveno sestavování dávek na zdravotní pojišťovnu, kdy systém zahrnoval do dávky doklady z více kalendářních roků, což zdravotní pojišťovny odmítají.

## ePoukazy zobrazovány v nesprávné odbornosti

Elektronické poukazy vystavené v jedné odbornosti se nesprávně zobrazovaly i v jiné odbornosti téhož pacienta. Chyba byla opravena a ePoukazy se nyní zobrazují jen v odbornosti, ve které byly vystaveny.

## eDPN: nelze odeslat změny

Při odeslání změn v elektronické neschopence docházelo k chybě způsobené duplicitním záznamem. Oprava také zajišťuje, že data přílohy nejsou odstraňována v případě, kdy se odeslání nepodařilo a uplynul rok od původního pokusu.

## Opakované upozornění k předchozí neschopence / ošetřovnému

Notifikace týkající se ošetřovného a dlouhodobého ošetřovného nebyly správně označovány jako zpracované, což způsobovalo opakované zobrazování upozornění i po jejich odsouhlasení. Tato chyba byla opravena.

## Výpadek Galenu při komunikaci s ISIN

Ve dnech 8. a 9. 4. 2026 docházelo k hromadnému výpadku způsobenému zpožděnými odpověďmi ze systému ISIN. Byl nastaven odpovídající timeout pro vyhledávání RID, čímž se předchází zamrzání aplikace při nedostupnosti externího systému.

## Neaktivní kurzor při zadávání kódu dvoufaktorového ověření

Po spuštění aplikace a zadání hesla se kurzor při dvoufaktorovém ověření automaticky nepřesouval do pole pro kód. Chyba byla opravena a fokus se nyní nastaví automaticky.

## Špatně vypočítané datum narození

Při ručním zadání data narození nesouladného s rodným číslem docházelo k nesprávnému zobrazení data. Systém nyní při uložení upozorní uživatele, pokud zadané datum není v souladu s rodným číslem.

## Chyba při aktualizaci číselníku NRZP

Při pokusu o aktualizaci číselníku NRZP v modulu ISIN docházelo k chybě způsobené neočekávanou hodnotou z ÚZIS. Chyba byla opravena a aktualizace číselníku nyní probíhá bez problémů.

## Info panel – nesprávná hodnota posledního měření

V info panelu pacienta se zobrazovala nesprávná hodnota posledního měření výšky. Opraveno tak, aby se měření aktualizovalo pouze tehdy, kdy k němu skutečně došlo.

## Dashboard – zobrazení dat z nepřístupného přehledu

Při přepnutí na přehled, ke kterému nemá uživatel přístup, se v dashboardu zobrazovala data z předchozího přehledu. Nyní se při přepnutí na nepřístupný přehled data správně nevykreslí.

## ÚZIS statistiky rehabilitace – chybné hodnoty

Ve statistikách ÚZIS rehabilitace byly generovány nesprávné hodnoty, zejména v kategorii fyzikální terapie. Chyba byla opravena a statistiky nyní odpovídají skutečně vykázaným výkonům.

## Připomínací SMS/e-mail – odesílání na více kontaktů

Připomínací zprávy k objednávkám byly odesílány na všechny kontakty pacienta, pokud měl uloženo více kontaktních údajů a alespoň jeden byl označen jako primární. Chyba byla opravena – zpráva se odesílá pouze na primární kontakt.
