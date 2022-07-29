from flask import Flask
from config import config


app = flask(__name__)


if __name__ == '__main__':
    app.config.from_object(config['development'])
    # app.run()
    # confi para que los cambios se visualizen
    #  y sincronas
