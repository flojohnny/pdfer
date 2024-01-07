from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello, World!")


@app.route("/api/call-python-function", methods=["POST"])
def call_python_function():
    # Implement your Python function logic here
    result = {"result": "Python function called successfully!"}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
