---
title: "Slovník pojmů"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/436273154
---

# Slovník pojmů

| **Pojem** | **Vysvětlení** |
| --- | --- |
| Balíček (nadstandardní péče) | Pojmenovaná skupina položek NP nabízená pacientům. Evidován v Galen.Balicek. |
| Sortiment | Položka zboží, materiálu nebo výkonu; typy: S (sortiment), P (prohlídka), O (očkování). Evidován v Galen.Sortiment. |
| Položka balíčku | Přiřazení sortimentu do balíčku s parametry (počet, sleva, typ účtování). Evidována v Galen.NadstandardPolozka. |
| Ceník | Cena sortimentu s platností od–do, sazbou DPH a vazbou na pracoviště. Evidován v Galen.Cenik. |
| Kategorie ceníku | Pojmenovaná skupina ceníkových záznamů pro přehledné přiřazení k položkám balíčku. Evidována v Galen.KategorieCeniku. |
| Závazek | Finanční pohledávka vůči pacientovi vzniklá vyučtováním balíčku. Evidován v Galen.Zavazek. |
| Plně hrazeno | Příznak: pacient za položku nic nedoplácí — je zahrnuta v ceně balíčku. |
| Hromadně | Příznak: položku lze vykázat pro více pacientů najednou. |
| Pracoviště | V aplikaci Galen odpovídá DB entitě Lekar. Určuje, pro které pracoviště je ceník platný. |
| PLS (Pracovnělékařské služby) | Část modulu pro evidenci a fakturaci pracovnělékařských prohlídek pro zaměstnavatele. |
| Smlouva PLS | Smluvní dohoda s firmou (zaměstnavatelem). Evidována v Galen.SmlouvaPLS. |
| Položka smlouvy PLS | Konkrétní typ prohlídky nebo sortimentu ve smlouvě s cenou, slevou, limitem a omezením. Evidována v Galen.PolozkaSmlouvyPLS. |
| Skupina PLS (Pozice PLS) | Pracovní skupina zaměstnanců u firmy s prohlídkovou povinností. Evidována v Galen.PozicePLS. |
| Akce PLS | Záznam konkrétní prohlídky s workflow stavů od plánování po fakturaci. Evidována v Galen.PLSAkce. |
| Faktura PLS | Faktura pro zaměstnavatele za realizované PLS akce. Evidována v Galen.FakturaPLS. |
| Stav akce PLS | Fáze: Nová plánovaná akce → Přiděleno dalšími IČP → Vráceno → Uzavřena fakturovat/nefakturovat → Faktura vystavena. |
| Výsledek posudku PLS | Závěr posudku po prohlídce: Z / N / K / M / D / B / X. Enumerace PLSResult. |
| Vazba položky smlouvy PLS | Způsob fakturace: Výkon (zvlášť nad paušál) nebo V paušálu smlouvy. Enumerace VazbaPLS. |
| Typ faktury PLS | Paušál (pevná cena) nebo Výkony (dle skutečnosti). Enumerace TypFakturyPLS. |
| Identifikace pacientů na faktuře | Jméno/příjmení/datum nar. nebo Osobní číslo — volí se při vystavení faktury dle dohody se zaměstnavatelem. |
| Rizika skupiny PLS | Druhy rizik (pracovní zátěž) dle § 37 zák. 373/2011 Sb. Evidována v Galen.PozicePLSRizika. |
