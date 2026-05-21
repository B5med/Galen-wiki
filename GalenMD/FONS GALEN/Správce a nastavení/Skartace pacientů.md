---
title: "Skartace pacientů"
version: 1
updated_at: 2025-07-01
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/61079557
---

# Skartace pacientů

## **Princip skartace ve FONS Galen**

Skartace ve FONS Galen je řešena formou pseudonymizací osobních údajů pacientů uchovávaných v databázi. Systém zároveň zajišťuje logování provedených pseudonymizací.

**Princip generování identity**

Princip generování identity se odvíjí dle toho, zda je skartována dokumentace za pracoviště nebo za celou společnost a zda se skartuje celá dokumentace nebo dokumentace typu kurativa nebo PLS.

Při skartaci za jedno pracoviště nebo pro jednotlivé typy dokumentace - je vygenerována zcela nová identita, na kterou je převázána dokumentace pacienta vzniklá na pracovišti nebo jednotlivý typ dokumentace, pro které provádíme skartaci.

Kontrola: Systém zkontroluje, jestli pro skartovaného pacienta existuje dokumentace na jiném pracovišti nebo jiný typ dokumentace. Pokud taková dokumentace neexistuje, nevytváří se nová identita, ale pacient se rovnou přepisuje, tzn. skartace je realizována jako za všechna pracoviště.

Při skartaci celé společnosti (za všechna pracoviště) a celé dokumentace – je vygenerována nová identita, kterou jsou přepsány údaje pacienta.

Při procesu skartování je každému pacientovi vygenerováno GUID číslo, toto číslo je uloženo do čísla pojištěnce a zároveň je použito u přepisu položek.

## **Popis základních obrazovek**

Obrazovka Pacienti navržení ke skartaci slouží k vytvoření seznamu pacientů, kteří mají být skartováni. Obrazovka se skládá z lišty se záložkami (Návrhy, Záznamy, Skartovat, Tisk), ovládacích tlačítek, filtru a tabulky pacientů navržených ke skartaci.

**Záložky (tlačítka)**

- Návrhy – tlačítko slouží k zobrazení obrazovky Pacienti navržení ke skartaci
- Záznamy - tlačítko slouží k zobrazení obrazovky Záznamy o skartaci (logy skartace)
- Skartovat – tlačítko slouží ke skartaci vybraných záznamů z tabulky pacientů navržených ke skartaci
- Tisk – tlačítko slouží k vytištění tabulky navržených záznamů ke skartaci.

**Ovládací tlačítka**

Generovat – tlačítko slouží k hromadnému vygenerování pacientů navržených ke skartaci za určitých podmínek, např. vygenerování pacientů bez dokumentace

Importovat – tlačítko slouží k importu souboru se seznamem pacientů navržených ke skartaci

Plus – tlačítko slouží pro přidání nového pacienta do tabulky pacientů navržených ke skartaci

Mínus – tlačítko slouží pro smazání vybraného pacienta z tabulky pacientů navržených ke skartaci

**Filtr**

Umožňuje vyhledávat v seznamu pacientů navržených ke skartaci za pomocí:

- Pracoviště
- Pacient – lze vyhledávat dle jména, příjmení, čísla pojištěnce

Do filtru lze zadat jen část textu (např. 92) a stisknout tlačítko *Aplikovat*. Systém v takové případě vyhledá pacienty s číslem pojištěnce začínajícím na 92.

Pro potvrzení filtru slouží tlačítko *Aplikovat* a pro zrušení filtru tlačítko *Zrušit*.

**Tabulka**

- Checkbox – slouží k výběru pacienta a jeho následné skartaci za pomocí tlačítka Skartovat
- Příjmení
- Jméno
- Č. pojištěnce
- Pracoviště – pracoviště, pro které bude provedena skartace pacienta
- Pozn.: Pokud není pracoviště vyplněno, skartace bude provedena za všechna pracoviště.
- Skartovat
- Typ dokumentace
- Poznámka

Dokumentace navržená ke skartaci:

![image-20250701-082652.png](<../../../pages/FONS GALEN/Správce a nastavení/Skartace pacientů/assets/image-20250701-082652.png>)
**Obrazovka Záznamy o skartaci** slouží k zobrazení údajů o skartované dokumentaci. Obrazovka se skládá z lišty se záložkami Návrhy a Záznamy, filtru a tabulky se záznamy.

**Záložky**

- Návrhy – tlačítko slouží k zobrazení obrazovky Pacienti navržení ke skartaci
- Záznamy - tlačítko slouží k zobrazení obrazovky Záznamy o skartaci (logy skartace)

**Filtr**

Umožňuje vyhledávat v záznamech o skartaci za pomocí:

Pacient – lze vyhledávat dle jména, příjmení, čísla pojištěnce

Do filtru lze zadat jen část textu (např. 92) a stisknout tlačítko aplikovat. Systém v takové případě vyhledá pacienty s číslem pojištěnce začínajícím na 92.

- Pracoviště
- Uživatel
- Datum

Pro potvrzení filtru slouží tlačítko *Aplikovat* a pro zrušení filtru tlačítko *Zrušit*.

**Tabulka**

- Datum – datum, kdy byl záznam skartován
- Příjmení
- Jméno
- Číslo pojištěnce
- Pracoviště – pracoviště, pro které byla provedena skartace
- Pozn.: Pokud není pracoviště vyplněno, skartace byla provedena za všechna pracoviště.
- Uživatel – uživatel, který skartaci provedl

Poznámka

![image-20250701-082727.png](<../../../pages/FONS GALEN/Správce a nastavení/Skartace pacientů/assets/image-20250701-082727.png>)

## **Zapnutí modulu Skartace**

- Modul Správce lze zapnout:
- Přihlášení do FONS Galen
- Zvolit modul Správce
- Zvolit modul Správa organizace
- Přejít na záložku Uživatelé
- Vyhledat ze seznamu uživatele, kterému má být zapnut modul Skartace, a otevřít jeho detail.
- V části Dostupnost modulů zatrhnout možnost Skartace.
- Změny potvrdit tlačítkem *OK*

Postup vypnutí modulu správce je obdobný, jen v bodě 6 je možnost Skartace odtrhnuta.

**Přidat pacienta na seznam navržené dokumentace se skartaci** lze z obrazovky Pacienti navržení ke skartaci

**Postup:**

- Stisknout tlačítko *Plus* (Přidat nový záznam).
- Po stisku tlačítka se zobrazí okno Nový návrh ke skartaci.

![image-20250701-082817.png](<../../../pages/FONS GALEN/Správce a nastavení/Skartace pacientů/assets/image-20250701-082817.png>)
- Vyplnit číslo pojištěnce a výběr potvrdit tlačítkem *Vyhledat*.
- Při správném zadání údajů se doplní Jméno a Příjmení pacienta.
- Rozkliknout šipku směřující dolů a vybrat, co má být skartováno – Vše nebo Dle lhůty.
- Rozkliknout šipku směřující dolů a vybrat typ dokumentace, pro které má být skartace provedena.
- Rozkliknout šipku směřující dolů a vyhledat pracoviště, pro které má být skartace provedena.
- Pokud nevyberete žádnou možnost, bude skartace provedena pro všechna pracoviště.
- Vyplnit poznámku ke skartaci (není nutná).
- Výběr potvrdit tlačítkem *Přidat*.

Po potvrzení lze pacienta dohledat v seznamu dokumentace navržené ke skartaci.

Skartovat pacienty lze z obrazovky Pacienti navržení ke skartaci.

**Postup:**

- Vybrat pacienty ke skartaci zatržením checkboxu v tabulce vedle příjmení pacienta.
- Pro výběr všech pacientů z tabulky lze zatrhnout checkbox v záhlaví tabulky.
- Stisknout tlačítko *Skartovat*.
- Po stisku tlačítka se zobrazí okno Skartovat vybranou dokumentaci.

![image-20250701-082859.png](<../../../pages/FONS GALEN/Správce a nastavení/Skartace pacientů/assets/image-20250701-082859.png>)
- Samotný proces skartace spustit tlačítkem *Skartovat*.
- Potvrdit tlačítkem *Ano*.
- Po skončení procesu skartace zavřít okno tlačítkem *Zavřít*.

Uložení do souboru a načtení ze souboru se používá zejména při postupné skartaci za jednotlivá pracoviště pro zachování vazby mezi identitami.

**Uložení do souboru**

Po skartaci je uživateli nabídnuta možnost uložit si csv soubor, ve kterém je uchována vazba mezi pacientem a jeho „novou“ identitou.

**Načíst ze souboru**

Při spuštění procesu skartace je uživateli nabídnuta možnost načíst csv soubor. Pokud je v tomto souboru pacient, který má být skartován, převáže se jeho dokumentace na fiktivního pacienta, na kterého byla již dokumentace tohoto pacienta převedena.

Důvodem, proč zachovávat stejnou vazbu, jsou statistiky. V případě, že nebude zachována stejná vazba, bude ve statistikách jeden pseudonymizovaný pacient vystupovat jako dva.

## **Kontrola na vykázané výkony**

Při procesu skartace systém zkontroluje, jestli má pacient vykázaný výkon, který nebyl vyúčtován na pojišťovnu. Pokud systém takový výkon objeví, zobrazí se uživateli dialogové okno „Pacient Jan Novák (RČ 9051237895) má vykázané výkony, který nebyly odeslány na pojišťovnu. Přejete si pacienta přesto skartovat?“

*Ano* – pacient je skartován

*Ne* – pacient není skartován

## **Importování dokumentace do návrhu skartace**

Import dokumentace do návrhu dokumentace ke skartaci lze provést stiskem tlačítka *Importovat* z obrazovky Pacienti navržení ke skartaci.

Struktura importovaného souboru:

- Číslo pojištěnce – povinný údaj
- Jméno pojištěnce – povinný údaj
- Příjmení pojištěnce – povinný údaj
- Pracoviště – vyplňovaná hodnota je IČP
- Poznámka

Importovaný soubor bude obsahovat hlavičku (= 1. řádek), která nebude importována.

Systém při importu vyhledá pacienta v souboru ve FONS Galen a pokud jej najde, zapíše jej do seznamu dokumentace navrhované ke skartaci.

V případě chyby při importu se zobrazí informační okno s popisem chyby a se souřadnicemi, kde se chyba nachází.

## **Hromadné generování návrhů ke skartaci**

Hromadné vygenerování návrhů dokumentace lze provést stiskem tlačítka *Generovat* z obrazovky Pacienti navržení ke skartaci.

Postup:

1. Stisknout tlačítko **Generovat**.

Po stisku tlačítka se zobrazí okno Generovat návrhy ke skartaci.

![image-20250701-083046.png](<../../../pages/FONS GALEN/Správce a nastavení/Skartace pacientů/assets/image-20250701-083046.png>)
2. Vybrat typ generování – Pacient bez dokumentace nebo Pacient s posledním zápisem v dekurzu před více než x dny nebo Dle skartačních lhůt

- Pacient bez dokumentace – budou vygenerováni pacienti, kteří nemají žádný záznam v dekurzu a nemají vyplněnou žádnou anamnézu.
- Upozornění: V případě, že lékař vytvoří vyšetření (medikaci, formulář,…), ale do dekurzu nenapíše žádný záznam, bude tento pacient také navržen ke skartaci.
- Pacient s posledním zápisem v dekurzu před více než x dny – budou vygenerování pacienti, u kterých nebyl proveden žádný zápis do dekurzu po více než zadaný počet dnů
- Dle skartačních lhůt

3. V případě výběru možnosti „Pacient s posledním zápisem v dekurzu před více než x dny“ doplnit počet dnů.
4. V případě výběru možnosti „Dle skartačních lhůt“ je možné generovat návrhy pro dokumentaci typu kurativa, PLS nebo vše.

Rozhodným datem pro vygenerování záznamu ke skartaci jsou různá data, konkrétně:

- V5 - ostatní ambulantní péče - od data dokumentu
- V10 - dispenzarizace - od data dokumentu
- S10 - 10 let od úmrtí pacienta s uznanou nemocí z povolání - od úmrtí  nebo registrovaný pacient - od data dokumentu
- V15 - 15 let od data uznání ohrožení nemocí z povolání - od data dokumentu  nebo 15 let od ukončení zaměstnání osoby vykonávající rizikovou práci podle zákona o ochraně veřejného zdraví - od ukončení zaměstnání posledního zaměstnání
- V10 - 10 let od ukončení zaměstnání osoby vykonávající práci zařazenou podle zákona o ochraně veřejného zdraví do kategorie první nebo druhé - od ukončení posledního zaměstnání nebo 10 let od vzniku ostatních pracovních úrazů - od data dokumentu
- V40 - 40 let od ukončení zaměstnání osoby vykonávající rizikovou práci ve smyslu jiného právního předpisu - od ukončení zaměstnání posledního zaměstnání
- S30 - u zaměstnance kategorie A[^14^)](https://www.zakonyprolidi.cz/cs/2012-98#f4599370) do doby, kdy zaměstnanec dosáhl nebo by dosáhl věku 75 let, vždy však nejméně 30 let od ukončení pracovní činnosti v kategorii A - od ukončení posledního zaměstnání
- V30 - 30 let od vzniku pracovního úrazu spojeného s hospitalizací přesahující 5 kalendářních dnů nebo 10 let po úmrtí osoby, která utrpěla takový úraz - od data dokumentu

5. Rozkliknout šipku směřující dolů a vyhledat pracoviště, pro které má být skartace provedena.

- Pokud nevyberete žádnou možnost, bude podmínka aplikována na všechna pracoviště a skartace bude také navržena pro všechna pracoviště.

6. Vyplnit poznámku ke skartaci (není nutná).
7. Výběr potvrdit tlačítkem *Generovat*.

## **Tisk navržených pacientů ke skartaci**

Vytisknout seznam navržených pacientů ke skartaci lze stiskem tlačítka *Tisk* z obrazovky Pacienti navržení ke skartaci.
