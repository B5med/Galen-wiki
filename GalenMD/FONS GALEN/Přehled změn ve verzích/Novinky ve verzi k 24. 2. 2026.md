---
title: "Novinky ve verzi k 24. 2. 2026"
version: 2
updated_at: 2026-02-23
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/280494081
---

# Novinky ve verzi k 24. 2. 2026

# Novinky a vylepšení

---

## Preventivní prohlídky

### Oprava zobrazení prázdných sekcí vyšetření v prohlídce

Pokud prohlídka obsahuje podmíněné zobrazení bloku a u pacienta se daný blok nezobrazí, v prohlídce se již nezobrazuje prázdná mezera. Obsah prohlídky je nyní zobrazen kompaktně bez zbytečných mezer.

## Biometrický podpis

### Úprava odesílání údajů do SignoSoft

Byla provedena úprava, aby se do systému biometrického podpisu SignoSoft neodesílalo jméno a příjmení pacienta k podpisovým polím.

# Opravy chyb

---

## Hromadné podepisování EZD

Byl optimalizován výkon při hromadném podepisování elektronické zdravotnické dokumentace (EZD).

## Upozornění – Pacient bez provozovny

Bylo opraveno chybné zobrazování upozornění „Pacient není přiřazen k žádné provozovně" u pacientů, kteří byli správně přiřazeni.

## Odesílání ukončení OČR do ČSSZ

Byla opravena chyba, kvůli které nebylo možné odeslat ukončení ošetřovného (OČR) do ČSSZ. Oprava zahrnuje korektní deserializaci neodeslaných změn a zajištění uložení odeslaného podání i v případě, kdy po odeslání dojde k výjimce v aplikaci.

## Dialog pro výběr podpisového certifikátu

Byl opraven problém, kdy dialog pro výběr podpisového certifikátu byl skrytý za původním oknem konfigurace FONS Galen. Dialog se nově zobrazuje vždy v popředí.

## Změna údajů pojištěnce

Byla opravena chyba, která se zobrazovala při změně údajů pojištěnce v případě nesprávného vyplnění formuláře.
