from flask import Flask, jsonify, request
import spacy
import json  # Import the json module

app = Flask(__name__)

@app.route('/', methods=['POST'])
def disp():
    model = spacy.load('./model-last')
    text = request.json['name']
    try:
           result = model(text).cats
           Keymax = max(zip(result.values(), result.keys()))[1]
           return json.dumps({
                'category' : Keymax
		   })
    except:
          print("Unable to take")
          return json.dumps({
               "result" : "Something went wrong"
		  })

# Driver function
if __name__ == '__main__':
    app.run()