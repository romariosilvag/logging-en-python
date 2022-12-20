import logging

# Establecer el nivel de registro en DEBUG
logging.basicConfig(level=logging.DEBUG)

# Registrar un mensaje con el nivel DEBUG
logging.debug("This is a debug message")

# Registrar un mensaje con el nivel INFO
logging.info("This is an info message")

# Registrar un mensaje con el nivel WARNING
logging.warning("This is a warning message")

# Registrar un mensaje con el nivel ERROR
logging.error("This is an error message")

"""
Los niveles de severidad utilizados en la libreria logging de Python se utilizan para indicar la importancia de un mensaje de registro. Los niveles más comunes son:

DEBUG: Mensajes de depuración y detalles técnicos que pueden ser útiles para depurar problemas.
INFO: Mensajes informativos que indican que la aplicación está funcionando correctamente.
WARNING: Mensajes de advertencia que indican que algo puede estar mal, pero que la aplicación puede continuar funcionando.
ERROR: Mensajes de error que indican que algo ha fallado y que la aplicación puede tener problemas para funcionar correctamente.
CRITICAL: Mensajes críticos que indican un fallo grave que puede impedir que la aplicación funcione correctamente.
Los niveles se utilizan para filtrar los mensajes de registro y mostrar solo aquellos que son relevantes para el problema que se está tratando de resolver. 
Por ejemplo, si se está depurando un problema, es posible que se desee ver todos los mensajes de DEBUG y INFO, pero ignorar los mensajes de WARNING, ERROR y CRITICAL. 
Por otro lado, si se está buscando problemas graves, es posible que se desee ver solo los mensajes de ERROR y CRITICAL.
"""