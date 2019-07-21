from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def hello():
    message = os.environ.get("MESSAGE")
    return f'<h1>Hello World from {message}!<br></h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
