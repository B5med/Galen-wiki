---
title: "Externí přístup"
version: 3
updated_at: 2026-10-01
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/616202241
---

# Externí přístup

# Konfigurace

Konfigurace se provádí přes aplikaci *Galen*

Správce -> Správa organizace -> Agendy -> Externí přístup

Pokud přístup není ještě vytvořen, tak se může vytvořit nový přes tlačítko, popřípadě upravit existující. Pokud by měl někdo pod jedním počítačem registrováno více portů. Tak se vždy bere ten první vytvořený v databázi.

![image-20260313-093618.png](<../../../pages/FONS GALEN/Správce a nastavení/Externí přístup/assets/9cc991ba-c289-44aa-97f8-4df31a1ba848>)
Při vytváření je potřeba definovat počítač, nastavit port (je potřeba zvolit takový, který není ještě používán v rámci *Windows*) a zvolit typy přístupu, které budou zpřístupněny.

![image-20260313-120549.png](<../../../pages/FONS GALEN/Správce a nastavení/Externí přístup/assets/27f09fe1-b29b-4d5e-94c8-7534b1fb3e5c>)
Pro přístup je potřeba i klíč, který se dá vygenerovat pomocí tlačítka.

![image-20260313-120326.png](<../../../pages/FONS GALEN/Správce a nastavení/Externí přístup/assets/image-20260313-120326.png>)

# Registrace adresy

Kvůli bezpečnostnímu omezení *Windows*, musí aplikace pro poslouchání dostat povolení nebo by aplikace musela být zapnutá jako administrátor. Povolení je možné udělat pomocí příkazového řádku. Je potřeba tedy na počítači zapnout příkazový řádek jako administrátor.
Adresa běží na *localhostu*, ke kterému je potřeba dopsat nastavený port z konfigurace (v mém případě 80). Zpřístupnění všem uživatelům je možné pomocí příkazu:

> [!abstract]
> ```
> netsh http add urlacl url=http://localhost:80/ user=Everyone
> ```

Popřípadě konkrétnímu uživateli:

> [!abstract]
> ```
> netsh http add urlacl url=http://localhost:80/ user=DOMAIN\Username
> ```

Pro zjištění informace kdo jsem, je možné použít příkaz:

> [!abstract]
> ```
> whoami
> ```

![image-20260313-094459.png](<../../../pages/FONS GALEN/Správce a nastavení/Externí přístup/assets/3f8f3808-467e-45fe-85f7-6fb485df86e5>)
Kdybych chtěl zrušit registrovanou adresu, tak přes příkaz:

> [!abstract]
> ```
> netsh http delete urlacl url=http://localhost:80/
> ```

# Testování

Funkci je možné otestovat několika způsoby, asi nejjednodušší je z webového prohlížeče pomocí *WebSocket API*.

Stačí zapnout prohlížeč a otevřít si *DevTools* přes *F12*.

![image-20260313-095425.png](<../../../pages/FONS GALEN/Správce a nastavení/Externí přístup/assets/image-20260313-095425.png>)
Pro otevření *DevTools* je potřeba se v tomto panelu přepnout dole do záložky *Console*, kde je možné psát příkazy.

Je možné, že do *Console* nebude možné vkládat kód přes *CTRL+V*, takže bych doporučil si tuto možnost zpřístupnit napsáním do *Console* (pokud bylo vkládání již povoleno, tak vypisuje chybu):

> [!abstract]
> ```
> allow pasting
> ```

*WebSocket* připojení není možné psát nad otevřenou webovou stránkou (z bezpečnostních důvodů). Je tedy potřeba se přepnou mimo konkrétní webovou stránku, například zadat do adresního řádku prohlížeče:

> [!abstract]
> ```
> about:blank
> ```

Tím dojde k otevření prázdné stránky, kde nejsou bezpečnostní omezení a je možné vytvořit spojení. Spojení s aplikací může vypadat například takto s informacemi o spojení (je potřeba zde nastavit port z konfigurace):

> [!abstract]
> ```
> const ws = new WebSocket("ws://localhost:80");
> ws.onopen = () => console.log("Připojeno!");
> ws.onmessage = (e) => console.log("Odpověď:", e.data);
> ws.onclose = () => console.log("Odpojeno");
> ```

![image-20260313-100002.png](<../../../pages/FONS GALEN/Správce a nastavení/Externí přístup/assets/image-20260313-100002.png>)
Odeslání požadavku pak může vypadat takto:

> [!abstract]
> ```
> ws.send(JSON.stringify({
>     Id: "245",
>     Authorization: "2Hah0FF/3gj7sfAP855oTZTqEpNzliMw",
>     Method: "OpenPatientClinic",
>     PatientNumber: "435717097"
> }));
> ```

*Authorization* je vygenerovaný token z konfigurace, *Method* je název volané funkce, v aktuální implementaci aplikace Galen podporuje pouze *OpenPatient* a *OpenPatientClinic*. Obě tyto funkce pracují s *PatientNumber*, kde je rodné číslo pacienta, pro kterého se provádí objednání (pro *OpenPatient*) nebo jehož karta se má zobrazit (pro *OpenPatientClinic*). Identifikátor *Id* slouží pouze ke svázání odpovědi s požadavkem, může zde být nastaven libovolný text, popřípadě se nemusí vyplňovat. Aplikace *Galen* s tímto *Id* nijak nepracuje.

Při odeslání požadavku dojde k obdržení odpovědi:

![image-20260313-103019.png](<../../../pages/FONS GALEN/Správce a nastavení/Externí přístup/assets/image-20260313-103019.png>)
