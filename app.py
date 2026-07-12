from flask import Flask, render_template, request
from recommendation import get_recommendations

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    movie = request.form.get("movie")

    recommendations = get_recommendations(movie)

    return render_template(
        "index.html",
        movie=movie,
        recommendations=recommendations
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")




@app.route("/movie/<path:title>")
def movie_details(title):
    return render_template(
        "movie_details.html",
        title=title
    )


if __name__ == "__main__":
    app.run(debug=True)