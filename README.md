# Flask application

> Технологии, которые использовались.
>  
> - Python 3.8.10
> - Flask 2.1.1
> - PostgreSQL
> - SQLAlchemy 2.1.2

## Как запустить

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
```

```bash
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

Шаг 5. Создать директории для логов

```bash
$ mkdir logs
```

```bash
mkdir logs/debug && mkdir logs/error
```

Шаг 5. Запустить приложение.

```bash
$ python wsgi.py
```
