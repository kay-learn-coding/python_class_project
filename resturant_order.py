class resturant_order:
    def __init__(self):
        self.total_item_list=[] #list containing (item object, item quantity)
        self.total_bill=0.0 #current bill balance

    def add_item(self,item_object,order_quantity):
        if order_quantity<=0: #verify stock limit
            return "Quantity must be greater than zero."#return to confirm quantity
        
        if item_object.quantity>=order_quantity:#check_stock
            item_object.quantity-=order_quantity#deduct_amount
            batch_cost=item_object.cost*order_quantity
            self.total_bill+=batch_cost

            #record transaction inside item tracker
            self.total_item_list.append((item_object.name,order_quantity,batch_cost))
            return "success"
        else:
            return f"order failed. Only {item_object.quantity} unit of {item_object.name} availble."
