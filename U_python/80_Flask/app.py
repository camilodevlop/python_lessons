from flask import Flask, request, render_template, url_for, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = 'my_secret_key'    # Enables the use of session objects.

#http://localhost:5000/
@app.route('/')
def begin():
    if 'username' in session:
        print(session)   
        return f'The user is logged: {session["username"]}'

    return 'The user is not logged.'
    # app.logger.info(f'We entered the path: {request.path}')

#-------------------------------------------------------------------

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Adding the user to the session.
        session['username'] = request.form['username']
        return redirect(url_for('begin'))

    return render_template('loggin.html')

#-------------------------------------------------------------------

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('begin'))

#-------------------------------------------------------------------

@app.route('/greet/<name>')
def greet(name):
    return f'Greetings {name.upper()}!'

#-------------------------------------------------------------------

@app.route('/age/<int:age>')
def show_age(age):
    return f'You are {age} years old!'

#-------------------------------------------------------------------

@app.route('/show/<name>', methods = ['GET', 'POST'])
def show_name(name):
    return render_template('show.html', name = name)
    #return f'You\'re name is {name}.'

# GET is useful to recover information to the server.
# POST is useful to send informacion to the server.

#-------------------------------------------------------------------

@app.route('/redirect/<name>')
def redir(name):
    return redirect(url_for('show_name', name = name))
    # return redirect(url_for('begin'))

#-------------------------------------------------------------------

@app.route('/exit')
def exit():
    return abort(404)

#-------------------------------------------------------------------

@app.errorhandler(404)
def not_found_page(error):
    return render_template('error404.html', error = error), 404
    # Returns a tuple, You can omit the parethesis.

#-------------------------------------------------------------------

# REST: Representational State Transfer.
@app.route('/api/show/<name>', methods = ['GET', 'POST'])
def show_jason(name):
    values = {'name' : name, 'http_method' : request.method }
    return values    

#-------------------------------------------------------------------
