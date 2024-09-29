class Microwave:
    def __init__(self, brand:str, power_rating:str, turned_on:bool,):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = turned_on

    def turn_on():
        if self.turned_on:
            print(f"Microwave brand {self.brand} is turned on!")
        else:
            print(f"The microwave brand {self.brand} is turned off!")


smeg = Microwave("Smeg", "B")
bosch = Microwave("Bosch", "C")



