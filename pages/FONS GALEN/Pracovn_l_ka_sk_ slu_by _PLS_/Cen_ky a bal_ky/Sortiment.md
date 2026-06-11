---
id: 57507841
title: "Sortiment"
version: 1
updated_at: 2025-06-26T13:35:33.443Z
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/57507841
---

# Sortiment

**Sortiment – jednotlivá pole**

**Aktivní** – může získat tři stavy

1. **Aktivní** – ve stávajícím stavu funkční dle logiky funkcionality

2. **Neaktivní** – nezobrazuje při vytváření položek smlouvy ani v nabídce sortimentu v     okně Stav účtu (modul Ordinace)

3. **Neexistuje** – logika chování identická jako stav Neaktivní (pouze informativní rozdělení)

**Kód** (povinné pole u všech skupin)

**Název** (povinné pole u všech skupin)

**Doplněk** (uživatel zde může doplnit vlastní popis položky)

**Pořadí** – tento údaj určuje pořadí zobrazení položek sortimentu při tisku a exportu PLS faktur (PLS vyúčtování)

**Variabilní cena** – při zatrženém checkboxu, lze v okně Stav účtu (modul Ordinace) editovat cenu této položky

**Ceník** – cena se zobrazuje pouze při výběru sortimentu v okně Stav účtu, až na výjimku: V případě firmy, která nemá příznak PLS a nemá vytvořenou žádnou smlouvu, je tato cena přenesena při vytváření PLS prohlídky v modulu Ordinace (cena se musí vztahovat na PLS prohlídku). Pokud není zadaná ani odbornost ani pracoviště, zobrazuje se všem takovým firmám, jinak se zobrazení filtruje podle těchto dvou parametrů

**Sazba DPH** – při vytváření nové sazby, musí mít hodnoty - 0 %, 10 %, 15 %, 21 %

**Cena/ Cena vč. DPH** – při zadání jedné, je druhá dopočítávána

**Platnost od – do** – kdy je aktuální cena platná

**Odbornost** – pro jakou odbornost cena platí. Je-li zadána, nesmí být zadáno pracoviště. Pracoviště – (pro jaké pracoviště cena platí). Je-li zadáno, nesmí být zadána odbornost
