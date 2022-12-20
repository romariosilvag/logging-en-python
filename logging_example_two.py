import logging


# Establezca el nivel de registro en DEBUG, especifique un formato de registro y especifique un archivo de registro
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename='app.log', filemode='w')

"""
El método basicConfig() de la libreria logging de Python permite configurar de manera básica el módulo de registro. Algunos de los parámetros que puedes utilizar son:

    level: Especifica el nivel de severidad mínimo para mostrar los mensajes de registro. Los valores válidos son DEBUG, INFO, WARNING, ERROR y CRITICAL. 
    Si se especifica un nivel más alto, solo se mostrarán los mensajes de ese nivel o de niveles superiores.

    filename: Especifica el nombre del archivo donde se deben escribir los mensajes de registro. Si se especifica un nombre de archivo, 
    los mensajes de registro se escribirán en ese archivo en lugar de en la consola.

    filemode: Especifica el modo en que se debe abrir el archivo especificado con filename. Los valores válidos son 'w' para sobrescribir el archivo 
    cada vez que se inicie la aplicación, 'a' para agregar los mensajes al final del archivo y 'x' para crear un nuevo archivo si no existe (o lanzar una excepción si el archivo ya existe).

    format: Especifica el formato de los mensajes de registro. Este parámetro toma una cadena de formato que puede incluir placeholders para diferentes 
    elementos del mensaje de registro, como la fecha y hora del mensaje, el nivel de severidad, el mensaje en sí, etc.

    datefmt: Especifica el formato de la fecha y hora en los mensajes de registro. Este parámetro se utiliza junto con el parámetro format para formatear 
    la fecha y hora del mensaje de registro.


Estos son algunos de los parámetros más comunes que se pueden utilizar con basicConfig(). Hay otros parámetros disponibles, como stream, que permite especificar un objeto de flujo de salida diferente a la consola para escribir los mensajes de registro, o handlers, que permite especificar una lista de manejadores de registro personalizados para procesar los mensajes de registro.

"""

# Registrar un mensaje
logging.info("This is an info message")
