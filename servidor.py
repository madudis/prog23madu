from flask import Flask 

app = Flask(__name__)
@app.route("/")
def run():
    return "<b>AAAAAAAAAAAAAAAAAAAAAAAABA</b>"
app.run(debug= True)

