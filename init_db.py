import psycopg2

from config import DB_NAME, DB_PASSWORD, DB_USERNAME


conn = psycopg2.connect(
    host="localhost",
    database=DB_NAME,
    user=DB_USERNAME,
    password=DB_PASSWORD
)

# Users
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

# Open a cursor to perform database operations
cur = conn.cursor()

# Creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                'login varchar (50) NOT NULL,'
                                'password varchar (100) NOT NULL,'
                                'date_added timestamp DEFAULT CURRENT_TIMESTAMP);')


# Insert data into the table
for user, password in users.items():
    cur.execute('INSERT INTO users (login, password)'
                'VALUES (%s, %s)',
                (
                    user,
                    password
                ))


# Commit changes
conn.commit()


# Dispose cursor and connection
cur.close()
conn.close()
