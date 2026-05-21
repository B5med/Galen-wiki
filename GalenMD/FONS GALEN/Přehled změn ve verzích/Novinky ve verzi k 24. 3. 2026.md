---
title: "Novinky ve verzi k 24. 3. 2026"
version: 1
updated_at: 2026-03-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/316211203
---

# Novinky ve verzi k 24. 3. 2026

# Novinky a vylepšení

#### **Konfigurace Info panelu pacienta přímo v Nástrojích**

Nově můžete upravovat nastavení Info panelu pacienta přímo v modulu Nástroje vašeho pracoviště – bez nutnosti kontaktovat administrátora.

*Kde najdete nastavení*

Přejděte do: Pracoviště → Nástroje → Šablony → Zobrazení

V nové záložce Zobrazení najdete položku Info panel pacienta. Kliknutím na ikonu tužky otevřete její konfiguraci.

*Jak to funguje*

Nastavení je sdílené pro celé pracoviště – jakákoli změna, kterou provedete, se okamžitě projeví pro všechny uživatele. Zároveň platí, že konfigurace je vždy synchronizována se Správcem, takže změny provedené administrátorem se promítnou i do Nástrojů a naopak.

*Jak funkci zpřístupnit*

Záložka Zobrazení je ve výchozím stavu skrytá. Administrátor ji může povolit v: Správce → Správa organizace → Pracoviště → UI konfigurace → Info panel pacienta, kde zaškrtne volbu „Zobrazovat konfiguraci v modulu Nástroje pracoviště".

**PLS – Rozšíření práce s poskytovateli PLS**

Systém nově podporuje filtrování a zobrazení údajů o poskytovateli PLS napříč moduly. Cílem je zjednodušit vyhledávání podle smluvního poskytovatele a zpřehlednit vazby mezi smlouvou, prohlídkami, službami a fakturací.

*Modul Firmy*

Přidán nový filtr **Poskytovatel PLS**, který zobrazí pouze firmy s platnou smlouvou PLS u vybraného poskytovatele (platnost smlouvy zahrnuje dnešní datum nebo datum do není uvedeno).

*Modul PLS Admin*

Přidán filtr **Poskytovatel PLS** zobrazující prohlídky navázané na firmy s evidovanou smlouvou PLS u vybraného poskytovatele – zahrnuje i neplatné smlouvy pro zachování kompletní historie. Filtr funguje obousměrně (reversní filtr): výběrem poskytovatele se zobrazí firmy a jejich prohlídky, výběrem firmy se zobrazí její poskytovatel PLS. Přidán nový sloupec **Poskytovatel PLS**.

*Modul PLS Admin Služby*

Analogicky k PLS Admin – přidán filtr **Poskytovatel PLS** (evidované smlouvy včetně neplatných), reversní filtr a nový sloupec **Poskytovatel PLS**.

*Modul PLS Faktury*

Přidán nový sloupec **Poskytovatel PLS** (umístění: mezi sloupci „Popis" a „Podřízená společnost"). Doplněn filtr **Poskytovatel PLS** s možností zaškrtnutí **„Vyloučit poskytovatele"** – při zaškrtnutí zobrazí všechny položky kromě těch navázaných na vybraného poskytovatele. Filtr lze kombinovat s ostatními filtry modulu (logika AND).

**Nová metoda externího přístupu**

Do socket JSON rozhraní (externí přístup) byla přidána nová metoda `OpenPacientOrdinace`. Umožňuje jedním klikem v externí aplikaci otevřít v FONS Galenu kartu pacienta přímo z ordinace, na které je uživatel aktuálně přihlášen – bez nutnosti pacienta ručně dohledávat.
