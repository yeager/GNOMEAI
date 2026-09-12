# Extension Pack Installer

A local GNOME Shell extension ZIP installer. It validates archive paths and `metadata.json`, refuses to overwrite an installed UUID, and writes only after the user clicks **Install locally**.

```sh
python3 extension_pack_installer.py
pytest -q
```
