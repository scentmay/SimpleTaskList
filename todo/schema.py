# aquí pondremos las instrucciones sql a ejecutar
# si queremos eliminar una tabla, no nos va a dejar si tiene refernecias cruzadas (foreign key)
# para eliminar esa validación colocamos la instrucción de la línea 8, posteriormente hay que vovler a activarla
# todo lo que va entre 3 comillas dobles se considera un único string de varias líneas
# vamos a encriptar las contraseñas, llegarán a una longitud de aprox 91 caracteres, le damos en la tabla 100 a la columna de password

instructions = [
    'SET FOREIGN_KEY_CHECKS=0',
    'DROP TABLE IF EXISTS todo ',
    'DROP TABLE IF EXISTS user',
    'SET FOREIGN_KEY_CHECKS=1',
    """
        CREATE TABLE user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(200)
        )
    """,
    """
        CREATE TABLE todo (
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL,
            FOREIGN KEY (created_by) REFERENCES user(id)
        )
    """
]