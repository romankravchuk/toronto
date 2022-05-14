# Flask application

> Технологии, которые использовались  
> - Python 3.8.10
> - Flask 2.1.1
> - PostgreSQL
> - SQLAlchemy 2.1.2


## Как запустить.

---

Шаг 1. Настройка **virtualenv**.

```bash
$ python3 -m virtualenv env
```

В итоге получим:

![env](./images/env.png)

Шаг 2. Активация **env** и установка необходимых библиотек.

```bash
$ source env/bin/activate
$ pip install -r requirements.txt
```

Шаг 3. Создать файл `.env` и добавить туда переменные.

```bash
$ touch .env
```

Вот ты должно выглядель содержимое `.env`

```bash
CONNECTION_STRING="postgresql+psycopg2://username:password@localhost:port/dbname"
SECRET_KEY="v3ry-s3cr37-k3y"
```

Шаг 4. Создать таблицу в вашей бд.

```SQL
CREATE TABLE users (
    id serial PRIMARY KEY,
    login varchar(50) NOT NULL,
    password varchar(100) NOT NULL,
    date_added date DEFAULT CURRENT_DATE
);
```

Шаг 5. Запустить приложение.

```bash
$ python app.py
```
