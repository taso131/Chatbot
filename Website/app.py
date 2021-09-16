import datetime
from functions import BotLogic
import textprints as text
from os import name
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
bot = BotLogic()


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/process", methods=['GET'])
def load_welcome_text():
    return text.print_welcome()


@app.route("/time", methods=['GET'])
def load_time():
    return format(datetime.datetime.now())


@app.route("/needAnswer", methods=['POST'])
def need_answer():
    return bot.look_for_command(request.args.get('message'))


@app.route("/newQuestion", methods=['GET'])
def new_question():
    return "Is there anything else I can help you with? If not, just type in 'kthxbye'"
