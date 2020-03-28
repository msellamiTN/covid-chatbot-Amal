from flask import Flask
from flask import jsonify
import numpy as np
import pandas as pd
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from flask_cors import CORS
from flask_cors import CORS, cross_origin
 

chatbot = ChatBot('Amal')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.english")
trainer.train(
        "chatterbot.corpus.english.covid19"

)
 
app = Flask(__name__)
#CORS(app)
#Cross Origin
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, headers=(
             'x-requested-with',
             'content-type',
             'accept',
             'origin',
             'authorization',
             'x-csrftoken',
             'withcredentials',
             'cache-control',
             'cookie',
             'session-id',
         ),
         supports_credentials=True)

@app.route('/')
@cross_origin(origin='*',headers=['Content-Type', 'application/json'])
def index():
  return 'Welcome, I am Amal, \n I am here to help you!'

@app.route('/ask/api/v1.0/en/<string:question>',methods=['GET'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def ask_me_en(question):
    """Base url to test API."""
    # Some test questions 
    q1 = [question]
    q2 = ["What is the incubation period?"]
    q3 = ["Are pets also vulnerable to COVID-19?"]
    q4 = ["Are there any drugs against the coronavirus?"]
    q5 = ["Are children at risk for the coronavirus?"]
    q6 = ["Why am I not allowed to shake hands anymore?"]
     # Get a response to an input statement
    responses_en =chatbot.get_response(question)

    response = {
        'response': (str(responses_en)).encode('utf8')
    }
    anwsers= jsonify(response)
    #anwsers.headers.add('Access-Control-Allow-Origin', '*')  
  
    return  anwsers

@app.route('/ask/api/v1.0/ar/<string:question>',methods=['GET'])
def ask_me_ar(question):
    """Base url to test API."""
    # Some test questions 
    q1 = [question ]
    q2 = ["What is the incubation period?"]
    q3 = ["Are pets also vulnerable to COVID-19?"]
    q4 = ["Are there any drugs against the coronavirus?"]
    q5 = ["Are children at risk for the coronavirus?"]
    q6 = ["Why am I not allowed to shake hands anymore?"]
 
    chatbot = ChatBot('Amal')

    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot based on the english corpus
    #trainer.train("chatterbot.corpus.english")
    trainer.train(
            "chatterbot.corpus.arabic.covid19"

    )
   # Get a response to an input statement
    responses_en =chatbot.get_response(question)

    response = {
        'response': (str(responses_en)).encode('utf8')
    }
    anwsers= jsonify(response)
    #anwsers.headers.add('Access-Control-Allow-Origin', '*')  
  
    return  anwsers

if __name__ == '__main__':
    #app.run(ssl_context=('cert.pem', 'key.pem'))
    app.run(host='0.0.0.0', port=5000, debug=True)
