from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_home():
    return render_template("index.html")

@app.route("/data")
def hello_data():
    return render_template("data.html")


if __name__ == "__main__":
    app.run()
