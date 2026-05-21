---
title: "Novinky ve verzi k 19. 5. 2026"
version: 2
updated_at: 2026-05-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/406781968
---

# Novinky ve verzi k 19. 5. 2026

# Novinky a vylepšení

---

## Upozornění / Dekurz

### Uložení přílohy z Upozornění do Dekursu pro všechny uživatele

Přílohu z modulu Upozornění nyní může uložit přímo do Dekursu pacienta každý přihlášený uživatel — nejen autor nebo správce upozornění.

## ePoukaz

### Načítání kontaktů při výchozí hodnotě „Bez notifikace“

Při otevření formuláře ePoukazu jsou vždy načteny kontaktní údaje pacienta označené příznakem SÚKL — i pokud má pracoviště nastavenou výchozí hodnotu „Bez notifikace“. Uživatel může notifikaci zvolit ručně z nabídky dostupných typů kontaktů.

### Automatické zjišťování stavu výdejů

Na pracovišti, které má aktivní ePoukaz a odesílá eRecepty, probíhá zjišťování stavu výdejů léků nyní automaticky — bez nutnosti ručního nastavování v konfiguraci.

## Karta pacienta

### Vysvětlivka u pole Zákaz nahlížení v anamnéze

K poli **Zákaz nahlížení** v anamnéze pacienta přibyl popisný tooltip, který uživatelům objasní, co toto nastavení ovlivňuje.

## Konfigurace

### Vyhledávání v konfiguraci Galenu

V okně konfigurace Galenu přibyla možnost vyhledat konkrétní nastavení zadáním textu do vyhledávacího pole.

## Vyúčtování

### Upozornění u dokladu s výkony s navázaným ZUM

Při změně stavu dokladu tlačítkem „Nově vyúčtovat“ je nyní zobrazeno upozornění v případě, že doklad obsahuje výkony, na které je navázán ZUM proto, aby stejná operace použita i pro doklad ZUM.

# Opravy chyb

---

## Refresh stavu nahrání přílohy na cloud

Po uložení přílohy přes přístroj se ikona stavu nahrávání nyní správně aktualizuje okamžitě po dokončení uploadu — bez nutnosti znovu načíst pacienta.

## Seznam NSP – selhání při hromadném přepočtu

V modulu Nástroje → Seznam NSP selhávala funkce **Přepočíst vše** s chybou „An item with the same key already exists“. Chyba byla odstraněna.

## eDPN – převzetí DPN u pacientů cizinců

Opravena chyba, která znemožňovala převzít dočasnou pracovní neschopnost od jiného zdravotnického zařízení u pacientů cizinců identifikovaných datem narození místo evidenního čísla pojištěnce.

## Pozvánka do Portálu pacienta – chyba „Read not allowed“

Opravena chyba, kvůli které se při odeslání pozvánky do Portálu pacienta zobrazovala zpráva o zamítnutém přístupu k verifikacínmu kódu a blokovala přístup ke kartě pacienta.

## Vyúčtování – pojištěnci s kódem pojištění 1A

Opravena chyba, při níž u pojištěnců cizinců s kódem 1A (žadatelé o mezinárodní azyl) po použití tlačítka Přepočíst nevyúčtované výkony odcházely kapitované výkony s nenulovou hodnotou.

## Recepce – nelze otevřít pacienta přes objednávání

Opravena chyba, při níž z modulu Recepce nebylo po aktualizaci možné otevřít kartu pacienta přes objednávání — systém hlásil chybu přístupu k dokladu pacienta.

## PLS posudky – přenos čísla OP po přesunu pole

Po přesunu pole Občanský průkaz do záložky kontaktů přestalo číslo dokladu přecházet do PLS posudku. Přidána zpětná kompatibilita zajišťující správný přenos bez nutnosti úpravy existujících formulářů.

## Nelze otevřít dekurz u pacienta

Opravena databázová chyba, ke které docházelo u pacientů s příliš dlouhou poznámkou k objednávce — výsledkem bylo, že u takového pacienta nešlo otevřít dekurz.
