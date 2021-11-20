from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://waggingmongrel.com/wp-content/uploads/2018/10/shutterstock_265071971.jpg"
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
