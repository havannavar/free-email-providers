'''
Created on 23 Aug 2017

@author: sats
'''
from app import app, api, validate_email, controller

@app.route(api.get('login'), methods=['POST'])
@validate_email.validate
def login():
    return controller.login()


def runserver():
    app.run(host='localhost', port=8081)

if __name__ == '__main__':
    runserver()