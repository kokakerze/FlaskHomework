
import random
import string
from faker import Faker
from flask import Flask, render_template
import requests
import ast

app = Flask(__name__)

fake= Faker()

class Users:
    def __init__(self,name):
        self.name=name

def astros():
    r = requests.get(' http://api.open-notify.org/astros.json')
    string1 = r.text
    dict1 = ast.literal_eval(string1)
    return str(dict1["number"])

def users_generator(len):
    fakeppl = {}
    fakelist = []
    for _ in range(len):
        fakeppl["name"] = fake.name()
        fakeppl["email"] = fake.email()
        fakelist.append(fakeppl.copy())
    return fakelist

def password_generator(len):
    password_list= random.sample(string.printable,k=len)
    password = "".join([str(elem) for elem in password_list])
    return password


@app.route('/generate-users')
@app.route('/users/generate')
@app.route('/users/generate/<int:len>')
def users(len=20):
    print(users_generator(len))
    return render_template("users.html", fakelist1=users_generator(len))


@app.route('/password/generate')
@app.route('/password/generate/<int:len>')
def password(len=0):
    return render_template("password.html", password1=password_generator(len))

@app.route('/astro')
def astro():
    return 'ASTRONAUTS: ' + astros()

if __name__ == '__main__':
    app.run()

