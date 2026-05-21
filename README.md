# Galen wiki archive

Denní automatický snapshot prostoru **FONS Galen** (`fg`) z `https://stapro-galen.atlassian.net/wiki/spaces/fg`.

## Struktura

```
pages/<Cesta/Ve/Stromu>/<Titul stranky>/
├── index.html         (export_view — kompletní HTML, otevři dvojklikem v prohlížeči)
├── source.xhtml       (storage — kanonický Confluence zdroj)
├── content.adf.json   (Atlas Document Format — strukturovaný JSON)
├── meta.json          (id, version, updated_at, author_id, attachments)
└── assets/            (obrázky a přílohy, přes Git LFS)

_meta/index.json       (globální index všech stránek)
scripts/               (sync skript a OneDrive mirror)
.github/workflows/     (denní cron 04:00 UTC)
```

Každá stránka je samostatná složka, takže odkazy v `index.html` vedou na `./assets/...` a fungují offline.

## Lokální spuštění

```bash
pip install -r scripts/requirements.txt
python scripts/sync_confluence.py --out .
```

Druhý běh je rychlý — version cache přeskočí stránky beze změny.

## Mirror do OneDrive

```bash
python scripts/mirror_to_onedrive.py --src . --dst "D:\OneDrive - mediclinic.cz\3R Resource\Galen"
```

Jednosměrné: git je zdroj pravdy, OneDrive jen čistý snapshot pro náhled (bez `.git/`).

## Prohlížení historie

- Diff jednoho dne: na GitHubu klikneš na commit
- Historie stránky: `git log --follow "pages/<cesta>/<titul>/source.xhtml"`
- Hledání ve všech verzích: `git log -S "hledaný text"`

## Formáty

| Soubor | Co to je | K čemu |
|---|---|---|
| `index.html` | Plně renderované HTML | Otevřít v prohlížeči, vidět jako na webu |
| `source.xhtml` | Confluence storage (XHTML s `ac:` a `ri:` tagy) | Kanonický zdroj, malé textové diffy |
| `content.adf.json` | Atlas Document Format | Strukturované zpracování (parsování blok po bloku) |
| `meta.json` | Metadata | Verze, autor, datum, seznam příloh |
