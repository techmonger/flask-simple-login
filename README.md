## Flask Simple Login without Extensions

### [https://techmonger.github.io/10/flask-simple-authentication/]("https://techmonger.github.io/10/flask-simple-authentication/")

## Getting Started

- Install required packages `pip -r install requirements.txt`
- Create empty database 

```
cd flask-simple-login/
python
    >>> from app import create_db
    >>> create_db()
```

...or,
    python create_db.py

- Run application `python app.py`
- Create new account  http://127.0.0.1:5000/signup
- Login account  http://127.0.0.1:5000/login

## For Automate Login

    cd autologin
    python auth.db