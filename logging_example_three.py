import logging

# Configuramos el módulo logging para que escriba los mensajes de registro en la consola
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# Registramos un mensaje informativo
logging.info('Este es un mensaje informativo')

# Registramos un mensaje de advertencia
logging.warning('Este es un mensaje de advertencia')

# Registramos un error
try:
    1 / 0
except Exception:
    logging.exception('Ha ocurrido un error')

# Registramos un mensaje de depuración
logging.debug('Este es un mensaje de depuración')
