---
title: "Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL"
version: 5
updated_at: 2025-11-07
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/109248514
---

# Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL

> [!info]
> Tato stránka popisuje nastavení certifikátu potřebného pro komunikaci se systémem **eRecept**.
> Certifikát může být:
>
> - vydaný **SÚKLem** – není nutné jej instalovat, pouze připojit k pracovišti,
> - nebo **kvalifikovaný certifikát** vydaný jinou certifikační autoritou (např. PostSignum, [I.CA](http://I.CA)).

---

## ⚙️ Nastavení certifikátu vydaného SÚKLem

Certifikát vydaný SÚKLem není nutné instalovat.
Nastavení probíhá přímo v modulu **Správa organizace**.

---

**🔹 Postup**

> **Cesta:**
> **Správce → Správa organizace → Rozbalit strukturu → vybrat IČP**
> → v pravé části se zobrazí informace o pracovišti.

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/assets/image-20250901-085123.png]]
1. **Vyplňte pole „Kód SÚKL“**.
2. Klikněte na tlačítko **„Nastavit“**.
3. Klikněte na **„Vybrat soubor“** → vyhledejte certifikát vydaný SÚKLem → potvrďte tlačítkem **„Otevřít“**.
4. Vyplňte **heslo** k certifikátu a potvrďte tlačítkem **„OK“**.
5. Klikněte nahoře na **„Uložit“**.

✅ Pokud bylo nastavení úspěšné, v poli *Platnost* se zobrazí datum platnosti certifikátu.

---

## 💳

### 🧩 **Možnost 1 – nastavení v modulu Ordinace**

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/assets/image-20250901-084659.png]]

**Cesta:**
Ordinace → Konfigurace a nastavení → záložka Certifikát

**Postup:**

1. Klikněte na tlačítko **„Vybrat“** u pole *Certifikát (sériové číslo)*.
2. Vyhledejte certifikát → potvrďte **„OK“**.
   → Sériové číslo certifikátu se automaticky doplní.
3. V části **eRecept** doplňte údaje:

   - **Identifikace SÚKL**
   - **Heslo**
4. Potvrďte změny tlačítkem **„OK“**.
5. **Restartujte Galen** – vypněte a znovu zapněte aplikaci, aby se změny projevily.

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/assets/image-20250901-084722.png]]

### 🧩 **Možnost 2 – nastavení ve Správě organizace (uživatel)**

> **Cesta:**
> **Správce → Správa organizace → záložka Uživatelé → dvojklik na uživatele**

---

**Postup:**

1. V nastavení uživatele klikněte na **„Vybrat“** u pole *eRecept*.
2. Vyhledejte certifikát → potvrďte tlačítkem **„OK“**.
   → Sériové číslo certifikátu se automaticky doplní.
3. V části **eRecept** doplňte:

   - **Identifikace SÚKL**
   - **Heslo**
4. Potvrďte tlačítkem **„OK“**.

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/assets/image-20250901-085337.png]]

---

## 🧠 **Doporučení**

- Před výběrem certifikátu zkontrolujte, zda je **nainstalován v osobním úložišti certifikátů Windows**.
- Pokud certifikát vypršel, musí být vydán nový a nastavení zopakováno.
- Heslo k certifikátu si bezpečně uložte – bez něj nelze komunikovat se SÚKLem.

---

> [!info]
> Po změně nebo doplnění certifikátu je nutné aplikaci FONS Galen znovu spustit, aby se nový certifikát načetl.
