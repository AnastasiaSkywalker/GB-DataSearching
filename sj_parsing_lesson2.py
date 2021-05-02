from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import json
import pandas as pd

#keywords = input('Название профессии: ')

params = {'keywords': 'Python'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}

main_url = 'https://russia.superjob.ru/vacancy/search'
response = requests.get(main_url, params=params, headers=headers)

dom = bs(response.text, 'html.parser')

vacancies_list = dom.find_all('div', {'class': 'jNMYr GPKTZ _1tH7S'})  #этот блок закхватывает название и зарплату
#pprint(vacancies_list)


vacancies = []
for vacancy in vacancies_list:
    current_vacancy = {}
    name = vacancy.find('a', {'class': 'icMQ_'}).text
    link = vacancy.find('a', {'class': 'icMQ_'})['href']
    salary = vacancy.find('span', {'class': '_1h3Zg _2Wp8I _2rfUm _2hCDz _2ZsgW'})
    if salary is not None:
        salary = salary.text.replace('\xa0', '').split(' ')
        current_vacancy['salary'] = salary
        # for p in salary:
        #     if p.isdigit():
        #         salary.append(p)
        # min_salary = float('')
        # max_salary = float('')
        # total_salary = (min_salary(), max_salary())
        # for s in salary:
        #     if 'от' in salary:
        #         min_salary.append(s[1:3])
        #         max_salary.append(0)
        #     if 'до' in salary:
        #         min_salary.append(0)
        #         max_salary.append(s[1:3])
        #     if '-' in salary:
        #         min_salary.append(s[0:2])
        #         max_salary.append(s[3:5])
        # print(total_salary)
    current_vacancy['link'] = link
    current_vacancy['name'] = name
    print(f"{name} с зарплатой {salary} с {link}")
    vacancies.append(current_vacancy)

#pprint(vacancies)
print(len(vacancies))






#data_sj_vacancies = pd.DataFrame(data=vacancies, columns=['link', 'name', 'salary'])
#print(data_sj_vacancies)  искать на седующих страницах уже сил нет, с тим еле справилась
# в первый раз выходила на сайты - и в поисковой строке просто копиравала url и параметры для headers,
# а сейчас они не определяются. Еси фильтр включаю на самом сайте, тогда что-то есть
