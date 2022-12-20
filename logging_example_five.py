import logging
import logging.handlers
import sys

if __name__ == "__main__":

    # Cambie el nivel del registrador raíz de ADVERTENCIA (predeterminado) a NOTSET para que se deleguen todos los mensajes.
    logging.getLogger().setLevel(logging.NOTSET)

    # Agregar controlador de salida estándar, con nivel INFO
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    formater = logging.Formatter('%(name)-13s: %(levelname)-8s %(message)s')
    console.setFormatter(formater)
    logging.getLogger().addHandler(console)

    # Agregar controlador giratorio de archivos, con nivel DEBUG
    rotatingHandler = logging.handlers.RotatingFileHandler(filename='rotating.log', maxBytes=1000, backupCount=3)
    rotatingHandler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rotatingHandler.setFormatter(formatter)
    logging.getLogger().addHandler(rotatingHandler)

    log = logging.getLogger("app." + __name__)

    log.debug('Debug message, should only appear in the file.')
    log.info('Info message, should appear in file and stdout.')
    log.warning('Warning message, should appear in file and stdout.')
    log.error('Error message, should appear in file and stdout.')