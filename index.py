'''resturant system

#resturant_name == Simple Food
#input_system

#menu
food?
cost?
quantity?

drink?
cost?
quantity?

#total_sys
total_item_list
total_bill


'''
import tkinter

class menu_item:
    num_of_food=0
    def __init__(self,name,cost,quantity):
        self.name=name
        self.cost=float(cost) #money need to be float
        self.quantity=int(quantity) #quantity need to be num

    def __str__(self): #how data will be displayed when called
        return f"{self.name}-${self.cost:.2f} (stock:{self.quantity})"

class drink(menu_item):
    num_of_drink=0
    def __init__(self,name,cost,quantity):
        super().__init__(name,cost,quantity) #takes data from MenuItem
        drink.num_of_drink+=1

class food(menu_item):
    num_of_food=0
    def __init__(self,name,cost,quantity):
        super().__init__(name,cost,quantity) #takes data from MenuItem
        drink.num_of_drink+=1
           
class restaurant_order:

    def __init__(self):
        self.total_item_list=[] #list containing (item object, item quantity)
        self.total_bill=0.0 #current bill balance

    def add_item(self,item_object,order_quantity):
        if order_quantity<=0: #verify stock limit
            print("Quantity must be greater than zero.")
            return False
        
        if item_object.quantity>=order_quantity:
            #check if the resturant as enough stock
            item_object.quantity-=order_quantity
            #deduct the ordered amount directly from item's stock tracking
            batch_cost=item_object.cost*order_quantity
            self.total_bill+=batch_cost

            #record transaction inside item tracker
            self.total_item_list.append((item_object.name,order_quantity,batch_cost))
            print(f"added {order_quantity}x {item_object.name} to order.")
            return True
        else:
            print(f"order failed. Only {item_object.quantity} unit of {item_object.name} availble.")
            return False
        
    def print_receipt(self):
        print("\n"+"="*35)
        print("  Simple Food   ")
        print("="*35)

        for name,qty,cost in self.total_item_list:
            print(f"{qty}x {name:<18} ${cost:>6.2f}")
            print("_"*35)
            print(f"TOTAL BILL:         ${self.total_bill:>6.2f}")
            print("="*35)



f1 = food("seabass",20.00,20)
f2 = food("ribye",25.00,30)
f3 = food("chicken",20.00,50)

d1 = drink("water",2.00,50)
d2 = drink("coke",3.00,50)
d3 = drink("orange",4.00,50)

#create directory
menu_directory={
    "seabass":f1, "ribeye":f2, "chicken":f3,
    "water":d1, "coke":d2, "orange":d3
}

#create customer transaction
customer_cart=restaurant_order()
print("--- Welcome to Simple Food ---")
print(f1)
print(f2)
print(d1)

#simulating run:show how the receipt would look like.
print("\n--- Simulation: Ordering Items ---")

customer_cart.add_item(menu_directory["seabass"],2)
customer_cart.add_item(menu_directory["ribeye"],1)
customer_cart.add_item(menu_directory["orange"],2)
customer_cart.add_item(menu_directory["coke"],1)

#attempt to over order test
customer_cart.add_item(menu_directory["seabass"],50)

#print final_bill
#customer_cart.print_recipt()

print("\n--- Order Stock Check ---")
print(f1)
print(f2)
print(d1)
print(d2)
