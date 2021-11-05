
#daniol0xA41
# usage: python3 s0b.py {domain} {wordlist} {cookie} {verbose}

import time
import requests
import sys
from termcolor import colored
import pyfiglet

text = pyfiglet.figlet_format("s0b")
colortext = colored(text, 'yellow')
text2 = "// Directory enumeration // version 0.5"
colortext2 = colored(text2, "yellow")
print(colortext)
print(colortext2)

try:
    rawcookie = {sys.argv[3]}
    cookie = dict(value=f"{rawcookie}")
    print(f"> domain= {sys.argv[1]}")
    print(f"> cookie= {cookie}\n")
except KeyboardInterrupt:
    exit()
except IndexError:
    cookie = dict(value="defaultvalue")
    print(f"cookie= {cookie}")
    pass

file = f"{sys.argv[2]}"
word_list = open(file).read()
splitlist = word_list.splitlines()

for dir in splitlist:

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

    if r.status_code==200:
        text = f"{r} {r3quest}"
        colortext = colored(text, "green")
        print(colortext)

    if not r.status_code==200:
        try:
            verbose = {sys.argv[4]}
            print(f"{r} {r3quest}")
        except IndexError:
            pass
