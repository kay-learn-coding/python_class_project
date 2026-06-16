class menu_item:#parent_class
    def __init__(self,name,cost,quantity):
        self.name=name
        self.cost=float(cost) #cash=float
        self.quantity=int(quantity) #count in int

    def __str__(self): #data_display
        return f"{self.name}-${self.cost:.2f} (stock:{self.quantity})"

class drink(menu_item):#drink_class(call parent)
    num_of_drink=0#give a starting int of 0
    def __init__(self,name,cost,quantity):
        super().__init__(name,cost,quantity) #takes data from MenuItem
        drink.num_of_drink+=1

class food(menu_item):#food version of drinks^^^
    num_of_food=0
    def __init__(self,name,cost,quantity):
        super().__init__(name,cost,quantity)
        food.num_of_food+=1