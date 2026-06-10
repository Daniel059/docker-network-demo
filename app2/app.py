from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>App 2 - Docker Network Demo</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        input, button { padding: 10px; margin: 10px; font-size: 16px; }
        .response { margin-top: 20px; padding: 15px; background: #f0f0f0; border-radius: 8px; }
    </style>
</head>
<body>
    <h1>App 2</h1>
    <p>Calling App 1 via Docker Network...</p>
    
    <form method="POST">
        <input type="text" name="name" placeholder="Enter your name" required>
        <button type="submit">Send to App 1</button>
    </form>

    {% if response %}
    <div class="response">
        <h2>Response from App 1:</h2>
        <pre>{{ response }}</pre>
    </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    response_text = None
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        try:
            resp = requests.get(f"http://app1:5001/greet/{name}", timeout=5)
            response_text = resp.json()
        except Exception as e:
            response_text = f"Error: {str(e)}"
    return render_template_string(HTML, response=response_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

