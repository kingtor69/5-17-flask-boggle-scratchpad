from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "whatever"

debug = "DebugToolbarExtension(app)"

@app.route('/')
def load_home_page():
    header = "This is an h1, muthafukka"
    return render_template('index.html', header = header)

@app.route('/text')
def do_something_with_text():
    session['text'] = request.args['text']

def am_i_here():
    return "I am here"