class Product:
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
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Der Bestand darf nicht negativ sein.")

        self.quantity = quantity
        self.active = quantity > 0

    def is_active(self):
        return self.active

    def deactivate(self):
        self.active = False

    def show(self):
        print("Name:", self.name, "Price", self.price, "Quantity", self.quantity)

    def buy(self, quantity) -> float:
        if type(quantity) is not int or quantity <= 0:
            print("Die Kaufmenge muss eine positive ganze Zahl sein.")
            return 0
        if not self.active:
            print(f"Es tut uns leid, aber {self.name} haben wir nicht mehr im Sortiment.")
            return 0
        if quantity > self.quantity:
            print(f"Der Lagerbestand gibt das nicht her! Du kannst maximal {self.quantity} von {self.name} bestellen.")
            return 0

        price_total = quantity * self.price
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return price_total

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

    # Zu viel bestellt: Warnung und Abbruch
    bose.buy(50000000)
    bose.show()

    # Gültige Bestellung, neuer Lagerbestand wird angezeigt
    bose.buy(5)
    bose.show()

if __name__ == "__main__":
    main()