---
title: "Uživatelská hlavička a příznak na bankovním spojení"
version: 7
updated_at: 2026-08-26
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/109051919
---

# Uživatelská hlavička a příznak na bankovním spojení

> [!info]
> Tato funkce umožňuje:
>
> - přiřadit **příznak** ke konkrétnímu bankovnímu spojení (např. pro fakturaci pacientů nebo PLS),
> - a upravovat **záhlaví tisku** (např. hlavičku faktury).

## 💳 Příznak na bankovním spojení

> **Cesta:**
> **Správce → Správa organizace → Stromová struktura → úroveň Společnost → dvojklik na vybrané bankovní spojení**

Každému bankovnímu spojení lze přiřadit příznaky:

| **Příznak** | **Použití** | **Poznámka** |
| --- | --- | --- |
| **Faktura pro pacienta** | Zobrazuje se při vytváření faktury v ordinaci (okno *Stav účtu*) | Lze označit více spojení |
| **Faktura PLS** | Používá se v modulu *Design* a při generování záhlaví tisku v *Nástrojích* | Lze použít pouze **jedno** bankovní spojení |

![image-20250901-083939.png](<../../../pages/FONS GALEN/Finance a účetnictví/Uživatelská hlavička a příznak na bankovním spojení/assets/image-20250901-083939.png>)

## 🏦 **Výběr bankovního spojení při vystavení faktury**

> **Cesta:**
> **Ordinace → Stav účtu → Faktura - výběr/ Faktura - vše**

Při způsobu úhrady bankovním převodem se ve výběru čísla účtu zobrazuje jeho číslo a název, který si uživatel sám zadává u bankovních spojení (v políčku Banka). Pro zjednodušení výběru se pole s bankovním účtem automaticky předvyplní podle následujícího rozhodovacího pravidla (v tomto pořadí priority):

1. účet naposledy použitý **přihlášeným uživatelem**na daném pracovišti,
2. pokud takový není, účet naposledy použitý **kýmkoli jiným** na daném pracovišti,
3. pokud dosud nebyla na pracovišti provedena žádná volba, předvyplní se **první aktivní bankovní účet** společnosti ze seznamu bankovních spojení.

Výběr účtu zůstává i nadále zcela volný – v číselníku jsou k dispozici všechny aktivní účty společnosti jako dosud, předvyplněná hodnota slouží pouze jako usnadnění a uživatel si může kdykoli vybrat jiné bankovní spojení.

---

## 🖊️ **Editace záhlaví tisku**

> **Cesta:**
> **Správce → Nástroje → Šablony → Záhlaví tisku**

Zde lze upravovat nebo vytvářet hlavičky pro tisk dokumentů (např. PLS faktury, pacientské faktury apod.).

---

### 🔹 Postup vytvoření nové hlavičky

1. Klikněte na **zelenou ikonu „+“**
   → vytvoří se nová, prázdná šablona záhlaví tisku.
2. (Volitelně) klikněte na **modré tlačítko „Převzít výchozí“**
   → doplní nejčastěji používané položky (např. název organizace, IČO, adresa).
3. Vyplňte **typ záhlaví**
   → určuje, při jakém tisku se dané záhlaví použije (např. *Faktura PLS*).
4. Doplňte **název záhlaví** (např. *PLS – Faktura*).
5. Vyplňte **obsah záhlaví**

   - Použijte systém **drag-and-drop**:
      z pravého panelu přetáhněte požadované proměnné do dokumentu.
   - Před nebo za proměnnou lze doplnit vlastní text.

   **Příklad:**
   „Toto je IČO naší společnosti: “ **[@S.ICO]**
6. **Formátování textu:**
   Pomocí modrých ikon nad dokumentem můžete měnit zarovnání, velikost písma, přidávat obrázky apod.
7. **Zaškrtněte příznak „Implicitní“**
   → pokud existuje více šablon pro stejný typ, systém použije tu s tímto příznakem.
8. **Uložení změn:**
   Úpravy se ukládají automaticky po opuštění obrazovky.

![image-20250901-084507.png](<../../../pages/FONS GALEN/Finance a účetnictví/Uživatelská hlavička a příznak na bankovním spojení/assets/image-20250901-084507.png>)
