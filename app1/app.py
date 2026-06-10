from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from App 1! 🚀",
        "status": "running",
        "container": "app1",
        "info": "I am a Flask app running in Docker"
    })

@app.route('/greet/<name>')
def greet(name):
    return jsonify({
        "greeting": f"Hello {name}! Nice to meet you from App 1.",
        "from": "app1"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
