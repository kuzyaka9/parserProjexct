import pandas as pd
from ast import literal_eval as le

file = open('itog.txt', 'r', encoding = 'utf-8')

data = file.readlines()

file.close()


storage = {'Страна': [], 'Название': [], 'Адрес': [], 'Сайт': [], 'Телефон': [], 'Сфера деятельности': []}
for item in data:
    tmp_dict = le(item)
    storage['Страна'].append(tmp_dict['Страна'])
    storage['Название'].append(tmp_dict['Название'])
    storage['Адрес'].append(tmp_dict['Адрес'])
    if ('Сайт' in tmp_dict.keys()):
        storage['Сайт'].append(tmp_dict['Сайт'])
    else:
        storage['Сайт'] .append('')
    if ('Телефон' in tmp_dict.keys()):
        storage['Телефон'].append(tmp_dict['Телефон'])
    else:
        storage['Телефон'].append('')
    st = ''
    for elem in tmp_dict['Сфера деятельности']:
        st += str(elem)+', '
    st = st[0:st.rfind(' ')-1]
    storage['Сфера деятельности'].append(st)
##for item in storage['Сфера деятельности']:
    ##print(item, '\n')
df = pd.DataFrame(storage)
df.to_excel('./Data.xlsx')
    
