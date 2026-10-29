import sys

import products
import store


def handle_show_all_products(store):
  """Zeigt alle Produkte an."""
  print("\nAlle verfügbaren Produkte:\n")
  store.show_all_products()


def handle_show_total_quantity(store):
  """Zeigt die Gesamtmenge aller Produkte."""
  print(f"\nMenge aller Produkte im Lager: {store.get_total_quantity()}")


def handle_add_to_basket(store):
  """Hinzufügen eines Produkts zum Warenkorb."""
  available_products = store.get_all_products()
  store.show_all_products()

  try:
    number = int(input("\nWählen sie ein Produkt: "))
    if not 1 <= number <= len(available_products):
      print("Dieses Produkt gibt es nicht.")
      return True

    product = available_products[number - 1]

    amount = int(input("\nGeben sie die Bestellmenge an: "))
    if not 1 <= amount <= product.quantity:
      print(f"Bitte wähle zwischen 1 und {product.quantity} Stück.")
      return True

  except ValueError:
    print("Bitte gib eine ganze Zahl ein.")
    return True

  shopping_list = [(product, amount)]
  total = store.order(shopping_list)
  store.create_basket(shopping_list)
  print(f"\nTotal: {total:.2f} €\ Warenkorb:")
  store.show_basket()


def handle_clear_basket(store):
  """Warenkorb leeren / Bestellung abbrechen."""
  store.clear_order()
  print("\nBestellung abgebrochen. Warenbestand wieder hergestellt.")


def handle_exit():
  """Programm beenden."""
  print("\nAuf Wiedersehen!")
  sys.exit()


def go_ahead(store, choice):
  try:
    choice = int(choice)
  except ValueError:
    print("\nWählen sie eine Aktion von 1 bis 6.\n")
    return True

  # Mapping von Auswahl zu dedizierten Funktionen
  if choice == 1:
    handle_show_all_products(store)
  elif choice == 2:
    handle_show_total_quantity(store)
  elif choice == 3:
    pass  # Platzhalter für zukünftige Logik
  elif choice == 4:
    handle_add_to_basket(store)
  elif choice == 5:
    handle_clear_basket(store)
  elif choice >= 6:
    handle_exit()
  else:
    print("\nWählen sie eine Aktion von 1 bis 6.\n")

  return True

def start(store):
    menu = [
        "Zeige alle Produkte",
        "Menge aller Produkte",
        "Bestellen",
        "In den Warenkorb legen",
        "Warenkorb leeren",
        "Beenden"
    ]
    while True:
        print("\n===== Best Buy =====\n")
        for index, item in enumerate(menu, start=1):
            print(f"{index}. {item}")
        choice = input("\nWählen sie eine Aktion von 1 bis 6: ").strip()
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
