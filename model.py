import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

data = pd.read_excel("ecommerce_sales_dataset.xlsx")

user_encoder = LabelEncoder()
product_encoder = LabelEncoder()

data["user"] = user_encoder.fit_transform(data["user_id"])
data["product"] = product_encoder.fit_transform(data["product_name"])

def recommend_products(user_id):

    history = data[data["user_id"] == user_id]

    if history.empty:
        return [], [], []

    categories = history["category"].unique()

    recommendations = data[data["category"].isin(categories)]

    recommendations = recommendations.sort_values("rating", ascending=False)

    recommendations = recommendations.drop_duplicates("product_name")

    top5 = recommendations.head(5)

    return (
        top5["product_name"].tolist(),
        top5["image"].tolist(),
        history["product_name"].tolist()
    )

def trending_products():

    return data["product_name"].value_counts().head(5).index.tolist()

def popular_this_month():

    data["purchase_date"] = pd.to_datetime(data["purchase_date"])

    recent = data[data["purchase_date"] > "2025-01-01"]

    return recent["product_name"].value_counts().head(5).index.tolist()