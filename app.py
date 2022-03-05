"""
Simple login mechanism implemented with Flask and Flask-Sqlalchemy
Makes use of werkzeug.security for password hashing.

1. Create new user with signup form.
2. Authenticate user with Login form
3. Send authorized user to home page

https://techmonger.github.io/10/flask-simple-authentication/
"""

import profile
from flask import Flask, render_template, request, url_for, redirect, flash, \
session, abort, send_from_directory
from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
# from werkzeug.utils import secure_filename
import os

# Change dbname here
db_name = "auth.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# SECRET_KEY required for session, flash and Flask Sqlalchemy to work
app.config['SECRET_KEY'] = 'configure strong secret key here'

db = SQLAlchemy(app)
# db.create_all()

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    bio = db.Column(db.String(500), nullable=True)
    dp_url = db.Column(db.String(600), nullable=True)
    pass_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '' % self.username


def create_db():
    """ # Execute this first time to create new db in current directory. """
    db.create_all()


# @app.route('/static/<filename>')
# def send_reels(filename):
#     return send_from_directory("static", filename)


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    # when someone signup, set amount as 0 in firebase

    """
    Implements signup functionality. Allows username and password for new user.
    Hashes password with salt using werkzeug.security.
    Stores username and hashed password inside database.

    Username should to be unique else raises sqlalchemy.exc.IntegrityError.
    """

    if request.method == "POST":
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        bio = request.form['bio']
        print('=====>>> ', type(bio))
        if bio is None:
            bio = 'hey...'

        dp_url = request.form['dp_url'].strip()

        # file = request.files['files[]']        
        # filename = secure_filename(file.filename)
        # print('********--> ', (file.filename))

        # if filename == '':
        #     loc = 'static/Profile_NULL.png'
        # else:
        #     loc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #     file.save(loc)

        if not (username and password):
            flash("Username or Password cannot be empty")
            return redirect(url_for('signup'))
        else:
            username = username.strip()
            password = password.strip()

        # Returns salted pwd hash in format : method$salt$hashedvalue
        hashed_pwd = generate_password_hash(password, 'sha256')
        # print(hashed_pwd)
        
        new_user = User(username=username, bio=bio, pass_hash=hashed_pwd, dp_url=dp_url)
        db.session.add(new_user)

        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            flash("Username {u} is not available.".format(u=username))
            return redirect(url_for('signup'))

        flash("User account has been created.")
        return redirect(url_for("login"))

    return render_template("signup.html")


# @app.route("/", methods=["GET", "POST"])
@app.route("/login/", methods=["GET", "POST"])
def login():
    """
    Provides login functionality by rendering login form on get request.
    On post checks password hash from db for given input username and password.
    If hash matches redirects authorized user to home page else redirect to
    login page with error message.
    """

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if not (username and password):
            flash("Username or Password cannot be empty.")
            return redirect(url_for('login'))
        else:
            username = username.strip()
            password = password.strip()

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.pass_hash, password):
            session[username] = True
            return redirect(url_for("user_home", username=username))
        else:
            flash("Invalid username or password.")

            flash('''If your account has lost,
            please signup again with same username, 
            your money has not lost yet.''')

    return render_template("login_form.html")


@app.route("/user/<username>")
def user_home(username):
    """
    Home page for validated users.

    """
    if not session.get(username):
        abort(401)

    from vicks import flower as fire
    obj = fire.Bank_Account(username)
    user = User.query.filter_by(username=username).first()
    
    return render_template("user_home.html", 
                            username=username,
                            bio=user.bio,
                            dp_url=user.dp_url,
                            disp = obj.display()
                            )


@app.route("/account/<username>", methods=["GET", "POST"])
def user_account(username):
    """
    Home page for validated users.

    """
    if not session.get(username):
        abort(401)

    money = float(request.form['money'])
    from vicks import flower as fire

    '''
    # flower as fire

    flower samjhi kya ?
    fire hai mai... XD

    (firebase chatting feature will be add soon...)
    '''

    obj = fire.Bank_Account(username)
    pay = request.form['pay']
    obj_pay = fire.Bank_Account(pay)

    if money>0:
        obj_pay.deposit(money)
        disp = obj.withdraw(money)

        flash(f'''
        Paid Successfully
        ''')

    else:
        disp = obj.display()
        flash("Amount should NOT be Negative number.")

    user = User.query.filter_by(username=username).first()
    return render_template("user_home.html", 
                            username=username,
                            bio=user.bio,
                            dp_url=user.dp_url,
                            disp = disp,
                            )


@app.route("/logout/<username>")
def logout(username):
    """ Logout user and redirect to login page with success message."""
    session.pop(username, None)
    flash("successfully logged out.")
    return redirect(url_for('login'))


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    e = 'Error 404, Page not Found'
    return ( render_template('404.html', e=e), 404 )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
