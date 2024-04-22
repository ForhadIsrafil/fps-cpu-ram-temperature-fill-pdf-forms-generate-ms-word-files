from ahk import AHK
from ahk.directives import NoTrayIcon
import pandas as pd
import time

ahk = AHK(directives=[NoTrayIcon])
ahk.set_clipboard("")


def copy_excel_file(value):
    df = pd.read_excel("data.xlsx")
    df.loc[len(df.index)] = [value.strip()]
    df.to_excel("data.xlsx", index=False)


old_d = ''

while True:
    d = ahk.get_clipboard()
    if d != None:
        if d.strip() != "":
            if old_d != d:
                print(d)
                copy_excel_file(d)
                old_d = d
    time.sleep(0.5)


