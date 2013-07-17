from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy import func

from .models import (
    DBSession,
    Task,
    User,
    )

from pyramid.httpexceptions import (
    HTTPException,
    HTTPNotFound,
    HTTPFound,
    HTTPForbidden,
    )


@view_config(route_name='pokus', renderer='project:templates/pokus.mako')
def pokus_view(request):
    return {}

@view_config(route_name='tasks', renderer='project:templates/tasks.mako')
def tasks(request):
    tasks=DBSession.query(Task, User.email, User.name).join(User).all()
    return {'tasks': tasks}

@view_config(route_name='users', renderer='project:templates/users.mako')
def users(request):
    users=DBSession.query(User).all()
    return {'users': users}

@view_config(route_name='create', request_method="GET", renderer='project:templates/create.mako')
def create(request):
    return {}

@view_config(route_name='create', request_method="POST", renderer='project:templates/create.mako')
def create_post(request):
    post = request.POST
    
    if DBSession.query(User).filter_by(email = post['email']).first() == None:
        user = User(email = post['email'], name = post['name'])
        DBSession.add(user)
        
    user = DBSession.query(User).filter_by(email = post['email']).first()
    task = Task(task = post['task'], user = user)
    DBSession.add(task)
    return HTTPFound(request.route_path('tasks'))

@view_config(route_name='user', request_method="GET", renderer='project:templates/user_task.mako')
def user_task(request):
    dct = request.matchdict
    tasks=DBSession.query(Task, User.email).join(User).filter_by(email = dct['user']).all()
    return {'tasks': tasks, 'user': dct['user']}

@view_config(route_name='delete', request_method="GET")
def delete_user(request):
    dct = request.matchdict
    user = DBSession.query(User).filter_by(id = dct['id']).first()
    tasks = DBSession.query(Task).filter_by(user = dct['id']).all()
    for task in tasks:
        DBSession.delete(task)
    DBSession.delete(user)
    tasks=DBSession.query(Task, User.email).join(User).filter_by(email = dct['id']).all()
    return HTTPFound(request.route_path('tasks'))
