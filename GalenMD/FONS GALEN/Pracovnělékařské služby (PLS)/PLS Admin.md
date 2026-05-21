---
title: "PLS Admin"
version: 1
updated_at: 2025-06-26
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/57147399
---

# PLS Admin

Okno PLS Admin slouží k celkovému přehledu provedených PLS akcí, a to zadaných prohlídek a očkování, v rámci PLS.

![[pages/FONS GALEN/Pracovnělékařské služby (PLS)/PLS Admin/assets/image-20250626-134732.png]]
Výsledné zobrazení všech PLS záznamů lze filtrovat viz. Obrázek.

**Stav může nabýt hodnoty**:

o **Nová naplánovaná akce** – nově založená PLS prohlídka nebo PLS očkování

o **Přiděleno dalšími IČP** – aktuálně může nastat pouze u nehlavních položek smlouvy

o **Vráceno**– aktuálně může nastat pouze u nehlavních položek smlouvy

o **Uzavřena, fakturovat**– uzavřená služba, kde ještě neproběhla fakturace (v okně PLS Faktury)

o **Uzavřena, nefakturovat**– stav nastává, pokud je výsledek prohlídky „Nedostavil/a se, a v nastavení smlouvy není zatržen příznak o fakturování tohoto stavu

o **Faktura vystavena**– uzavřená služba, proběhla fakturace

**Cena při PLS očkování není zobrazena.**

Doplnění PLS očkování se v seznamu nezobrazuje. Uzavřené položky na prohlídce jsou označeny zelenou ikonou, viz. Obrázek výše. Při uzavřené celé prohlídce (je stanoveno datum Uzavřeno), je zobrazen také Výsledek prohlídky (té je zobrazen pouze pokud se jedná o prohlídku založenou v definici designéru jako PLS). Tyto uzavřené položky lze znovu otevřít. Při neuzavřených prohlídkách lze měnit způsob úhrady na Hotovost a opačně. Dodatečně přidané položky na prohlídce (nejsou vedeny ve smlouvě, ale byly přidány ručně na prohlídku) lze odstranit

**Zadání data příští prohlídky**

V kontextovém menu (klik pravým tlačítkem myši) nad zvoleným záznamem, je možné určit Datum příští prohlídky a také datum, odkdy je tato změna platná. K určení data je možné přidat poznámku. Tato poznámka je zobrazena okně PLS admin, v recepci a PLS aplikaci pod datem plánované prohlídky. Změna se váže na firmu, kde byl PLS záznam vytvořen

Datum příští prohlídky je možné určit i ze záznamu PLS očkování. Toto datum se však váže pouze k prohlídkám. Pokud má prohlídka určené datum příští prohlídky, toto datum je v tomto okně zobrazeno. Změna data plánované prohlídky je viditelná v modulu Recepce a v PLS aplikaci (není viditelná v samotné prohlídce). Za datem je označení "(určeno správcem)". Datum má platnost pouze v případě že datum Platnost ke dni > datum poslední PLS OL prohlídky, nebo datum z importu.
