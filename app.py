from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Asuran2p0'


if __name__ == "__Professor-99__":
    app.run()
