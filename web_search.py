# A MODULE FOR WEB SEARCHES
## IMPLEMENTED LATER? HAVE TO FIGURE OUT HOW TO PROPERLY ADD THE SEARCH WEB FUNCTION HERE

import webbrowser

def open_webpage(url):
    webbrowser.open(url)

def search_web(query): 
    query = query.replace(" ", "+")
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    return

def open_website(query):
    search_url = f"https://{query}"
    webbrowser.open(search_url)
    return

webpages = {
    'open dnd map' : "https://darkanddarker.map.spellsandguns.com/map/Crypt-01-N",
    "open youtube" : "https://www.youtube.com",
    "open chat gpt" : "https://chatgpt.com/",
}
