from flask import Flask
from flask import jsonify
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import json
from flask_cors import CORS

# dataset coronavirus 
data_en = pd.read_excel("COVID_FAQ_E-A.xlsx",sheet_name="English")
data_ar = pd.read_excel("COVID_FAQ_E-A.xlsx",sheet_name="Arabic")
#data.head()
# Replace COVID-19 to coronavirus and remove \xa0 for both the answers and the context
answ_en = [a.replace('COVID-19', 'coronavirus') for a in data_en['Answer'].to_numpy()]
answer_en = [b.replace('\xa0', ' ') for b in answ_en]

cont_en = [c.replace('COVID-19', 'coronavirus') for c in data_en['Context'].to_numpy()]
context_en = [d.replace('\xa0', ' ') for d in cont_en]

# Replace COVID-19 to coronavirus and remove \xa0 for both the answers and the context
answ_ar = [a.replace('COVID-19', 'coronavirus') for a in data_ar['Answer'].to_numpy()]
answer_ar = [b.replace('\xa0', ' ') for b in answ_ar]

cont_ar = [c.replace('COVID-19', 'coronavirus') for c in data_ar['Context'].to_numpy()]
context_ar = [d.replace('\xa0', ' ') for d in cont_ar]
# Load module containing USE
module = hub.load('https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/3')

# Variables containing answers and context
responses_en = answer_en
response_contexts_en = context_en

# Create response embeddings
response_encodings_en = module.signatures['response_encoder'](
        input=tf.constant(responses_en),
        context=tf.constant(response_contexts_en))['outputs']

# Variables containing answers and context
responses_ar = answer_ar
response_contexts_ar = context_ar

# Create response embeddings
response_encodings_ar = module.signatures['response_encoder'](
        input=tf.constant(responses_ar),
        context=tf.constant(response_contexts_ar))['outputs']

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
#CORS(app)
#Cross Origin
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
  return 'Welcome, I am Amal, \n I am here to help you!'


greeting_inputs = ("hey", "good morning", "good evening", "morning", "evening", "hi", "whatsup")
greeting_responses = ["hey", "hey hows you?", "*nods*", "hello, how you doing", "hello", "Welcome, I am good and you"]

def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)


@app.route('/ask/api/v1.0/en/<string:question>',methods=['GET'])
def ask_me_en(question):
    """Base url to test API."""
    # Some test questions 
    q1 = [question]
    q2 = ["What is the incubation period?"]
    q3 = ["Are pets also vulnerable to COVID-19?"]
    q4 = ["Are there any drugs against the coronavirus?"]
    q5 = ["Are children at risk for the coronavirus?"]
    q6 = ["Why am I not allowed to shake hands anymore?"]
# Question encoding based on USE pretrained model
    question_encodings_en = module.signatures['question_encoder'](
            tf.constant([q.replace('COVID-19', 'coronavirus') for q in q1]))['outputs']

    maxElement = np.where(np.inner(question_encodings_en, response_encodings_en) 
                      == np.amax(np.inner(question_encodings_en, response_encodings_en)))
 
    response = {
        'response': responses_en[maxElement[1][0]]
    }

    return jsonify(response) 

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
# Question encoding based on USE pretrained model
    question_encodings_ar = module.signatures['question_encoder'](
            tf.constant([q.replace('COVID-19', 'coronavirus') for q in q1]))['outputs']

    maxElement = np.where(np.inner(question_encodings_ar, response_encodings_ar) 
                      == np.amax(np.inner(question_encodings_ar, response_encodings_ar)))
 
    response = {
        'response': responses_ar[maxElement[1][0]]
    }
    data= json.dumps(response, ensure_ascii=False).encode('utf8')
    return data

if __name__ == '__main__':
     
    app.run(host='0.0.0.0', port=5000, debug=True)
