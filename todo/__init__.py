# utilizaremos import os para acceder a las variables de entorno
import os 
from flask import Flask


# las aplicaciones que creamos son instancias de flask, es muy importante la función create_app para crear el objeto app

def create_app():
    app = Flask(__name__)

    # configuramos ahora nuestras vbles de entorno para nuestra app
    # en producción, debemos poner una secret key difícil de romper para un hacker
    # el objeto os.environ tiene todas las variables de entorno, lo utilizamos para poder acceder a nuestra BBDD
    app.config.from_mapping(
        SECRET_KEY = 'mikey',
        DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
        DATABASE = os.environ.get('FLASK_DATABASE'),
    )
    
    # aplicamos la función init_app del archivo db.py a nuestra app para que cierre la conexión tras su uso, para ello hay que importar el archivo primero
    from . import db
    db.init_app(app)

    from . import auth
    from . import todo

    # con esta línea nos suscribimos al blueprint creado en auth, que le llamamos bp
    app.register_blueprint(auth.bp)

    # con esta línea nos suscribimos al blueprint creado en todo, que le llamamos bp   

    app.register_blueprint(todo.bp)

    @app.route('/hola')
    def hola():
        return 'hola mundo'
    
    return app


