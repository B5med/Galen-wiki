---
title: "Obrazovka: Výchozí údaje"
version: 2
updated_at: 2026-05-12
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/113999874
---

# Obrazovka: Výchozí údaje

Slouží k zadávání klíčových vstupních údajů, které mají přímý vliv na výpočty a analýzy. Údaje lze definovat obecně, nebo pro konkrétní pojišťovny a IČZ. Některá pole se vyplňují ručně, jiná jsou automaticky dopočítána systémem a zobrazují se jako neaktivní (šedě).

### Záložka: Úhradové parametry

Záložka Úhradové parametry slouží k zadávání vstupních údajů pro výpočet. Klíčovým polem je **Vstupní úhrada**, bez jehož vyplnění není možné provést kompletní výpočet. Ostatní hodnoty lze zadat ručně, nebo je systém v případě prázdných polí automaticky dopočítá.

![image-20260512-060429.png](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20260512-060429.png>)
Editace údajů:

1. V seznamu úhradových parametrů vyberte požadovaný řádek.
2. Řádek otevřete:

a.      dvojklikem, nebo

b.      tlačítkem **Otevřít nový záznam** (ikona tužky).

3. Zobrazí se obrazovka **Úhradové parametry** – detail.
4. Vyplňte nebo upravte potřebné údaje (např. Vstupní úhrada).
5. Potvrďte změny tlačítkem **OK**.

![image-20260512-060503.png](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20260512-060503.png>)

| **Položka** | **Povinná** | **Poznámka** |
| --- | --- | --- |
| Vstupní úhrada | Ano | Povinné pole |
| Počet bodů (ref. období) | Ne | Lze nechat dopočítat |
| Počet unikátních pojištěnců | Ne | Lze nechat dopočítat |
| PURO (ref. období) | Ne | Lze nechat dopočítat |
| Počet UOP limitní úhrady | Ne | Používá se u limitované péče |
| Koeficient navýšení | Ne | Používá se k navýšení koeficientu navýšení. Lze nechat hodnotu stanovenou vyhláškou. |

**Poznámka:** Položka *Koeficient navýšení* je dostupná pouze pro rok 2026 a novější. Pro rok 2025 a starší není tato položka k dispozici – příslušné nastavení lze pro rok 2025 nalézt pod záložkou *Koeficient navýšení*.

### Záložka: Hodnota bodu

Tato záložka slouží k nastavení či kontrole hodnoty bodu pro jednotlivé segmenty a podsegmenty, případně konkrétní pojišťovny a IČZ.

![image-20250905-065341.png](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20250905-065341.png>)
Editace údajů:

1. V seznamu vyberte požadovaný řádek.
2. Řádek otevřete:

a.      dvojklikem, nebo

b.      tlačítkem **Otevřít nový záznam** (ikona tužky).

3. Zobrazí se obrazovka **Hodnota bodu** – detail.
4. Vyplňte nebo upravte potřebné údaje.

a.      Kliknutím na tlačítko Přidat nový záznam (ikona plus) se přidá nový řádek, kde lze zadat hodnoty specifické pro pojišťovny a IČZ.

b.      Vybráním řádku a kliknutím na tlačítko Smazat vybraný záznam (ikona mínus) se vybraný řádek smaže.

5. Potvrďte změny tlačítkem **OK**.

![image-20250905-065359.png](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20250905-065359.png>)
Specifické nastavení umožňuje přidat kombinace pojišťovna + IČZ s pravidly:

- Musí být vyplněna minimálně pojišťovna nebo IČZ.
- Není možné zadat dvě stejné kombinace.
- Pokud není hodnota zadána, použije se obecná.

### Záložka: Koeficient navýšení

Zde se nastavují nebo kontrolují koeficienty, které ovlivňují celkové ocenění výkonů.

![image-20250905-065424.png](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20250905-065424.png>)
Editace údajů:

1. V seznamu vyberte požadovaný řádek.
2. Řádek otevřete:

a.      dvojklikem, nebo

b.      tlačítkem **Otevřít nový záznam** (ikona tužky).

3. Zobrazí se obrazovka **Koeficient navýšení** – detail.
4. Vyplňte nebo upravte potřebné údaje.

a.      Kliknutím na tlačítko Přidat nový záznam (ikona plus) se přidá nový řádek, kde lze zadat hodnoty specifické pro pojišťovny a IČZ.

b.      Vybráním řádku a kliknutím na tlačítko Smazat vybraný záznam (ikona mínus) se vybraný řádek smaže.

5. Potvrďte změny tlačítkem **OK**.

![image-20250905-065456.png](<../../../../pages/FONS GALEN/Finance a účetnictví/Modul Finanční analýza/Obrazovka_ Výchozí údaje/assets/image-20250905-065456.png>)
Specifické nastavení umožňuje přidat kombinace pojišťovna + IČZ s pravidly:

- Musí být vyplněna minimálně pojišťovna nebo IČZ.
- Není možné zadat dvě stejné kombinace.
- Pokud není hodnota zadána, použije se obecná.

**Poznámka:** Položky *Koeficientu navýšení* jsou dostupná pouze pro rok 2025 a starší. Pro rok 2026 a novější se příslušné nastavení nachází pod záložkou *Úhradové parametry*.
