#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *
import subprocess

application = Flask(__name__)




@application.route('/', methods=['GET', 'POST'])    
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
    return render_template('template.html', name=name)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
