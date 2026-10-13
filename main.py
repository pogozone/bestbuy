import products
import store

def go_ahead(store, choice):
    if choice == "1":
        print("\nAll products available:\n")
        store.show_all_products()

    elif choice == "2":
        print(f"\nTotal amount in store: {store.get_total_quantity()}")

    elif choice == "3":
        available_products = store.get_all_products()
        store.show_all_products()

        product_number = int(input("\nChoose product: "))
        amount = int(input("\nAmount to buy: "))

        product = available_products[product_number - 1]
        shopping_list = [(product, amount)]
        store.create_basket(shopping_list)

        print(f"Total: {store.order(shopping_list)}")
        print("Basket:")
        store.show_basket()

    elif choice == "4":
        store.clear_basket()

    elif choice == "5":
        print("\nGoodbye!")
        return False

    else:
        print("\nPlease enter a number from 1 to 4.")
    start(store)

def start(store):
    menu = [
        "List all products in store",
        "Show total amount in store",
        "Make an order",
        "Clear basket",
        "Quit"
    ]
    print("\n===== Best Buy =====\n")
    for index, item in enumerate(menu, start=1):
        print(f"{index}. {item}")
    choice = input("\nPlease choose a number: ")
    go_ahead(store, choice)

def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()
