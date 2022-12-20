import logging
from logging.handlers import RotatingFileHandler

"""
Configuramos el módulo logging para que escriba los mensajes de registro en un archivo
y utilice un manejador de archivo rotativo para limitar el tamaño del archivo
"""

handler = RotatingFileHandler('test.log', maxBytes=1024, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])

# Registramos algunos mensajes de registro
logging.info('Este es un mensaje informativo')
logging.warning('Este es un mensaje de advertencia')
logging.error('Este es un mensaje de error')


"""

En este ejemplo, se utiliza el manejador de archivo rotativo RotatingFileHandler para escribir los mensajes de registro en un archivo y limitar su tamaño a 1 MB. 
Cuando se alcanza este límite, el manejador rota el archivo y crea una copia de respaldo, de modo que siempre se mantienen las últimas 3 copias del archivo.

También se utiliza un formateador de mensajes de registro para dar formato a los mensajes y hacerlos más legibles. 
El formateador especifica que se deben incluir la fecha y hora del mensaje, el nivel de severidad y el mensaje en sí.

"""