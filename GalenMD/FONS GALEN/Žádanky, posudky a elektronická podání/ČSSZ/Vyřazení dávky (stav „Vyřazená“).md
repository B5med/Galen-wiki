---
title: "Vyřazení dávky (stav „Vyřazená“)"
version: 3
updated_at: 2026-07-29
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/518717444
---

# Vyřazení dávky (stav „Vyřazená“)

Stav **„Vyřazená“** je interní stav systému FONS Galen, kterým lze označit neschopenku, ošetřovné nebo dlouhodobé ošetřovné, jež ČSSZ ve svém systému neeviduje. Do tohoto stavu převádí dávku uživatel ručně; slouží k tomu, aby dávky bez protějšku na straně ČSSZ nezatěžovaly běžné přehledy, ale zůstaly dohledatelné.

> [!abstract]
> Stav **„Vyřazená“** je pouze interní stav systému FONS Galen. Jeho použití nemění evidenci na straně ČSSZ.

# Chování stavu „Vyřazená“

Dávka ve stavu **„Vyřazená“** se chová stejně jako dávka ve stavu **Ukončená**.

- Nezobrazuje se v dlaždici pacienta.
- Nezobrazuje se v přehledu neodeslaných lístků na peníze.
- Není aktivní pro další zpracování; k vyřazené dávce není možné odesílat podání na ČSSZ.

# Vyřazení dávky

Do stavu **„Vyřazená“** lze dávku převést **pouze ručně**.

1. V přehledu dávek klikněte pravým tlačítkem myši na konkrétní dávku.
2. V kontextovém menu zvolte možnost **Změnit stav na Vyřazená**.

![image-20260729-095954.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Vyřazení dávky (stav „Vyřazená“)/assets/image-20260729-095954.png>)
3. Systém zobrazí dotaz **„Změnit stav dávky na Vyřazená?“**. V dialogu lze vyplnit nepovinnou **poznámku k vyřazení**.

![image-20260729-100029.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Vyřazení dávky (stav „Vyřazená“)/assets/image-20260729-100029.png>)
4. Po potvrzení se stav okamžitě aktualizuje.

# Obnovení původního stavu

Dávku lze ze stavu **„Vyřazená“** vrátit do původního stavu, například **Otevřená** nebo **Ukončená**, dvěma způsoby. V obou případech jde pouze o interní změnu; obnovením se **neaktivuje** opětovné odesílání dat na ČSSZ.

## Ručně uživatelem

Klikněte pravým tlačítkem myši na dávku a zvolte **Obnovit původní stav**. Tato volba je v kontextovém menu viditelná pouze tehdy, je-li dávka ve stavu **„Vyřazená“**. Systém zobrazí dotaz **„Obnovit původní stav dávky?“**, v němž lze vyplnit nepovinnou **poznámku k obnovení**.

![image-20260729-100140.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Vyřazení dávky (stav „Vyřazená“)/assets/image-20260729-100140.png>)
![image-20260729-100516.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Vyřazení dávky (stav „Vyřazená“)/assets/image-20260729-100516.png>)

## Automaticky systémem

Systém vrátí dávku do původního stavu ve chvíli, kdy k ní přijde notifikace z ČSSZ. Současně s obnovením stavu se přijatá notifikace zpracuje.

> [!warning]
> Obnovení původního stavu neznamená automatické znovuzapojení dávky do odesílání na ČSSZ. Jde pouze o interní změnu stavu v systému.

# Historie vyřazení

Každá změna stavu, tedy vyřazení i obnovení, se zaznamenává do samostatné evidence **Historie vyřazení**, kterou si uživatel může zobrazit na detailu dávky.

U každého záznamu je uveden:

- **zdroj změny** – zda ji provedl *Uživatel*, nebo *Notifikace ČSSZ* při automatickém obnovení,
- **poznámka** zadaná při vyřazení nebo obnovení,
- datum změny a uživatel, který ji provedl.

![image-20260729-100321.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Vyřazení dávky (stav „Vyřazená“)/assets/image-20260729-100321.png>)

# Filtrování vyřazených dávek

Vyřazené dávky jsou ve výchozím stavu skryté. Zobrazíte je pomocí checkboxu **Vyřazené**.

![image-20260729-100421.png](<../../../../pages/FONS GALEN/Žádanky, posudky a elektronická podání/ČSSZ/Vyřazení dávky (stav „Vyřazená“)/assets/image-20260729-100421.png>)

| Oblast | Umístění filtru | Chování |
| --- | --- | --- |
| Přehledy dávek ČSSZ | Checkbox **Vyřazené** je součástí filtru dávek. | Po zatržení se v přehledu zobrazí i dávky ve stavu **„Vyřazená“**. |
| Historie pacienta, sekce ČSSZ | Checkbox **Vyřazené** je v hlavní liště za checkboxem **Ukončené**. | Po zatržení se v přehledu zobrazí i dávky ve stavu **„Vyřazená“**. |

V obou případech je výchozí stav checkboxu nezatržený, takže se vyřazené dávky standardně nezobrazují. Filtr zároveň funguje v kombinaci s ostatními filtry.

> [!info]
> Pokud hledáte dávku, která se standardně nezobrazuje v přehledech, nejprve ověřte, zda není zapotřebí zapnout filtr **Vyřazené**.
