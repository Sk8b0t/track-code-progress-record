class repairingShop():
    def __init__(self, name, brand, no, amt):
        self.name = name
        self.brand = brand
        self.phoneNumber = no
        self.amount = amt

    def printDetails(self):
        print("Name of Customer:", self.name)
        print("brand:", self.name)
        print("contact no:", self.name)

    def __add__(self, other):
        return f"Total money earned = {self.amount + other.amount}"

    def __floordiv__(self, other):
        return self.amount // other.amount

    def __pos__(self):
        if self.amount > 0:
            return "positive earning"
        else:
            return "negative value entered"

    def __repr__(self):
        return "This takes name,brand,phone number and cost"

    def __str__(self):
        return "why did u print the object u dumb mf"


if __name__ == '__main__':
    C1 = repairingShop("Sayan Biswas", "Acer", 8969101484, 3800)
    C2 = repairingShop("Likitha Reddy", "Lenovo", 7209537974, 5000)
    print(C1 + C2)
    print(C2 // C1)
    print(+C1)
    print(C1)
    print(C2)
    print(repr(C1))
    print(str(C2))
