from flask import Flask, request,  jsonify #, g
import json

app = Flask(__name__)

direction = "stop"

@app.route('/',methods = ['POST', 'GET'])
def result():
    global direction
    print("Entered result()")

    if request.method == 'POST':
        content = request.get_json(force=True)
        direction = content["Button"]
        return jsonify(content)

    if request.method == 'GET':
        c = direction
        direction = "stop"
        return c

if __name__ == "_main_":
    app.run(debug=True)
