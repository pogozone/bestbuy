""" product class """
class Product:
    """ Repräsentiert ein einzelnes Produkt im Shop mit Preis und Bestand. """
    quantity = 0
    active = True

    def __init__(self, name, price, quantity):

        # input validation
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Der Name muss ein nicht-leerer String sein.")

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Der Preis muss eine positive Zahl sein.")

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Die Menge muss eine ganze Zahl >= 0 sein.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self):
        """ Return the quantity of the product """
        return self.quantity

    def set_quantity(self, quantity):
        """
        set the quantity of the product.
        deactivate the product.
        """
        if quantity < 0:
            raise ValueError("Der Bestand darf nicht negativ sein.")

        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        """ return the active state of the product """
        return self.active

    def deactivate(self):
        """ deactivate the product """
        self.active = False

    def show(self):
        """ print out the current state of the product """
        print("Name:", self.name, "Preis", self.price, "Menge", self.quantity)

    def add_to_basket(self, quantity: int) -> float:
        """Legt ein Produkt in den Warenkorb.

          Prüft, ob die Menge gültig, das Produkt aktiv und ausreichend
          Lagerbestand vorhanden ist. Bei Erfolg wird der Bestand reduziert
          und der Gesamtpreis berechnet.

          Args:
              quantity (int): Die Anzahl der Einheiten, die gekauft werden sollen.

          Returns:
              float: Der zu zahlende Gesamtpreis oder 0.0, falls der Kauf fehlschlägt.
          """
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            print("Die Kaufmenge muss eine positive ganze Zahl sein.")
            return 0
        if not self.active:
            print(f"Es tut uns leid, aber {self.name} haben wir nicht mehr im Sortiment.")
            return 0
        if quantity > self.quantity:
            print(f"Du kannst maximal {self.quantity} von {self.name} bestellen.")
            return 0

        price_total = quantity * self.price

        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)

        return price_total


def main():
    """
    run products on commandline.
    for development and bugfix purposes
    """
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.add_to_basket(50))
    print(mac.add_to_basket(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

    # Zu viel bestellt: Warnung und Abbruch
    bose.add_to_basket(50000000)
    bose.show()

    # Gültige Bestellung, neuer Lagerbestand wird angezeigt
    bose.add_to_basket(5)
    bose.show()


if __name__ == "__main__":
    main()
