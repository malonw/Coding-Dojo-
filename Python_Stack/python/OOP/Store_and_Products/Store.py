class Store:

    def __init__ (self, name, products=[]):
        self.name = name
        self.prods=products
        self.prod = products.append
    
        
    def add_product(self, new_product):
        self.new_product = new_product
        self.prod(new_product)
        
    
    def sell_product(self,id):
        # self.products.pop(id)    
        pass

    def inflation(self,percent_increase):
        # self.percent_increased = percent_increase
        # self.percent_increased = Products.is_increased
        pass

    def set_clearance(self,catagory,percent_discount):
        # self.percent_discount=percent_discount
        # if self.catagory == catagory:
        #     Products.price = Products.price - (Products.price * percent_discount)
        pass


Toy=Store("RcVheicles")
Toy.add_product("RcBoat")
Toy.add_product("RcSub")
Toy.add_product("RcMini")
Toy.add_product("RcCars")





class Products:
    def __init__(self, name, price, catagory):
        self.name = name
        self.price = price
        self.catagory = catagory
        Store.add_product
        
        
    
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
