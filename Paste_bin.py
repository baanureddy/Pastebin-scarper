import requests
import json
import re
from bs4 import BeautifulSoup

#pattern = r'([A-Za-z]+) ([0-9]+(st|nd|rd|th)), ([0-9]+)'
pattern = r'/[a-zA-Z0-9]{8}'
url = 'https://pastebin.com/search?q=hotstar&sort=-date'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}
cookies = {'_identity-frontend': '<session-cookie>','__viCookieActive': 'true'}

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
