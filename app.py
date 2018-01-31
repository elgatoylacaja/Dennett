from config import Config
from factory import create_app

app = create_app()

if __name__ == '__main__':
    if Config.DEVELOPMENT == 'True':
        app.run(host='0.0.0.0')
    else:
        app.run()
