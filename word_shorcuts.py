from ahk import AHK
import pyautogui
ahk = AHK()



if "__main__" == __name__:

    while True:
        # ahk.key_down('ctrl')  # Press down (but do not release) Control key
        # ahk.key_up('ctrl')  # Release the key

        ctrl_key = ahk.key_state('ctrl')
        alt_key = ahk.key_state('alt')
        a_key = ahk.key_state('a')

        if ctrl_key == 1 and alt_key==1 and a_key == 1:
            print(ctrl_key)
            print(alt_key)
            print(alt_key)
            # print("ä")
            ahk.type("ä")


