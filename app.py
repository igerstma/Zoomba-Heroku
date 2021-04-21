from flask import Flask, request, jsonify
import json

app = Flask(__name__)

direction = "stop"

@app.route('/',methods = ['POST', 'GET'])
def result():
    global direction

    if request.method == 'POST':
        content = request.get_json(force=True)
        direction = content["Button"]
        return jsonify(content)

        # direction = request.args.get("Button")
        # return jsonify(request.args)

    if request.method == 'GET':
        c = direction
        direction = "stop"
        return c

if __name__ == "_main_":
    app.run(debug=True)
