# A TIME MODULE
## MORE FUNCTIONALITY TO BE ADDED

import datetime
from time import time

current_time = datetime.datetime.now()

def current_time():
    return time.strftime('%I:%M %p')
