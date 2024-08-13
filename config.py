# CONFIG FILE TO HOLD ALL HARDCODED OPEN / CLOSE APPLICATION PATHS, AND OPEN WEB PAGES
import os

def open_application(path): #! ADDED IN V4
    os.startfile(path)


def close_application(process_name): #! ADDED IN V4
    os.system(f"taskkill /im {process_name} /f")


app_paths = {
"""
These were hard coded paths in a dictionary structured as:
'command name (close chrome) : path/to/chrome' 
"""
}

close_commands = {
"""
These were hard coded paths in a dictionary structured as:
'command name (close chrome) : app.exe' 
"""
}
