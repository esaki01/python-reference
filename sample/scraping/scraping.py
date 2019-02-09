import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.python.org')

soup = BeautifulSoup(html.text, 'html5lib')

titles = soup.find_all('title')
print(titles[0].text)

intro = soup.find_all('div', {'class': 'introduction'})
print(intro[0].text)
