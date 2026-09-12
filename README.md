# GNOMEAI

GNOMEAI är ett öppet arkiv för GNOME-relaterade patchserier, felsökning och implementationsplaner där AI får användas som ett produktivt utvecklingsverktyg.

AI är inte ett hot mot programvaruutveckling. Rätt använd kan den korta tiden från felrapport till begriplig reproduktion, hjälpa till att läsa stora kodbaser, föreslå avgränsade ändringar och hitta testfall som annars lätt missas. Den frigör tid för det arbete som fortfarande kräver omdöme: att förstå användarbehov, välja rätt arkitektur, granska risker och ta ansvar för resultatet.

Ett bra bidrag bedöms efter samma saker oavsett vilka verktyg som användes för att skapa det:

- Löser det ett verkligt problem?
- Är ändringen liten nog att förstå och granska?
- Finns en reproduktion eller ett relevant test?
- Fungerar den med projektets design, API:er och underhållsbehov?
- Är upphov, licens och begränsningar tydliga?

AI-assisterade bidrag är välkomna här. De ska vara sakliga, testade där det är möjligt och möjliga att granska rad för rad. Inga hemligheter, byggkataloger eller oinspekterade genererade ändringar hör hemma i repot.

## Innehåll

- [`patches/`](patches) innehåller en katalog per arbetsgren. Varje katalog har en ordnad `git format-patch`-serie och `METADATA.json` med källprojekt, upstream-bas, commit-ID:n och arkivkatalog.
- [`PATCHES.json`](PATCHES.json) är ett maskinläsbart index över alla patchserier.
- [`PLAN.md`](PLAN.md) innehåller den löpande granskningen och implementationsplanen för 250 GNOME-ärenden.
- [`issues-250.csv`](issues-250.csv) är ärendeinventeringen som planen bygger på.

## Använd en patchserie

Klona källprojektet från `METADATA.json`, checka ut en kompatibel upstream-revision och tillämpa serien:

```sh
git am /sökväg/till/GNOMEAI/patches/PROJEKT/ARKIVKATALOG/*.patch
```

Vissa serier beror på andra serier. Se `PLAN.md` och respektive metadata innan de skickas uppströms.

## Bidra

Läs [CONTRIBUTING.md](CONTRIBUTING.md). Ange alltid målprojekt, upstream-bas, vad ändringen löser, hur den har validerats och kända begränsningar. Den som skickar ett bidrag ansvarar för den slutliga diffen.
