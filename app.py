from flask import Flask
from datetime import datetime
import re
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello, Flask! This is the home page:)'

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d, %B, %Y at %X")
    content = "<strong>Hello there, " + name + "!</strong> It's " + formatted_now

    return render_template("hello_there.html", title='Hello, Flask', content = content)
""" Commented out this block of code from original 'hello_there.html'
    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content
"""