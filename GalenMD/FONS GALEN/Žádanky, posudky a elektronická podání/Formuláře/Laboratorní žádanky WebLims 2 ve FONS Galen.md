---
title: "Laboratorní žádanky WebLims 2 ve FONS Galen"
version: 1
updated_at: 2026-08-11
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/537952257
---

# Laboratorní žádanky WebLims 2 ve FONS Galen

## 1. K čemu integrace slouží

FONS Galen (FG) umožňuje lékaři otevřít a vyplnit elektronickou laboratorní žádanku systému **WebLims 2 (WL2)** přímo z karty pacienta, bez přepínání do jiné aplikace. Žádanku lékař vyplní a odešle v prostředí WL2; FG si po jejím odeslání automaticky založí vlastní záznam se seznamem vyžádaných metod. Kromě zakládání nových žádanek nabízí FG i živý přehled již odeslaných žádanek přímo z WL2.

---

## 2. Podmínky použití

- **Každý lékař musí mít vlastní individuální přístup do WL2.** Sdílený účet za pracoviště podporován není (v souladu s NIS2). K pracovišti lze ve WL2 přiřadit více lékařů, kteří se pak v žádance nabízí k výběru.
- Zákazník musí mít u dané laboratoře zřízen přístup na portál **WebLims** – nejde o stávající zákaznický portál FG.

> [!warning]
> **Důležité:** FG zprostředkovává **pouze** předání kontextu pacienta a otevření okna. **Samotné přihlášení do WL2 a jeho správa je vždy záležitostí zákazníka a administrátora dané laboratoře – FG do tohoto procesu nijak nezasahuje ani ho nezajišťuje.**

- Prohlížeč, ve kterém se WL2 otevírá, si drží přihlašovací relaci – lékař se nemusí přihlašovat při každém otevření žádanky, pokud relace nevypršela.

---

## 3. Nastavení integrace (role Správce)

Než se laboratoř WL2 objeví lékařům v modulu Formuláře, musí ji administrátor pracoviště nakonfigurovat.

1. Otevřete **detail pracoviště** (role Správce).
2. Klikněte na modré tlačítko **„Konfigurace lab. žádanek“**.
3. V modálním okně vidíte seznam existujících konfigurací (aktivních i neaktivních) pro dané pracoviště. Pro přidání nové zvolte možnost přidat konfiguraci a vyplňte:

   - **Formulář** – vyberte laboratoř, kterou chcete napojit. V případě, že v seznamu chybí požadovaná laboratoř, zadejte požadavek na FONS Galen prostřednictvím helpdesku [https://helpdesk.stapro.cz/](https://helpdesk.stapro.cz/).
   - **URL WebLims** – adresa instalace WL2 dané laboratoře (včetně `/fol_weblims2/`).
   - **Client ID** a **Client Secret** – přístupové údaje přidělené laboratoří pro OAuth komunikaci.
   - **Aktivní** – zaškrtnutím konfiguraci zapnete.
4. Konfiguraci lze kdykoli upravit nebo deaktivovat.

> **Poznámka:** Jedno pracoviště může mít nakonfigurováno více laboratoří WL2 současně – každá se pak v modulu Formuláře zobrazí jako samostatná karta.

---

## 4. Vytvoření nové žádanky (role Lékař)

1. Otevřete kartu pacienta a přejděte do modulu **Formuláře**.
2. Pokud má vaše pracoviště nakonfigurovánu alespoň jednu aktivní laboratoř WL2, uvidíte kartu s názvem odpovídající šabloně formuláře (např. Synlab, MeDiLa apod.). Pokud je laboratoří více, zobrazí se karty vedle sebe. Pokud pracoviště nemá žádnou aktivní konfiguraci, karty se nezobrazí vůbec.
3. Klikněte na kartu vybrané laboratoře. FG na pozadí připraví kontext žádanky (pacient, diagnózy, pojišťovna atd.).
4. Otevře se okno WL2 s předvyplněnými údaji pacienta. V prostředí WL2 vyberete konkrétní typ žádanky (např. biochemie, mikrobiologie) a doplníte požadované metody.
5. Žádanku můžete **odeslat**, nebo **odeslat a vytisknout průvodku**. V případě potřeby můžete rovněž vytisknout štítek.
6. Okno WL2 se po odeslání **nezavírá automaticky** – po dokončení je nutné jej zavřít tlačítkem **„Zpět“**.
7. Po zavření okna FG automaticky načte seznam vyžádaných metod a založí záznam žádanky (Galen.Zadanka) – druh formuláře odpovídá kartě/dlaždici, kterou jste použili, a text obsahuje přehled vyžádaných metod.

### Možné chybové hlášky po odeslání žádanky

| Situace | Hláška | Žádanka se založí? |
| --- | --- | --- |
| Metody se podařilo načíst | – (žádanka se založí automaticky) | Ano |
| K žádance nebyly nalezeny žádné metody | „K odeslané žádance nebyly nalezeny žádné vyžádané metody.“ | Ne |
| Odkaz na žádanku vypršel | „Odkaz na žádanku již není platný, seznam metod nelze načíst.“ | Ne |
| Chyba na straně WebLims | „Při načítání seznamu metod došlo k chybě na straně WebLims. Zkuste to prosím znovu.“ | Ne |

Pokud se žádanka nezaložila, zkontrolujte, zda byla ve WL2 skutečně odeslána (uložena), a zkuste ji vytvořit znovu.

### Pole „odebráno na oddělení“

Tato volba se **nezapamatovává** – při každém vytváření žádanky je potřeba ji nastavit znovu.

---

## 5. Živý přehled odeslaných žádanek WL2

Kromě záznamu, který FG založí automaticky po odeslání žádanky, si lékař i správce mohou kdykoli zobrazit aktuální seznam žádanek přímo z WL2.

1. Otevřete modul **Komunikace** (Log elektronické komunikace).
2. Pokud máte přístup k alespoň jedné aktivní konfiguraci WL2, uvidíte novou záložku **„WebLims“** vedle ostatních (Notifikace, eRecepty, ČSSZ, Elektronické žádanky, Očkování apod.).
3. Chování po kliknutí na záložku se liší podle role a počtu nakonfigurovaných laboratoří:

| Role | Počet aktivních konfigurací | Co se stane |
| --- | --- | --- |
| Lékař | 0 | Záložka se nezobrazuje |
| Lékař | 1 | Rovnou se otevře přehled žádanek dané laboratoře |
| Lékař | 2 a více | Zobrazí se okno s výběrem **laboratoře** (pracoviště je dané přihlášením) |
| Správce | 1 (napříč pracovišti) | Rovnou se otevře přehled žádanek |
| Správce | 2 a více | Zobrazí se okno s výběrem **pracoviště** i **laboratoře** (nabídka laboratoří se řídí zvoleným pracovištěm) |

4. Ve výběrovém okně potvrďte tlačítkem **„Zobrazit“** (nebo zrušte tlačítkem **„Storno“**). Otevře se okno s aktuálním seznamem žádanek přímo z prostředí WL2.

Pokud se přehled nepodaří načíst, zobrazí se srozumitelná chybová hláška a okno s přehledem se neotevře.

> [!warning]
> **Důležité upozornění:** Pokud si obsah žádanky později změníte nebo ji v tomto přehledu žádanek stornujete přímo ve WL2, **záznam žádanky ve FG (formulář v kartě pacienta) se o této změně nedozví a jeho obsah se neaktualizuje.** V kartě pacienta lze pouze založit novou žádanku a zobrazit seznam vyžádaných metod ve formuláři, ke kterému se dostanete proklikem z dekurzu nebo z historie formulářů. **FG neřeší obsah samotné žádanky (jaké metody byly vyžádány, jejich případnou změnu apod.) – v těchto případech je nutné se obrátit přímo na laboratoř.**

---

## 6. Shrnutí – co integrace řeší a co ne

**Řeší:**

- Otevření předvyplněné žádanky WL2 přímo z karty pacienta ve FG.
- Automatické založení záznamu žádanky ve FG po jejím odeslání (vč. seznamu metod).
- Živý přehled odeslaných žádanek přímo z WL2 bez nutnosti se do WL2 zvlášť přihlašovat.

**Neřeší:**

- FG nijak neřídí ani neukládá vlastní přihlašovací údaje uživatele do WL2 – přihlášení probíhá přímo v embedded okně WL2 a je plně v gesci zákazníka a laboratoře.
- FG neřeší obsah žádanky (vyžádané metody, jejich změny, storno) – jakékoli změny provedené přímo ve WL2 se do záznamu ve FG nepromítnou. V případě potřeby úpravy obsahu žádanky je nutné kontaktovat laboratoř.
