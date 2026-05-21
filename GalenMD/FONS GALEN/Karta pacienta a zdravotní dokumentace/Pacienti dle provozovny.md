---
title: "Pacienti dle provozovny"
version: 3
updated_at: 2026-03-03
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/108757007
---

# Pacienti dle provozovny

Pro každé pracovišti je možné definovat provozovny. Pacienty na pracovišti je pak možné přiřazovat do takto definovaných provozoven. Uživatel může definovat svoji preferovanou provozovnu, kdy pak vidí přednostně pacienty přiřazené na svoji provozovnu. Údaje definované v rámci provozovny vstupují do notifikací (např. mobil, adresa).

## Konfigurace společnosti

Funkcionalitu lze zapnout v konfiguraci společnosti. Následně se v konfiguraci definují jednotlivé provozovny na pracovištích.

### Zapnutí funkcionality

*Cesta: modul Správce -> modul Správa organizace -> vybrat pracoviště*

1. Pro zapnutí funkcionality uživatel vybere v pravé části možnost „Přiřazení pacientů na provozovny“ a tuto možnost zatrhne.
2. Změny potvrdí tlačítkem Uložit.

### Provozovny

*Cesta: modul Správce -> modul Správa organizace -> vybrat pracoviště -> záložka Provozovna*

#### Vytvoření nové provozovny

1. Uživatel stiskne tlačítko Přidat nový záznam.
2. Uživatel vyplní údaje provozovny.
3. Údaje potvrdí tlačítkem OK.

![image-20250901-074820.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Pacienti dle provozovny/assets/image-20250901-074820.png>)

![image-20250901-074848.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Pacienti dle provozovny/assets/image-20250901-074848.png>)

#### Editace provozovny

1. Uživatel vybere provozovnu.
2. Uživatel stiskne tlačítko Otevřít vybraný záznam.
3. Alternativa je dvojklik na vybraný záznam.
4. Uživatel provede změny.
5. Uživatel údaje potvrdí tlačítkem OK.

#### Zneaktivnění provozovny

1. Uživatel vybere provozovnu.

2. Uživatel stiskne tlačítko Otevřít vybraný záznam.

1. Alternativa je dvojklik na vybraný záznam.

3. Uživatel odtrhne možnost Aktivní.

4. Uživatel údaje potvrdí tlačítkem OK.

## Uživatelské nastavení

V uživatelském nastavení lze nastavit výchozí provozovnu.

*Cesta: Vybrat pracoviště -> modul Ordinace -> Konfigurace a nastavení (vpravo nahoře)*

1. Uživatel zůstane na záložce Nastavení.

2. U položky Výchozí provozovna uživatel vybere provozovnu ze seznamu.

3. Uživatel výběr potvrdí tlačítkem OK.

![image-20250901-075125.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Pacienti dle provozovny/assets/image-20250901-075125.png>)

## Kartotéka

*Cesta: Vybrat pracoviště -> modul Ordinace*

V kartotéce je položka „Zobrazit jen provozovnu“ a výběr ze seznamu provozoven daného pracoviště. Pokud má uživatel definovanou provozovnu, checkbox je zatržený a je vybrána provozovna definovaná uživatelem v nastavení.

V seznamu je dostupná také volba „Nepřiřazení“. Po jejím zvolení se zobrazí pacienti, kteří nejsou přiřazeni k žádné provozovně.

![image-20250901-075149.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Pacienti dle provozovny/assets/image-20250901-075149.png>)
V kartotéce je možné přiřazovat/vyřazovat pacienty k provozovně a to následujícím způsobem:

**Přiřazení**

1. Vybrat pacienta a stisknout pravé tlačítko myši.

2. Vybrat možnost Zařadit -> K provozovně.

3. Uživatel vybere provozovnu a případě upraví datum přiřazení.

4. Údaje uživatel potvrdí tlačítkem OK.

![image-20250901-075207.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Pacienti dle provozovny/assets/image-20250901-075207.png>)
**Vyřazení**

1. Vybrat pacienta a stisknout pravé tlačítko myši.

2. Vybrat možnost Vyřadit -> Z provozovny.

3. Potvrdit ukončení tlačítkem Ano.

4. Uživatel je vyřazen.

![image-20250901-075219.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Pacienti dle provozovny/assets/image-20250901-075219.png>)

## Upozornění k pacientovi

V okně **Upozornění k pacientovi** se zobrazuje sekce **„Provozovna pacienta“**, pokud pacient není přiřazen k žádné provozovně.
Sekce obsahuje informaci *„Pacient není přiřazen k žádné provozovně. Přiřaďte pacienta na provozovnu.“* a tlačítko **„Přiřadit k provozovně“**.
Po kliknutí na tlačítko je uživatel přesměrován do karty pacienta, kde může přiřazení provést.

## Karta pacienta

*Cesta: Vybrat pracoviště -> modul Ordinace -> vybrat pacienta -> karta pacienta*

Na kartě pacienta je vidět aktuálně přiřazená provozovna. Provozovny lze na kartě pacienta přiřazovat nebo vyřazovat.

![image-20250901-075238.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Pacienti dle provozovny/assets/image-20250901-075238.png>)
Přiřazení pacienta je za pomocí tlačítka Přiřadit k provozovně a vyřazení tlačítkem Vyřadit z provozovny. Postup pro přiřazení/vyřazení je stejný, jako je v kartotéce.

## Dashboard

V dashbordu lze zobrazovat data dle provozovny. Jako výchozí je zobrazena provozovna definovaná v uživatelském nastavení. Provozovny lze přepínat výběrem ze seznamu provozoven v položce „Zobrazit jen provozovnu“.

![image-20250901-075304.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Pacienti dle provozovny/assets/image-20250901-075304.png>)

## Recepce

*Cesta: modul Recepce -> modul Objednávání -> vybrat pacienta -> pravá strana*

V recepci v informacích o pacientovi je vidět položka „Přiřazen k provozovně:“ včetně názvu provozovny. Pokud pacient není přidělen k žádné provozovně, položka se nezobrazuje.

![image-20250901-075327.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Pacienti dle provozovny/assets/image-20250901-075327.png>)

## Nastavení kalendáře pro provozovnu

V nastavení kalendáře lze definovat, které provozovně vybraný kalendář patří.

*Cesta: modul Správce -> Správa organizace -> Agendy -> záložka Kalendář -> vybrat kalendář*

1. Otevřít nastavení vybraného kalendáře.

2. Otevřít Nastavení.

3. U položky Provozovna vybrat ze seznamu provozovnu.

4. Nové údaje potvrdit tlačítkem OK.

![image-20250901-075351.png](<../../../pages/FONS GALEN/Karta pacienta a zdravotní dokumentace/Pacienti dle provozovny/assets/image-20250901-075351.png>)
***Poznámka:**Na záložce Notifikace lze definovat výchozí notifikace. V nastavení šablon lze definovat údaje pro provozovnu.*

## Rozdělení notifikací na provozovnu (nároky)

*Cesta: modul Správce -> modul Nároky*

1. Uživatel stiskne tlačítko Notifikace pro zobrazení obrazovky Hromadné notifikace.

2. Uživatel stiskne tlačítko Přidat nový záznam.

3. Uživatel vyplní potřebné údaje

1. Termín

2. Typ

3. Podtyp

4. Počet notifikací na pracoviště

5. Pracoviště

6. Provozovna – zde uživatel vybere provozovnu, pro kterou mají být notifikace odesílány

1. Lze definovat pouze provozovny jednoho pracoviště.

7. Počet notifikací pro jeden nárok

8. Mimo pojišťovny

9. Rozestup notifikací [dny]

***Poznámka:**Pro oslovování pacientů k nárokům se používají šablony notifikací. Do těchto šablon lze nastavit údaje provozoven.*
