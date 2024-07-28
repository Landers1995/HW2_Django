import json
from pathlib import Path
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(Path(__file__).parent.parent.parent.parent.joinpath("catalog2.json"), encoding="utf-8") as file:
            values = json.load(file)
        categories = [value for value in values if value['model'] == "catalog.category"]
        return categories

    @staticmethod
    def json_read_products():
        with open(Path(__file__).parent.parent.parent.parent.joinpath("catalog2.json"), encoding='utf-8') as file:
            values = json.load(file)
        products = [value for value in values if value['model'] == 'catalog.product']
        return products

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    name=category['fields']['name'],
                    description=category['fields']['description'],
                    pk=category['pk'],
                )
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    name=product['fields']['name'],
                    description=product['fields']['description'],
                    price=product['fields']['price'],
                    photo=product['fields']['photo'],
                    created_at=product['fields']['created_at'],
                    updated_at=product['fields']['updated_at'],
                    category=Category.objects.get(pk=category['pk']),
                )
            )

        Product.objects.bulk_create(product_for_create)
