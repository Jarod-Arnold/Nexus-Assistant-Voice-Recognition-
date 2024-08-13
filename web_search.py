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
    "open d2l" : "https://login.pcc.edu/cas/login?service=https%3a%2f%2fonline.pcc.edu%2fd2l%2fcustom%2fcas%3ftarget%3d%252fd2l%252flp%252fouhome%252fhome.d2l%253fou%253d6605",
    "open my pcc" : "https://my.pcc.edu", #! REFINED IN V8
    "open chat gpt" : "https://chatgpt.com/", #! ADDED IN V8
}