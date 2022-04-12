
# s0b.py -- dir


its pretty slow and shitty, it is based on a python challenge from tryhackme.com (this was in my first week in python pls dont judge)

> Usage: python3 s0b.py {domain} {wordlist} {cookie} {verbose}
- {domain} = enter target domain 
- {wordlist} = path to your wordlist
- {cookie} = enter custom cookie value if you dont need that just write default or something.
- {verbose} = shows all Status codes, if you leave it blank only 200 Respone Codes will show up (enter any character to activate)


examples:

- normal scan 
  `python3 s0b.py example.org dir.txt`

- with custom cookie value (dont work at moment)
  `python3 s0b.py example.org dir.txt cookievalue`
  
- verbose mode
  `python3 s0b.py example.org dir.txt cookievalue x`  
