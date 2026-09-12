# Name Shift

Name Shift is a local GTK 4 batch rename tool. Choose files, describe the name change, inspect every resulting filename, and explicitly apply the valid plan.

It keeps extensions intact and refuses duplicate targets, existing unselected targets, target swaps, and unchanged names. It does not scan folders or rename anything until **Rename files** is pressed.

```sh
python3 name_shift.py
```

Run the backend checks with:

```sh
python3 -m pytest tests
```
