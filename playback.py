import pyautogui
from time import sleep, time
import os
import json


def main():
    
    initializePyAutoGUI()
    countdownTimer()

    playActions("macro_1.json")

    print("Done")


def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True


def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 5):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")

def load_all_macros(directory_path):
    macros = {}
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            macro_name = os.path.splitext(filename)[0]
            filepath = os.path.join(directory_path, filename)
            try:
                with open(filepath, 'r') as jsonfile:
                    macros[macro_name] = json.load(jsonfile)
            except json.JSONDecodeError:
                print(f"Error decoding JSON from {filepath}.")
    return macros


def playActions(filename):
    # Read the file
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, 'recordings', filename)
    with open(filepath, 'r') as jsonfile:
        # parse the json
        data = json.load(jsonfile)
        
        # Calculate the base delay
        base_delay = 0.025
        
        # Record the start time
        start_time = time()
        
        # Loop over each action
        for index, action in enumerate(data):
            # Calculate the time when this action should be performed
            action_time = start_time + action['time']
            
            # Wait until it's time to perform the action
            current_time = time()
            delay = action_time - current_time
            
            # Ensure we do not sleep for negative or too little time
            # if delay > 0:
            #     sleep(delay)
            
            # Perform the action
            if action['button'] == 'Key.esc':
                break

            if action['type'] == 'keyDown':
                key = convertKey(action['button'])
                pyautogui.keyDown(key)
                print("keyDown on {}".format(key))
            elif action['type'] == 'keyUp':
                key = convertKey(action['button'])
                pyautogui.keyUp(key)
                print("keyUp on {}".format(key))
            elif action['type'] == 'click':
                pyautogui.click(action['pos'][0], action['pos'][1], duration=0.25)
                print("click on {}".format(action['pos']))

            # Wait for the base delay between actions
            sleep(base_delay)



# convert pynput button keys into pyautogui keys
# https://pynput.readthedocs.io/en/latest/_modules/pynput/keyboard/_base.html#Key
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
def convertKey(button):
    PYNPUT_SPECIAL_CASE_MAP = {
        'alt_l': 'altleft',
        'alt_r': 'altright',
        'alt_gr': 'altright',
        'caps_lock': 'capslock',
        'ctrl_l': 'ctrlleft',
        'ctrl_r': 'ctrlright',
        'page_down': 'pagedown',
        'page_up': 'pageup',
        'shift_l': 'shiftleft',
        'shift_r': 'shiftright',
        'num_lock': 'numlock',
        'print_screen': 'printscreen',
        'scroll_lock': 'scrolllock',
    }

    # example: 'Key.F9' should return 'F9', 'w' should return as 'w'
    cleaned_key = button.replace('Key.', '')

    if cleaned_key in PYNPUT_SPECIAL_CASE_MAP:
        return PYNPUT_SPECIAL_CASE_MAP[cleaned_key]

    return cleaned_key


if __name__ == "__main__":
    main()