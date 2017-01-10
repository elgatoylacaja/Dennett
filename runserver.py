from factory import create_app

if __name__ == '__main__':
    app = create_app('config.DevelopmentConfig')
    app.run(threaded=True)
