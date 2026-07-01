from flask import Flask as fk, render_template
app=fk(__name__)


@app.route("/")
def hello():
   return render_template('index.html')

@app.route("/coolshit")
def show():
    return render_template('some cool shit.html')


@app.route("/sk8")
def sk():
  return render_template('sk.html')


@app.route("/about")
def about():
    name="सायन विश्वास"
    return render_template('about.html',n=name)

app.run(host="0.0.0.0", port=5000, debug=True)

