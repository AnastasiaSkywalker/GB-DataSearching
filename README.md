# GB-DataSearching

Урок 1. Основы клиент-серверного взаимодействия. Парсинг API
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

Урок 2. Парсинг HTML. BeautifulSoup, MongoDB

Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы) с сайтов Superjob и HH. Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
* Наименование вакансии.
* Предлагаемую зарплату (отдельно минимальную, максимальную и валюту).
* Ссылку на саму вакансию.
* Сайт, откуда собрана вакансия.

По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.

Урок 3. Системы управления базами данных MongoDB и SQLite в Python
1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, записывающую собранные вакансии в созданную БД.
2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы.
3. Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта.


Урок 4. Парсинг HTML. XPath

    Написать приложение, которое собирает основные новости с сайтов news.mail.ru, lenta.ru, yandex-новости. Для парсинга использовать XPath. Структура данных должна содержать:
        название источника;
        наименование новости;
        ссылку на новость;
        дата публикации.
    Сложить собранные данные в БД

Сдайте задание до: 5 мая, 18:22 +03:00




Урок 5. Scrapy

1) Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить данные о письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный)
Логин тестового ящика: study.ai_172@mail.ru
Пароль тестового ящика: NextPassword172!

2) Написать программу, которая собирает «Новинки» с сайта техники mvideo и складывает данные в БД. Магазины можно выбрать свои. Главный критерий выбора: динамически загружаемые товары
Время для сдачи практического задания вышло

Урок 6. Scrapy. Парсинг фото и файлов

I вариант
1) Доработать паука в имеющемся проекте, чтобы он формировал item по структуре:
*Наименование вакансии
*Зарплата от
*Зарплата до
*Ссылку на саму вакансию
*Сайт откуда собрана вакансия
И складывал все записи в БД(любую)

2) Создать в имеющемся проекте второго паука по сбору вакансий с сайта superjob. Паук должен формировать item'ы по аналогичной структуре и складывать данные также в БД

II вариант
1) Создать двух пауков по сбору данных о книгах с сайтов labirint.ru и book24.ru
2) Каждый паук должен собирать:
* Ссылку на книгу
* Наименование книги
* Автор(ы)
* Основную цену
* Цену со скидкой
* Рейтинг книги
3) Собранная информация дожна складываться в базу данных
