import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://sekolah.data.kemdikbud.go.id/index.php/chome/profil/00fd0c95-2bf5-e011-9d0f-3362f81251aa'

page = requests.get(URL)

soup = bs(page.text, 'html.parser')
s = soup.find('font', class_='small')
b = soup.find_all('li', class_='list-group-item')

c = []
for data in b[1:]:
    result = data.text
    c.append(result)
print(c[1])
print(s.text)
 
# URL = 'https://sekolah.data.kemdikbud.go.id/index.php/chome/profil/400A0D95-2BF5-E011-89BC-41ED4E528912'
# page = requests.get(URL)
 
# soup = bs(page.text, 'html.parser')
# s = soup.find('small')
# # tag = s.font
# print(s.text)

# lines = s.find_all('p')

# for line in s:
#     print(line.text)
 
# titles = soup.find_all('div', attrs={'class', 'head'})
# titles = soup.find_all('table', class_={'table', 'table-hover', 'table-striped', 'dataTable' })
# titles_list = []
 
# count = 1
# for title in lines:
#     d = {}
#     d['No'] = f'{count}'
#     d['Nama Sekolah'] = title.text
#     count += 1
#     titles_list.append(d)
 
# filename = 'titles6.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f,['No','Nama Sekolah'])
#     w.writeheader()
     
#     w.writerows(titles_list)