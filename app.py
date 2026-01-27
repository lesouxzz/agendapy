from flask import Flask, render_template

app = Flask(__name__)
 
@app.route('/')
def home():
    return '<p style=c"color:red">Seja bem-vindo'

 @app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"