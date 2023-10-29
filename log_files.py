import logging

# Configurar el registro
logging.basicConfig(filename='mi_archivo_de_registro.log', level=logging.DEBUG)

# Crear registros
logging.debug('Este es un mensaje de depuración.')
logging.info('Este es un mensaje informativo.')
logging.warning('Este es un mensaje de advertencia.')
logging.error('Este es un mensaje de error.')
