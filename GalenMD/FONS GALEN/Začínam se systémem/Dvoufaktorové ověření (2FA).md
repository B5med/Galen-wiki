---
title: "Dvoufaktorové ověření (2FA)"
version: 5
updated_at: 2025-11-07
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/103415835
---

> [!info]
> Dvoufaktorové ověření (2FA) zvyšuje bezpečnost přihlášení do systému **FONS Galen**.
> Po aktivaci musí uživatel při přihlášení kromě hesla zadat i ověřovací kód z autentizační aplikace, např. **Microsoft Authenticator**.

> [!warning]
> *Pro správnou funkčnost 2FA musí mít uživatel nainstalovanou a aktivní autentizační aplikaci.*

## 🧭  Přehled oblastí

| **Oblast** | **Role** | **Popis** |
| --- | --- | --- |
| Správa organizace | Správce | Nastavení rozsahu a frekvence 2FA, možnost deaktivace |
| Ordinace | Uživatel | Propojení aplikace Authenticator, ověření a přihlášení |
| Přihlášení | Všichni uživatelé | Zadání kódu při startu aplikace FONS Galen |

---

## ⚙️ Konfigurace v modulu Správa organizace

**Cesta:**
Správce → Správa organizace → vybrat *Společnost* → **Konfigurace** → záložka **Konfigurace** → část *Dvoufaktorové ověření*

### 🔸 Stanovení rozsahu

Správce může určit, pro které uživatele bude 2FA vyžadováno:

- **Všichni aktivní uživatelé** – 2FA je povinné pro všechny.
- **Vybraní uživatelé** – možnost určit konkrétní uživatele.

Nad seznamem lze filtrovat podle **pracoviště** nebo **role**.
Výběr potvrďte tlačítkem **OK**.

### 🔸 Frekvence dvoufaktorového ověření

Správce může určit, jak často bude 2FA požadováno:

- **Při každém přihlášení** – ověření se vyžaduje při každém startu aplikace.
- **Poprvé na daném PC v daný den** – ověření proběhne pouze při prvním přihlášení v daný den na konkrétním zařízení.

### 🔸 Deaktivace aplikace správcem

V případě ztráty mobilního zařízení může správce deaktivovat 2FA daného uživatele.

> **Cesta:**
> Správce → Správa organizace → záložka **Uživatelé** → vybrat uživatele → část **Autentizační aplikace** → tlačítko **Smazat**

Po deaktivaci bude uživatel při dalším přihlášení vyzván k novému nastavení autentizační aplikace.

![[pages/FONS GALEN/Začínam se systémem/Dvoufaktorové ověření (2FA)/assets/image-20250825-100054.png]]

---

## 👤

> **Cesta:**
> Vybrat pracoviště → Ordinace → **Konfigurace a nastavení** → záložka **Zabezpečení** → část *Autentizační aplikace* → tlačítko **Nastavit**

Pokud autentizační aplikace není nastavena, klikněte na **Nastavit** a spusťte průvodce.

### 🔹 Stažení a instalace aplikace Microsoft Authenticator

1. Stáhněte **Microsoft Authenticator** z Google Play nebo App Store.
2. Spusťte aplikaci a připravte ji k naskenování QR kódu.

![[pages/FONS GALEN/Začínam se systémem/Dvoufaktorové ověření (2FA)/assets/image-20250825-100131.png]]

### 🔹

V průvodci nastavením v Galenovi naskenujte QR kód zobrazený na obrazovce pomocí aplikace **Microsoft Authenticator**.

![[pages/FONS GALEN/Začínam se systémem/Dvoufaktorové ověření (2FA)/assets/image-20250825-100152.png]]

### 🔹

Aplikace vygeneruje šestimístný kód. Tento kód zadejte a potvrďte.

![[pages/FONS GALEN/Začínam se systémem/Dvoufaktorové ověření (2FA)/assets/image-20250825-100213.png]]
**Chybné ověření:**
Pokud je kód neplatný, zobrazí se hlášení:

> „Ověření neproběhlo úspěšně. Opište nový kód.“

Zadejte nový kód z aplikace.

### 🔹

Po úspěšném ověření klikněte na **Uložit**.
Nastavení je tím dokončeno.

![[pages/FONS GALEN/Začínam se systémem/Dvoufaktorové ověření (2FA)/assets/image-20250825-100314.png]]

### 🔹

Doporučujeme aktivovat **zálohování účtu** v aplikaci Microsoft Authenticator, abyste mohli 2FA snadno obnovit v případě ztráty nebo výměny telefonu.

![[pages/FONS GALEN/Začínam se systémem/Dvoufaktorové ověření (2FA)/assets/image-20250825-100342.png]]

### 🔹

Pro opětovní nastavení autentizační aplikace je možné proces znovu vyvolat a to za pomocí tlačítka **Změnit**. Za pomocí tlačítka **Smazat** lze nastavení smazat.

![[pages/FONS GALEN/Začínam se systémem/Dvoufaktorové ověření (2FA)/assets/image-20250825-100412.png]]

## 🔑

Pokud uživatel dosud 2FA nenastavil, může být po přihlášení k tomuto kroku vyzván.

1. Na přihlašovací stránce vyplňte jméno a heslo.
2. Potvrďte tlačítkem **Přihlášení do aplikace**.
3. Zobrazí se průvodce nastavením 2FA (viz kroky „Stažení a instalace aplikace“ až „Záloha“).

## 🚪 Přihlášení s 2FA

1. Spusťte FONS Galen.
2. Zadejte uživatelské jméno a heslo.
3. Opište kód z autentizační aplikace a klikněte na **Přihlášení do aplikace**.

Uživatel je po úspěšném ověření přihlášen.

## 🔄 Dva způsoby ověření

Pokud má uživatel aktivní **dva způsoby ověření** (např. SMS a autentizační aplikaci), může po zadání přihlašovacích údajů kliknout na:

> **„Vybrat jiný způsob dvoufaktorového ověření“**

a zvolit preferovanou metodu.

![[pages/FONS GALEN/Začínam se systémem/Dvoufaktorové ověření (2FA)/assets/image-20250825-100505.png]]
![[pages/FONS GALEN/Začínam se systémem/Dvoufaktorové ověření (2FA)/assets/image-20250825-100513.png]]
