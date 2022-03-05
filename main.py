from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def main():
    r = requests.get("https://api.punkapi.com/v2/beers/random")
    beer_json = r.json()
    beer = {
        "name": beer_json[0]["name"],
        "abv": beer_json[0]["abv"],
        "desc": beer_json[0]["description"],
        "food_pair": beer_json[0]["food_pairing"][0]
    }

    return render_template("index.html",beer=beer)


if __name__ == "__main__":
    app.run(debug=True)
