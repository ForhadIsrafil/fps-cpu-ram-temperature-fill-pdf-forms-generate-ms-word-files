from ahk import AHK
from ahk.directives import NoTrayIcon
import pandas as pd
import time

ahk = AHK(directives=[NoTrayIcon])
ahk.set_clipboard("")


def copy_txt_file(value):
    with open("data.txt", 'a', encoding='utf-8') as f:
        f.write(value + '\n')


old_d = ''

while True:
    d = ahk.get_clipboard()
    if d != None:
        if d.strip() != "":
            if old_d != d:
                print(d)
                # with open("data.txt", 'a', encoding='utf-8') as f:
                #     f.write(d + '\n')
                copy_txt_file(d)
                old_d = d
    time.sleep(0.5)


