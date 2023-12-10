from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, welcome to my Flask web page!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
