from os import environ
from flask import Flask
import botnadamus

app = Flask(__name__)

@app.route("/")
def home():
    botnadamus.create_api()
    return

app.run(host= '0.0.0.0', port=environ.get('PORT'))
