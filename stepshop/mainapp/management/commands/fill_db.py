import json
import os.path

from django.contrib.auth.models import User
from django.core import management
from django.core.management.base import BaseCommand

from mainapp.models import ProductCategory, Product


JSON_PATH = 'mainapp/fixtures'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='UTF-8') as f:
        return json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        management.call_command('flush', verbosity=0, interactive=False)

        categories = load_from_json('categories')
        products = load_from_json('products')

        for category in categories:
            new_category = ProductCategory(**category.get('fields'))
            new_category.save()

        for product in products:
            category_pk = product['pk']
            _category = ProductCategory.objects.get(pk=category_pk)
            product['fields']['category'] = _category
            new_product = Product(**product.get('fields'))
            new_product.save()

        User.objects.create_superuser('admin', 'admin@stepshop.kz', '123')
