---
title: "Editace smlouvy"
version: 1
updated_at: 2025-06-26
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/57376772
---

# Editace smlouvy

![image-20250626-133009.png](<../../../../pages/FONS GALEN/Pracovnělékařské služby (PLS)/Smlouvy PLS/Editace smlouvy/assets/image-20250626-133009.png>)
**Nefakturovat**

Pokud je zatržen tento příznak, na dané smlouvě se negenerují faktury (ani výkonové ani paušální).

### Způsob platby

1. **Kombinovaně**

Generují se faktury s vazbou na výkon is paušální faktury

2. **Paušál**

Generují se pouze pravidelné, paušální faktury Pravidelnost určuje údaj Počet měsíců paušálu, viz níže

3. **Výkony**

Generují se pouze faktury s vazbou na výkon Tyto faktury se vytvářejí pouze zpětně! Pouze na položky s vazbou na výkon, které byly uzavřeny předchozí měsíc a dříve

### Režim platby paušálu

Nevztahuje se na faktury s vazbou na výkony

1. **Předem**

Faktura je vytvořena za aktuální měsíc vůči datu vystavení

2. **Zpětně**

Faktura je vytvořena za minulý měsíc vůči datu vystavení

**Počet měsíců paušálu**

Tento údaj určuje interval, jak často se generuje faktura paušálu Pokud nezadáno, bere se jako default 1 měsíc

**Typ paušálu**

Nevztahuje se na faktury s vazbou na výkony

1. **Jednorázový**

Faktura obsahuje cenu paušálu 1x

2. **Za 1 pacienta**

Faktura obsahuje cenu paušálu x počet hlavních (uzavřených a nevyfakturovaných) položek, bez ohledu na vazbu hlavní položky.

Příklad: Cena paušálu je 1000 Kč. Na pacientovi 1 byla vytvořena jedna PLS prohlídka (i s výsledkem "Nedostavil se"). Na pacientovi 2 byla vytvořena jedna PLS prohlídka a jedno PLS očkování. Faktura paušálu bude vystavena na 3000 Kč.

**Fakturovat stav, ”Nedostavil se”**

Nevztahuje se na paušální faktury.

**Nezatržený příznak**

Při výsledku prohlídky "Nedostavil se" se nevygeneruje žádná výkonová faktura z této prohlídky (bez ohledu jaké byly na prohlídce rozšiřující položky).

**Zatržený příznak**

% z ceny se vztahuje pouze na cenu hlavní položky.
