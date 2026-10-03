@app.route("/predict", methods=["GET", "POST"])
def predict():
    salary = None

    if request.method == "POST":
        experience = float(request.form["experience"])

        # Simple salary prediction formula
        salary = 25000 + (experience * 5000)

    return render_template("predictor.html", salary=salary)