import re
from bs4 import BeautifulSoup

# get list of suburbs
with open('suburbs.txt', 'r') as f:
    t = f.readlines()
r1 = re.compile('href="(.*?)"')
l = list(map(lambda x: r1.search(x), t))
l = [x.group(1) for x in l if x is not None]
    
mmap = []

for i, d in enumerate(l):
    with open(f"malton/{d.replace('/index.php/', '')}.html") as f:
        soup = BeautifulSoup(f, "html.parser")
        submap = soup.find(id='Suburb_Map').find_all_next('tbody')[2]
    
    # remove links and imgs
    for a in submap.find_all("a"):
        a.unwrap()
    for img in submap.find_all("img"):
        img.extract()

    # finds all tr tags
    for j, r in enumerate(submap.find_all("tr")):
#         print(i,j,d)
        if (i%10==0):
            mmap.append(str(r))
        else:
            mmap[i//10*10+j] += str(r)
            
# combine rows
for i, r in enumerate(mmap):
    mmap[i] = r.replace('</tr><tr style="height:10%">', '')

head = '''<html>
<table style="background:inherit; margin:auto; padding:5px; color:inherit; text-align:center;">
<tbody><tr>
<td><b>Malton</b>
</td></tr>
<tr>
<td>
<table style="border:1px solid black; font-size:.75em; line-height:100%; width:700px; height:600px; margin:auto;font-family: sans-serif; text-align: center;">
'''

tail = '''</table></td></tr></tbody>
</table>'''

with open('map.html', 'w') as f:
    f.write(head+'\n'.join(mmap)+tail)