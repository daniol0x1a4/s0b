Directory enumeration tool build with the requests library.

> Usage: python3 s0b.py {domain} {wordlist} {cookie} {verbose}
- {domain} = enter target domain 
- {wordlist} = path to your wordlist
- {cookie} = enter custom cookie value if you dont need that just write default or something.
- {verbose} = shows all Status codes, if you leave it blank only 200 Respone Codes will show up (enter any character to activate)

examples:

- normal scan 
  `python3 s0b.py example.org rockyou.txt`
- with custom cookie value
  `python3 s0b.py example.org rockyou.txt cookievalue`
- verbose mode
  `python3 s0b.py example.org rockyou.txt cookie value x`  
