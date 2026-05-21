---
title: "Online objednávání pacientů"
version: 1
updated_at: 2026-01-19
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/230031362
---

# Online objednávání pacientů

> [!info]
> Online objednávání umožňuje pacientům objednat se na vyšetření nebo výkon **přes Portál pacienta**, aniž by museli volat do ordinace.

> [!info]
> Objednávky se automaticky zapisují do **kalendáře v AIS FONS Galen**, kde s nimi zdravotnický personál pracuje stejně jako s běžnými objednávkami.

---

## Kdo s funkcí pracuje

| Role | Co dělá |
| --- | --- |
| Pacient | Vytváří, ruší nebo sleduje objednávku |
| Recepce / sestra | Vidí a spravuje objednávky v kalendáři |
| Lékař | Pracuje s objednávkou v Galenu |
| Správce | Nastavuje kalendáře, ordinační dobu a pravidla |

---

## Konfigurace

Online objednávání **nefunguje automaticky**. Je nutné provést správné nastavení v Galenu.

### 1️⃣ Nastavení kalendáře

V Galenu otevřete:

**Správce → Správa organizace → Agendy → Kalendáře**

U kalendáře musí být:

- ✔️ **Aktivní**
- ✔️ **Veřejný**
- ✔️ **Vyplněné odpovědné pracoviště**

⚠️ Pokud není vyplněno odpovědné pracoviště, **nelze kalendář označit jako veřejný**.

---

### 2️⃣ Nastavení ordinačních hodin

Online objednávání funguje **pouze v ordinačních hodinách**, které mají povoleno veřejné objednávání.

U každého bloku ordinační doby:

- zaškrtnout **Veřejný**
- vybrat **povolené typy objednávek**

Bez tohoto nastavení se pacient **na daný termín neobjedná**, i když je kalendář veřejný.

---

### 3️⃣ Nastavení typů objednávek

Typy objednávek určují:

- na co se pacient může objednat
- jak dlouho objednávka trvá

U typu objednávky se nastavuje:

- název (např. „Preventivní prohlídka“)
- délka trvání
- minutový interval

Pacient vidí **pouze ty typy objednávek**, které jsou:

- povoleny v kalendáři
- povoleny v ordinační době

---

## Jak probíhá objednání z pohledu pacienta

1. Pacient otevře Portál pacienta
2. Vybere provozovnu (ordinaci)
3. Vybere kalendář
4. Vybere typ vyšetření
5. Vybere volný termín
6. Vyplní své údaje
7. Odešle objednávku

Po odeslání:

- objednávka se zobrazí v kalendáři Galenu
- pacient obdrží potvrzení (SMS / e-mail – dle nastavení)

---

## Jak se objednávka zobrazí v Galenu

Objednávka se v Galenu objeví jako:

### ✔️ Objednávka pacienta

Pokud se podaří pacienta jednoznačně identifikovat.

### ✔️ Záznam v kalendáři

Pokud pacienta nelze spárovat s kartotékou (např. nový pacient).

Obě varianty jsou **plnohodnotně viditelné a editovatelné** v kalendáři.

---

## Změna nebo zrušení objednávky

Změnu nebo zrušení může provést:

- pacient (přes Portál pacienta – pokud je povoleno)
- personál v Galenu

Možnost změn závisí na nastavení:

- **Uzavření rezervací předem (v hodinách)**

Po překročení tohoto času:

- objednávku nelze měnit
- nelze ji zrušit

---

## Notifikace pacientovi

Portál pacienta umožňuje automatické notifikace:

- potvrzení objednávky
- změna objednávky
- zrušení objednávky
- připomenutí před termínem

Notifikace se nastavují:
**Správce → Kalendáře → Notifikace a připomínání**

Kanály:

- SMS
- e-mail

Každý kalendář (a dokonce každá ordinační doba) může mít **vlastní nastavení**.

---

## Nejčastější problémy a jejich příčina

| Problém | Pravděpodobná příčina |
| --- | --- |
| Pacient nevidí kalendář | Kalendář není veřejný |
| Pacient nevidí termíny | Ordinační doba není veřejná |
| Pacient nevidí typ objednávky | Typ není povolen |
| Nelze zrušit objednávku | Je po uzávěrce rezervací |

---

## Doporučení pro správce

✔️ Začněte s **jednoduchým kalendářem**
✔️ Omezte počet typů objednávek
✔️ Nastavte připomenutí objednávek
✔️ Pravidelně kontrolujte kalendář po nasazení

---

## Související funkce

- Hlídací pes (upozornění na volný termín)
- Moje rezervace
- Notifikace
- Nastavení kalendářů

---

> [!tip]
> **Online objednávání:**
>
> - šetří čas personálu
> - snižuje počet telefonátů
> - funguje při správném nastavení kalendářů
> - je plně pod kontrolou ordinace
