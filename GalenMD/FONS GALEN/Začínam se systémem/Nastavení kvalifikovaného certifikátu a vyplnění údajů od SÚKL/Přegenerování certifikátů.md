---
title: "Přegenerování certifikátů"
version: 3
updated_at: 2025-11-07
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/109215766
---

# Přegenerování certifikátů

Diagnostikovali jsme problém s některými certifikáty, který způsoboval, že při odesílání elektronického receptu docházelo k odmítnutí receptu ze strany Centrálního úložiště. To vracelo chybovou hlášku „*Byl zadán neplatný algoritmus“*.

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085524.png]]
Problém se podle všeho nachází v samotném certifikátu, který v sobě obsahuje tzv. Crypto Service Providera. Při podepisování se používá metoda definovaná daným providerem, který však v případě popisovaného problému nepodporuje algoritmus SHA256 vyžadovaný Centrálním úložištěm. (Na tuto skutečnost nás naved přímo jeden vydavatel certifikátu.)

Nejjednodušším řešením je kontaktovat vydavatele certifikátu se žádostí o přegenerování certifikátu s tzv. *Microsoft Enhanced RSA and AES Cryptographic Provider*, který SHA256 obsahuje.

Pokročilejší uživatelé mohou přegenerování provést svépomocí s využitím následujícího postupu.

## **(1) Instalace OpenSSL**

Nejprve je zapotřebí nainstalovat pomocnou utilitu zvanou OpenSSL. Tuto je možné stáhnout z webových stránek [https://slproweb.com/products/Win32OpenSSL.html](https://slproweb.com/products/Win32OpenSSL.html)

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085614.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085626.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085637.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085646.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085655.png]]
Další okna odklikat pomocí *Next*a poslední pomocí *Install*.

## **(2) Vyexportování certifikátu z úložiště**

Pomocí tlačítka *Start*na hlavním panelu Windows a vepsáním textu *certmgr.msc* a potvrzení enterem je možné zobrazit certifikáty nainstalované v úložišti.

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085737.png]]
Zde je zapotřebí vybrat certifikát, který má být opraven a ten vyexportovat.

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085818.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085827.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085839.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085849.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085900.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085909.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085917.png]]

## **(3) Potvrzení, že se jedná o popisovaný problém, s využitím OpenSSL**

OpenSSL nemá standardní grafické rozhraní, ovládá se z příkazové řádky.

Příkazovou řádku je možné spustit pomocí tlačítka *Start* na hlavním panelu Windows, vepsáním textu *cmd* a potvrzením enter.

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085939.png]]
Objeví se „černé okénko“, co kterého je nutné napsat a vždy potvrdit enterem následující příkazy:

- c:

- cd c:\OpenSSL-Win32\bin

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-085956.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090005.png]]
Dále napsat a potvrdit enterem tento příkaz:

- openssl pkcs12 -info -nodes -in puvodni.pfx

a poté, co se objeví výzva k zadání hesla (*Enter Import Password*), napsat heslo, které bylo zadáno při exportu výše.

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090019.png]]
Po úspěšném zadání hesla se zobrazí dlouhý výpis informací, podstatný je řádek začínající textem *Microsoft CSP Name.* Pokud je zde uvedeno cokoli jiného, než *Microsoft Enhanced RSA and AES Cryptographic Provider*(např. *Microsoft Enhanced Cryptographic Provider v1.0*), je třeba certifikát opravit.

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090044.png]]

## **(4) Oprava certifikátu pomocí OpenSSL**

Oprava certifikátu se provede ve stejné „černém okně“, jako předchozí diagnostika. Postupně se zadají příkazy:

- openssl pkcs12 -in puvodni.pfx -nocerts -out puvodni.key -nodes

- openssl pkcs12 -in puvodni.pfx -clcerts -nokeys -out puvodni.crt

- openssl pkcs12 -export -in puvodni.crt -inkey puvodni.key -CSP "Microsoft Enhanced RSA and AES Cryptographic Provider" -out opraveny.pfx

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090112.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090121.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090130.png]]

## **(5) Instalace opraveného certifikátu**

Opravený certifikát je nutné nainstalovat. Nachází se v adresáři *C:\OpenSSL-Win32\bin* a jmenuje se *opraveny.pfx*. Instalaci je možné pustit dvojklikem.

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090150.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090200.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090210.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090219.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090227.png]]
![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090236.png]]
Pokud instalace proběhla úspěšně, zobrazí se následující hláška

![[pages/FONS GALEN/Začínam se systémem/Nastavení kvalifikovaného certifikátu a vyplnění údajů od SÚKL/Přegenerování certifikátů/assets/image-20250901-090249.png]]

---

## 🧠 **Shrnutí**

| Krok | Popis | Výsledek |
| --- | --- | --- |
| (1) | Instalace OpenSSL | nástroj pro práci s certifikáty |
| (2) | Export původního certifikátu | soubor `puvodni.pfx` |
| (3) | Ověření CSP | zjištění problému |
| (4) | Oprava pomocí OpenSSL | vytvoření `opraveny.pfx` |
| (5) | Instalace opraveného certifikátu | funkční certifikát s SHA256 |

> [!info]
> Než provedete opravu, zálohujte původní soubor certifikátu `puvodni.pfx` i klíč `puvodni.key`.

> [!info]
> Po instalaci opraveného certifikátu je nutné aplikaci FONS Galen restartovat, aby se změny projevily.
