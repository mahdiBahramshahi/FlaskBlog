from flask import session
from . import admin


@admin.route('/')
def index():
    return "Hello from admin Index"


@admin.route('/login/')
def login():
    session['name'] = 'mahdi'
    print(session)
    return "<h1>1<h1/>"
