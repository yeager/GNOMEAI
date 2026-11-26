# Validation

Target: GIMP master, base revision `47f51b5b538cf1b27634b4c6f4f98b553138dbad`.

The patch starts plug-in `query()` calls asynchronously, schedules them in bounded waves, and waits for all results before initialization and plug-in cache registration. Concurrency is half the available CPU threads, with a maximum of eight.

## Startup measurements

Seven cold starts per version, using fresh profiles and the same plug-in set, with the UI in Swedish:

| Metric | Original serial query | Concurrent query | Change |
| --- | ---: | ---: | ---: |
| Plug-in query median | 3355 ms | 879 ms | −73.8% |
| Core restore median | 4756 ms | 2220 ms | −53.3% |
| Time to Swedish main window median | 5322 ms | 2773 ms | −47.9% |

The concurrent main-window samples were 2698–2847 ms except for one 8451 ms Xvfb scheduling outlier. The 2773 ms median is reported as measured; the outlier is retained in that sample set.

## Build and runtime checks

- The changed C sources were compiled and the local GIMP binary relinked.
- A final cold launch completed all 112 plug-in queries with exit status 0.
- Warm profile plug-in-query median was 32 ms.
- No formal GIMP test suite was run for this patch.

## Limitations

The timing comparison used a local Xvfb session; UI wall time can vary with scheduling. The full existing Meson build directory was stale, so validation used the existing local compile configuration and manual relink rather than a clean full build. Query concurrency is intentionally capped at eight to limit startup resource contention.
