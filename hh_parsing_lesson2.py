from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import json
import pandas as pd

params = {'clusters': True,
        'area': '113',
        'enable_snippets': True,
        'is_part_time_clusters_enabled': True,
        'salary': '',
        'st': 'searchVacancy',
        'text': 'Data scientist',
        'from': 'suggest_post'
        }

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}

main_url = 'https://hh.ru/vacancies/podrabotka'
response = requests.get(main_url, params=params, headers=headers)

dom = bs(response.text, 'html.parser')
vacancies_list = dom.find_all('div', {'class': 'vacancy-serp-item'})
#pprint(vacancies_list) #закомментировала т.к. много текста

vacancies = []
for vacancy in vacancies_list:
    current_vacancy = {}
    name = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-title'}).text  #getText отсуствует
    link = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})['href']
    salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
    # min_salary = () #NonType object не дает циклом выдрать числовые значения, где они есть
    # max_salary = ()
    # total_salary = (min_salary, max_salary)
    if salary is not None:
        salary = salary.text.split(' ')
        current_vacancy['salary'] = salary
        # for s in salary:
        #     if s.isnumeric():
        #         salary.append(float(s))
        # salary = salary.replace('\xa0', '').replace('от', '').replace('до') # выдается NonType object, с которым нельзя ничего провернуть
    #     for s in salary:
    #         if 'от' in salary:
    #             min_salary.append(s[1])
    #             max_salary.append(0)
    #         if 'до' in salary:
    #             min_salary.append(0)
    #             max_salary.append(s[1])
    #         if '-' in salary:
    #             min_salary.append(s[0])
    #             max_salary.append(s[2])
    #         if 'USD' in salary:
    #             min_salary.append(s[0])
    #             max_salary.append(s[2])
    # pprint(total_salary)
    current_vacancy['link'] = link
    current_vacancy['name'] = name
    current_vacancy['salary'] = salary
    print(f"{name} с зарплатой {salary} с {link}")
    vacancies.append(current_vacancy)

#pprint(vacancies)
#print(len(vacancies))

#это самый работоспособный вариант. Зарплату во float int  учше переведу через таблицу следующего задания


#data_hh_vacancies = pd.DataFrame(data=vacancies, columns=['link', 'name', 'salary'])  #почему имя не выводится?
#print(data_hh_vacancies)

