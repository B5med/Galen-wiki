---
title: "Nákladová střediska"
version: 2
updated_at: 2025-07-21
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/75268151
---

Pokud je na společnosti aktivní nadstandardní modul „Nákladová střediska“, je možné na jednotlivých firmách nákladová střediska definovat a ty následně přednastavovat ve formuláři žádanky.

## **Přiřazení nákladového střediska na firmě**

Uživatel s rolí Správce v modulu Nadstandardní péče -> detail konkrétní firmy -> záložka Nákladová střediska přiřazuje k firmě nákladová střediska.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Nákladová střediska/assets/image-20250701-082241.png]]
Nákladová střediska jsou třech typů:

1. PLS – indikuje vyšetření v rámci PLS

1. Vstupní prohlídka – indikuje vstupní prohlídku

1. Spalničky – indikuje, že v žádance je požadováno pouze vyšetření spalniček

Ke každé firmě je možné přiřadit více nákladových středisek stejného typu, ale pouze jedno z nich je možné označit příznakem „Primární“.

V detailu firmy uživatel zároveň definuje počet dní před nástupem a po nástupu do zaměstnání, kdy se ještě vystavuje vstupní prohlídka.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Nákladová střediska/assets/image-20250701-082308.png]]

## **Přiřazení alternativního nákladového střediska**

Nákladové středisko se v žádance vyplňuje podle pravidel uvedených v následující kapitole. Uživatel má však možnost přednastavit jiné nákladové středisko v kartě zaměstnání pacienta.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Nákladová střediska/assets/image-20250701-082335.png]]

## **Vyplnění nákladového střediska v žádance**

V žádance se automaticky vyplňuje pole Nákladové středisko dle následujících pravidel:

1. Pokud je zaškrtnut pouze konkrétní NČLP kód v žádance (Morbilli (Spalničky) (IgG)), tak se automaticky vyplní nákladové středisko s příznakem "spalničky", které je nastavené u daného zaměstnavatele (Nadstandardní péče – detail firmy). Pokud daný zaměstnavatel nebude mít definovanou položku s příznakem "Spalničky NS", pokračuje krokem 2). Vyplňuje se NS s příznakem spalničky a příznakem primární. Pokud neexistuje příznak primární a existuje právě jedno „spalničky“, vyplní se toto.

1. Pokud má pacient v kartě zaměstnání vyplněné pole „Alternativní nákladové středisko“, doplní se automaticky tato hodnota.

1. Pokud má zadané datum začátku zaměstnání, které odpovídá intervalu definovaným správcem na firmě na počet dní před a počet dní po nástupu do, pak se automaticky v žádance vyplní nákladové středisko s příznakem "Vstupní prohlídka NS" a příznakem primární. Pokud neexistuje příznak primární a existuje právě jedno vstupní, vyplní se toto. Jinak: se automaticky vyplní nákladové středisko s příznakem "PLS NS" a „primární“, Pokud neexistuje příznak primární a existuje právě jedno „PLS NS“, vyplní se toto.
