---
title: "Editace vyšetření různými odpovědnými lékaři"
version: 1
updated_at: 2025-09-03
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/111017986
---

Modul Vyšetření byl rozšířen o možnost, aby jedno vyšetření (prohlídku) mohlo doplnit více odpovědných lékařů ze stejného pracoviště. Jedná se tak o jedno vyšetření pacienta, na kterém pracuje více lékařů stejného pracoviště (např. ve chvíli, kdy lékař vyplňuje pouze část prohlídky), většinou během několika dní.

## Výchozí stav

Dosud bylo možné, aby je jedno vyšetření editoval pouze jeho autor, nebo sestra (tzn. uživatel, který není odpovědným lékařem). Jiný lékař (uživatel, který je odpovědným lékařem, tzn. při vstupu na pracoviště se nepřihlašuje na jiného odpovědného lékaře) vyšetření nemohl doplnit, editovat.

## Aktuální stav

Nyní je možné, aby jiný odpovědný lékař na stejném pracovišti doplnil vyšetření, které bylo zadáno jiným lékařem. Vytvoří se tak řetězec na sebe navazujících prohlídek, kdy nejnovější prohlídka vychází z prohlídky předcházející.

### Vytvoření prvního vyšetření

První odpovědný lékař vyplní vyšetření stejně jako obvykle. Z vyšetření je možné podle potřeby vytvořit navazující formulář, vykázat výkon, nebo vyšetření uzamknout a podepsat v rámci EZD.

### Vytvoření nového hlavního vyšetření a podzáznamu

Jiný odpovědný lékař ze stejného pracoviště najde vyšetření a stiskne tlačítko Doplnit záznam.

![[pages/FONS GALEN/Vyšetření, dekurz a klinická péče/Editace vyšetření různými odpovědnými lékaři/assets/image-20250903-100634.png]]

Po stisknutí tlačítka Doplnit záznam se vytvoří kopie původní prohlídky: Do záznamu se přenesou všechny informace z původní prohlídky a záznam se stane editovatelným. Zároveň se záznam původního odpovědného lékaře stane tzv. podzáznamem. To znamená, že na vyšetření prvního odpovědného lékaře navazuje záznam dalšího odpovědného lékaře. Nejnovější prohlídka je vždy hlavní prohlídkou, podzáznamy (tzn. předcházející prohlídky, ze kterých hlavní nejnovější prohlídka vychází) je možné zobrazit tlačítkem ▼

![[pages/FONS GALEN/Vyšetření, dekurz a klinická péče/Editace vyšetření různými odpovědnými lékaři/assets/image-20250903-100814.png]]

### Editace a mazání

Tlačítko Doplnit záznam vidí pouze jiný odpovědný lékař. To znamená, že uživatel, který původní záznam vytvořil, nemůže záznam doplnit, musí editovat stávající záznam.

Sestra (tzn. uživatel, který není odpovědným lékařem) může editovat původní záznam (změna bude provedena pod odpovědným lékařem, který původní záznam vytvořil), nebo doplnit záznam a vytvořit tak novou hlavní prohlídku, která bude jako záznam odpovědného lékaře, na kterého je sestra aktuálně přihlášena.

Z nově vzniklé hlavní prohlídky je možné opět vytvořit navazující formulář. Výkon lze z prohlídky vykázat pouze jeden za den, tzn. pokud nová hlavní prohlídka vznikne ten stejný den, není již možné z ní výkon vykázat.

Pokud se hlavní prohlídka stane podzáznamem, tzn. na jejím základě vznikla novější prohlídka, která z ní vychází, není možné tuto předcházející prohlídku smazat (ani uživatelem, který původní prohlídku vytvořil). Podzáznam je možné pouze uzamknout a podepsat v rámci EZD. Podzáznam také není možné editovat (ani uživatelem, který původní prohlídku vytvořil). Pokud uživatel potřebuje doplnit prohlídku, musí doplnit hlavní, tzn. nejnovější prohlídku.

Pokud je však smazána hlavní prohlídka (oprávnění mazat prohlídku odpovídá již existujícím pravidlům mazání a editace záznamů), stává se podzáznam opět hlavní prohlídkou.

### PLS prohlídka

Jediným rozdílem PLS prohlídek je, že tlačítko Doplnit záznam není dostupné ve chvíli, kdy na poslední prohlídce uzavře položku smlouvy, která je hlavní prohlídkou. V tu chvíli ostatní lékaři nevidí na prohlídce tlačítko Doplnit záznam.
