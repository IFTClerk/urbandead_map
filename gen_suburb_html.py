import re
import requests

with open('suburbs.txt', 'r') as f:
    t = f.readlines()
    
r1 = re.compile('href="(.*?)"')

l = list(map(lambda x: r1.search(x), t))
l = [x.group(1) for x in l if x is not None]

for d in l:
    s = d.replace('/index.php/', '')
    print(f"Getting wiki page for {s}")
    req = requests.get('http://wiki.urbandead.com' + d)
    with open(f"malton/{s}.html", 'w') as f:
        f.write(req.text)