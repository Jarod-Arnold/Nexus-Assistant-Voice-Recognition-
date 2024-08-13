# *****************************************************************************
# Author: Jarod Arnold
# Version Date: 7/7/2024
# Description: A voice recognition program that executes functions like:
# Search the internet, open / close applications, type whats dictated, and more
# Input: Press F12 to initiate voice listening to execute commands
# Output: opening / closing of applications, keyboard presses, TTS
# *****************************************************************************

import pyttsx3
import speech_recognition as sr
import keyboard
import threading
import winsound
import time
from config import *
from macros_pyautogui import *
from web_search import *
from time_cmd import current_time
from recorder import record, is_recording_macro
from playback import playActions

# Initialize speech engine
engine = pyttsx3.init()
# listening_thread_running = False #! BUGGED always leaves listen thread open, present on lines 63, 64, 143, 145
#! Listen thread closes after command wihtout this flag

def speak(text): #* CHANGED IN V8, REMOVED ENGINE.RUNANDWAIT FOR STARTLOOP, SAY, ITERATE, ENDLOOP,STOP. 
    #* PREVENTS LISTEN THREAD FROM STAYING OPEN
    engine.setProperty('rate', 180) #! ADDED IN V8
    try:
        engine.startLoop(False)  # Manually start the engine's processing loop if not already started
        engine.say(text)
        engine.iterate()  # Process pending events in the engine's loop
        print("Nexus:", text)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        engine.endLoop()  # Manually end the engine's processing loop if it was started
        engine.stop()  # Ensure engine is stopped after speaking


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            print("-"*30)
            return query.lower()  # Convert to lowercase for consistency
        except Exception as e:
            print("Say that again please...")
            return None
        

def set_voice_volume(volume_level):
    volume = min(max(volume_level, 0), 1.0)
    engine.setProperty('volume', volume)
    speak(f"Volume set to {int(volume * 100)} percent.")
    return


def start_listening():
    global is_recording_macro
    if is_recording_macro:
        return
    
    spoken_query = take_command()
    if spoken_query:

        #* Application commands
        for command, path in app_paths.items():
            if command in spoken_query:
                open_application(path)
                return

        for command, process_name in close_commands.items():
            if command in spoken_query:
                close_application(process_name)
                return
            

        #* Type and enter command
        if "nexus write this" in spoken_query:  #! ADDED IN V5
            text = take_command()
            if text:
                type_and_enter(text)
            return


        #* Macro commands
        if spoken_query in macros:  #! ADDED IN V6
            macros[spoken_query]()
            return
        
        #* More Macro commands / Click commands
        if "clic" in spoken_query: #! ADDED IN V8
            try:
                words = spoken_query.split()
                click_index = words.index("clic")
                click_count = words[click_index + 1]
                click_mouse(click_count) 
                speak(f"Clicked {click_count} times.")
                return
            except (IndexError, ValueError):
                speak("Please specify the number of clicks.")
                return
            
        
        #* Macro Recording and Playback
        if "record macro" in spoken_query:
            try:
                speak("Prepare to record macro")
                record()
            except Exception as e:
                speak("Unexpected error" + str(e))
            return
        
        macro_name = spoken_query.strip().lower()
        macro_files = [f[:-5] for f in os.listdir('recordings') if f.endswith('.json')]  # Get all filenames without extension
        if macro_name in macro_files:
            try:
                filename = f"{macro_name}.json"
                playActions(filename)
                return
            except Exception as e:
                speak(f"Error executing macro: {e}")
                return

        #* Webpage commands
        for command, webpage in webpages.items():
            if command in spoken_query:
                open_webpage(webpage)
                return
            
        if "search the web for" in spoken_query: #! ADDED IN V8
            web_query = spoken_query.replace("search the web for", "").strip()
            search_web(web_query)
            speak(f"Searching the web for {web_query}")
            return
            
        if "open website" in spoken_query: #! ADDED IN V8
            web_query = spoken_query.replace("open website", "").strip()
            open_website(web_query)
            return


        #* Time commands    
        if "nexus what time is it" in spoken_query or "what time is it" in spoken_query:
            time_speak = f"It is currently {current_time()}"
            speak(time_speak)
            return


        #* TTS commands
        if "nexus set voice volume to"  in spoken_query:
            try:
                volume_level = float(spoken_query.split()[-1]) /100
                set_voice_volume(volume_level)
            except ValueError:
                speak("Please specify a valid volume between 0 and 100.")
            return

        if not is_recording_macro:
            speak("Command not recognized.")
            engine.stop()
            return
            

def on_press_f12(event):
    # global listening_thread_running
    if event.name == 'f12':
        # if not listening_thread_running:
            print("F12 pressed. Starting listening...")
            threading.Thread(target=start_listening).start()
            winsound.Beep(350,100)
    else:
            print("Listening thread is already running.")


def main():
    keyboard.on_press_key('f12', on_press_f12)

    print("Press F12 to start listening...")

    while True:
        # Your main application logic can continue here
        # This loop will run concurrently with the listener threads
        input_command = input("Enter a command ('exit' to quit): ").lower().strip()
        if input_command == 'exit':
            print("Exiting...")
            break

    # Cleanup: Unhook the F12 key listener
    keyboard.unhook_all()

    engine.stop()

if __name__ == "__main__":
    main()
