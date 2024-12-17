from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hewo():
  return render_template("index.html")

@app.route("/form")
def form():
  py_var = request.args.get("html_name")
  return render_template("form.html", jinja_var=py_var)

if __name__ == "__main__":
  app.run(debug=True)