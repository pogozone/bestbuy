""" a small example to fill a basket """
import sys

import products
import store


def handle_show_all_products(this_store):
    """Zeigt alle Produkte an."""
    print("\nAlle verfügbaren Produkte:\n")
    this_store.show_all_products()


def handle_show_total_quantity(this_store):
    """Zeigt die Gesamtmenge aller Produkte."""
    print(f"\nMenge aller Produkte im Lager: {this_store.get_total_quantity()}")


def handle_add_to_basket(this_store):
    """Hinzufügen von mehreren Produkten zum Warenkorb."""

    shopping_list = []

    while True:
        available_products = this_store.get_all_products()
        if not available_products:
            print("\nAktuell sind keine Produkte mehr verfügbar.")
            break

        this_store.show_all_products()

        try:
            number = int(input("\nWählen sie ein Produkt: "))
            if not 1 <= number <= len(available_products):
                print("Dieses Produkt gibt es nicht.")
                continue  # Zurück zum Start der Schleife

            product = available_products[number - 1]
            queued_quantity = sum(  # <-- NEU
                qty for item_product, qty in shopping_list if item_product == product  # <-- NEU
            )
            max_selectable = product.quantity - queued_quantity
            if max_selectable <= 0:  # <-- NEU
                print(  # <-- NEU
                    f"Von {product.name} sind bereits alle verfügbaren "  # <-- NEU
                    f"({product.quantity}) Stück in dieser Auswahl vorgemerkt."  # <-- NEU
                )  # <-- NEU
                continue  # <-- NEU

            amount = int(input("\nGeben sie die Bestellmenge an: "))
            if not 1 <= amount <= max_selectable:
                print(f"Bitte wähle zwischen 1 und {max_selectable} Stück.")
                continue  # Zurück zum Start der Schleife

        except ValueError:
            print("Bitte gib eine ganze Zahl ein.")
            continue

        # Produkt zur lokalen Einkaufsliste hinzufügen
        shopping_list.append((product, amount))
        print(f"-> {amount}x {product.name} wurde dem Warenkorb hinzugefügt.")

        # Nachfragen, ob ein weiteres Produkt gewünscht ist
        another = (
            input(
                "\nMöchtest du ein weiteres Produkt hinzufügen? (j/n): "
            )
            .strip()
            .lower()
        )
        if another != "j":
            break

    # Wenn Produkte im Warenkorb gelandet sind, Bestellung abschließen
    if shopping_list:
        this_store.order(shopping_list)
        this_store.create_basket(shopping_list)
        handle_show_basket(this_store)
    else:
        print("\nEs wurden keine Produkte ausgewählt.")


def handle_show_basket(this_store):
    """Zeigt den aktuellen Warenkorb und die Gesamtsumme an."""
    if not this_store.basket:
        print("\nDer Warenkorb ist leer.")
        return

    # Gesamtsumme sicher aus den bereits im Warenkorb gespeicherten Preisen berechnen
    total = this_store.get_total()
    print(f"\nGesamtsumme: {total:.2f} €\nWarenkorb:")
    this_store.show_basket()


def handle_clear_basket(this_store):
    """Warenkorb leeren / Bestellung abbrechen."""
    if not this_store.basket:
        print("\nEs befinden sich keine Waren im Warenkorb.")
        return

    this_store.clear_order()
    print("\nBestellung abgebrochen. Warenbestand wieder hergestellt.")

def handle_checkout(this_store):
    """Schließt den Kauf der Warenkorb-Artikel ab und gibt einen Beleg aus."""
    if not this_store.basket:
        print("\nDer Warenkorb ist leer.")
        return

    receipt = this_store.checkout()
    print("\n===== Kaufbeleg =====")
    for item in receipt["items"]:
        print(
            f"- {item['name']} | Menge: {item['amount']} | "
            f"Einzelpreis: {item['unit_price']:.2f} € | "
            f"Gesamt: {item['total_price']:.2f} €"
        )
    print("---------------------")
    print(f"Zu zahlen: {receipt['total']:.2f} €")
    print("Vielen Dank für deinen Einkauf!")

def handle_exit():
    """Programm beenden."""
    print("\nAuf Wiedersehen!")
    sys.exit()


def go_ahead(this_store, choice):
    """ do order step by step """
    try:
        choice = int(choice)
    except ValueError:
        print("\nWählen sie eine Aktion von 1 bis 7.\n")
        return True

    # Mapping von Auswahl zu dedizierten Funktionen
    if choice == 1:
        handle_show_all_products(this_store)
    elif choice == 2:
        handle_show_total_quantity(this_store)
    elif choice == 3:
        handle_add_to_basket(this_store)
    elif choice == 4:
        handle_show_basket(this_store)
    elif choice == 5:
        handle_clear_basket(this_store)
    elif choice == 6:
        handle_checkout(this_store)
    elif choice >= 7:
        handle_exit()
    else:
        print("\nWählen sie eine Aktion von 1 bis 7.\n")

    return True


def start(this_store):
    """ start application on command line """
    menu = [
        "Zeige alle Produkte",
        "Menge aller Produkte",
        "In den Warenkorb legen",
        "Warenkorb anzeigen",
        "Warenkorb leeren",
        "Bestellung abschließen",
        "Beenden"
    ]
    while True:
        print("\n===== Best Buy =====\n")
        for index, item in enumerate(menu, start=1):
            print(f"{index}. {item}")
        choice = input("\nWählen sie eine Aktion von 1 bis 7: ").strip()
        go_ahead(this_store, choice)


def main():
    """ run application """
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
