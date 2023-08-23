from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "fasfafs"

@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    
    return render_template("login.html")
