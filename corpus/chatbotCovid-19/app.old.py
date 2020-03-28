from flask import Flask
from flask import jsonify
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
# dataset coronavirus RIVM
data = pd.read_excel("COVID_FAQ_E-A.xlsx",sheet_name="English")
data.head()
# Replace COVID-19 to coronavirus and remove \xa0 for both the answers and the context
answ = [a.replace('COVID-19', 'coronavirus') for a in data['Answer'].to_numpy()]
answer = [b.replace('\xa0', ' ') for b in answ]

cont = [c.replace('COVID-19', 'coronavirus') for c in data['Context'].to_numpy()]
context = [d.replace('\xa0', ' ') for d in cont]
# Load module containing USE
module = hub.load('https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/3')

# Variables containing answers and context
responses = answer
response_contexts = context

# Create response embeddings
response_encodings = module.signatures['response_encoder'](
        input=tf.constant(responses),
        context=tf.constant(response_contexts))['outputs']
app = Flask(__name__)

@app.route('/', methods=['GET'])
def base_url():
    """Base url to test API."""
    # Some test questions 
    q1 = ["What about pregnant women?"]
    q2 = ["What is the incubation period?"]
    q3 = ["Are pets also vulnerable to COVID-19?"]
    q4 = ["Are there any drugs against the coronavirus?"]
    q5 = ["Are children at risk for the coronavirus?"]
    q6 = ["Why am I not allowed to shake hands anymore?"]
# Question encoding based on USE pretrained model
    question_encodings = module.signatures['question_encoder'](
            tf.constant([q.replace('COVID-19', 'coronavirus') for q in q2]))['outputs']

    maxElement = np.where(np.inner(question_encodings, response_encodings) 
                      == np.amax(np.inner(question_encodings, response_encodings)))
 
    response = {
        'response': responses[maxElement[1][0]]
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
