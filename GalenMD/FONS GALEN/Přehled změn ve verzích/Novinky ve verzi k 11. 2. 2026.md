---
title: "Novinky ve verzi k 11. 2. 2026"
version: 2
updated_at: 2026-02-09
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/264208385
---

## **Nastavení výchozích hodnot ePoukazu**

Do FONS Galen bylo implementováno několik výchozích možností ePoukazu:

A) Možnost nastavení na pracovišti, aby se ePoukaz ve výchozím stavu vystavoval bez notifikace pacientovi. Nastavení může provést uživatel s rolí sp*rávce* v modulu *Správa organizace - struktura organizace - pracovišti - UI konfigurace:*Popis nastavení je zde [[Záložka UI konfigurace]]

B) Možnost nastavení výchozích hodnot platnosti ePoukazu na pracovišti. Nastavení může provést uživatel s rolí sp*rávce* v modulu *Správa organizace - struktura organizace - pracovišti - UI konfigurace:*Popis nastavení je zde [[Záložka UI konfigurace]]

C) Výchozí vyplnění Úhrada 1 při předpisu pomůcky.

Pokud lékař předepisuje pomůcku, která je ze strany pojišťovny hrazení v rámci základní úhrady (UHR1) vyplní se tato úhrada automaticky při předpisu. Výše úhrady je možné ze strany uživatele dále editovat.

Pokud lékař vyplnil stupeň inkontinence, nastaví se následně výše úhrady předepisované pomůcky dle nastaveného stupně inkontinence (Stupeň 1=UHR1, Stupeň 2=UHR2, Stupeň 3=UHR3). Výše úhrady je možné ze strany uživatele dále editovat.

Při předpisu pomůcky se automaticky nastavuje počet 1, který je možný ze strany uživatele dále editovat.
