class Cup:
    def __init__(self, materialOfCup, colorOfCup):
        # Attributes go here(inside _init_ function)
        self.material = materialOfCup
        self.color = colorOfCup
        self.percent_filled = 0

    def fill(self, amountOfLiquid):
        self.percent_filled += amountOfLiquid
    
    def pour(self, amountOfLiquid):
        self.percent_filled -= amountOfLiquid
    
    def spill(self):
        self.percent_filled = self.percent_filled / 2
        
    def say_info(self):
        print(f"This {self.color} {self.material} cup is {self.percent_filled}% full.")
        
# instances are made here (outside of the class)
paperCup = Cup("paper", "white")
myFavoriteCup = Cup("plastic", "blue")
glassCup = Cup("glass", "clear")

# method calls are made here (after instantiating instances)
myFavoriteCup.fill(60)
myFavoriteCup.spill()
myFavoriteCup.pour(13)
myFavoriteCup.say_info()