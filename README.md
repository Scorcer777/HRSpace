# Описание
hr_space - это микросервис для создания работодателем заявки на поиск сотрудника с привлечением рекрутера. Frontend, с которым взаимодействует данный API, представляет собой страницу входа и страницы формы для заполнения полей заявки. Заявка состоит из обязательных и необязательных полей. При отправке запроса на сохранение данных с помощью Postman(или аналогичных программ) стоит придерживаться формата, указанного в данной инструкции. Предполагается, что микросервис будет интегрирован с системой аутентификации и другими сервисами hh.ru, поэтому в самом микрорвисе реализована возможность аутентификации под логином и паролем заранее созданного суперпользователя(без регистрации).

## Стек технологий
Django==4.2.1,
Django Rest Framework,
Docker

## Автоматическая документация Swagger. Работает после выполнения локального запуска проекта.
http://localhost:8000/api/swagger/

## Ссылки на документацию использованных библиотек и фреймворков
https://www.django-rest-framework.org/, 
https://docs.djangoproject.com/en/5.0/, 
https://pypi.org/project/django-rest-authtoken/, 
https://pypi.org/project/django-filter/, 
https://pypi.org/project/django-multiselectfield/, 
https://pypi.org/project/django-cors-headers/, 
https://pypi.org/project/uritemplate/, 
https://pypi.org/project/PyYAML/


## Ссылка на работающий проект:
https://hrspace-frontend.vercel.app/
документация http://80.249.149.201:8000/api/swagger/

# Запуск проекта локально.
### 1. В VS Code(или аналогичной IDE) клонировать репозиторий командой в терминале Git Bash:
```bash
git clone git@github.com:Scorcer777/hr_space.git
```
### 2. Создать файл с переменными окружения в головной директории проекта:
```bash
cd hr_space/
touch .env
```
### 3.Скопировать в файл следующее содержимое файла env.example в файл .env
### 4. Открыть файл starter.sh, поменять End Of Line Sequence c CRLF на LF(в правом нижнем углу VS CODE) и сохранить.
### 4. Установить приложение Docker Desktop со страндарстными настройками.
### 5. Собрать контейнеры. Находясь в директории с файлом docker-compose.yml введя в терминале команду:
```bash
docker compose up
```
### 5. Миграции, создание суперюзера, загрузка тестовых данных произойдет автоматически.
### 6. Запустить программу Postman(или аналогичную для работы с API) для выполнения запросов. 
Импортировать небольшую коллекцию запросов: File - Import - указать файл hr_space.postman_collection.json, который находится в hr_space/postman_collection. Выполнить первый запрос "Получение токена", полученный токен вставить в Headers: Key = Authorization, Value = Token <значение токена> при выполнении всех последующих запросово. Как альтернатива Pоstman, можнго открыть в браузере URL http://localhost:8000/api/v2/ для работы с интерфейсом API через браузер.


# ПРИМЕРЫ ЗАПРОСОВ 
## Алгоритм аутентификации.
Для получения auth token пользователь отправляет POST-запрос с параметрами username и password на эндпоинт http://localhost:8000/api/v2/auth/login/:
```JSON
{
    "email": "test@test.com",
    "password": "123"
}
```
Далее, при выполнении запросов через Postman, требующих аутентификации пользователя, необходимо указываеть в Headers параметр Autorization со значением Token <код полученного auth token>.

## Базовые запросы к API c помощью POSTMAN(или аналогичной программы для работы с API):

Все запросы доступны только авторизованным пользователям.
1. GET http://localhost/api/v2/applications/ - получить список всех заявок.
2. GET http://localhost/api/v2/applications/id(целое число)/ - получить заявку по id.
3. GET http://localhost/api/v2/applications/?title=
Показать список заявок, отфильтрованный с помощью query params,
- Точное совпадение по email пользователя, создавшего заявку "user=";
- Частичное совпадение по названию заявки "title=";
- Точное совпадение по названию заявки "titleexact=";
- Частичное совпадение по названию профессии "profession=";
- Точное совпадение по названию города "city=";
5. POST http://localhost/api/v2/applications/ - сохранить заявку в БД.
В структуре передаваемых данных должны обязательно присутствовать все 5 верхнеуровневых ключей, как указано ниже.
Также поля под ключами "application" и "payment" - ОБЯЗАТЕЛЬНЫЕ.
Пример запроса (payload)
```JSON
{
    "application": {
        "title": "НОВАЯ ЗАЯВКА",
        "city": 3,
        "profession":  2,
        "min_salary":80,
        "max_salary": 9000,
        "number_of_employees": 1,
        "start_working": "tomorrow",
        "number_of_recruiters": 1
    },
     "job_info": {
        "employment_type": ["part-time", "full-time"],
        "schedule": ["flexible"],
        "work_model": ["office", "remote"],
        "contract_type": ["civil-personal_contract"],
        "working_conditions": [],
        "description": "ОБНОВИЛ."
    },
    "candidate_requirements": {
        "education": ["higher"],
        "experience": ["1-3_years"],
        "language_skills": [1,2],
        "driving_skills": ["B"],
        "has_medical_sertificate": false,
        "has_photo": false,    
        "citizenship": [2, 5],
        "coreskills_and_responsibilities": "Какие-то требования к соискателю."
    },
    "recruiter_requirements": {
        "industry": 1,
        "english_skills": "Advanced",
        "recruiter_responsibilities": ["recomendation_request"],
        "description": "ПОСЛЕ SERVICE.",
        "candidate_resume_form": "no_pre_interview",
        "stop_list":  "Какой-то нехороший соискатель другой."
    },
    "payments": {
        "payment_amount": 800000,
        "payment_type": "100%_first_day"
    }
}
```
4. PUT http://localhost/api/v2/applications/<id>/ - изменить определенную заявку в БД.
Обязательные поля здесь такие же, как в запросе на сохранение.
Если необязательные поля отстутсвуют, то их значения в БД не изменятся после выполнения запроса.
Пример запроса (payload)
```JSON
{
    "application": {
        "title": "ИЗМЕНЕННАЯ ЗАЯВКА",
        "city": 3,
        "profession":  2,
        "min_salary":80,
        "max_salary": 9000,
        "number_of_employees": 1,
        "start_working": "tomorrow",
        "number_of_recruiters": 1
    },
     "job_info": {},
    "candidate_requirements": {
        "education": ["higher"],
        "experience": ["1-3_years"],
        "coreskills_and_responsibilities": "Какие-то требования к соискателю поменялись."
    },
    "recruiter_requirements": {},
    "payments": {
        "payment_amount": 800000,
        "payment_type": "100%_first_day"
    }
}
```

## Эндпоинты только для чтения:
9. GET http://localhost:8000/api/v2/citizenships/ - просмотр всех доступных в базе гражданств(для выбора в форме).
10. GET http://localhost:8000/api/v2/languages/ - просмотр всех доступных в базе языков(для выбора в форме).
11. GET http://localhost:8000/api/v2/professions/ - просмотр всех доступных в базе профессий.(для выбора в форме).
12. GET http://localhost:8000/api/v2/cities/ - просмотр всех доступных в базе городов.(для выбора в форме).


