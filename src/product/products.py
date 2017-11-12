import os
import flask

product_blueprint = flask.Blueprint('product', __name__)

@product_blueprint.context_processor
def some_processor():
    def full_name(product):
        return '{0} / {1}'.format(product['category'], product['name'])
    return {'full_name': full_name}


@product_blueprint.route('/teste')
def home():
    #return "Olá mundo!"
    return flask.render_template('home_produtos.html', products=src.product.models.PRODUCTS)

@product_blueprint.route('/product/<key>')
def product(key):
    product = src.product.models.PRODUCTS.get(key)
    if not product:
        os.abort(404)
    return flask.render_template('product.html', product=product)
