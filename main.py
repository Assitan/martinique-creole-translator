from bs4 import BeautifulSoup
import requests

with open("Le-premier-dictionnaire-du-creole-martiniquais.html", "r") as fp:
    content = fp.read()
soup = BeautifulSoup(content, 'html.parser')

# content = requests.get('https://www.potomitan.info/dictionnaire/francais.php')
# soup = BeautifulSoup(content, 'lxml')

tags = soup.find_all('p')
# print(tags)
paragraph = tags[5:len(tags) - 20]
for p in paragraph:
    lines = p.text.replace(' ', '')
    trad = lines.replace(':', '\t')
    # append text
    with open(f'creole.txt', 'a') as f:
        f.write(trad)
