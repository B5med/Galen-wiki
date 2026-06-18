---
title: "FAQ — Časté otázky"
version: 1
updated_at: 2026-06-17
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/436011024
---

# FAQ — Časté otázky

## Často kladené otázky

1. **Co je to balíček nadstandardní péče?**

Balíček je pojmenovaná skupina položek (sortiment, prohlídky, očkování) nehrazených zdravotní pojišťovnou, nabízená pacientům jako soubor nadstandardních služeb za definovanou cenu.

---

2. **Mohu do jednoho balíčku přidat různé typy položek?**

Ano. Jeden balíček může kombinovat Sortiment, Prohlídku i Očkování. Typ se volí při přidávání každé položky zvlášť.

---

3. **Nemám přístup k modulu Nadstandardní péče — co mám dělat?**

Přístup závisí na nastavení role Vašeho uživatelského účtu. Kontaktujte správce systému Vaší ordinace a požádejte o přidělení příslušného oprávnění.

---

4. **Jaký je rozdíl mezi přepínači „Plně hrazeno“ a „Sleva (%)“?**

**Plně hrazeno** znamená, že pacient za tuto konkrétní položku nic nedoplácí — je zcela v ceně balíčku. **Sleva (%)** je procentuální sleva z ceníkové ceny položky. Pokud je položka plně hrazena, sleva se neuplatní.

---

5. **Proč se při ukládání závazku zobrazuje chyba „Nenalezena platná cena“?**

Systém nedókázal dohledat platný ceník pro dané datum. Zkontrolujte, zda má sortiment zadanou cenu s platností pokrývající aktuální datum. Pokud cena chybí nebo je platnost ukončena, přidejte nový záznam ceníku.

---

6. **Jak provedu storno vyúčtovaného závazku?**

Otevřete kartu pacienta → záložku Závazky. Vyberte závazek, který chcete stornovat, a klikněte na **Storno**. Systém vytvoří opravný záznam. Původní záznam zůstane v historii zachován.

---

7. **Lze tisk pokladního dokladu provést přímo z modulu?**

Ano. Po uložení závazku se způsobem platby „Hotově“ nabídne systém automaticky tisk pokladního dokladu. Tisk lze opakovat kdykoliv později ze záložky Závazky.

---

8. **Jak nastavím, aby cena platila jen pro konkrétní pracoviště?**

Při zadávání záznamu ceníku vyplněte pole **Pracoviště**. Cena pak bude platit výlučně pro toto pracoviště. Pokud pracoviště nevyplníte, cena platí globálně.

---

9. **Mohu exportovat přehled závazků pacienta?**

Přehled závazků je dostupný na kartě pacienta v záložce Závazky. Export (tisk, PDF) zajištíte přes funkci **Tisk přehledu** v panelu nástrojů.

---

10. **Jak zjištím, kdo a kdy balíček vytvořil nebo naposledy upravil?**

V detailu záznamu klikněte na tlačítko **Auditní informace** nebo záložku **Historie**.

---

11. **Co se stane s historickými závazky, když deaktivuji položku sortimentu?**

Deaktivace položky neovlivní existující závazky. Všechna historická data zůstávají zachována. Deaktivovaná položka se pouze přestane nabízet při nových vyúčtováních.

---

12. **Lze jeden sortiment zařadit do více balíčků?**

Ano. Jedna položka sortimentu může být součástí libovolného počtu různých balíčků, vždy s vlastním nastavením počtu, slevy a způsobu účtování.

---

13. **Jaký je rozdíl mezi způsoby platby smlouvy PLS — paušál, výkony a kombinovaně?**

**Paušál** — firma platí pevně dohodnutou částku za sledované období. **Výkony** — firma platí pouze za skutečně realizované prohlídky dle ceníku. **Kombinovaně** — část nákladů je kryta paušálem, zbytek se fakturuje jako výkony.

---

14. **Co se stane, když zaměstnanec na prohlídku nepřijde?**

Záleží na nastavení smlouvy PLS. Pokud je zaškrtnuto „Fakturovat stav Nedostavil se“, systém akci zahrne do faktury. Jinak akci uzavřete se stavem „Uzavřena, nefakturovat“.

---

15. **Jak přiřadím zaměstnance ke skupině PLS?**

Na kartě pacienta v části **Zaměstnání** — vyberte skupinu PLS příslušnou pro pracovní pozici zaměstnance.

---

16. **Lze v rámci jedné smlouvy PLS nastavit různé ceny pro různé skupiny zaměstnanců?**

Ano. Každá položka smlouvy PLS má vlastní nastavení ceny a slevy a lze ji omezit na konkrétní skupinu (pozici) PLS.

---

17. **Jak opravím fakturu PLS, která již byla vystavena?**

Vystavená faktura PLS je uzamčena. Opravu provede správce systému pomocí funkce **„Smazat fakturu PLS“**. Po smazání se akce PLS vrátí do stavu „Uzavřena, fakturovat“ a je možné fakturu znovu vystavit.
