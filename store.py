import products

class Store:

    def __init__(self, product_list):
        self.products_in_store = []
        self.product_list = product_list
        for product in product_list:
            self.add_product(product)

    def add_product(self, product):
        self.products_in_store.append(product)

    def remove_product(self, product):
        self.products_in_store.remove(product)

    def get_all_products(self):
        return [
            product
            for product in self.products_in_store
            if product.is_active()
        ]

    def order(self, shopping_list):
        total_price = 0.0
        for product, amount in shopping_list:
            total_price += product.buy(amount)
        return total_price

    def basket(self, shopping_list):
        basket = []
        for product, amount in shopping_list:
            basket.append({
                "name": product.name,
                "amount": amount,
                "total_price": product.price * amount,
            })
        return basket

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products_in_store:
            total_quantity += product.quantity
        return total_quantity

def main():

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    available_products = best_buy.get_all_products()

    print(f"Produkte insgesamt: {best_buy.get_total_quantity()}")

    shopping_list = [(available_products[0], 1), (available_products[1], 2)]
    print(f"Total: {best_buy.order(shopping_list)}")
    print(f"Basket: {best_buy.basket(shopping_list)}")

    print(f"Restbestand: {best_buy.get_total_quantity()}")

if __name__ == "__main__":
    main()