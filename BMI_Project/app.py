from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi():
    bmi_value = None
    category = None
    message = None

    if request.method == "POST":
        height = float(request.form["height"])
        weight = float(request.form["weight"])

        height_m = height / 100
        bmi_value = round(weight / (height_m * height_m), 2)

        if bmi_value < 18.5:
            category = "Underweight"
            message = "you should eat healthy food 🙂"
        elif bmi_value < 25:
            category = "Normal"
            message = "you are in a perfect range 👍"
        elif bmi_value < 30:
            category = "Overweight"
            message = "start light exercise regularly 🙂"
        else:
            category = "Obese"
            message = "Healthy lifestyle important 🏃‍♂️"

    return render_template("index.html",
                           bmi=bmi_value,
                           category=category,
                           message=message)

if __name__ == "__main__":
    app.run(debug=True)