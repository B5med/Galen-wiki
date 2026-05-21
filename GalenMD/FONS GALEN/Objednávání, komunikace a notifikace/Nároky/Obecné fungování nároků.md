---
title: "Obecné fungování nároků"
version: 1
updated_at: 2025-07-10
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/68091907
---

# Obecné fungování nároků

Nárok pacienta na vyšetření je datum, ke kterému by měl pacient absolvovat další vyšetření.  Nárok na prohlídku vzniká ve chvíli, kdy pacient absolvuje vyšetření a z tohoto vyšetření je vykázán výkon. Dalšími způsoby je vznik nároku při registraci pacienta, noční kontrolou věku pacienta, nebo hromadně tlačítkem v konfiguraci nároků. Vzniknutý nárok uživatel vidí v historii pacienta nebo v modulu Nároky (v případě, kdy má uživatel tento modul přístupný). V tomto modulu je dále možné nastavit automatické notifikace nebo přímo osloví konkrétního pacienta s informací, že by se pacient měl na dané vyšetření objednat. Každý pacient může mít 1 okamžik jenom 1 aktívní nebo budoucí nárok.

### Kroky potřebné ke zprovoznění funkcionality

a.      Zpřístupnění modulu Nároky ze strany STAPRO (v rámci placené funkcionality).

b.     Vytvoření definice nároku z vyšetření, jakým způsobem má být datum příštího nároku vypočítáno. Tato definice je specifická pro každou prohlídku a definuje se v modulu Nároky.

c.      Správce společnosti zpřístupní modul Nároky uživatelům, kteří s nároky budou pracovat.

d.     Vytvoření šablony notifikací.

e.      Odesílání notifikací pacientům s informací, že mají nárok na vyšetření, na které by se měli objednat.

Další funkcionality: odesílání SMS z aplikace (nadstandardní funkcionalita aktivovaná ze strany STAPRO).
