#!/bin/python3
import sys
import os
import subprocess as sp


if __name__ == "__main__":
    try:
        home = os.getenv('HOME')
        config = "/.config"
        themes = "/.local/share/themes"
        sp.run(["mkdir", "-p", f'{home}{config}/gtk-4.0'])
        sp.run(["mkdir", "-p", f'{home}{themes}'])
        if "--reset" in sys.argv:
            sp.run(["rm", f'{home}{config}/gtk-4.0/gtk.css'])
            sp.run(["rm", f'{home}{config}/gtk-4.0/gtk-dark.css'])
            sp.run(["rm", f'{home}{config}/gtk-4.0/assets'])
            sp.run(["rm", f'{home}{config}/assets'])
        else:
            all_themes = str(sp.run(["ls", f'{home}{themes}/'], stdout=sp.PIPE).stdout.decode("UTF-8")).split()
            for i, theme in enumerate(all_themes):
                print(f'{i+1}. {theme}')
            chk = input("Select a theme or type (e) to exit: ")
            match chk:
                case "e":
                    sys.exit()
                case _:
                    chk_value = int(chk)-1
                    chk_theme = all_themes[chk_value]
                    print(f'Installing {chk_theme}')
                    sp.run(["rm", "-f", f'{home}{config}/gtk-4.0/gtk.css'])
                    sp.run(["rm", "-f", f'{home}{config}/gtk-4.0/gtk-dark.css'])
                    sp.run(["rm", "-f", f'{home}{config}/gtk-4.0/assets'])
                    sp.run(["rm", "-f", f'{home}{config}/assets'])
                    sp.run(["ln", "-sf", f'{home}{themes}/{chk_theme}/gtk-4.0/gtk.css', f'{home}{config}/gtk-4.0/gtk.css'])
                    sp.run(["ln", "-sf", f'{home}{themes}/{chk_theme}/gtk-4.0/gtk-dark.css', f'{home}{config}/gtk-4.0/gtk-dark.css'])
                    sp.run(["ln", "-sf", f'{home}{themes}/{chk_theme}/gtk-4.0/assets', f'{home}{config}/gtk-4.0/assets'])
                    sp.run(["ln", "-sf", f'{home}{themes}/{chk_theme}/assets', f'{home}{config}/assets'])
    except ValueError:
        print("Incorrect value. Please try again!")
