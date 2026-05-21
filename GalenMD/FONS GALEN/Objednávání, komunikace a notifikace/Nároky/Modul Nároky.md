---
title: "Modul Nároky"
version: 2
updated_at: 2025-07-10
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/68517948
---

Pokud uživatel do modulu přistupuje v rámci pracoviště, vidí pouze aktivní nároky.

Pokud uživatel do modulu vstupuje jako Správce, vidí všechny nároky ve všech stavech.

Nároky na vyšetření nemají platnost do, nemají tedy určené datum, do kdy je nutné je splnit.

V tomto modulu by měl mít uživatel možnost zobrazit odpovědi na tyto otázky:

- Kteří pacienti mají v určitém období na nějaký nárok.
- Ke kterým nárokům již existuje nebo ještě neexistuje objednávka (budoucí i minulá).
- Zda byl pacient již osloven, případně kolikrát
- V modulu je možné pacienta na vyšetření objednat nebo jej oslovit pomocí SMS/e-mailu.

### Funkční tlačítka modulu pro roli Správce

Po označení alespoň jednoho nároku se zobrazí tlačítka. Tlačítka jsou aktivní v závislosti na stavu označeného nároku.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Modul Nároky/assets/image-20250710-123754.png]]
- ***Zelené tlačítko plus*** umožňuje vytvořit nový nárok zkopírováním údajů označeného nároku s možností editace údajů.
- ***Modré tlačítko*****pro editaci** umožňuje editovat údaje označeného nároku.
- ***Červené tlačítko mínus*** smaže vybraný/é nárok/y.
- ***Oslovit*** umožňuje odeslat SMS a/nebo e-mail pacientovi. V okně je, kromě volně vloženého textu, možné využít přednastavenou šablonu, viz. kapitola Šablony notifikací. Pacient je v rámci oslovení osloven pouze na vybraný nárok, tzn. pokud má pacient tři nároky a je osloven pouze v rámci jednoho nároku, u ostatních nároků se datum oslovení pacienta nepropíše. Po oslovení pacienta se datum odeslání SMS zobrazí v pravém sloupci po označení daného nároku.
- ***Již neoslovovat:***Tento stav uživatel zvolí ve chvíli, kdy už pacienta nechce oslovovat, např. ve chvíli, kdy je pacient již objednán.
- ***Zpět oslovovat*** umožňuje nárok opět aktivovat, tzn. vrátit zpět do množiny nároků, které budou oslovovány v rámci hromadných notifikací.
- ***Pozastavit:***Tento stav Správce zvolí ve chvíli, kdy ví, že pacient prohlídku absolvuje později. Po dobu, kdy bude nárok pozastaven, nebude pacient oslovován v rámci hromadných notifikací. Ze stavu Pozastavený se nárok dostane pouze manuální změnou stavu.
- ***Aktivovat*** umožňuje opět aktivovat pozastavený nárok.
- ***Objednat***zobrazí kalendář pro zadání objednávky pacienta s tím, že vznikne vazba mezi nárokem a objednávkou. V objednávce lze případně zaškrtnout i další nároky, které budou v rámci objednávky splněny. Informace o tom, že je pacient na vyšetření již objednán, je zobrazena v pravém sloupci po označení konkrétního nároku.
- ***Splnit***umožňuje zadat vazbu k již provedeným vyšetřením a očkováním a tím nárok splnit.

### Funkční tlačítka modulu pro roli *Zdravotník*

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Modul Nároky/assets/image-20250710-124100.png]]
Funkčnost tlačítek je shodná s tlačítky v modulu pro roli správce.

### Vytváření objednávek

Při vytváření objednávky (ve standardním modulu *Objednávání*) je detail vytvářené objednávky rozšířen o seznam nároků pacienta, které jsou ke dni objednávky aktivní a ke kterým ještě neexistuje objednávka do budoucnosti. Budou se tedy zobrazovat i nároky, ke kterým existuje objednávka v minulosti, za předpokladu, že tyto nároky budou stále aktivní.

V tomto seznamu má uživatel možnost vyznačit, které nároky mají být v rámci objednané návštěvy vyřízené.

V případě, že je kalendář zobrazen z modulu *Nároky pacienta* pomocí tlačítka *Objednat*, bude v okamžiku přechodu na kalendář kontextově vybrán pacient z daného nároku.

### Vytvoření vazby objednávka – nárok

Při oslovování pacientů je pro uživatele důležitá informace, zda již je pacient na dané vyšetření objednán. Proto je nutné, aby Správce nastavil v jednotlivých objednávkách vazbu mezi konkrétním objednávkou a nárokem, který daným ošetřením pacienta bude splněn.

Správa organizace – Agendy – Kalendáře – Objednávky

Po rozkliknutí konkrétního typu objednávky uživatel vytvoří vazbu na nárok(y) zaškrtnutím checkboxu *Nároky*.  Pokud vyšetření pacienta splní nárok na prohlídku, pak uživatel volí typ nároku „Vyšetření“ a jako podtyp vybere název prohlídky.

![[pages/FONS GALEN/Objednávání, komunikace a notifikace/Nároky/Modul Nároky/assets/image-20250710-124134.png]]
