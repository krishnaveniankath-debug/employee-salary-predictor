from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["GET", "POST"])
def predict():
    salary = None

    if request.method == "POST":
        experience = float(request.form["experience"])
        salary = 25000 + (experience * 5000)

    return render_template("predictor.html", salary=salary)

if __name__ == "__main__":
    app.run(debug=True)
