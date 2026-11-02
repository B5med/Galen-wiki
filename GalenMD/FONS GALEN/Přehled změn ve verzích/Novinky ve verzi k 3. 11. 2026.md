---
title: "Novinky ve verzi k 3. 11. 2026"
version: 1
updated_at: 2026-11-02
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/671481858
---

# Novinky ve verzi k 3. 11. 2026

# Novinky a vylepšení

---

## EZD – Správa dokumentů

### Nepodepsané dokumenty dle pacientů

V modulu EZD (Správa dokumentů) a na Dashboardu přibyla záložka „Nepodepsané dokumenty dle pacientů“. Zobrazuje nepodepsané dokumenty EZD seskupené podle pacienta a dne, takže pacient s několika dokumenty za jeden den má jen jeden řádek. Záložka je před původní záložkou „Nepodepsané dokumenty“, která zůstává beze změny.

Přehled obsahuje sloupce Datum, Pacient a „K podpisu / celkem“. První číslo říká, kolik podpisových úkonů je potřeba, druhé kolik dokumentů se tím podepíše. Například „1/3“ znamená, že jedním podpisem dekurzu se podepíší tři dokumenty. Pokud jsou obě čísla stejná, zobrazí se jen jedno. Ve Správci jsou navíc sloupce Pracoviště a Lékař. Na Dashboardu je sloupec „Cílový dokument“.

V modulu EZD lze přehled filtrovat. Po označení řádku se pod ním zobrazí detail dokumentů daného pacienta a dne. Dekurz je tučně a dokumenty, které se uzamknou spolu s ním, jsou pod ním odsazené šipkou „↳“ s ikonou ⓘ („Uzamkne se spolu s podpisem dekurzu.“). Pravidla pro uzamykání dokumentů pod dekurz určuje stávající „Konfigurace obsahu EZD“ a nezměnila se.

Podepisování je dostupné po přihlášení na konkrétní pracoviště. Označte jeden nebo více řádků (Ctrl nebo Shift) a použijte tlačítko „Podepsat vybrané (n)“. Podepíší se všechny nepodepsané dokumenty označených pacientů a dnů. Ve Správci je záložka jen přehledová a podpis zde není. Tlačítko je neaktivní, pokud podpis není možný, a v tooltipu je uveden důvod.

Na Dashboardu otevře dvojklik na řádek cílový dokument. Pokud ten den existuje dekurz, otevře se dekurz. Má-li pacient dekurzy dva, otevře se poslední nepodepsaný. Bez dekurzu se otevře poslední nepodepsaný dokument dne. Hromadné podepisování probíhá v modulu EZD.

### Hromadný podpis dokumentů EZD

Když v přehledu nepodepsaných dokumentů EZD zvolíte podpis u více dokumentů najednou, otevře se okno „Náhled dokumentů k podepsání (n)“. Při podpisu jednoho dokumentu zůstává stávající okno beze změny.

Před zobrazením okna se připraví PDF všech dokumentů.

V levém panelu je seznam dokumentů k podpisu. Klepnutím na dokument se náhled posune na něj. Dole je počet prohlédnutých dokumentů a ukazatel postupu. V hlavní části jsou všechny dokumenty pod sebou v jednom posuvném náhledu, aby bylo splněno, že každý podepisovaný dokument se zobrazí.

Tlačítko „Podepsat (k)“ je neaktivní, dokud nesjedete na konec posledního dokumentu. Po návratu nahoru zůstane aktivní. Zaškrtávátkem u dokumentu v levém panelu můžete dokument z podpisu vyřadit. Ten se pak nepodepíše a zůstane v přehledu nepodepsaných. Číslo „k“ v tlačítku odpovídá počtu zaškrtnutých dokumentů. Nápověda dole říká, co je potřeba udělat, nebo kolik dokumentů se podepíše.

„Zrušit vše“ zavře okno bez podpisu. Po podpisu se přehled obnoví.
