import requests
from bs4 import BeautifulSoup
import time
import re
import json


file = open('ans_comp.txt', 'r', encoding = 'utf-8')
tmplinks = file.readlines()
file.close()
links = []
for link in tmplinks:
    links.append(re.sub('[\t\r\n]', '', link[link.find('https')::]))
data = []
print(len(links))
kol = 0
for link in links:
    tmp_data = dict()
    comp_id= link[link.rfind('/')+1:link.find('.html')]
    url_data = 'https://www.europages.com.ru/ep-api/v2/epages/'+str(comp_id)+'?lang=ru'
    url_phone = 'https://www.europages.com.ru/ep-api/v2/epages/'+str(comp_id)+'/phones'
    r = requests.get(url_data)
    arr = json.loads(r.text)
    tmp_data["Страна"] = arr['address']['countryCode']
    tmp_data["Название"] = arr['name']
    if ('streetName' in arr['address'].keys()):
        tmp_data['Адрес'] = arr['address']['city']+', '+arr['address']['streetName']
    else:
        tmp_data['Адрес'] = arr['address']['city']
    if ('websiteUrl' in arr.keys()):
        tmp_data['Сайт'] = arr['websiteUrl']
    tmp_data['Сфера деятельности'] = arr['keywords']
    r = requests.get(url_phone)
    arr = json.loads(r.text)   
    if (arr):
        tmp_data['Телефон'] = ''
        for i in range(len(arr['phones'][0]['items'])):
            tmp_data['Телефон'] += arr['phones'][0]['items'][i]['number']+', '
        tmp_data['Телефон'] = tmp_data['Телефон'][0:tmp_data['Телефон'].rfind(' ')-1]
    data.append(tmp_data)
    kol += 1
    if (kol == 1000):
        f = open('itog.txt', 'w', encoding = 'utf-8')
        for items in data:
            f.write(str(items))
            f.write('\n')
        f.close()     
        kol = 0
    print(len(data))
    time.sleep(0.5)
    
f = open('itog.txt', 'w', encoding = 'utf-8')
for items in data:
    f.write(str(items))
    f.write('\n')
f.close()