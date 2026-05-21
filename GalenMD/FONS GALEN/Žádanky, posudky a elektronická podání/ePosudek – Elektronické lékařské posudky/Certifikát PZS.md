---
title: "Certifikát PZS"
version: 1
updated_at: 2026-04-29
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/377421825
---

> [!info]
> Aby FONS Galen mohl odesílat **ePosudky** (elektronické lékařské posudky), musí mít nastavený **Certifikát PZS**. Vydavá ho **EZCA II**, Portál certifikační autority Ministerstva zdravotnictví ČR.
>
> **Celý postup má 3 fáze:** přihlášení na národní portál → vystavení certifikátu v EZCA → nastavení v FONS Galen.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-123156.png]]

## 1. K čemu Certifikát PZS slouží

Certifikát PZS je **systémový přístupový certifikát organizace**. Neváže se na konkrétního lékaře, ale na celou ordinaci (IČO / IČZ). Pro odesílání ePosudky přes FONS Galen je jeho nastavení **povinné**.

> [!warning]
> **Kdo certifikát vyřizuje?**
>
> Certifikát musí vystavit **statutární zástupce** nebo **pověřená osoba PZS** zapsaná v Registru oprávnění. Přihlášení probíhá přes identitu občana (datová schránka, eObčanka, mobilní klíč eGov). Řadový lékař bez tohoto oprávnění certifikát vystavit nemůže.

## 2. Přihlášení na národní portál zdravotníka

Certifikát se vyřizuje přes národní portál eZdraví Ministerstva zdravotnictví.

> [!danger]
> **Pozor — přihlášuje se pověřená osoba, ne lékař**
>
> Přihlásit se musí osoba s oprávněním za organizaci (statutár nebo pověřenec). Přihlášení osobním občanským průkazem lékaře nestačí, pokud tato osoba nemá oprávnění za PZS.

1. Přejděte na [https://www.ezdravi.gov.cz/login/role?typ=zdravotnik&returnurl=%2Fprivate](https://www.ezdravi.gov.cz/login/role?typ=zdravotnik&returnurl=%2Fprivate). Zobrazí se stránka **Zdravotnický pracovník**.
2. Klikněte na **Identita občana** a přihlaste se: mobilní klíč eGov, bankovní identita nebo eObčanka (NIA).

   ![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-130220.png]]

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-130408.png]]
1. Po dokončení přihlášení se zobrazí **Pracovní přehled** portálu. V menu zvolte “**Poskytovatel zdravotnických služeb**”.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-130933.png]]
1. Vpravo nahoře zkontrolujte, že je vybrána **správná organizace (PZS)**.
2. Klikněte na dlaždici **Certifikáty**. Budete přesměrováni na portál EZCA.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-131630.png]]
1. Přejděte na přihlášení do Portálu EZCA

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-132406.png]]

## 3. Jak získat certifikát v portálu EZCA

Pokud jste přešli z národního portálu, jste již přihlášeni. Případně se přihlaste přímo na [https://ezca-ez.csez.cz](https://ezca-ez.csez.cz).

1. Na stránce **Subjekty** v sekci **Systémové certifikáty** klikněte na **Přejít** u vaší organizace.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-134755.png]]
1. Otevře se stránka **Certifikáty** s tabulkou stávajících certifikátů a tlačítky pro vystavení nových.
2. Klikněte na tlačítko **VYSTAVIT PŘÍSTUPOVÝ CERTIFIKÁT**.

   ![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-132900.png]]

1. Vyplňte formulář *Žádost o nový firemní přístupový certifikát*:

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-133146.png]]
1. Klikněte na **GENEROVAT**. Zobrazí se potvrzení *Žádost o vydání certifikátu byla odeslána.*

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-133536.png]]
1. V tabulce certifikátů klikněte na **STÁHNOUT** u nového certifikátu. Uložte soubor `.pfx` na bezpečné místo.

> [!danger]
> **Soubor .pfx obsahuje privátní klíč**
>
> Zacházejte s ním jako s heslem — nezasílejte e-mailem ani nesdílejte přes veřejná úložiště. Soubor je chráněn heslem nastaveným ve formuláři.

## 4. Jak nastavit Certifikát PZS v FONS Galen

Nastavení provádí administrátor (role **Správce**). Certifikát se nastavuje jednou za celou organizaci.

**Cesta:** Správce → Správa organizace → záložka Struktura → klikněte na název organizace → řádek **Certifikát PZS** → **Nastavit**

1. Otevřete **Správa organizace** (menu Správce), záložka **Struktura**.
2. V levém stromě klikněte na název vaší organizace.
3. V pravém panelu klikněte na **Nastavit** u řádku Certifikát PZS.
4. Vyberte soubor `.pfx` a zadejte heslo z EZCA.
5. Klikněte na **Uložit**.
6. **Restartujte FONS Galen** — bez restartu se certifikát neaktivuje.

> [!tip]
> **Ověření funkčnosti**
>
> Po restartu klikněte na **Ověřit PZS** v detailu organizace. Zelená ikona = certifikát funguje správně.

![[pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/assets/obrazek-20260429-133850.png]]

## 5. Obnova certifikátu před vypršením

Certifikát PZS má platnost **3 měsíce**. Bez platného certifikátu přestanou fungovat ePosudky.

1. Vystavte nový certifikát v EZCA stejným postupem jako v části 3.
2. Stáhněte nový soubor `.pfx`.
3. V Galenu: Správa organizace → Struktura → organizace → Certifikát PZS → **Nastavit** → nahrajte nový soubor.
4. Restartujte Galen.

## 6. Časté otázky

> [!summary]- ![](https://stapro-galen.atlassian.net/wiki/images/icons/grey_arrow_down.png)
Může certifikát vystavit přímo lékař?
> Ne. Certifikát musí vystavit statutární zástupce nebo pověřená osoba PZS zapsaná v Registru oprávnění.

> [!summary]- ![](https://stapro-galen.atlassian.net/wiki/images/icons/grey_arrow_down.png)
Musím certifikát instalovat do Windows?
> Ne. Certifikát PZS se do Windows neinstaluje — Galen pracuje přímo se souborem `.pfx`.

> [!summary]- ![](https://stapro-galen.atlassian.net/wiki/images/icons/grey_arrow_down.png)
Kmenové registry, ePosudky nefungují — co zkontrolovat?
> 1. Je Certifikát PZS nastaven? (Správa organizace → Struktura → organizace → Certifikát PZS)
> 2. Je certifikát platný? (datum expirace v EZCA nebo v detailu organizace)
> 3. Byl Galen po nastavení restartován?

> [!summary]- ![](https://stapro-galen.atlassian.net/wiki/images/icons/grey_arrow_down.png)
Potřebuji pro ePosudky osobní certifikát lékaře?
> Ne. Stačí Certifikát PZS — autenticita je zajištěna pečetí poskytovatele na úrovni organizace.

> [!summary]- ![](https://stapro-galen.atlassian.net/wiki/images/icons/grey_arrow_down.png)
Kde uchovávat soubor .pfx po nastavení?
> Po nahrání do Galenu uložte soubor jako zálohu na bezpečné offline místo (např. šifrovaný USB disk dostupný jen správci). V Galenu je certifikát uložen v databázi.
