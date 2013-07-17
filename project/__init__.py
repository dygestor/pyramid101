from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    #route configuration
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('pokus', '/pokus')
    config.add_route('tasks', '/tasks')
    config.add_route('users', '/users')
    config.add_route('create', '/create')
    config.add_route('delete', '/delete/{id}')
    config.add_route('user', '/user/{user}')

    config.scan()
    return config.make_wsgi_app()
