---
title: "Rizika"
version: 1
updated_at: 2025-06-26
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/56918042
---

# Rizika

Okno pro správu práci rizik a intervalů prohlídek. Tato rizika se následně zadávají do jednotlivých PLS skupin. Přepočet lhůt pro pacienty s daným rizikem proběhne automaticky po editaci daného rizika.

**Rizika jsou rozdělena do tří skupin:**

1. **Kategorie**

2. **Faktory prostředí**

3. **Ohrožení zdraví**

Lze je smazat, jedině pokud nemají vytvořenou referenci (nebyly použity) Při vytváření nebo editaci uživatel pracuje se stejnou obrazovkou ve všech třech skupinách:

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/Rizika/assets/image-20250626-135127.png]]
**Mimořádná prohlídka** – aktuálně pouze informativní charakter, nepoužívá se v žádné jiné logice

**Následná prohlídka** – aktuálně pouze informativní charakter, nepoužívá se v žádné jiné logice

**Periodické prohlídky** – Interval prohlídek lze vztahovat na věk pacientů, a to zadáním věku od –  do. Věk se bere zpětně a zjišťuje se při uzavření prohlídky. Tento interval lze odstranit i v případě že již je použit (pokud se datum následující prohlídky bralo z tohoto intervalu, bude datum smazáno).

Na základě přiřazených rizik u PLS skupiny pacienta je vypočítán interval prohlídky tak, že interval prohlídky odpovídá nejkratšímu intervalu rizika.

Tento interval je zobrazen v modulu Recepce – Objednávání (viýz kap. PLS - modul objednávání a recepce).
