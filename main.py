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

@app.route("/index/<par>")
def index_par(par):
    return render_template("base.html", par=par)

@app.route("/training/<prof>")
def training(prof:str):
    if ("инженер" in prof.lower()) or ("строитель" in prof.lower()):
        return render_template("train.html", prof=1, par="Инженерные тренажеры")
    else:
        return render_template("train.html", prof=0, par="Научные симуляторы")

@app.route("/list_prof/", defaults={"listT":None})
@app.route("/list_prof/<listT>")
def list_prof(listT):
    if listT in ["ol", "ul"]:
        return render_template("prof.html", list=listT)
    else:
        return "<b style='font-size:100px;'>BAD PARAMETER<b>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8086)