# libadwaita-theme-changer

Theme changer for Libadwaita

## Disclaimer!

Use this script at your own risk!

## How it works?

It creates symlinks between `~/.local/share/themes` and `~/.config` with assets and GTK 4.0 theme CSS files.

## Requirements

- Selected theme must support GTK 4.0

## How to use?

1. Clone this repository:

```sh
git clone https://github.com/otapliger/libadwaita-theme-changer
```

2. Add run permissions to the script:

```sh
chmod +x libadwaita-tc.py
```

3. Run it:

```sh
./libadwaita-tc.py
```

## How to reset to default Adwaita theme?

Run script with --reset parameter:

```sh
./libadwaita-tc.py --reset
```
