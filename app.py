from flask import Flask, render_template, request, jsonify
from chat import predict_class, get_response
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open(r'C:\Users\Mabrouk\Desktop\Stage ARZAK\chatbot\intetnts.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

#@app.route('/', methods=['GET'])
#def home():
    #return render_template('base.html')


@app.route('/chat', methods=['POST'])
def chat():
    text = request.get_json().get("message")
    pred = predict_class (text)
    res = get_response (pred, intents)
    response = {'answer': res}
    return jsonify(response)


if __name__ == '__main__' :
    app.run(debug=True, port='3000')
