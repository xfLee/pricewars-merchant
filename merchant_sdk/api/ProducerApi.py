from typing import List

from .PricewarsBaseApi import PricewarsBaseApi
from ..models import Product, ApiException


class ProducerApi(PricewarsBaseApi):

    def __init__(self, host='http://producer', debug=False):
        PricewarsBaseApi.__init__(self, host=host, debug=debug)

    def buy_product(self) -> Product:
        return self.buy_products(amount=1)

    def buy_products(self, amount) -> Product:
        r = self.request('get', 'buy/{}'.format(amount))
        if 400 <= r.status_code < 500:
            raise ApiException(r.json())
        return Product.from_dict(r.json())

    def get_products(self) -> List[Product]:
        r = self.request('get', 'products')
        if 400 <= r.status_code < 500:
            raise ApiException(r.json())
        return Product.from_list(r.json())

    def add_products(self, products: List[Product]):
        product_dict_list = [p.to_dict() for p in products]
        r = self.request('post', 'products', json=product_dict_list)
        if 400 <= r.status_code < 500:
            raise ApiException(r.json())

    def update_products(self, products: List[Product]):
        product_dict_list = [p.to_dict() for p in products]
        r = self.request('put', 'products', json=product_dict_list)
        if 400 <= r.status_code < 500:
            raise ApiException(r.json())

    def get_product(self, product_uid) -> Product:
        r = self.request('get', 'products/{}'.format(product_uid))
        if 400 <= r.status_code < 500:
            raise ApiException(r.json())
        return Product.from_dict(r.json())

    def add_product(self, product: Product):
        r = self.request('post', 'products', json=product.to_dict())
        if 400 <= r.status_code < 500:
            raise ApiException(r.json())

    def update_product(self, product: Product):
        r = self.request('put', 'products/{}'.format(product.uid), json=product.to_dict())
        if 400 <= r.status_code < 500:
            raise ApiException(r.json())

    def delete_product(self, product_uid):
        r = self.request('delete', 'products/{}'.format(product_uid))
        if 400 <= r.status_code < 500:
            raise ApiException(r.json())
