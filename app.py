from flask import Flask, render_template
from datetime import datetime


def now():
  return datetime.utcnow()


app = Flask(__name__)


@app.route('/home')
@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/jinja')
def jinja():
    hour = 10
    fruite = ["apple", "banana", "cherry"]
    fruits = []
    return render_template('Jinja.html', hour=hour, now=now, fruite=fruite, fruits=fruits)


if __name__ == '__main__':
    app.run()

