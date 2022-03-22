from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def top_page():
    return render_template("index.html")

    if __name__ == "__main__":
        app.run(debug=True)

from flask import Flask,render_template,request

@app.route("/square_input")
def square_input():
    return render_template("square_input.html")

@app.route("/square_result")
def square_result():
    height = int(request.args.get("height"))
    bottom = int(request.args.get("bottom"))
    result = height * bottom
    return render_template("square_result.html",result=result)
