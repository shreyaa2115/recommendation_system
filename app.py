from flask import Flask, render_template, request
from model import recommend_products, trending_products, popular_this_month
import pandas as pd

app = Flask(__name__)

data = pd.read_excel("ecommerce_sales_dataset.xlsx")

@app.route("/", methods=["GET","POST"])
def home():

    recommendations = []
    images = []
    history = []
    trending = trending_products()
    recent = popular_this_month()

    if request.method == "POST":

        user_id = int(request.form["user_id"])

        recommendations, images, history = recommend_products(user_id)

    return render_template(
        "index.html",
        recommendations=recommendations,
        images=images,
        history=history,
        trending=trending,
        recent=recent
    )

if __name__ == "__main__":
    app.run(debug=True)