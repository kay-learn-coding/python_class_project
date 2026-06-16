import time
import tkinter as tk#interface
from tkinter import Label, Button, Entry, Frame, messagebox
from menu_item import food,drink#OOP classes
import resturant_order
from data import load_menu_from_json, save_menu_to_json#read_write_data

#defining directory and cus_cart to avoid error
menu_directory={}
customer_cart=resturant_order.resturant_order()

def main():#main def to cointain all code
    def menu_database():#menu_items
        global menu_directory
        
        menu_directory=load_menu_from_json()
        
        if not menu_directory:
            f1 = food("seabass",20.00,20)
            f2 = food("ribye",25.00,30)
            f3 = food("chicken",20.00,50)
            d1 = drink("water",2.00,50)
            d2 = drink("coke",3.00,50)
            d3 = drink("orange",4.00,50)
            
            menu_directory={
                "seabass":f1, 
                "ribeye":f2, 
                "chicken":f3,
                "water":d1, 
                "coke":d2, 
                "orange":d3
                }

    def load_order_screen():
        for widget in root.winfo_children():
            widget.destroy()
        
        title=Label(root, text="Simple Food - Digital Ordering System", font=("arial",16,"bold"),
                fg="#ffcc00",bg="#1a1a1a")
        title.pack(pady=15)
        
        menu_frame = Frame(root, bg="#262626", padx=10, pady=10)
        menu_frame.pack(pady=10, fill="both", expand=True, padx=20)
        
        Label(menu_frame, text="Item Details", font=("Arial", 11, "bold"), fg="#ffffff", bg="#262626").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        Label(menu_frame, text="Order Quantity", font=("Arial", 11, "bold"), fg="#ffffff", bg="#262626").grid(row=0, column=1, padx=10, pady=5)
        
        global entry_widget_map
        entry_widget_map = {}
        
        for idx,(key_name,item_obj) in enumerate(menu_directory.items(),start=1):
            
            item_lbl=Label(menu_frame,text=str(item_obj),font=("Arial", 11), fg="#ffffff", bg="#262626")
            item_lbl.grid(row=idx, column=0, sticky="w", padx=10, pady=8)
            
            qty_entry = Entry(menu_frame, font=("Arial", 11), width=8, justify="center")
            qty_entry.insert(0, "0")
            qty_entry.grid(row=idx, column=1, padx=10, pady=8)
            
            entry_widget_map[key_name] = qty_entry
            
        checkout_btn = Button(root, text="Process Order & Generate Receipt", command=lambda: process_checkout(root),
                      font=("Arial", 12, "bold"), bg="#333333", fg="#ffcc00", activebackground="#ffcc00", relief="groove")
        checkout_btn.pack(pady=20)

    menu_database()
    global customer_cart
    load_order_screen()

def process_checkout(root):
    has_orders=False
    for key_name,entry_box in entry_widget_map.items():
        raw_val=entry_box.get().strip()
        try:
            qty_to_buy=int(raw_val)
        except ValueError:
            messagebox.showerror("wrong Input", f"whole number only for '{key_name.capitalize()}'.")
            return  
        
        if qty_to_buy > 0: #add item to cart if amount greater than 0
            has_orders=True
            item_target_obj=menu_directory[key_name]
            status_msg=customer_cart.add_item(item_target_obj,qty_to_buy)
    
            if status_msg !="success":
                messagebox.showwarning("stock alert",status_msg)
                return
    
    if not has_orders:
        messagebox.showinfo("cart is empty,pls add atleast one item")
        return 
    
    save_menu_to_json(menu_directory)#save updated stock data
    
    load_receipt_screen(root)

def load_receipt_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    #styling how my receipt will look like
    receipt_box = Frame(root, bg="#ffffff", padx=20, pady=20, bd=2, relief="solid")
    receipt_box.pack(pady=40, padx=40, fill="both", expand=True)

    receipt_lines=[
        "======================================",
        "             Simple Food              ",
        "======================================\n"
    ]

    for name,qty,cost in customer_cart.total_item_list:
        receipt_lines.append(f"{qty}x {name:<16} ${cost:>6.2f}")#layout of data

    #add the totals and footer
    receipt_lines.extend([
        "========================================",
        f"TOTAL BILL:          ${customer_cart.total_bill:>6.2f}",
        "======================================\n",
        "     Thank you for dining with us!    "
    ])
    full_receipt_text="\n".join(receipt_lines)
    Label(receipt_box, text=full_receipt_text, font=("Courier", 11),
          fg="#000000", bg="#ffffff", justify="left").pack(anchor="n", pady=10)
    Button(root, text="Close Application", command=root.destroy, 
           font=("Arial", 10, "bold"), bg="#d9534f", fg="white").pack(pady=15)
    

#loop window setup
root=tk.Tk()
root.title("Simple Food - POS Order Desk")
root.geometry("600x650")
root.configure(bg="#1a1a1a")

main()
root.mainloop()
