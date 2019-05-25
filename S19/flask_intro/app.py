from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("bmi.html")
    else:
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        bmi = weight / height ** 2
        return  render_template("bmi.html", bmi=bmi)

# @app.route("/greeting/<int:m>/<int:n>")
# def whatever(m, n):
#     return render_template("index.html", m=m, n=n)


app.run(host="10.10.210.245", port=8080)
