from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/leading")
def leading():
    return render_template("leading.html")

@app.route("/predict", methods=["POST"])
def predict():
    # prediction logic 
    result = "Transaction is Safe"
    return render_template("result.html", prediction_text=result)

if __name__ == "__main__":

    app.run(debug=True)
