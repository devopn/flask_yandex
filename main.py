from flask import Flask, render_template, request

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

@app.route("/astronaut_selection", methods=["GET", "POST"])
def astronaut_selection():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        class_ = request.form["class"]
        print(name, surname, email, class_)
        profession = request.form.getlist("profession")
        return render_template("astronaut_selection.html", name=name, surname=surname, email=email, class_=class_, profession=profession)
    else:
        return render_template("astronaut_selection.html")
    
@app.route("/choice/<planet>")
def choice(planet):
    return render_template("choice.html", planet=planet)

@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return render_template("results.html", nickname=nickname, level=level, rating=rating)   

@app.route("/carousel")
def carousel():
    return render_template("carousel.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8089)