---
title: "Maximální preskripce"
version: 2
updated_at: 2025-11-28
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/173834242
---

# Maximální preskripce

Maximální preskripce se týká pouze prostředků v úhradových skupinách:

**06.01.11.01 – 06.01.11.05**

Pouze pro ně lze dohledat dříve přidělené číslo schválení.

---

## Tlačítko **„Doplnit číslo schválení“**

U položky **Číslo povolení přidělení ZP** je nově tlačítko: **Doplnit číslo schválení.**Uživatel jej využije, pokud chce zjistit, zda existuje předchozí platné schválení.

![image-20251128-111725.png](<../../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ePoukaz/ePoukaz – změny platné od 1. 1. 2026/Maximální preskripce/assets/image-20251128-111725.png>)

---

## **Co systém udělá po stisku tlačítka**

### 1) Ověří, zda pomůcka spadá do maximální preskripce

Pokud ne, zobrazí se upozornění:

> „Zdravotnický prostředek nespadá do úhradové skupiny 06.01.11.01 až 06.01.11.05 a nepodléhá maximální preskripci, tzn. nelze pro něj dohledat číslo schválení.“

A dál se nepokračuje.

### 2) Vyhledá číslo schválení (pokud prostředek do skupiny spadá)

#### A) Nebylo nalezeno žádné číslo

- nic se nedoplní
- ePoukaz zůstává Ke schválení

#### B) Je nalezeno jedno číslo

- nabídne se doplnění
- po potvrzení:

   - číslo se vyplní
   - stav = Nevyžaduje schválení
   - ePoukaz lze uložit jako Předepsaný

#### C) Je nalezeno více čísel

- uživatel si vybere z nabídky
- předvybrané je nejnovější

---

## **Podmínky platného čísla schválení**

Číslo je platné, pokud:

- není starší než 12 měsíců
- odpovídá 4 údajům:

   - IČZ
   - SÚKL kód
   - kód pojišťovny
   - pacient

---

## **Shrnutí**

- Tlačítko **Doplnit číslo schválení** používejte **jen** u pomůcek, kde může být maximální preskripce.
- Systém sám pozná, zda pomůcka do režimu spadá.
- Pokud existuje platné číslo → **nemusí se žádat o schválení znovu**.
- Pokud neexistuje → ePoukaz **se odesílá ke schválení**.
