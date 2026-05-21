---
title: "Novinky ve verzi k 8. 4. 2026"
version: 8
updated_at: 2026-04-07
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/336199681
---

# Novinky ve verzi k 8. 4. 2026

# Novinky a vylepšení

---

## Modul Nadstandardní péče

### Rozšíření práce s Poskytovateli PLS

V modulu Nadstandardní péče (**Firmy**, **PLS Admin**, **PLS Admin Služby** a **PLS Faktury**) byl přidán nový filtr **Poskytovatel PLS**, který umožňuje zobrazovat a vyhledávat záznamy podle smluvního poskytovatele pracovnělékařských služeb.

*Firmy*

Po výběru poskytovatele se zobrazí pouze firmy s platnou smlouvou PLS u daného poskytovatele (platnost smlouvy zahrnuje dnešní datum nebo datum do není uvedeno).

*PLS Admin a PLS Admin Služby*

Filtr zobrazí prohlídky a služby navázané na firmy s evidovanou smlouvou (včetně neplatných, pro zachování historie). Přibyl také **reversní filtr**: výběrem firmy se automaticky zobrazí její poskytovatel PLS a naopak. Přidán nový sloupec **Poskytovatel PLS**.

*PLS Faktury*

Nový sloupec **Poskytovatel PLS** (umístění: mezi sloupci Popis a Podřízená společnost) a filtr s možností poskytovatele naopak **vyloučit** (checkbox Vyloučit poskytovatele).

# Opravy chyb

---

## Oprava zobrazení autora v auditní stopě

Byla opravena chyba, kdy se v auditní stopě lékařské zprávy a formuláře zobrazovalo nesprávné jméno autora. Auditní stopa nyní správně uvádí, kdo záznam **vytvořil**, **upravil** nebo **smazal**, včetně správného data a času každé události.

## Oprava vkládání obrázků v Designeru

V nástroji Designer byla opravena chyba, která znemožňovala vložit obrázek do formuláře využívajícího rozložení s bloky.

## Opravy kapitačního modulu

Byly odstraněny dvě chyby v oblasti kapitací:

- Opraven chybný nápoček kapitací DP4 u pojišťovny VZP.
- Opraveno chybné zařazování kapitovaných výkonů do KDAVKA.

## Oprava úpravy ePoukazu

Byla odstraněna chyba, která znemožňovala editaci již vystaveného ePoukazu.

## Oprava funkce Přepočíst vše

Odstraněna chyba, která způsobovala selhání při použití funkce pro hromadný přepočet.

## Oprava naskladňování vakcín pomocí čtečky

Odstraněna chyba při naskladňování vakcín prostřednictvím čtečky čárových kódů.

## Oprava nesprávné hodnoty v info panelu měření

Opravena chyba, kdy se v info panelu pacienta zobrazovala nesprávná hodnota posledního měření. Údaj se nově aktualizuje pouze tehdy, kdy k měření skutečně došlo.

## Oprava zobrazení stavu eReceptu po odeslání

Po odeslání receptu se nyní správně zobrazuje označení eRecept, díky kterému lékař okamžitě vidí, že recept byl úspěšně odeslán elektronicky.

## Oprava zamrznutí aplikace při práci s kalendářem

Opravena chyba, při které Galen zamrzl během operací s kalendářem. Příčinou bylo zpracování všech dnů od nejstaršího záznamu, bez ohledu na to, zda v daný den existuje nějaký záznam. Nově se zpracují pouze dny, které skutečně obsahují záznamy.
