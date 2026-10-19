---
title: "Obnova certifikátu PZS ve FONS Galen"
version: 2
updated_at: 2026-10-19
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/643497986
---

# Obnova certifikátu PZS ve FONS Galen

Certifikát PZS se dá obnovit přímo ve FONS Galen, bez portálu EZCA.

> [!danger]
> **Obnovit lze jen aktivní certifikát.** Musí být ve společnosti nastavený a nesmí mít prošlou platnost. Jinak je tlačítko Obnovit zašedlé. Prošlý certifikát je nutné vystavit znovu v EZCA (viz stránka [[Certifikát PZS]]).

## Postup

1. Otevřete detail společnosti a klikněte na **Konfigurace PZS**.

   - Hlavní společnost: Správce → Správa organizace → Struktura → společnost.
   - Podřízená společnost: Správce → Správa organizace → Agendy → Podřízené společnosti → společnost.
   - Společnost musí být uložená.

![image-20261019-085602.png](<../../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/Obnova certifikátu PZS ve FONS Galen/assets/image-20261019-085602.png>)
2. V části **Obnova certifikátu** zadejte **Nové heslo** a stejné heslo do **Potvrzení hesla**. Heslo musí mít 17 až 100 znaků a obsahovat znaky alespoň ze 3 skupin: malá písmena, velká písmena, číslice, speciální znaky. Heslo si uložte.

![image-20261019-085711.png](<../../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePosudek – Elektronické lékařské posudky/Certifikát PZS/Obnova certifikátu PZS ve FONS Galen/assets/image-20261019-085711.png>)
3. Klikněte na **Obnovit**.
4. Podle zprávy:

   - „Certifikát PZS byl obnoven. Platnost do …“: hotovo.
   - „Žádost se zpracovává…“: dialog zavřete, později jej otevřete znovu a klikněte na **Zjistit stav**.
5. V **Historii obnovy** zkontrolujte stav **Obnoven**. Dialog zavřete tlačítkem **OK**.

Každá společnost, hlavní i podřízená, má vlastní certifikát a obnovuje se zvlášť.

## Když něco nejde

| Situace | Co dělat |
| --- | --- |
| Obnovit je zašedlé | Najedťte myší na tlačítko, zobrazí se důvod: špatné heslo, neshoda hesel, neaktivní certifikát nebo probíhající žádost. |
| Stav **Zpracovává se** | Klikněte na Zjistit stav. |
| Stav **Chyba** | Text chyby uvidíte po najetí myší na řádek v Historii. Zkuste Obnovit znovu a zadejte nové heslo. Při opakování kontaktujte podporu. |
