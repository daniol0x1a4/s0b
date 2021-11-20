# daniol0x1a4

import time
import requests
import sys
from termcolor import colored
import pyfiglet
from rich import print
from rich import inspect
from rich.console import Console
from rich.progress import track
from datetime import datetime

console = Console()

print(f"""[green] 
        "e.  "$$$.
         ^$$bc "$$b
           ^"*$$c$$F
                ^"3$
       .....   .z$$$$"$.
    .d$$$$$$$$$$$$$$$$$$%
   J$$$$$$$$$$$$$$$$$"
  4$$$$$[white][0x1a4][/white]$$$$$$
  $$$$$$$$$$$$$$$$$$
  *$$$$$$$$$$$$$$$$"
 . $$$$$$$$$$$$$$$F
'$$$$$$$$$$$$$"  *$.[/green]
---------------------------------------
| s0b [Directory FUZZ] // version 0.5 |
---------------------------------------
""")

try:
    x = sys.argv[2]
except IndexError:
    print("python3 s0b.py <domain> <wordlist> [white]<cookie> <verbose>[/white]\n")
    exit() 

file = f"{sys.argv[2]}"
word_list = open(file).read()
splitlist = word_list.splitlines()

#cookie input index exception 
try:
    rawcookie = {sys.argv[3]}
    cookie = dict(value= f"{rawcookie}")
    print(f">TargetDomain= {sys.argv[1]}")
    print(f">CookieValue= {cookie}\n")
except KeyboardInterrupt:
    exit()
except IndexError:
    cookie = dict(value="")
    print(f">TargetDomain= {sys.argv[1]}\n")
    pass

 
for dir in track(splitlist):
    
    #this is the actual request 
    r3quest = f"{sys.argv[1]}/{dir}"
   
    try:
        requests.get(r3quest, cookies=cookie)
        r = requests.get(r3quest, cookies=cookie)
    except KeyboardInterrupt:
        exit()
    except requests.ConnectionError:
        print(f"connection error: {sys.argv[1]} not found")
        exit()
    except requests.exceptions.MissingSchema:
        r3quest = f"http://{sys.argv[1]}/{dir}"
        requests.get(r3quest, cookies=cookie)
        r = requests.get(r3quest, cookies=cookie)
        pass
    
    #time for the response
    now = datetime.now()
    currenttime = now.strftime("[%H:%M:%S]")
    
    if r.status_code==200:
        print(f"{currenttime} [green]{r}[/green] {r3quest}")

    if not r.status_code==200:
        try:
            verbose = {sys.argv[4]}
            print(f"[white]{currenttime} {r} {r3quest}[/white]")
        except IndexError:
            pass
    time.sleep(1)
