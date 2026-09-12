# Clip Shelf

Clip Shelf is a small GTK 4 app for keeping a local, manual history of clipboard text.

It never watches the clipboard. A text item is stored only after selecting **Capture clipboard**. The history is limited to 100 unique entries and stored at `$XDG_STATE_HOME/clip-shelf/items.json` with user-only file permissions.

## Run

```sh
python3 clip_shelf.py
```

Dependencies: Python 3, PyGObject, GTK 4.
