
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
        id(self.prods)
        
        
    def add_product(self, new_product):
        self.new_product = new_product
        self.prods.append(new_product)
        return self
    
    def sell_product(self,ind):
        self.ind =ind  
        if id == ind:
            self.prods.pop(id)
        return self

    def inflation(self,percent_increase):
        # self.percent_increased = percent_increase
        # self.percent_increased = Products.is_increased
        pass

    def set_clearance(self,catagory,percent_discount):
        # self.percent_discount=percent_discount
        # if self.catagory == catagory:
        #     Products.price = Products.price - (Products.price * percent_discount)
        pass


Toy=Store("RcVehicles")
Toy.add_product("Erevo").add_product("RedOct").add_product("MiniCoop").add_product("MustangGT").add_product("RamTruck4x4")
print(Toy.prods)
Toy.sell_product(2)




