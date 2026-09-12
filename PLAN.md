# GNOME: arbetsstatus för 250 ärenden

Mål: granska och arbeta med samtliga 250 högst prioriterade GNOME-ärenden, ta fram verifierade lösningar och skicka bidrag upstream. GNOME Shell !4405 är mergad. libgtop !54 är verifierad och öppen. Nautilus !2125 är inskickad och väntar på CI.

| # | Ärende | Status |
|---|---|---|
| 1 | [Separate workspaces on multiple monitors](https://gitlab.gnome.org/GNOME/mutter/-/work_items/37) | Ej kodgranskat |
| 2 | [Implement "Jump to file" feature (type ahead / type to seek)](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/1157) | Detaljerat användningsfall för tangentstyrd prefixnavigering. Sökning bland öppna MR:er för ”typeahead” gav inga träffar. Nuvarande fönsterhändelse skickar tangenttryck till QueryEditor och öppnar rekursiv sökning; typeahead behöver därför en ny interaktionsmodell och list-/grid-fokusering, inte bara en ny genväg. |
| 3 | [Unified inbox](https://gitlab.gnome.org/GNOME/geary/-/work_items/53) | 92 röster men märkt Needs Design och Help Wanted. Implementationen kräver ny sidofältsmodell och kontoidentifiering i konversationsvyn; inte en liten separat patch. |
| 4 | [Ability to save screenshots to clipboard only (without saving to disk)](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/5208) | Befintlig MR !3928 hämtad (8b21ff45649f). Sju lagringstester passerar med MR !3928 + separat historikfix i isolerad Shell 50.1. Ingen MR skickad. Full main-build och UI-tester återstår. |
| 5 | [Tracking: Transparent encryption and signing with GPG](https://gitlab.gnome.org/GNOME/geary/-/work_items/6) | Ej kodgranskat |
| 6 | [Top bar on all monitors](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/4603) | Märkt Needs Design samt Panel och Display. Kräver beslut om panelens funktion och innehåll på sekundära skärmar före implementation. |
| 7 | [Ability to set scroll speed in system settings](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/379) | Ärendet kräver en gemensam inställning genom Mutter, GTK, Qt och Wayland-protokollet. Control Center kan inte ge fungerande rullhastighet ensamt; ingen isolerad patch. |
| 8 | [Port to GTK4](https://gitlab.gnome.org/GNOME/geary/-/work_items/1212) | Ej kodgranskat |
| 9 | [Login controls not displayed on all screens](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/3867) | Märkt Enhancement. Föreslår spegling eller konfiguration av inloggningsskärmens bildskärmar; kräver Mutter/GDM-policy och designbeslut, inte en Shell-ändring isolerat. |
| 10 | [Rework GNOME Shell's architecture to allow restarting under Wayland without crashing / taking down the spawned apps with it](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/5634) | Ej kodgranskat |
| 11 | [File Roller drag'n'drop extraction to Nautilus folder is broken](https://gitlab.gnome.org/GNOME/file-roller/-/work_items/4) | GTK4-portningen saknar helt dragkälla; tidigare XDS-extraktion togs bort i commit 8b26a13. Större återinförande krävs. |
| 12 | [Quit when inactive](https://gitlab.gnome.org/GNOME/gnome-software/-/work_items/942) | README förbjuder AI-genererade bidrag; ej skickat. |
| 13 | [Wrong keyboard layout in lock screen](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/225) | Aktiv MR [!3681](https://gitlab.gnome.org/GNOME/gnome-shell/-/merge_requests/3681) hanterar #225 och flera relaterade fel; den har uppdaterats mot main. Ingen dubblettändring. |
| 14 | [Update for the Wayland tearing protocol](https://gitlab.gnome.org/GNOME/mutter/-/work_items/2517) | Märkt Wayland Protocol Request/Performance. Förslaget kräver ny klientprotokollshantering, policies för VRR och helskärmsinnehåll samt KMS-presentation; för stort för en oberoende punktpatch. |
| 15 | [Ability to "mark all emails as read"](https://gitlab.gnome.org/GNOME/geary/-/work_items/101) | Ärendet vill ha ett tydligt ”markera alla”. Maintainer efterfrågar GNOME-design innan implementation; nuvarande funktion kan bara markera markerade konversationer. Ingen egen dubblettändring. |
| 16 | [Disable focus stealing prevention](https://gitlab.gnome.org/GNOME/mutter/-/work_items/673) | Ändringen skulle medvetet ta bort Mutter-policy mot fokusstöld. Ärendet efterfrågar en ny generell aktiveringsmodell för GAction, WebKitGTK och andra verktygslådor; ingen lämplig punktfix. |
| 17 | [Selecting a folder to save to loses focus on file name](https://gitlab.gnome.org/GNOME/gtk/-/work_items/326) | Märkt GTK3. I GTK main flyttas fokus till fillistan men skrivning startar inte längre sökning, enligt maintainer. De relevanta GTK4-MR:erna !4945 och !4960 är stängda; ingen säker dubblettändring. |
| 18 | [Blur semi-transparent backgrounds in some of GNOME Shell's UI components](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/1590) | Shell har redan en `Shell.BlurEffect` för låsskärmens bakgrund, men ärendet föreslår flera olika komponenter (sökning, popovers och låsskärm) utan kontrast-, prestanda- eller designbeslut per yta. Ingen generell effektpatch. |
| 19 | [Snap to top and bottom (edges) too](https://gitlab.gnome.org/GNOME/mutter/-/work_items/579) | Nuvarande Mutter har bara `META_TILE_LEFT`, `META_TILE_RIGHT` och maximering. Top/botten och hörnplattor kräver nya tile-lägen genom fönsterkonfiguration, kantbegränsningar, områdesberäkning och tangentbindningar. Ingen säker punktpatch. |
| 20 | [Remote desktop with locked local screen](https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/work_items/16) | Märkt Feature. Kravet behöver en separat virtuell session eller säkert skärmsekretessläge på compositor-nivå; det går inte att ge med en ändring i fjärrskrivbordets anslutningskod. |
| 21 | [Allow sorting/grouping conversations in the list](https://gitlab.gnome.org/GNOME/geary/-/work_items/85) | Ej kodgranskat |
| 22 | [OSK needs (at least the option of) modifiers (Ctrl/Alt/Super)](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/181) | Terminalinmatning väljer redan `*-extended`-layouter. De exponerar låsbara Ctrl- och Alt-tangenter, och `KeyboardController` skickar modifierar före/efter råa tangenttryck. Super finns inte i layouterna; att lägga till den kräver beslut om Shell-genvägar och fokus, inte en säker layoutändring. |
| 23 | [Port to GTK4](https://gitlab.gnome.org/GNOME/Initiatives/-/work_items/26) | Ej kodgranskat |
| 24 | [Better Window Tiling](https://gitlab.gnome.org/GNOME/mutter/-/work_items/704) | Ej kodgranskat |
| 25 | [color management: support scRGB](https://gitlab.gnome.org/GNOME/mutter/-/work_items/4083) | Ej kodgranskat |
| 26 | [Add automatic and manual scheduling for light and dark theme switching](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/2060) | Backgroundpanelen skriver bara `org.gnome.desktop.interface color-scheme` när användaren väljer tema. Night Light har egen Mutter-backad schema- och schemaläggning. Temaschema kräver nya beständiga inställningar och en långlivad tjänst som växlar dem; enbart Settings-UI skulle inte fungera utanför appen. |
| 27 | [Add per-monitor min/max brightness settings](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/1209) | Ärendet pekar själv på gnome-settings-daemon- och kernelarbete för externa paneler och flera enheter. Nuvarande Settings läser bara Shells globala `HasBrightnessControl` för funktioner som automatisk ljusstyrka. Per-monitor gränser kräver per-skärm-backend/API först, inte en fristående inställningspanel. |
| 28 | [Extension installation?](https://gitlab.gnome.org/GNOME/gnome-extensions-app/-/work_items/6) | Ärendet identifierar två konkurrerande riktningar: en sandboxbar URI-/D-Bus-installationsväg från extensions.gnome.org eller sökning och installation i appen. Båda kräver produkt- och säkerhetsbeslut; dagens app är uttryckligen ett verktyg för att hantera installerade Shell-tillägg. |
| 29 | [An easy way to return the Application Grid positions to its default? (Gnome 3.38)](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/3180) | Märkt Feature/Icon Grid. Återställning skulle radera användarens ordning och kräver ett utformat, bekräftat återställningsflöde samt placering i Shells gränssnitt. |
| 30 | [Cannot login to microsoft office365 "exchange" account with 2fa enabled](https://gitlab.gnome.org/GNOME/gnome-online-accounts/-/work_items/102) | Märkt Feature/EWS. Lösenordsbaserad EWS-inloggning kan inte genomföra Microsofts MFA; lösningen kräver OAuth/OIDC-providerflöde och Microsoft-konfiguration, inte att ett TOTP-fält läggs till. |
| 31 | [Fractional Scaling Known issues and TODO](https://gitlab.gnome.org/GNOME/mutter/-/work_items/478) | Ej kodgranskat |
| 32 | ["Open with other application" will set selected application as default](https://gitlab.gnome.org/GNOME/glib/-/work_items/1026) | GLib erbjuder redan separata API:er för att starta en vald app och för att ändra standardapp. Felet beskrivs i Nautilus kontextmeny och kan inte lösas i GLib utan att fel komponent ändras. |
| 33 | [Recoloring API](https://gitlab.gnome.org/GNOME/libadwaita/-/work_items/53) | Ej kodgranskat |
| 34 | [Import of certificate with seahorse does not work; Import button stays disabled](https://gitlab.gnome.org/GNOME/seahorse/-/work_items/205) | Knappen kräver en importer från GCR. GCR skapar bara PKCS#11-importörer för skrivbara, initierade token; ingen generell systemcertifikat-destination finns. Kräver produktbeslut, inte en säker enradsfix. |
| 35 | [Allow that alarms also beep when gnome-clocks is not running](https://gitlab.gnome.org/GNOME/gnome-clocks/-/work_items/1) | Aktiv MR [!336](https://gitlab.gnome.org/GNOME/gnome-clocks/-/merge_requests/336) lägger till autostart som tjänst och har passerande pipeline. Ägaren pekar även på det öppna portal-arbetet [#281](https://gitlab.gnome.org/GNOME/gnome-clocks/-/work_items/281); skapa inte en konkurrerande implementation. |
| 36 | [ListView scrolling sometimes jumps up and down when doing high-resolution scrolling](https://gitlab.gnome.org/GNOME/gtk/-/work_items/6344) | Aktiv upstream-MR [!8042](https://gitlab.gnome.org/GNOME/gtk/-/merge_requests/8042) arbetar med scrollinterpolation. Rotorsaken är varierande, uppskattade radhöjder i virtuella listor; en fix måste provas på stora listor med varierande höjd. Ingen ogenomskinlig dubblettpatch. |
| 37 | [provide the option to change the default window size](https://gitlab.gnome.org/GNOME/console/-/work_items/140) | README förbjuder AI-genererade bidrag; ej skickat. |
| 38 | [App grid: Allow uninstalling apps](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/4752) | Märkt Feature. Ärendet saknar beslut om bekräftelse eller ångra-flöde och kräver integrering med GNOME Software/pakethantering; ingen Shell-patch utan design. |
| 39 | [GTK 4 Spellcheck Support](https://gitlab.gnome.org/GNOME/gtk/-/work_items/3814) | Upstream har en aktiv WIP-gren, `wip/chergert/spellcheck` (dd7ce2e), och planeringen omfattar plattformsleverantörer, flerspråkighet, Flatpak/portal, textregioner och rendering. Detta är ett flerlagersarbete; skapa inte en parallell, ofullständig stavningspatch. |
| 40 | [Provide GPU and vRAM usage in the Resources tab's graphs and counters](https://gitlab.gnome.org/GNOME/gnome-system-monitor/-/work_items/62) | AMDGPU-metriker är inskickade som [libgtop!54](https://gitlab.gnome.org/GNOME/libgtop/-/merge_requests/54). API:t rapporterar belastning, GTT, synligt VRAM och VRAM från DRM-sysfs och behåller rätt `cardN`-sökväg på blandade GPU-system. Fedora-, Ubuntu- och ABI-pipelinen passerar. |
| 41 | [Improve running binaries experience](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/443) | Märkt Needs Design och RFC. Förslaget ändrar Nautilus säkerhetsmodell och kräver dialogtexter, trust-flöde och terminalbeteende; ingen säker kodpatch utan godkänd design. |
| 42 | [Mouse not being recorded when screencasting (Even when enabled)](https://gitlab.gnome.org/GNOME/mutter/-/work_items/3182) | Aktuell Mutter har en separat cursor-ström med stöd för inbäddad bild och metadata, samt testklient för cursor-lägen. Ärendet gäller X11; utan reproduktion där går det inte att avgöra om felet fortfarande finns eller göra en säker patch. |
| 43 | [Add support for OSC 52](https://gitlab.gnome.org/GNOME/vte/-/work_items/2495) | VTE parsern känner redan igen OSC 52. Maintainer kräver uttryckligt användarsamtycke per clipboard-begäran, där VTE signalerar och terminalen visar godkännande. En gammal patch med appinställning räcker inte. |
| 44 | [Include additional mimetype icons?](https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/work_items/24) | Efterfrågar egna, enkla ikoner för vanliga programmeringsspråk men saknar vald design och lista över MIME-typer. Skapa inte generiska eller maskinskapade ikoner utan designbeslut. |
| 45 | [[Feature] Blurred wallpaper as overview background](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/4307) | Låsskärmen använder redan `Shell.BlurEffect` på bakgrunden. Översikten har en annan rendering och gest-/prestandamodell; att kopiera låsskärmens effekt skulle ändra avsedd design och behöver ett godkänt översiktsförslag. |
| 46 | [Prompt rename automatically when a new file is created from template](https://gitlab.gnome.org/GNOME/nautilus/-/work_items/524) | Tilldelat upstream. MR !1658 ersätter !647; skapa inte dubblett. |
| 47 | [Ability to record system audio in video screencasts](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/5524) | Screencasttjänsten bygger en ren videopipeline från Mutters PipeWire-ström; D-Bus-API:t har bara markör, bildfrekvens och videopipeline som val. Systemljud kräver en PipeWire-audiokälla, synkronisering och muxning för varje videoencoder samt ett uttryckligt UI-/integritetsval. Ingen säker checkbox-patch. |
| 48 | [More flexible event recurrence UI (repeat every X number of days/weeks/months/years, specific days of the week or month, etc.)](https://gitlab.gnome.org/GNOME/gnome-calendar/-/work_items/272) | Ej kodgranskat |
| 49 | [Can't zoom in on screenshots](https://gitlab.gnome.org/GNOME/gnome-software/-/work_items/313) | Kodväg granskad. README förbjuder AI-genererade bidrag; ej skickat. |
| 50 | [New design for fractional scaling setting](https://gitlab.gnome.org/GNOME/gnome-control-center/-/work_items/2516) | Aktuell Display-panel använder en knappgrupp för få skalor och växlar till combobox för fler eller hopfällt läge, i stället för en lång lista. Den saknar fortfarande den föreslagna förhandsvisningen och en definierad backend för X11-kompatibilitetsläget; den senare kan inte läggas till som bara UI. |

Publicering: En reproducerbar uppföljning för GNOME Shell-historikfelet är publicerad i [#6540](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/6540#note_2868214). Fixin är inskickad som [GNOME Shell !4405](https://gitlab.gnome.org/GNOME/gnome-shell/-/merge_requests/4405) från forken `yeager/gnome-shell`. Commitmeddelandet har uppdaterats enligt maintainer-kommentaren och hela pipelinen passerar efter en omkörning av ett instabilt compositor-test.

## Utökning till 250 ärenden

Alla 250 ärenden finns i [gnome-250-oppna-arenden-2026-09-11.csv](gnome-250-oppna-arenden-2026-09-11.csv). Plats 1–50 kommer från GitLabs globala röstsortering. Plats 51–250 är ett verifierat aktuellt urval med faktiska röstsiffror, tydligt märkt som ej globalt röstsorterat medan GraphQL-anropet är rate-limitat.

## Separat fel hittat vid arbete med #4

Första skärmbilden registreras inte i Senaste filer om recently-used.xbel saknas. Enradsfix finns i [screenshot-recent-files/fix.patch](screenshot-recent-files/fix.patch). Före/efter-test med verkliga GNOME-bibliotek: originalet misslyckas, fixen passerar. Orsaken och fixriktningen är publicerade som en uppföljning till [#6540](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/6540#note_2868214), och patchen finns i [!4405](https://gitlab.gnome.org/GNOME/gnome-shell/-/merge_requests/4405). Det här stänger inte #4.

GitLab GraphQL ger tillgång till kopplade MR:er trots att REST-kommentarer nekas. Batchfältet relatedMergeRequests tillåter bara ett ärende per anrop. Ytterligare insamling fick HTTP 429 och pausades; partiella verifierade resultat finns i work/issue-details.

## Nautilus: Zstandard-arkiv

Nautilus [!2125](https://gitlab.gnome.org/GNOME/nautilus/-/merge_requests/2125) för #1936 finns på grenen `yeager/nautilus:compression-tar-zstd` (commit `5f8df94`). Den höjer minsta gnome-autoar till 0.5.0, lägger till `.tar.zst` i komprimeringsdialogen och lägger till ett displayless-test. Schemat har validerats; Fedora- och Flatpak-CI är gröna.

## NetworkManager-openvpn: OpenVPN 2.6-DNS

[MR !117](https://gitlab.gnome.org/GNOME/NetworkManager-openvpn/-/merge_requests/117) lägger till stöd för OpenVPN 2.6:s DNS-miljövariabler och behåller den äldre `foreign_option_N`-parsern. Pipeline `1108593` byggde distributionsarkivet, men Fedora-testet faller på samma const-kvalificeringsfel i oförändrade `shared/utils.c` och `properties/nm-openvpn-editor.c` som huvudgrenens pipeline `1107872`. Den nya hjälparfilen kompilerade klart.

En separat pipelinefix är inskickad som [NetworkManager-openvpn !118](https://gitlab.gnome.org/GNOME/NetworkManager-openvpn/-/merge_requests/118): const-korrekta läspekarna i de två berörda befintliga filerna.


## Shell !4405 — mergad

Fixen för saknad recent-files-historik mergades 2026-09-11 efter att pipeline 1108595 passerade.


## NetworkManager-openvpn !118 — grön

Pipeline 1108601 passerade både distributionsbygge och Fedora-test efter typkorrigeringen i den befintliga parsern.

## gnome-autoar: asynkrona signalreturer

[!57](https://gitlab.gnome.org/GNOME/gnome-autoar/-/merge_requests/57) uppdaterades till commit `512a9c1`. Den väntar på retursignaler från huvudtråden och har nu ett tidsbegränsat regressionstest för asynkron lösenordsbegäran. `meson test -C _build gnome-autoar:test-extract-unit --print-errorlogs` passerar lokalt.

## libgtop: procmap-smaps

[!55](https://gitlab.gnome.org/GNOME/libgtop/-/merge_requests/55) fixar #70. Parsern startade siffertolkningen på kolon i smaps-raden, vilket gav noll för storlek, RSS och delade/privata clean/dirty-fält. Den startar nu efter kolonet. Verifierat med `LIBGTOP_SERVER=:direct ./examples/procmap <pid>` mot systemets `/proc/<pid>/smaps`.

## Epiphany: WebExtension-krasch

[!2205](https://gitlab.gnome.org/GNOME/epiphany/-/merge_requests/2205) fixar #2908. WebKit kan serialisera ett tomt svarsnamn som `NULL`; svarshanteraren använde `strcmp()` och kraschade då webbprocessen. MR:n använder `g_strcmp0()`. Full Meson-konfiguration saknar lokalt beroendet `gck-2`; den NULL-säkra GLib-jämförelsen har syntaxkontrollerats.

## Papers: kontrast i sidlisten

#749 granskades mot aktuell CSS. Papers har ingen lokal färgregel för den berörda sidlisten utan använder GTK/Adwaitas semantiska färger. Ingen hårdkodad CSS-patch skickas utan widget- och temaspecifik reproduktion.

## Epiphany !2205 — grön

Pipeline för WebExtension-fixen passerade och MR:n är mergebar.

## libsecret: intermittenta Secret Service-fel

#115 är triagerad. Rapporten behöver GNOME Keyring- och DBus-spårning för att placera det intermittenta krypteringsfelet; ingen säker libsecret-ändring skickas.

## libgtop !55 — grön

ABI-pipelinen passerade efter att den byggbara basrevisionen användes. MR:n innehåller procmap-fixen för #70 och är redo för granskning.

| 133 | [Crash in `meta_wayland_tablet_update_sprite()` due to NULL `tablet`](https://gitlab.gnome.org/GNOME/mutter/-/work_items/5043) | Skickad som [Mutter !5322](https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/5322). Skyddar sprite-uppdateringen mot proximity-händelser utan matchande tablet, vilket tar bort den rapporterade NULL-avrefereringen. |

| 140 | [Crashes with LG webOS builtin chromecast receiver](https://gitlab.gnome.org/GNOME/gnome-network-displays/-/work_items/500) | Skickad som [GNOME Network Displays !259](https://gitlab.gnome.org/GNOME/gnome-network-displays/-/merge_requests/259). Förhindrar rekursiv anslutningsstängning och stack overflow när en Chromecast-mottagare stänger TLS-anslutningen. |

| 141 | [`to_preview_text()` hänger på stora e-postmeddelanden](https://gitlab.gnome.org/GNOME/geary/-/work_items/1712) | Skickad som [Geary !899](https://gitlab.gnome.org/GNOME/geary/-/merge_requests/899). Begränsar den text som normaliseras till 64 KiB och behåller giltig UTF-8. |

| 157 | [MprisSource/MprisPlayer SignalTracker leak on lock screen](https://gitlab.gnome.org/GNOME/gnome-shell/-/work_items/9410) | Skickad som [GNOME Shell !4406](https://gitlab.gnome.org/GNOME/gnome-shell/-/merge_requests/4406). Frigör MPRIS-spelar- och proxyanslutningar när låsskärmens notifieringsruta tas bort. |

GNOME Shell !4406 passerade pipeline och är mergebar.
- 2026-09-11: GTK !10371 submitted for #8295: avoid preloading SVG icons in worker threads, preventing Pango Fontconfig font-map races during fallback rasterization.
- 2026-09-11: GNOME Shell !4408 submitted for #9394: unpack MPRIS metadata once per update to avoid quadratic main-thread work.
- 2026-09-11: Pango !927 submitted for #900: keep Clang 23's generated unused-global warning non-fatal while retaining the warning.
- 2026-09-11: Nautilus !2126 submitted for #4321: focus Replace when the file-conflict dialog is shown.
- 2026-09-11: GNOME Shell !4408 kördes om efter ett ensamt fel i den intermittenta huvudlösa testen `closeWithActiveWindows`; omkörningen passerade och MR:n är mergebar.
- 2026-09-11: GTK #8399 är redan löst i GTK 4.24 enligt upstream; ingen patch behövs.
- 2026-09-11: GNOME Control Center #3756 behöver layoutfilens plats och reproduktion. Tecla har redan stöd för `~/.config/xkb`; Shell använder dessutom compositorns aktiva keymap.
- 2026-09-11: GNOME Settings Daemon #888 saknar status/loggar som identifierar ansvarig dimningskodväg.
- 2026-09-11: GNOME Characters !182 submitted for #187: return one search-result meta per identifier even when icon-data is unavailable.
- 2026-09-11: GIMP !3000 submitted for #15742: update color-picker information when exact channel values differ at the same coordinates.
- 2026-09-11: GNOME Terminal !12 submitted for #8155: pop down the header menu before the delayed fullscreen transition on Wayland.

## MR-kontroll 2026-09-12

- Nautilus [!2125](https://gitlab.gnome.org/GNOME/nautilus/-/merge_requests/2125) stängdes av underhållaren med hänvisning till #1936; den bevakas inte längre.
- Nautilus [!2126](https://gitlab.gnome.org/GNOME/nautilus/-/merge_requests/2126) uppdaterades enligt granskning: Blueprint använder nu `focus-widget: replace_button` i stället för en särskild `map`-handler. Ny pipeline körs.
- Epiphany [!2205](https://gitlab.gnome.org/GNOME/epiphany/-/merge_requests/2205) har `Fixes #2908` i commitmeddelandet och är fortsatt grön.
- GIMP [!3000](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/3000) använder nu commitprefixet `app/widgets:` och är markerad redo för granskning. Ny pipeline körs.
- GTK [!10371](https://gitlab.gnome.org/GNOME/gtk/-/merge_requests/10371) kördes om efter ett ensamt fel i det orelaterade X11-testet `gtk:clipboard-x11`; omkörningen pågår.
- Pango [!927](https://gitlab.gnome.org/GNOME/pango/-/merge_requests/927) faller endast i Windows-testmiljöerna efter lyckat bygge; felen gäller installerade typsnitt, WIC och bidi-tester och påverkas inte av compiler-flaggan i patchen.

## GIMP #16751 — lokaliserade menyvägar i åtgärdssökningen

[GIMP !3002](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/3002) delar upp menymodellens engelska kanoniska sökväg från den lokaliserade presentationsvägen. Uppslagning av menyobjekt fortsätter använda den kanoniska vägen, medan Action Search nu visar de översatta undermenynamnen. `git diff --check` passerar. Lokal Meson-konfiguration når projektet men saknar `atk`-utvecklingspaketet; upstream-CI bygger ändringen.

## libgnome-games-support #41 — återanvänd poängrader

[libgnome-games-support !59](https://gitlab.gnome.org/GNOME/libgnome-games-support/-/merge_requests/59) skapar poängdialogens spelarcell i `Gtk.SignalListItemFactory.setup` i stället för att skapa en ny `Gtk.Entry` vid varje `bind`. Cellen växlar mellan återanvänd etikett och inmatning och nollställer sin bundna poäng vid `unbind`. `git diff --check` passerar; lokalt saknas `valac`, så CI gör den fulla Vala-kompileringen.
Senast kontrollerad: 2026-09-12 08:10 CEST — GTK !10371 är nu grön och mergeable; fyra kända externa/baseline-fel återstår.

- Uppföljning 2026-09-12: commit `8d85c0a` regenererade POT-filen efter CI-felet; både native- och Flatpak-jobbet passerade.

- Uppföljning 2026-09-12: commit `f09bf64` ersätter den flytande GMime-grenen med den verifierade källutgåvan 3.2.15, som innehåller `configure`; ny Flatpak-pipeline startad.

## xdg-desktop-portal-gnome #225 — InputCapture-version på GNOME 50
- Lokal branch: `fix-input-capture-version-50`, commit `a629b1c`.
- Ändring: annonserar InputCapture API-version 2 i `gnome-50`; main annonserar senare version 3.
- Verifierat: `git diff --check`. Lokal Meson-konfiguration stoppas av saknat GTK4-utvecklingspaket.
- Skickad som [xdg-desktop-portal-gnome !272](https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/merge_requests/272); CI kör.

- Uppföljning 2026-09-12: Geary !899:s Flatpak-bygg använder nu GMime 3.2.15 och libhandy 1.6.4 som kontrollerade arkivkällor; pipeline `1108830` kör.
- Uppföljning 2026-09-12: Pango !927:s Windows-fel reproduceras på `main`; de ligger utanför compiler-varningspatchen och lämnas utan orelaterad ändring.
- Uppföljning 2026-09-12: Geary !899 kompilerar nu med aktuell Vala genom att returnera den konfigurerade eller beräknade språklistan direkt; commit `f29d17f` är pushad och ny pipeline kör.
- Uppföljning 2026-09-12: Geary !899 pipeline `1108832` passerade Fedora- och Flatpak-jobben efter beroende- och Vala-kompatibilitetsfixarna.
- Uppföljning 2026-09-12: GNOME Shell !4410 skickad för #9413; kortlivade notifieringssändare får en 500 ms-graceperiod. `tools/run-eslint.sh js/ui/notificationDaemon.js` passerar.
- Uppföljning 2026-09-12: GNOME Shell !4410 pipeline `1108844` passerade och MR:n är mergebar.

## GNOME Shell #urklippshistorik — ändringssignal

[GNOME Shell !4411](https://gitlab.gnome.org/GNOME/gnome-shell/-/merge_requests/4411) exponerar signalen `changed` på `St.Clipboard` när ägaren till systemurklippet byts. Bygget i CI passerade; den enda testkörningen föll i det befintliga intermittenta testet `closeWithActiveWindows`, och körs om.

- Uppföljning 2026-09-12: GNOME Shell !4411 byggde hela projektet i pipeline `1108847`. Den enda felande testen var `closeWithActiveWindows`; samma test föll i två körningar medan övriga 21 tester passerade. Ändringen berör endast `StClipboard` och testet skapar/förstör testfönster; ingen godtycklig ändring av testet skickas.
- Baslinje verifierad 2026-09-12: GNOME Shells `main`-pipeline `1108600` för commit `fa82d28c` föll i exakt samma `closeWithActiveWindows`-test; efterföljande `main`-pipeline `1108709` passerade. !4411:s två testfel är därför ett känt intermittent baslinjefel.

## gdk-pixbuf #308 — ICNS-läsning utanför buffert

Lokal commit `80407c1ea` lägger gränskontroller vid varje RLE-läsning och för den avbrutna 128×128-preamble-läsningen. Reproduceraren accepteras på ofixad `master` men avvisas av den patchade laddaren; en giltig RLE-ICNS laddas. Hela lokala testsviten passerar (23 tester). Skickad som [gdk-pixbuf !280](https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/merge_requests/280); CI kör.

- Uppföljning 2026-09-12: gdk-pixbuf !280:s Linux-, sanitizer- och MSYS2-byggen passerar. `style-check-diff` rapporterar en clang-format-diff, men jobbet är uttryckligen advisory (`allow_failure`) och dess egna instruktioner säger att projektets GTK-kodstil går före formatterarens förslag; den befintliga tabbindenteringen i `io-icns.c` behålls. MSVC-bygget passerade. Därmed passerar alla blockande CI-jobb; formatteringsjobbet är fortsatt en icke-blockerande rekommendation.

## Shotwell #5195 — onödiga nätverksläsningar vid import

Skickad som [Shotwell !112](https://gitlab.gnome.org/GNOME/shotwell/-/merge_requests/112), commit `ae34254c`. Kopierade foton analyseras och får miniatyrer från källfilen före kopian; efter kopian uppdateras bara master-sökvägen till målet. Därmed läses inte den nykopierade filens innehåll tillbaka från ett nätverksmonterat bibliotek. `git diff --check` passerar. Lokal Meson-konfiguration saknar `valac`; pipeline `1108865` kör.

## libadwaita #1159 — apply-knapp efter suffixar

Skickad som [libadwaita !1819](https://gitlab.gnome.org/GNOME/libadwaita/-/merge_requests/1819), commit `88f14d20`. Apply-knappen är nu en trailing action efter suffixwidgets, så lösenordsradens visa/dölj-knapp ligger före den. Regressionstestet kontrollerar mallens ordning. `git diff --check` passerar. Lokal konfiguration stoppas av GLib 2.88.0 medan huvudgrenen kräver 2.89.3; CI startar.

## libmanette #53 — egen GLib-main context

Skickad som [libmanette !159](https://gitlab.gnome.org/GNOME/libmanette/-/merge_requests/159), commit `e6daef5`. HID-pollning, evdevs IO-watch och Steam Decks rumble-timeout fästs nu i den tråd-lokala main contexten. Det gör att program med en pushad egen context får händelser där, samtidigt som standardloopen används när ingen egen context finns. `git diff --check` passerar. Lokal Meson-konfiguration stoppas av saknat `libevdev`; CI bygger och testar ändringen.

- Uppföljning 2026-09-12: Epiphany #1859 är redan löst i upstream-MR !2182; ingen dubblett skickades.

## GNOME Connections #209 — F10 i RDP

Skickad som [GNOME Connections !187](https://gitlab.gnome.org/GNOME/gnome-connections/-/merge_requests/187), commit `a21c59c`. När en fjärrdisplay visas konsumeras F10 efter att displayen har tagit emot händelsen, så GTK:s standardnavigering inte flyttar fokus till Tillbaka-knappen. `git diff --check` passerar. Lokal Meson-konfiguration stoppas av saknat `valac`; CI kör.

- Uppföljning 2026-09-12: Shotwell !112:s båda Flatpak-byggen passerade.

## Uppföljning 2026-09-12

- Nautilus [!2127](https://gitlab.gnome.org/GNOME/nautilus/-/merge_requests/2127) passerade alla automatiska jobb: Flatpak, Fedora Rawhide, kodstil, POT och täckning. De återstående ASan- och aarch64-jobben är manuella.
- GNOME Connections [!187](https://gitlab.gnome.org/GNOME/gnome-connections/-/merge_requests/187) passerade Flatpak; Fedora-jobbet är manuellt.
- GNOME Shell #9327 är redan löst i glycin [!470](https://gitlab.gnome.org/GNOME/glycin/-/merge_requests/470); ingen dubblett skickas.
- gThumb [!63](https://gitlab.gnome.org/GNOME/gthumb/-/merge_requests/63) kör Flatpak-CI.

## Console #384 — xdg-terminal-exec
[Console !198](https://gitlab.gnome.org/GNOME/console/-/merge_requests/198) lägger till `X-ExecArgs=-e` i desktop-filen. Console har redan stöd för `-e`; metadata gör att `xdg-terminal-exec` kan skicka kommandoargument på det sätt som specifikationen anger.

Båda GitLab-pipelines (1108883 och 1108885) är gröna: release-tarball, coverage, Fedora (GCC/Clang), Flatpak (x86_64/aarch64) och samtliga GNOME OS-sanitizerbyggen passerar.

- Uppföljning 2026-09-12: ersatte felaktiga `X-ExecArgs` med kompatibilitetsnyckeln `X-ExecArg`, som den installerade `xdg-terminal-exec` faktiskt läser. En isolerad XDG-miljö väljer `org.gnome.Console.desktop` med den nya desktop-filen. Commit `4ad9d2f` är pushad; pipeline `1108914` passerade helt.

## gtk-frdp / GNOME Connections #203 — RDP-loop vid död värd
[gtk-frdp !34](https://gitlab.gnome.org/GNOME/gtk-frdp/-/merge_requests/34) ändrar felvägen efter `freerdp_check_event_handles()`: idle-källan stoppas och den befintliga frånkopplingsvägen köas. Det förhindrar att den misslyckade kontrollen körs på nytt omedelbart och lämnar CPU-användningen hög när RDP-värden slutat svara.

MR:n har ingen pipeline eftersom projektet saknar CI-konfiguration. `git diff --check` passerar. Den är öppen och har inga kommentarer eller granskningar.

## Uppföljning 2026-09-12 — pipelineåtgärder
- GIMP [!3000](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/3000): clang-format avvek i den ändrade färgramefunktionen. Formateringen är korrigerad i `74ea32dd0f`; ny pipeline 1108894 har passerat commit-logg, clang-format och beroendebygget. Debianbygget kör fortfarande.
- GNOME Shell [!4411](https://gitlab.gnome.org/GNOME/gnome-shell/-/merge_requests/4411): det enda misslyckade jobbet är den tidigare reproducerade flakiga baslinjetesten `closeWithActiveWindows`; övriga bygg-, lint- och referensjobb passerar.
- NetworkManager-openvpn [!117](https://gitlab.gnome.org/GNOME/NetworkManager-openvpn/-/merge_requests/117) och Pango [!927](https://gitlab.gnome.org/GNOME/pango/-/merge_requests/927) har plattformsberoende CI-fel som kräver full felutskrift för en källkodsfix; de har inte ändrats på gissning.

## Pango !927 — Windows-CI
[!927](https://gitlab.gnome.org/GNOME/pango/-/merge_requests/927) fick två uppföljningscommitar efter Windows-felen:

- `0eef67d`: Meson provar `-Wno-error=unused-but-set-global` före användning, så äldre MinGW-GCC inte får en okänd varningsflagga.
- `d759ec1`: MSYS2-jobbet aktiverar Fontconfig som det redan installerar, så render- och fontliststegen får den dependency de använder.

Pipeline 1108899 kör på GitLab.

## Kalender #1454
Ingen dubblettpatch: aktuell libadwaita annonserar vid visning av en `AdwToast` dess titel och knapp via `gtk_accessible_announce()`. Detta åtgärdar exakt den Orca-timing som rapporten beskriver.

### Uppföljning: Pango Windows-CI
Pipeline 1108899 för !927 passerar referens, Fedora och sanitizer. MSYS2 och Visual Studio fallerar, men samma två jobb fallerar också i GNOME/Pangos senaste `main`-pipeline 1108386 (commit `8e74c27c`). Det är en upstream Windows-CI-baslinje och inte en regression i MR:n.

## Kontrollcenter #3756
Tecla kan ta emot ett layoutnamn men får för `custom` bara id:t, inte den kompositörbyggda keymapen. Skalets ”Show Keyboard Layout” startar Tecla utan layoutargument och visar därför aktuell keymap. En korrekt förhandsvisning av en vald, icke-aktiv custom-källa behöver ett API för just den källans serialiserade keymap; ingen felaktig fallback skickas.

## GNOME Settings Daemon #952
`find_timezone()` använder rå GeoClue-koordinater och sorterar tzdb:s platser efter geodetiskt avstånd. Systemets tzdb innehåller `America/Cancun` på `+2105-08646`, så den rapporterade platsen bör väljas före Mexico City. Rapporten saknar GSD:s `Got location <lat>,<lon>`-rad; utan den går det inte att skilja felaktig GeoClue-position från en algoritmregression. Ingen zonhårdkodning skickas.

## GIMP #16104
Ingen dubblettpatch. Aktuell master anropar `gimp_image_resize_to_layers()` efter varje lagerkopia, även när bilden saknar markering, och lagrar minsta lagerförskjutning för in-place-klistring. Detta trimmas bort transparent canvas runt ett mindre kopierat lager och hanterar lager som ligger delvis utanför bilden, vilket är exakt regressionen som rapporterades för 3.2.0.

## GIMP #16163
Ingen dubblettpatch: upstream [GIMP !2290](https://gitlab.gnome.org/GNOME/gimp/-/merge_requests/2290), ”Undo actions for filter visibility”, är kopplad till ärendet, har passerat CI och är planerad för 3.3.2.

## GNOME Disks #496
Ingen dubblettpatch. Upstream-commit `9522d080` (”drive: Reconcile block changes by UDisks object identity”, 2026-08-06) uppdaterar managerns blockändringsväg så att återanslutna loop-enheter hittar eller skapar rätt sidomodellpost.

## GIMP #15595 — endian-känslig flyttalsimport

Källkontroll bekräftar felet: `file-raw-data.c` normaliserade heltal men inte 16-/32-bitars flyttalsord. En lokal gren `fix-raw-float-endianness` korrigerar både sammanhängande och planär import samt förhandsvisning. `git diff --check` och ändringsbegränsad `clang-format-diff` är rena. Lokal Meson-konfiguration slutfördes efter installation av GIMP:s utvecklingsberoenden. `file-raw-data.c` kompilerar rent; den lokala aarch64-länkningen faller sedan på befintliga GIMP-UI-symboler. GitLab-pipeline `1108905` passerade helt: Debian-bygg, ABI-kontroll, dokumentation, Meson, och filinsticks-testsviten. GIMP:s MR-formulär förbjuder uttryckligen AI-genererad kod och text, så ingen MR skickas in.

## Kontrollcenter #3374 — standardterminal

[Kontrollcenter !3486](https://gitlab.gnome.org/GNOME/gnome-control-center/-/merge_requests/3486) lägger till Terminal under Standardappar. Raden hittar TerminalEmulator-poster som stöds av `xdg-terminal-exec`, visar aktuell terminal och skriver användarens GNOME- och generella terminalprioritering. Diffen passerar `git diff --check` och ändringsbegränsad clang-format. Lokal byggning blockeras av systemets GTK 4.22/GLib 2.88 medan projektet kräver GTK 4.23/GLib 2.89; GNOME-CI kör.

## Kontrollcenter #3795 — WWAN utan SIM-ID

[Kontrollcenter !3487](https://gitlab.gnome.org/GNOME/gnome-control-center/-/merge_requests/3487) återanvänder enhetens aktiva NetworkManager-profil när ingen sparad profil matchar modemets SIM-ID. Det visar profilens faktiska roaming- och autoconnect-värden och säkerställer att ändringar committas till den befintliga fjärrprofilen. Pipeline `1108925` passerade helt: Fedora, GNOME OS, ASan, UBSan, LSan, statisk analys, täckning och kodstil.

## Kontrollcenter #3800 — bevara vald ljudutgång

MR [!3488](https://gitlab.gnome.org/GNOME/gnome-control-center/-/merge_requests/3488) blockerar komboradens urvals-signal medan en borttagen utgång tas ur modellen. Därmed kan bara ett avsiktligt användarval anropa `pa_context_set_default_sink()`, och PipeWires `default.configured.audio.sink` ändras inte när WirePlumber väljer en tillfällig reservutgång. `git diff --check` passerar; CI körs.

## Kontrollcenter #3803 — Processor på arm64

MR [!3489](https://gitlab.gnome.org/GNOME/gnome-control-center/-/merge_requests/3489) gör Processor-raden användbar när `/proc/cpuinfo` saknar modellnamn, vilket är normalt på upstream arm64. Den använder först enhetsträdets maskinmodell och sedan CPU-arkitekturen som garanterad reserv. `git diff --check` passerar; CI körs.

## Kontrollcenter #3736 — inspelningsnivåer

Utredning visar att nivåmätaren för `GvcMixerSourceOutput` använder `pa_stream_set_monitor_stream()`, som bara är avsedd för uppspelningsströmmar, och ansluter till source-output-indexet i stället för källan som strömmen spelar in från. En förberedd libgnome-volume-control-ändring (`52b39e7`) sparar den korrekta källans index vid varje uppdatering; den klarar syntaxkontroll. Kontrollcentrets följdändring inväntar att libgvc-ändringen kan publiceras.

## Kontrollcenter #3770 — Wayland-avstängning

MR [!3490](https://gitlab.gnome.org/GNOME/gnome-control-center/-/merge_requests/3490) undviker att förstöra öppna genvägsdialoger efter att Wayland-displayen är stängd. Den normala vägen lämnas oförändrad. Branchens fristående style-jobb saknade forkens ref, medan MR-pipelinen nu kör den faktiska ändringen.

## libgnome-volume-control — inspelningskälla

MR [!39](https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/merge_requests/39) exponerar källindexet för varje inspelningsström. Den är beroendet för den förberedda Kontrollcenter-ändringen till #3736. Lokal C-syntaxkontroll passerar.

## Power Saver: Dim Screen ignored (#3812)

- Orsak: `gsd-power-manager` satte en 30-sekunders dimningsvakt i Power Saver innan den kontrollerade `idle-dim`.
- MR: https://gitlab.gnome.org/GNOME/gnome-settings-daemon/-/merge_requests/494
- Ändring: kontrollera `idle-dim` före valet av Power Saver- eller normal timeout.
- Lokal validering: `meson setup` (med valfria orelaterade plugins avstängda) och `meson compile -C build` passerar.
