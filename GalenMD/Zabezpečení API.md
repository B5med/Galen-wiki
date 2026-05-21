---
title: "Zabezpečení API"
version: 1
updated_at: 2026-04-02
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/332693505
---

# Zabezpečení API

> [!info]
> Tento manuál popisuje novou možnost zabezpečení API přístupu pomocí klientského certifikátu. Poskytuje podrobný postup nastavení a porovnání se stávajícím tokenovým přístupem.

## Přehled a přínosy certifikátového zabezpečení

- Vyšší úroveň bezpečnosti: ověření identity probíhá na úrovni TLS (mTLS), čímž snižuje riziko kompromitace přístupových tajemství oproti samotným tokenům.
- Silná autentizace infrastruktury: vazba na privátní klíč v HSM/TPM a správu certifikátů pod centrální PKI.
- Granulární kontrola: možnost kombinovat s omezením na povolené IP adresy a platností certifikátů.

> [!abstract]
> Certifikátové zabezpečení je vhodné pro organizace vyžadující silnou autentizaci. Tokenový přístup zůstává podporovanou a výchozí metodou.

## Kde nastavení najdete

Nastavení API přístupu je dostupné v cestě: **Správa organizace → Agendy → Správa API**. Po otevření formuláře konkrétního API přístupu je k dispozici položka **Způsob zabezpečení**.

## Výběr způsobu zabezpečení

V rozbalovacím seznamu **Způsob zabezpečení** zvolte jednu z možností:

- Token – stávající metoda zabezpečení (výchozí nastavení).
- Certifikát – nová metoda zabezpečení pomocí klientského certifikátu.

> [!tip]
> Výchozí hodnota je Token. Pokud způsob zabezpečení neměníte, není třeba provádět žádné úpravy.

## Zabezpečení pomocí tokenu

Při zvolení možnosti Token se zobrazí standardní položky:

- Klíč – vygenerovaný přístupový token.
- Datum vygenerování – datum vytvoření tokenu.
- Platnost do – datum vypršení platnosti tokenu.
- Jen povolené IP adresy – omezení přístupu na vybrané IP adresy.

Chování tlačítka **Přegenerovat**: Tlačítko je viditelné pouze pro přístupy se způsobem zabezpečení Token. U certifikátového zabezpečení se nezobrazuje.

## Zabezpečení pomocí certifikátu

### Zobrazené položky

- Certifikát – pole zobrazující nahraný certifikát.
- Datum vygenerování  – datum nahrání certifikátu.
- Platnost do – datum vypršení platnosti certifikátu.
- Tlačítko Nastavit – slouží k nahrání certifikátu.
- Jen povolené IP adresy – omezení přístupu na vybrané IP adresy.

### Nahrání certifikátu – postup

1. Klikněte na tlačítko Nastavit.
2. V systémovém dialogu Windows zvolte certifikát určený pro klientskou autentizaci (Client Authentication, mTLS).
3. Potvrďte výběr. Systém nahraje certifikát a zobrazí jeho identifikaci a datum platnosti.

![[pages/Zabezpečení API/assets/image-20260402-070835.png]]
> [!abstract]
> Doporučení: Pro zabezpečení API doporučujeme použít certifikát DigiCert X9 PKI TLS splňující požadavky na bezpečnost a kompatibilitu se systémem.

## Upozornění na expiraci certifikátu

- Blížící se konec platnosti – systém zobrazí upozornění s dostatečným předstihem pro obnovu.
- Expirovaný certifikát – systém informuje správce o nutnosti výměny.

Mechanismus vychází ze stávající kontroly expirací certifikátů v systému.
