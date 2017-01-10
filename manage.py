import click
from factory import create_app
from database import db


@click.group()
def manager():
    pass


@manager.command()
def develop():
    app = create_app('config.DevelopmentConfig')
    app.run(threaded=True)


@manager.command()
def test():
    app = create_app('config.TestingConfig')
    app.run(threaded=True)


if __name__ == '__main__':
    manager()
