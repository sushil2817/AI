class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Sipping Chai")

    def add_sugar(self,amount):
        print("Added the sugar")


my_chai = Chai(sweetness=3,milk_level=2)

my_chai.add_sugar(3)