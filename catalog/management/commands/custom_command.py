import json
from pathlib import Path
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(Path(__file__).parent.joinpath("catalog2.json"), encoding="utf-8") as file:
            values = json.load(file)
        categories = [value for value in values if value['model'] == "catalog.category"]
        return categories

    @staticmethod
    def json_read_products():
        with open(Path(__file__).parent.joinpath("catalog2.json"), encoding='utf-8') as file:
            values = json.load(file)
        products = [value for value in values if value['model'] == 'catalog.product']
        return products

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(Product(**product))

        Product.objects.bulk_create(product_for_create)
