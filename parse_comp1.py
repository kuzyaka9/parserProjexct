import requests
from bs4 import BeautifulSoup
import time
import re



f = open('NormTags.txt', 'r', encoding = 'utf-8')
lines = f.readlines()
f.close()
links = []
for line in lines:
    links.append(re.sub('[\t\r\n]', '', line[line.find('https')::]))

companies_links = set()

count = 0
for link in links:
    page = 0
    lst = []    
    while True:
        page += 1
        url = link[0:link.find('предприятия/')+12]+'pg-'+str(page)+link[link.find('предприятия/')+11::]
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml') 
        if (r.status_code == 410):
            break          
        lst = soup.find_all('div', class_ = 'company-info')
        for item in lst:
            comp_link = item.find('a', class_ = 'company-name display-spinner').get('href')
            companies_links.add(comp_link)
            count += 1
        time.sleep(0.5)
    if (count >=10000):
        file = open('ans_comp.txt', 'w', encoding = 'utf-8')
        for elem in companies_links:
            file.write(elem+'\n')
        file.close()
        count = 0
file = open('ans_comp.txt', 'w', encoding = 'utf-8')
for elem in companies_links:
    file.write(elem+'\n')
file.close()

    