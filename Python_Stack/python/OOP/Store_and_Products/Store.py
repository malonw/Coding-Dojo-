
class Products:
    def __init__(self, name, price, catagory):
        self.name = name
        self.price = price
        self.catagory = catagory
        
        
    
    def update_price(self,percent_change, is_increased):
        if is_increased == True:
            self.price = (self.price * percent_change) + self.price
        else:
            self.price = self.price - (self.price * percent_change)
            
    def print_info(self):
        print(f"Name: {self.name} Catagory: {self.catagory}, Price: {self.price}")
        


RC = Products("Rambler", 100, "RcTruck")
RC.update_price(.20, True)
RC.print_info()
RC.update_price(.50, False)
RC.print_info()


class Store:

    def __init__ (self, name, products=[]):
        self.name = name
        self.prods=products
        self.price = Products
        
        
    def add_product(self, new_product, catagory, price):
        self.catagory = catagory
        self.price = price
        self.new_product = new_product
        self.prods.append(new_product)
        return self
    
    def sell_product(self,ind):
        self.ind =ind  
        for i in range(len(self.prods)):
            if i == ind:
                self.prods.pop(ind)
                return
        return self

    def inflation(self,percent_increase):
        self.percent_increased = percent_increase
        for i in self.prods:
            self.price = self.price + (self.price * percent_increase)
            print(self.price)
        return self
        
        


    def set_clearance(self,catagory,percent_discount):
        self.percent_discount=percent_discount
        if self.catagory == catagory:
            self.price = self.price - (self.price * percent_discount)
        return self
        # pass


Toy=Store("RcVehicles")
Toy.add_product("Erevo", "RcTruck", 500).add_product("RedOct", "RcSub", 200).add_product("MiniCoop", "RcCar", 100).add_product("MustangGT", "RcCar", 700).add_product("RamTruck4x4","RcTruck", 600)
print(Toy.prods)
Toy.sell_product(2)
print(Toy.prods)
Toy.inflation(.50)
Toy.set_clearance("RcSub", .80)
print(Toy.catagory)





