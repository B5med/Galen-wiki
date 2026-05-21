---
title: "Zástupy"
version: 1
updated_at: 2025-09-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/120029189
---

# Zástupy

Modul zástupy umožňuje v případě nepřítomnosti lékaře (např. z důvodu dovolené, nemoci atd.) určit a umožnit  jinému (zastupujícímu) lékaři pracovat v ordinaci nepřítomného lékaře. Zastupující lékař musí být uveden v seznamu uživatelů (správa seznamu uživatelů viz Modul Správce), ze kterého administrátor přidělí lékaře k požadovanému pracovišti a přidělí mu roli Zastupující lékař.

## Určení zastupujícího lékaře

Správce - > Správa organizace –> záložka Struktura -> rozbalit strukturu (vlevo nahoře)-> u daného pracoviště označíme vybraného uživatele -> zaškrtneme checkbox Zastupující lékař.

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/Zástupy/assets/image-20250917-075439.png]]
Aby uživatel viděl při přihlašování do IS Galen i pracoviště, kde je určený jako Zastupující lékař, musí být v okně výběru pracovišť zaškrtnut checkbox Včetně zastupovaných. V takovém případě uvidí po přihlášení do IS Galen v zobrazení výběru pracovišť pracoviště určené k zástupu v bledším modrém zbarvení s označením v levém horním rohu slovem (zástup).

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/Zástupy/assets/image-20250917-075449.png]]
Po přihlášení na pracoviště zástupu je uživatel vyzván k doplnění důvodu zástupu s možností upřesnění.

Důvod zástupu se nastavuje v modulu:

Správce -> Správa organizace –> Agendy –> Zástupy

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/Zástupy/assets/image-20250917-075501.png]]
Po stisknutí tlačítka ![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/Zástupy/assets/image-20250917-075516.png]]
 je možné zadat důvod zástupu, stisknutím ![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/Zástupy/assets/image-20250917-075539.png]]

ho lze upravit, případně ho odstranit stisknutím tlačítka ![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/Zástupy/assets/image-20250917-075553.png]]
 .

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/Zástupy/assets/image-20250917-075611.png]]
Poté se lze přihlásit do ordinace jako zastupující lékař.

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Agendy/Zástupy/assets/image-20250917-075628.png]]

## Práce zastupujícího lékaře s laboratorními výsledky

- Zastupující lékař může v období svého zástupu **nahlížet a komentovat laboratorní výsledky** stejně jako stálý lékař.
- **Komentáře zastupujícího lékaře se zaznamenávají do auditní stopy**, je tedy možné dohledat, kdo a kdy komentář vložil.
- **Odpovědnost za laboratorní výsledek však zůstává na stálém lékaři pracoviště.**

   - Pokud zastupující lékař výsledek okomentuje, systém **nevytváří vazbu** na tohoto lékaře.
   - Po ukončení zástupu tak může výsledek dále upravovat stálý lékař.
