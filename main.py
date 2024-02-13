from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/promotion")
def promotion():
    return render_template("promotion.html")

@app.route("/image_mars")
def image_mars():
    return render_template("mars_image.html")

@app.route("/promotion_image")
def promotion_image():
    return render_template("promotion_image.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)