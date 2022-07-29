from distutils.debug import DEBUG
from decouple import config

#archivo de configuracion para interactuar 
#con las variables de entorno
class Config:
    SECRET_KEY = config('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
