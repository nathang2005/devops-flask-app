from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
    return '<p>Hello, World, I am a Flask app!</p><p><a href="/about">About this application</a></p>'

@app.route('/about')
def about():
    return '<p>This application is running on the Flask web framework.</a>.</p>'

@app.route('/contact')
def contact():
    return '<p>Contact us at:</p><p>c24380043@mytudublin.ie:'