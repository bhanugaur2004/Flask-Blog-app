from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def bhanu():
    name = "Bhanu Gaur"
    return render_template('about.html', name2 = name)

@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

app.run(debug=True)