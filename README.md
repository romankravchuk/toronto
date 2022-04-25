# flask-app

В данном репозитории находится простейшее веб-приложение,  
сделанное с помощью **Flask**, а также файлы конфигурации  
для хостинга на **Apache**

## Настройка перед запуском

Шаг 1. Устанавливаем **venv**:

```bash
pip install virtualenv
```

Шаг 2. Создаем директорию **env** для проекта:

```bash
pythom3 -m virtualenv env
```

В итоге получим:

![env](./images/env.png)

Шаг 3. Настройка **env**

Открываем файл activate с помощью текстового редактора:

```bash
nano /env/bin/activate
```

Добавляем команды, расположенные между **...**.  
Значения меняем на свои.

```bash
export PATH

...
export DB_NAME="database"
export DB_USERNAME="user"
export DB_PASSWORD="password"

export SECRET_KEY="key"

export FLASK_ENV="development"
...
```

Шаг 4. Активируем **env**

```bash
source env/bin/activate
```

Если все прошло успешно, то получим:

```bash
(env) user@host:~/flask-app$
```

Шаг 5. Успанавливаем необходимые библиотеки python

```bash
pip install -r requirements.txt
```

## Настройка для Apache

Шаг 1. Установка и активация mod_wsgi

Устанавливаем mod_wsgi:

```bash
sudo apt-get install libapache2-mod-wsgi python-dev
```

Активируем mod_wsgi:

```bash
sudo a2enmod wsgi
```

Шаг 2. Подготовка файлов конфигурации

Копируем **flask-app.conf** в каталог с файлам конфигурации:

```bash
cp flask-app.conf /etc/apache2/sites-available/
```

Далле создаем каталог для логов:

```bash
mkdir logs
```

Копируем все содержимое репозитория в каталог, из которого **Apache** будет просматривать файлы

```bash
cp -pr . /var/www/flask-app/
```

Меняем владельца каталога flask-app

```bash
sudo chown -R www-data:www-data /var/www/flask-app
```

Шаг 3. Перезапуск **Apache**

```bash
sudo service apache2 restart
```
