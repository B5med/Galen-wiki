---
title: "Import seznamu registrovaných pojištenců"
version: 3
updated_at: 2026-01-28
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/46071809
---

# Import seznamu registrovaných pojištenců

**Postup importu:**

- Navigace: **Správce → Správa kartoték  → Kontrola**
- Zde lze nahrát FDávku od pojišťovny se seznamem registrovaných pojištěnců.

**Požadavky na název:**

- Délka názvu souboru: 12 znaků (včetně tečky).
- Pokud první písmeno názvu je **F**:

   - První řádek musí být dlouhý 20 znaků.
- Pokud první písmeno názvu je **E**:

   - První řádek musí být dlouhý 32 znaků.
- Název musí dále obsahovat:

   - Tříznakový kód pojišťovny.
   - Poslední dvě číslice z roku.
   - Dvojčíselné vyjádření měsíce.
- První řádek souboru musí začínat písmenem **H**.
- Následujících 8 znaků musí být IČP pracoviště, na které se provádí nahrání FDávky.

![image-20250616-093000.png](<../../../../pages/FONS GALEN/Správce a nastavení/Správa kartoték/Import seznamu registrovaných pojištenců/assets/image-20250616-093000.png>)
**Nový import seznamu pojištěnců:**

V modulu Správce -> Správa kartoték -> Kontrola -> je možné nahrát Fdávku od pojišťovny se seznamem registrovaných pojištěnců.
Pro import seznamu pojištěnců je nutné zvolit pracoviště, poté vybrat soubor, který budeme importovat. Zobrazí se seznam pojištěnců s možností volby vytvoření či nevytvoření registrační dávky, s možností vyloučit pojištěnce z importu odtržením checkboxu na začátku řádku. Sloupec operace oznamuje, jaká akce po importu má nastat. Tlačítkem Provést aktivujeme import zvolných položek souboru.

![image-20250616-093123.png](<../../../../pages/FONS GALEN/Správce a nastavení/Správa kartoték/Import seznamu registrovaných pojištenců/assets/image-20250616-093123.png>)
Tlačítkem Provést aktivujeme import zvolných položek souboru. Před samotným importem se zobrazí okno k výběru měsíce, ke kterému import provedeme. Systém poté oznámí, kolik změn bylo provedeno a ukáže se okno s dotazem, zda chceme seznam vytisknout. Import je dokončen.

![image-20250616-093145.png](<../../../../pages/FONS GALEN/Správce a nastavení/Správa kartoték/Import seznamu registrovaných pojištenců/assets/image-20250616-093145.png>)
