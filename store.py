""" class to store products """

import products


class Store:
    """ store products """

    def __init__(self, product_list):
        self.basket = []
        self.products_in_store = []
        self.product_list = product_list
        for product in product_list:
            self.add_product(product)

    def add_product(self, product):
        """ add product to store """
        self.products_in_store.append(product)

    def remove_product(self, product):
        """ remove product from store """
        self.products_in_store.remove(product)

    def get_all_products(self):
        """ get all products """
        return [
            product
            for product in self.products_in_store
            if product.is_active()
        ]

    def show_all_products(self):
        """ show all products """
        for index, product in enumerate(self.get_all_products(), start=1):
            print(
                f"{index}. {product.name} | "
                f"Preis: {product.price:.2f} | "
                f"Menge: {product.quantity}"
            )

    @staticmethod
    def order(shopping_list):
        """ add product to basket """
        total_price = 0.0
        for product, amount in shopping_list:
            total_price += product.add_to_basket(amount)
        return total_price

    def get_total(self):
        """ return total price of all products """
        return sum(item["total_price"] for item in self.basket)

    def create_basket(self, shopping_list):
        """ create basket """
        for product, amount in shopping_list:
            # Prüfen, ob das Produkt bereits im Warenkorb ist
            existing_item = None
            for item in self.basket:
                if item["product"] == product:
                    existing_item = item
                    break

            if existing_item:
                # Menge und Gesamtpreis des bestehenden Eintrags anpassen
                existing_item["amount"] += amount
                existing_item["total_price"] += product.price * amount
            else:
                # Neuen Eintrag hinzufügen, falls noch nicht vorhanden
                self.basket.append({
                    "product": product,
                    "name": product.name,
                    "amount": amount,
                    "total_price": product.price * amount,
                })
        return self.basket

    def clear_order(self):
        """ clear order """
        for item in self.basket:
            product = item["product"]
            product.set_quantity(product.quantity + item["amount"])

        self.basket.clear()

    def clear_basket(self):
        """ clear basket """
        self.basket = []

    def show_basket(self):
        """ show basket """
        for index, item in enumerate(self.basket, start=1):
            print(
                f'{index}. {item["name"]} | '
                f'Menge: {item["amount"]} | '
                f'Total: {item["total_price"]:.2f} €'
            )

    def get_total_quantity(self):
        """ return total quantity of all products """
        total_quantity = 0
        for product in self.products_in_store:
            total_quantity += product.quantity
        return total_quantity


def main():
    """
    run products on commandline.
    for development and bugfix purposes
    """
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    available_products = best_buy.get_all_products()

    print(f"Produkte insgesamt: {best_buy.get_total_quantity()}")

    shopping_list = [(available_products[0], 1), (available_products[1], 2)]
    print(f"Total: {best_buy.order(shopping_list)}")
    print(f"Warenkorb: {best_buy.create_basket(shopping_list)}")

    print(f"Restbestand: {best_buy.get_total_quantity()}")


if __name__ == "__main__":
    main()
