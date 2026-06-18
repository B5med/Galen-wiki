---
title: "Lékové interakce"
version: 1
updated_at: 2026-06-18
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/462913537
---

# Lékové interakce

## Co je modul Lékové interakce

Modul Lékové interakce je nadstavbová funkce systému FONS Galen, která lékaři v reálném čase zobrazuje informace o potenciálně problematických kombinacích léků předepsaných pacientovi. Systém automaticky sleduje aktuálně rozepsané recepty a upozorňuje na dvojice léků, které mohou navzájem ovlivnit svůj účinek, zvýšit riziko nežádoucích účinků nebo být jinak klinicky relevantní.

Modul je dostupný pouze uživatelům, kterým byl přístup aktivován správcem systému (viz kapitola 5).

## Princip fungování

### Kdy systém interakce kontroluje

Systém kontroluje lékové interakce automaticky vždy, když dojde ke změně v sestavě receptů aktuálního dne. Konkrétně:

- při přidání nového léku na recept,

- při odebrání léku z receptu,

- při každém otevření záložky Medikace s aktivním modulem interakcí.

### Jaké léky systém zahrnuje do kontroly

Do kontroly jsou zahrnuty tyto skupiny léků:

- Léky na receptech aktuálního dne – primární sada.

- Léky předepsané v posledních 30 dnech – zahrnují se jako doplňkový kontext (starší záznamy).

- Trvalé medikace pacienta – léky zadané v záložce Trvalé, které jsou v danou dobu platné.

Magistraliter přípravky (individuálně namíchané léky) nejsou do kontroly interakcí zahrnuty, neboť nemají kód z číselníku léčivých přípravků.

## Zobrazení varování uživateli

### Kde se varování zobrazuje

Přehled lékových interakcí se zobrazuje přímo v záložce Medikace v dolní části obrazovky, vedle sestavy receptů aktuálního dne. Panel je viditelný po celou dobu práce s recepty – lékař tak má přehled o interakcích přímo před sebou, aniž by musel otevírat další okno.

### Charakter varování

Varování má informativní charakter – lékař může recept uložit a odeslat i v případě, že systém detekuje interakci. Zobrazení interakce slouží jako podpora rozhodování, nikoliv jako tvrdý blok předpisu.

> [!info]
> Systém lékaře informuje, konečné rozhodnutí o předpisu léku je vždy na lékaři samotném.

### Typy zobrazovaných interakcí

Systém rozlišuje typy interakcí dle tříd závažnosti. U každé detekované kombinace lze zobrazit detail obsahující:

- názvy obou léků (resp. jejich ATC kódy),

- popis mechanismu interakce,

- doporučené klinické opatření.

Zvláštním případem je upozornění na shodnou ATC skupinu – pokud dva léky na receptu patří do stejné ATC skupiny, systém na tuto duplicitu upozorní.

### Chybový stav panelu

Pokud se nepodaří načíst data z externího serveru interakcí (např. výpadek připojení), panel zobrazí chybový stav s možností zopakovat načítání pomocí tlačítka Opakovat. Práce s recepty v takovém případě pokračuje normálně bez omezení.

## Napojení na předpis léku a chorobopis

### Kde v systému se interakce zobrazují

Lékové interakce jsou součástí záložky Medikace, která je přístupná z dekurzu pacienta. Interakce se vztahují vždy ke konkrétnímu pacientovi a aktuálně otevřenému záznamu – systém zobrazuje interakce pro léky tohoto pacienta.

### Vazba na aktuální recept

Panel interakcí se automaticky aktualizuje při každé změně receptů aktuálního dne – přidání nebo odebrání léku spustí nový dotaz na server interakcí. Lékař tak vidí aktuální stav bez nutnosti ručního obnovování.

### Trvalé medikace v kontextu interakcí

Trvalé medikace pacienta (léky zadané v záložce Trvalé, platné k aktuálnímu datu) jsou automaticky zahrnuty do kontroly interakcí. To umožňuje detekovat potenciální rizika i při předpisu nového léku, který by mohl interagovat s dlouhodobou medikací pacienta.

## Nastavení a konfigurace

### Aktivace modulu pro uživatele

Modul Lékové interakce musí být pro každého uživatele samostatně aktivován. Provádí to správce systému (administrátor) v nastavení uživatelů. Pokud příznak není aktivní, panel interakcí se v záložce Medikace nezobrazí.

### Omezení počtu aktivních uživatelů

Přístup k lékovým interakcím je licencován – každá ordinace má sjednán maximální počet uživatelů, kteří mohou mít modul aktivní současně. Při pokusu o aktivaci dalšího uživatele nad tento limit systém zobrazí chybové hlášení.

V takovém případě kontaktujte svého obchodního zástupce STAPRO pro rozšíření licence.

### Deaktivace při zneaktivnění uživatele

Pokud je uživatelský účet v systému deaktivován, přístup k lékovým interakcím se automaticky odebere.

### Konfigurace přihlašovacích údajů k serveru interakcí

Připojení k externímu serveru lékových interakcí (URL, přihlašovací jméno a heslo) konfiguruje správce systému nebo technik STAPRO v konfiguraci aplikačního serveru Galen. Toto nastavení je společné pro celou instalaci, uživatelé je nenastavují.

## Časté dotazy

| **Otázka** | **Odpověď** |
| --- | --- |
| Panel interakcí se mi nezobrazuje, přestože mám otevřenou záložku Medikace. | Pravděpodobně nemáte aktivován přístup k lékovým interakcím. Obraťte se uživatele ve vaší společnosti, který má ve FONS Galen přiřazenou roli *Správce*. |
| Proč systém hlásí interakci, ale přesto mohu recept uložit? | Varování je informativní. Konečné rozhodnutí je vždy na lékaři – systém Vás upozorňuje, neblokuje. |
| Zahrnuje kontrola i léky, které pacient bere dlouhodobě? | Ano – trvalé medikace pacienta jsou do kontroly automaticky zahrnuty. |
| Mohu se spolehnout, že databáze interakcí je aktuální? | Data jsou poskytována externím dodavatelem a průběžně aktualizována. FONS Galen vždy stahuje aktuální verzi. |
| Jak rozšíříme licenci na více uživatelů? | Uživatel s rolí *Objednavatel* provede objednávku dalších přístupů v modulu eShop. |
