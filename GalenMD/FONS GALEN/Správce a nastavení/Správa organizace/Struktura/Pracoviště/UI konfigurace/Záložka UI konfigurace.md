---
title: "Záložka UI konfigurace"
version: 3
updated_at: 2026-01-29
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/193363969
---

# Záložka UI konfigurace

Záložka UI konfigurace umožňuje definovat práci s kartou pacienta. Upravuje zobrazení, možnosti   tisku, editaci a další. Všechny volby v tomto okně se týkají pracoviště, tedy mohou se u jednotlivých IČP měnit.

V části *Skartační lhůta*uživatel nastaví výchozí skartační lhůty pro kurativu a PLS na daném pracovišti. Tyto lhůty může uživatel na pracovišti změnit, zde přednastavené lhůty slouží pouze jako výchozí.

## Upozorňovací okno

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/UI konfigurace/Záložka UI konfigurace/assets/image-20251210-150755.png]]

## Povinné údaje

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/UI konfigurace/Záložka UI konfigurace/assets/image-20251210-150829.png]]

## Laboratorní výsledky

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/UI konfigurace/Záložka UI konfigurace/assets/image-20251210-150859.png]]

## Dialog měření

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/UI konfigurace/Záložka UI konfigurace/assets/image-20251210-150946.png]]
Ve výchozím nastavení jsou všechna pole pro zadání měření v dekurzu viditelná. V závislosti na odbornosti pracoviště však nejsou pro všechna pracoviště neužitelná, a proto je zde možné vybraná pole měření skrýt.

Měření, která uživatel v tomto okně vybere, budou skryta. V konkrétním případě níže tak budou skryta všechna pole určená pro pediatra.

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/UI konfigurace/Záložka UI konfigurace/assets/image-20251210-151217.png]]
> [!abstract]
> Nově mají praktičtí lékaři pro dospělé sledovat mj. obvod pasu pacienta. Proto je nutné, aby si  pracoviště s odborností 001 skryla všechna měření v sekci pediatr kromě obvodu pasu.

## ePoukaz

![[pages/FONS GALEN/Správce a nastavení/Správa organizace/Struktura/Pracoviště/UI konfigurace/Záložka UI konfigurace/assets/image-20260126-134335.png]]
**(1)** Zjišťování stavu ePoukazu aktualizuje stav ePoukazu poté, co jiné pracoviště (pojišťovna, výdejna) změní jeho stav. Tato služba aktualizuje stavy přes noc. To znamená, že pokud bude pomůcka na ePoukazu vydána 22. 1., tak se tento stav ve FONS Galen zobrazí až 23. 1.

**(2)**Na ePoukazu nebude při jeho předpisu zvolena notifikace pacientovi i přesto, že má pacient kontakt označen příznakem pro notifikace SÚKL. Uživatel bude mít možnost kontakt vyplnit ručně.

**(3)**V těchto dvou řádcích je možné nastavit výchozí platnost pro ePoukazy v případě předpisu pomůcky bez schválení pojišťovnou a v případě pomůcky schvalované pojišťovnou. Pokud zde není vyplněna žádná hodnota, bude ePoukaz vystaven s platností 30 dní. Přednastavenou platnost může uživatel ručně upravit při předpisu konkrétního ePoukazu.
