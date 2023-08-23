from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "fasfafs"

@app.route("/", methods=["GET", "POST"])
def login():
    
    return 'àdsfdsfgsd'
