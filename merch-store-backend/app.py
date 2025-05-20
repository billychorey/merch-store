from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "title": "Unicorn Hoodie", "price": 39.99},
    {"id": 2, "title": "Terrier T-shirt", "price": 24.99},
]

@app.route("/products")
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)
