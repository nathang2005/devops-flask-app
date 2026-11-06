from flask import Flask
import redis
app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('hello', 123)
print(r.get('hello'))

@app.route('/')
def say_hello():
    return '<p>New String!!, I am a Flask app!</p><p><a href="/about">About this application</a></p>'

@app.route('/about')
def about():
    return '<p>This application is running on the Flask web framework.</a>.</p>'

@app.route('/contact')
def contact():
    return '<p>Contact us at:</p><p>c24380043@mytudublin.ie:'

app.run(host="0.0.0.0", port=5000)

