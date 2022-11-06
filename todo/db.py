#click nos va a servir para ejecutar en la terminal comandos que actúen sobre la BBDD sin tener que entrar a ella

#current_app mantiene la aplicación que estamos ejecutando
#g es una variable que se encuentra en toda nuestra aplicación para poder usarse en cualquier parte del código. Lo utilizaremos para almacenar el usuario

#with_appcontext nos proporcionará acceso a las vbles que tenemos en nuestra aplicación, como por ejemplo host de la BBDD, usuario....

# este fichero (schema) va a contener todos los scripts que necesitamos para crear nuestra BBDD

import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)
    db.commit()


# esta función nos va a permitir ejecutar comandos sobre la db desde la línea de comandos.
# para ello hay que utilizar el decorador @ y como argumento colocar el comando que debemos poner en la línea de comandos para que se ejcute la función
# en este caso habría que poner flask init-db
# tb hay que indicar que utilice el contexto de la app para que pueda acceder a database_host, database_user....
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')

# con esta función hacemos que se ejecute close_db cada vez que se termine de ejecutar una petición a la BBDD, de esa manera no dejamos ninguna conexión activa
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)