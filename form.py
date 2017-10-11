from flask import Flask,render_template,request,session,redirect,url_for,flash

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
        return render_template('welcome.html',username=session['username'])
    else:
        username = request.form['name']
        password = request.form['pass']
    if username in dict:
        if dict[username] == password:
            session['username'] = username
            flash('Successful login')
            return redirect(url_for('welcome'))
    if username in dict:
        flash('Bad password')
        return redirect(url_for('root'))
    else:
        flash('Bad username')
        return redirect(url_for('root'))

@app.route('/logout/',methods = ['POST','GET'])
def logout():
    username = session.pop('username')
    flash(username + ' has successfully logged out')
    return redirect(url_for('root'))
    
if __name__ == '__main__':
    app.debug = True
    app.run()
