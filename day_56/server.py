from flask import Flask, render_template

app = Flask(__name__)


# Render Homepage
@app.route("/")
def hello_world():
    return render_template('index.html')


# run the app
if __name__ == "__main__":
    app.run(debug=True)
