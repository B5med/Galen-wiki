---
title: "API StrukturaOrganizaceService"
version: 1
updated_at: 2025-05-15
source: https://stapro-galen.atlassian.net/wiki/spaces/fg/pages/30113793
---

> [!info]
> Toto API zasílá přehled pracovníků společnosti, tj. uživatelů přirazených na konkrétní pracoviště. Jeden uživatel může být přiřazen na více pracovištích.

## get /api/StrukturaOrganizaceService/Pracovnici

> [!warning]
> Informace o deaktivaci uživatele zasílání nejsou. Pokud je uživatel (resp. pracovník) deaktivován, je i přesto zaslán pomocí metody.

## get /api/StrukturaOrganizaceService/PracovniciZaObdobi

> [!warning]
> Metody *Pracovnici*a *PracovniciZaObdobi* zasílají přehled všech pracovníků  bez ohledu na to, zda je pracovník (uživatel na pracovišti) aktivní, či nikoli.

- Metoda zasílá přehled pracovníků, v jejichž nastavení byla provedena změna.
- Pracovník jako takový nemůže být deaktivován, může být pouze ukončen přístup pracovníka na pracoviště k určitému datu.
- V případě ukončení přístupu na pracoviště se nejedná o smazání, ale o editaci, a proto je zaslán záznam tohoto znění

` {       "prijmeni": "Dlaha",       "jmeno": "Julius",       "titul": "MUDr..",       "titulZa": "PhD.",       "platnostOd": "02052025",       "odpovednyLekar": true,       "icpPracoviste": "00000000",       "nazevPracoviste": "Springfield General Hospital",       "typZmeny": "U",       "datumCasZmeny": "15052025T08:13:52.304",       "externiId": "C6DFBF8B-007F-484D-A307-65E87A5546G2"     }`
