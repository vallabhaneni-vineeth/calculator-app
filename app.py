from flask import Flask, render_template, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            operation = request.form["operation"]
            result = OPERATIONS[operation](a, b)
        except ValueError as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)