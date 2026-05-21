---
title: "Potřebná nastavení"
version: 3
updated_at: 2025-12-05
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/75694423
---

# Potřebná nastavení

> [!info]
> Popis nastavení, která jsou nutná pro spuštění komunikace FONS Galen s ČSSZ. Dále jsou popsána volitelná nastavení jako je např. možnost nastavení upozornění na blížící se překročení podpůrčí doby pracovní neschopnosti.

## Nutná nastavení

Po aktivaci nadstandardního modulu je nutné ze strany uživatele s rolí *Správce*provést tato nastavení:

- *Správce → Správa organizace →*na konkrétním pracovišti nastavit *Kód SÚKL*

- *Správce → Správa organizace →*na konkrétním pracovišti nastavit certifikát SÚKL

*Poznámka: Jedná se o certifikát, který původně vydával SÚKL, nově jej vydává ÚZIS. Certifikát, i přesto, že je vydaný ÚZIS, je nutné nastavit na pracovišti, nikoli na úrovni společnost.*

- *Správce → Správa organizace →*na konkrétním pracovišti nastavit *Konfiguraci ČSSZ*

![image-20250721-122520.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Potřebná nastavení/assets/image-20250721-122520.png>)
![image-20250721-122552.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Potřebná nastavení/assets/image-20250721-122552.png>)
(1)   **IČPE**

Vyplňte osmimístné číslo IČPE, které vaše zdravotnické zařízení získalo na základě registrace na ČSSZ. Po uložení již tuto hodnotu není možné měnit.

(2)   **Kód územního pracoviště**

Vyberte hodnotu z číselníku tak, aby odpovídala informacím, které jste obdrželi v rámci vaší registrace na ČSSZ.

(3)   **Název územního pracoviště**

Není potřeba vyplňovat, vyplní se automaticky po výběru kódu územního pracoviště z číselníku.

(4)   **Test komunikace s ČSSZ**

Po zadání údajů otestujte, zda jsou zadané údaje správné.

## Volitelná nastavení

- Správa IČPE

V případě aktivní funkcionality *Správa IČPE* je možné spravovat IČPE vůči ČSSZ přímo z FONS Galen.

- Vytvořit IČPE

![image-20250721-122958.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Potřebná nastavení/assets/image-20250721-122958.png>)
V případě, kdy je na ČSSZ provedena registrace zdravotnického zařízení a je přiřazeno tzv. hlavní IČPE, tak je možno z FONS Galen vytvářet další IČPE pro jednotlivá pracoviště.

(1)   Pokud je pole IČPE prázdné, stane se tl. *Vytvořit IČPE* aktivním (2).

(3)   Je nutné zadat právě jedno jméno lékaře, tzv. garanta pracoviště

(4)   Jako název registrace je možné použít název společnosti nebo vepsat název pracoviště.

(5)   Vyplňte kód územního pracoviště z číselníku.

(6)   Vyplňte odbornost pro práci s IČPE z číselníku.

Stiskem tl. *Vytvořit IČPE*bude na ČSSZ odeslán požadavek se založením nového IČPE. Vytvoření na straně ČSSZ bude potvrzeno .

Okno Konfigurace opusťte tl. *OK* pro uložení zadaných informací.

- Přehled IČPE

Tlačítko zobrazí přehled hlavního a všech podřízených IČPE. Z tabulky je možné pomocí klávesových zkratek Ctrl+C kopírovat zobrazené údaje.

- Zneplatnit IČPE

Zneplatní zobrazení IČPE.

- Odeslat změnu jména

Tlačítko odešle požadavek na změnu jména, které je aktuálně u IČPE v přehledu IČPE ČSSZ vedeno.

- Odeslat změnu registrace

Tlačítko odešle požadavek na změnu názvu registrace, který je aktuálně u IČPE v přehledu IČPE ČSSZ vedeno.

- Zvýraznit pacienty v kartotéce, pokud DPN trvá déle než X dnů

Pacienti, kteří mají aktivní eDPN, která trvá déle než zadaný počet dnů, budou v kartotéce označeni symbolem ![image-20250721-123104.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Potřebná nastavení/assets/image-20250721-123104.png>)
 . Obvykle se pole využívá pro zadání 380 dní, což je v tuto chvíli maximální podpůrčí doba pro poskytování nemocenského.

- Upozornit na blížící se překročení podpůrčí doby pracovní neschopnosti

Upozornění je zasláno prostřednictvím echo zprávy s přehledem eDPN, které překročily dobu trvání 380 dní. Zprávu obdrží všichni uživatelé, kteří mají přístup na dané pracoviště.

Zpráva má tuto podobu

![image-20250721-123144.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Potřebná nastavení/assets/image-20250721-123144.png>)
