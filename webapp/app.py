import os, random, urlparse

from flask import Flask
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

@app.route('/')
def hello():

    if 'DATABASE_URL' in os.environ:
        # We're running on Heroku
        heroku = urlparse.urlparse(os.environ['DATABASE_URL'])
        dsn =  "postgres://" + heroku.username + ":" + heroku.password + "@" + heroku.hostname + ":" + str(heroku.port) + "/" + heroku.path[1:]
    else:
        # We're running locally
        dsn = "postgres://" + os.environ['POSTGRES_USER'] + ":" + os.environ['POSTGRES_PASSWORD'] + "@" + os.environ['POSTGRES_HOST'] + ":" + os.environ['POSTGRES_PORT'] + "/" + os.environ['POSTGRES_DB']
    
    engine = create_engine(dsn)
    metadata = MetaData(engine)
    people  = Table('people', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('count', Integer),
                    )

    Session = sessionmaker(bind=engine)
    session = Session()
    metadata.create_all(engine)

    rand_names = ['Jay', 'Albert', 'Oscar', 'Felipe', 'Bobo', 'Pancake', 'Mr. Spongebob']
    random_person = random.choice(rand_names)

    people_ins = people.insert().values(name=random_person, count=1)
    session.execute(people_ins)
    session.commit()

    result = session.execute(select([people]))
    output = 'Hello world: '

    for row in result:
        output += str(row) + ' '

    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0')
