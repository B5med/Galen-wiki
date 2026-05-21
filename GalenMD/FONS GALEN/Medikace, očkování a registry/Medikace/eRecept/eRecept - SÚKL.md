---
title: "eRecept - SÚKL"
version: 2
updated_at: 2025-07-21
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/75333635
---

# eRecept - SÚKL

Možnost odesílat eRecepty přímo do centrálního úložiště SUKLu vyžaduje zprovoznění funkcionality v IS Galen za použití dvou certifikátů – podpisového certifikátu lékaře a SUKL certifikátu daného pracoviště.

## **Přístupové údaje SUKL:**

O přístupové údaje sloužící ke zprovoznění funkcionality eRecept je nutné zažádat na stránkách SUKLu ([www.sukl.cz](http://www.sukl.cz/)). Během několika týdnů (cca 1 měsíc) ` `
​​přijde doporučený dopis ​​s ​​tímto ​​obsahem:

- Přístupové údaje OSOBY pro přístup do portálu
- Přístupové údaje OSOBY pro přístup do centrálního úložiště
- Přístupové údaje ZAŘÍZENÍ pro přístup do portálu
- Přístupové údaje ZAŘÍZENÍ pro přístup do centrálního úložiště

## **Přístupové údaje do za osobu i za zařízení slouží k:**

Přístupové údaje do za osobu i za zařízení slouží k:

1. přístupu do portálu [http://identity.sukl.cz](http://identity.sukl.cz)  – slouží ke správě přístupů a změně hesla

2. přístupu na portál [http://pristupy.sukl.cz](http://pristupy.sukl.cz)  – slouží ke generování certifikátu

3. přístupu do samotného centrálního úložiště receptů - slouží vašemu ambulantnímu softwaru k ověření pro komunikaci s centrálním úložištěm receptů.

Máte tedy celkem 4 přihlašovací údaje.  Centrální úložiště receptů vyžaduje pro svůj přístup dvojí ověření. Prvním je ověření zdravotnického zařízení, druhým je pak ověření samotné osoby.

Pozor, údaje, které jste dostali ze SÚKLu ještě nejsou aktivní, pro jejich aktivaci je třeba změnit heslo.

### Aktivace​​ údajů ​​pro ​​ověření ​​osoby na stránkách SUKLu

Pro​​ aktivací ​​údajů ​​pro​​ ověření​​ osoby ​​je ​​třeba ​​se ​​přihlásit​​ na ​​stránkách [http://identity.sukl.cz](http://identity.sukl.cz/)

Pro​​přístup ​​k ​​aktivaci ​​údajů​​ o ​​osobě ​​lékaře ​​(tedy ​​ne ​​o ​​zdravotnickém ​​zařízení) ​​je ​​třeba ​​napoprvé ​​použít přihlašovací​​ jméno ​​a ​​heslo ​​označené ​​(​​Údaje ​​osoby ​​pro​​ přístup ​​na​​ portál) .​​​Ihned ​​po ​​prvním ​​přihlášení ​​si​​ musíte ​​heslo​​ změnit.

## **Nastavení certifikátu vydaného SÚKLem do IS Galen**

(certifikát není nutné instalovat):

1. Modul Správce -> modul Správa Organizace -> tlačítko Rozbalit strukturu -> vybrat IČP -> v pravé části se zpřístupní informace o pracovišti.

![[pages/FONS GALEN/Medikace, očkování a registry/Medikace/eRecept/eRecept - SÚKL/assets/image-20250721-075514.png]]
2. V informacích o pracovišti vyplnit Kód SÚKL.

3. Stisknout tlačítko Nastavit -> tlačítko Vybrat soubor (vybrat certifikát **vydaný SÚKLem**) -> výběr potvrdit tlačítkem Otevřít.

4. Vyplnit Heslo a potvrdit změny tlačítkem OK.

5. Nastavení uložit tlačítkem Uložit (nahoře).

Pokud nastavení proběhlo v pořádku, po uložení se doplnilo datum u Platnosti.

## **Nastavení kvalifikovaného certifikátu vydaného certifikační autoritou:**

Nastavení certifikátu lze z pozice správce v modulu Správa organizace nebo z pozice uživatele v konfigurační hlavičce v ordinaci v pravém horním rohu.

1. V modulu Správa organizace přejít na záložku Uživatelé.

2. Vyhledat příslušného uživatele a otevřít jeho nastavení dvojklikem.

![[pages/FONS GALEN/Medikace, očkování a registry/Medikace/eRecept/eRecept - SÚKL/assets/image-20250721-094004.png]]
3. Stisknout tlačítko Vybrat (tlačítko u eRecept) a vyhledat certifikát -> výběr potvrdit tlačítkem OK -> po výběru se doplní sériové číslo certifikátu.

4. V části eRecept doplnit:

1. Identifikace SÚKL

2. Heslo

5. Změny potvrdit tlačítkem OK

Odeslané recepty na SUKL = eRecepty nelze již smazat, ale lze je stornovat obdobným způsobem jako již popsané smazání receptu. Informace o stornování eReceptu je také odesílána na SUKL.
