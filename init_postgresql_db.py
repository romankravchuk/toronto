import psycopg2
from config import config


users = {
    'ferrybustling' : 'hqZM4TY7',
    'bustlingpurple' : 'xkKwusPS',
    'purplerosy' : 'j8BeQVpc',
    'rosyblazerod' : 'BkQTaYsV',
    'crepeblockson' : 'mpJxMUmM',
    'weeklyblockson' : 'XvQxUkKc',
    'greetingsweekly' : 'LFLspw9G',
    'hoegreetings' : 'g8dhF9MZ',
    'reddoryran' : 'bte8KXyP',
    'pigman' : '9KrM2FGN'
}


try:
    conn = psycopg2.connect(
        host=config['DB_HOST'],
        database=config['DB_NAME'],
        user=config['DB_USER'],
        password=config['PGSQL_DB_PASSWORD']
    )
    
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS users;')
    cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                    'login varchar (50) NOT NULL,'
                                    'password varchar (100) NOT NULL,'
                                    'date_added date DEFAULT CURRENT_DATE);')

    for user, password in users.items():
        cur.execute('INSERT INTO users (login, password) VALUES (%s, %s)',
                    (user, password))

    conn.commit()

    cur.close()
    conn.close()
except Exception as e:
    print(e)
