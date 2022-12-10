from flask import current_app as app

def init():
    print("I'm a very useful application")
    app.config['UTILS'] = True