<div align="center">
    <img src='./docs/images/logo.jpg'>
    <h1>Toronto</h1>
    <a href='https://github.com/romankravchuk/toronto/releases'>
        <img src='https://img.shields.io/badge/VERSION-1.0-informational?style=for-the-badge&labelColor=000'>
    </a>
    <a href='./LICENSE.md'>
        <img src='https://img.shields.io/badge/LICENSE-MIT-ff69b4?style=for-the-badge&labelColor=000'>
    </a>
</div>

---

## Getting Started

---

### Create a Bot Account

Creating a Bot account is a pretty strightforward process.

1. Make sure you're logged on the [Discord website]([https://](https://discord.com/))
2. Navigate to the [application page](https://discord.com/developers/applications)
3. Click on the <kbd>New application</kbd> button
4. Give the application a name and click <kbd>Create</kbd>
5. Create a **Bot User** by navigating to the **Bot** tab and clicking <kbd>Add Bot</kbd>
6. Make sure that **Public Bot** is ticked if you want others to invite your bot
7. Invite bot to your servers

### Setup environments

Create a **.env** file like this:

```bash
CONNECTION_STRING='postgresql+psycopg2://user:password@localhost:port/dbname'
SECRET_KEY='v3ry-s3cr37-k3y'
DEBUG_LOG_PATH='/path/to/debug.log'
ERROR_LOG_PATH='/path/to/error.log'
TOKEN='Your bot token'
```

Use next command to create virtual environment source:

```bash
$ cd ./services && python3 -m virtualenv env
```

> Make sure you're installed virtualenv after using this command  
> `$ python3 -m pip install virtualenv`

Install python requirements:

```bash
$ source ./env/bin/activate
```

```bash
(env) $ pip install -r requirements.txt
```

### Run app and bot

```bash
(env) $ python ./run_web.py
```

```bash
(env) $ python ./run_bot.py
```

## Demo

---

### Login form

> You need to create user to see members tab  

![login form](./docs/images/login.png)

### Members table

![members table](./docs/images/members.png)

### Member profile

![member profile](./docs/images/member-profile.png)