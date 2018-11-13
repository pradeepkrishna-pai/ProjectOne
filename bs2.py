from bs4 import BeautifulSoup as bs
from collections import OrderedDict
import pandas as pd

with open('The Shooting Star _ Just a girl who travels..html') as f:
    soup = bs(f, 'lxml')

d = OrderedDict()
d['Title'] = []
d['Date'] = []
d['Link'] = []
for article in soup.find_all('article'):
    try:
        title = article.h3.text
        d['Title'].append(title)
    except:
        d['Title'].append('None')
    try:
        link = article.h3.a['href']
        d['Link'].append(link)
    except:
        d['Link'].append('None')
    try:
        date = article.find('div', class_='entry-date').text
        d['Date'].append(date)
    except:
        d['Date'].append('None').encode('utf-8')
        
df = pd.DataFrame(d)
writer = pd.ExcelWriter('excel_test.xlsx', engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = 'Test Sheet')
writer.save()