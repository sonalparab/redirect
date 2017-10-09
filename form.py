from flask import Flask,render_template, request, session, redirect, url_for

app = Flask(__name__)

dict = {'Bermet':'Sonal'}

app.secret_key = "this is totally secret"

@app.route('/',methods = ['POST','GET'])
def root():
    if 'username' in session:
        return redirect(url_for('welcome'))
    else:
        return render_template('form.html')

@app.route('/output/', methods = ['POST','GET'])
def welcome():
    if 'username' in session:
        username = session['username']
        password = dict[username]
    else:
        username = request.form['name']
        password = request.form['pass']
    if username in dict:
        if dict[username] == password:
            session['username'] = username
            return render_template('welcome.html', username=username)
    if username in dict:
        return render_template('error.html',bad='password')
    else:
        return render_template('error.html',bad='username')

@app.route('/logout/',methods = ['POST','GET'])
def logout():
    session.pop('username')
    return redirect(url_for('root'))
    
if __name__ == '__main__':
    app.debug = True
    app.run()
