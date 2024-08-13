# A PYAUTOGUI MODULE FOR HOTKEYS, MACRO'S, AND OTHER FUNCTIONS
## MORE FUNCTIONALITY TO BE ADDED LATER

import pyautogui as pg



## ARROW KEYS
# pg.press('up')
# pg.press('down')
# pg.press('left')
# pg.press('right')


def save_file():
    pg.hotkey ('ctrl', 's')


def copy_all():
    pg.hotkey('ctrl', 'a', 'ctrl', "c")


def paste():
    pg.hotkey('ctrl', 'v')

def close_tab():
    pg.hotkey("ctrl", "w")

def type_and_enter(text):
    pg.typewrite(text)
    pg.press('enter')

def click_mouse(click_count): #! MOVED FROM MAIN IN V8
    click_count = int(click_count)
    pg.click(clicks=click_count)


macros = {
    "save file" : save_file,
    "copy all" : copy_all,
    "paste" : paste,
    "close tab" : close_tab,
    "click mouse" : click_mouse,
}