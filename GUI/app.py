from flask import Flask, send_from_directory, request
import json


app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('./', 'index.html')
    
@app.route('/execute', methods=['POST'])
def execute():
    word = request.form['word']
    
    if word == "":
        return json.dumps({
            "error": "please send me something"
        }), 400, {
            "Content-Type": "application/json"
        }

    # complete some processing here
    knowledge = 'fatface'
    if knowledge == "again":
        return json.dumps({
                "instruction": 'please try again!'
            }), 200, {
                "Content-Type": "application/json"
            }
    return json.dumps({
            "instruction": 'done'
    
        }), 200, {
            "Content-Type": "application/json"
        }

app.run(debug=True)