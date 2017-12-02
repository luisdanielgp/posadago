#/user/bin/env python 
# -*- coding: utf-8 -*-

from flask import Flask, request
import requests
from respuestas import Respuestas
app = Flask(__name__)
ACCESS_TOKEN = 'EAACJaZAYR6lgBALKXq2jaWj0bF0BK92UOpWuZBbIOYP1t1PWZB4lYGikaZCPOCmL1aHy6HuXia5JxSr9S7Bqhxy2RfypPvdjMZCaZCkwhNkhOaSfVPJ2O2ZBvL6ZClrVpsTRJpzakPisFAUvhlzw7bDrx343JbzdRkN7uthD1pmBegZDZD'
VERIFY_TOKEN = 'cintaroja'
@app.route('/')
def home():
    return 'Inicio del servidor'
@app.route('/posadero', methods = ['GET','POST'])
def webhook():
    if request.method == 'POST':
        mensaje = request.json
        print(mensaje)
        for event in mensaje['entry']:
            messaging = event['messaging']
            for event_message in messaging:
                sender_id = event_message['sender']['id']
                try:
                    message = event_message['message']['text']
                    pln = event_message['message']['nlp']['entities']['intent'][0]['value']
                except:
                    message = "HOLA"
                print(message + 'por' + sender_id) 
                respuestas = Respuestas()
                if message.upper() == 'Hola':
                    respuestas.saluda(sender_id)
                elif message.upper() == 'QUICK':
                    respuestas.quick(sender_id)
                elif message.upper() == 'GENERIC':
                    respuestas.generic(sender_id)   
                elif pln.upper() == "QUIERO":
                    respuestas.pln(sender_id)
                     
        return 'ok'
    elif request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return 'Verificar token'
if __name__== '__main__':
    app.run(port = 5000, debug = True)