#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from functools import wraps
from flask import *
#from forms import AddTaskForm
import subprocess

application = Flask(__name__)
application.config.from_object('_config')

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login')) #send back to login.html, send flash.
    return wrap

# route handlers
@application.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('Goodbye!')
    return redirect(url_for('login'))


@application.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != application.config['USERNAME'] or request.form['password'] != application.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error) #failed login, get login.html and error.
        else:
            session['logged_in'] = True #from the SECRET_KEY ..creates a session signed cookie. Session cookie name.
            flash('Welcome!')
            return redirect(url_for('main')) #login success redirect to /tasks.
    return render_template('login.html') #when I '/' get the login.html page.



@application.route('/main/')
@login_required
def main():
    return render_template('tasks.html')

@application.route('/tasks/')
@login_required
def index(name=''):
    if request.method == 'POST':
        if request.form['submit'] == 'on':
            cmd=['ls', '-l']
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            out,error = p.communicate()
            results = out.splitlines()
            return render_template('results.html', results=results)
        elif request.form['submit'] == 'off':
            cmd=['uname', '-a']
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            out,error = p.communicate()
            results = out.splitlines()
            return render_template('results.html', results=results)
        elif request.form['submit'] == 'shell':
            cmd=['python2.7', 'ssh-mon-get-hostname.py']
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            out,error = p.communicate()
            results = out.splitlines()
            return render_template('results.html', results=results)
        elif request.form['submit'] == 'myping':
            cmd=['ping', '-c', '2', 'www.yahoo.com']
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            out,error = p.communicate()
            results = out.splitlines()
            return render_template('results.html', results=results)
    return render_template('tasks.html', name=name)


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
