import requests
import json
import re
from bs4 import BeautifulSoup

#pattern = r'([A-Za-z]+) ([0-9]+(st|nd|rd|th)), ([0-9]+)'
pattern = r'/[a-zA-Z0-9]{8}'
url = 'https://pastebin.com/search?q=hotstar&sort=-date'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}
cookies = {'_identity-frontend': '4d86740c4b73d87eb236d5defa4d902e0dc4da933dc21ebad817b7f4d2f18c69a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A53%3A%22%5B9311630%2C%22k8zpYILS9cHp5xnoXIQva5pxu2j7dk6N%22%2C15552000%5D%22%3B%7D','__viCookieActive': 'true'}

response = requests.get(url, headers=headers, cookies=cookies).text
soup = BeautifulSoup(response, 'html.parser')
#print(soup.get_text())

list_key=[]
for link in soup.find_all('a'):
    list_key.append(link.get('href'))

matches = re.findall(pattern, '\n'.join(list_key))
unique_strings = list(set(matches))
with open('strings.txt', 'r') as f:
    data = [line.strip() for line in f]
missing_strings = set(unique_strings) - set(data)
print(missing_strings)

with open('strings.txt', 'a') as f:
    f.writelines('%s\n' % string for string in missing_strings)