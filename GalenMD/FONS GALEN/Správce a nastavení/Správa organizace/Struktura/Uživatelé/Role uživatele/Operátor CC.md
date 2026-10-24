---
title: "Operátor CC"
version: 2
updated_at: 2026-10-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/657326095
---

# Operátor CC

Role je určená pro operátory call centra (CC), kteří objednávají pacienty do kalendářů zdravotnického zařízení. Jedná se o **placenou funkcionalitu**, kterou je možné objednat v **eShopu**.

Uživatel s touto rolí:

- má přístup **pouze do modulu Objednávání**,
- může objednávat jen do kalendářů a bloků ordinačních hodin, které jsou pro call centrum výslovně povolené (viz níže).

### Jak nastavit kalendář pro call centrum

Nastavení lze provést pro celý kalendář, nebo jen pro vybrané bloky ordinačních hodin.

| Kde | Příznak | Co operátor CC uvidí |
| --- | --- | --- |
| **Nastavení kalendáře** → záložka *Obecné* | **Kalendář CC** | Celý kalendář, tedy všechny bloky ordinačních hodin a všechny typy objednávek povolené v kalendáři. |
| **Blok ordinačních hodin** → záložka *Obecné* | **Blok CC** | Jen tento blok ordinačních hodin. Bloky CC jsou v kalendáři zvýrazněné šrafováním. |

V bloku ordinačních hodin s příznakem **Blok CC** lze v seznamu *Povolené typy objednávek* u každého typu zaškrtnout **Povolit objednávky CC**. Operátor CC pak může v tomto bloku použít jen typy objednávek s touto volbou.

> [!info]
> Pokud má kalendář zaškrtnutý **Kalendář CC**, v blocích ordinačních hodin se příznak **Blok CC** ani volba **Povolit objednávky CC** nezobrazují. Pro call centrum je v takovém případě otevřený celý kalendář.

### Jak roli přidělit

1. Otevřete *Správce → Správa organizace → záložka Uživatelé* a vyberte uživatele.
2. V sekci **Role uživatele** zaškrtněte **Operátor CC**.
3. V sekci modulů zůstane nabídnutý a automaticky zaškrtnutý jen modul **Objednávání**.
4. Uložte.

> [!info]
> Roli **Operátor CC** nelze kombinovat s žádnou jinou rolí. Pokud má uživatel zaškrtnutou jinou roli, je checkbox Operátor CC zašedlý. Po zaškrtnutí role Operátor CC se naopak zašednou všechny ostatní role.

> [!tip]
> Pokud není nastavený **Kalendář CC** ani **Blok CC**, operátor CC nemá kam pacienty objednat.
