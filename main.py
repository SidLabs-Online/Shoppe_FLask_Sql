from flask import Flask, render_template, url_for

app = Flask(__name__)

products = [{'pid': 1, 'name': 'apple','origin':'Hong Kong', 'description': 'big red apple', 'quantity': '10','unit_price':'6.0'},
            {'pid': 2, 'name': 'orange','origin':'Japan', 'description': 'small and juicy', 'quantity': '6','unit_price':'8.0'}]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products/')
def index_products():
    return render_template('index.html', rows = products)


@app.route('/products/<int:pid>')
def product_details(pid):
    return render_template('details.html', info=products[0])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

# app.run(host='0.0.0.0', port=8080)