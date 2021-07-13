class Products:
    def __init__(self, name, price, catagory):
        self.name = name
        self.price = price
        self.catagory = catagory
        
        
        
    
    def update_price(self,percent_change, is_increased):
        self.percent_change = percent_change
        if is_increased == True:
            self.price = (self.price * percent_change) + self.price 
            return self
        else:
            self.price -= (self.price * self.percent_change)
            return self
            
            
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
        self.prod = products.append
        id(self.prods)
    
        
    def add_product(self, new_product):
        self.new_product = new_product
        self.prod(new_product)
        return self
    
    def sell_product(self,ind):
        self.ind=ind
        # for i in range(len(self.prods)):
        if id== ind :
            self.prods.pop(ind)
        return self    

    def inflation(self,percent_increase):
        self.percent_increased = percent_increase
        Products.update_price
        return self

    def set_clearance(self,catagory,percent_discount):
        self.catagory = catagory
        self.percent_discount=percent_discount
        if self.catagory == catagory:
            Products.price = Products.price - (Products.price * percent_discount)
        return self


Toy=Store("RcVheicles")
Toy.add_product("RcSpeedBoat").add_product("RedOct").add_product("MiniCoop").add_product("MustangGt").inflation(20).sell_product(2).add_product("RamTruck4x4")

