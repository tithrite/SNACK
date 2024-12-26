import tkinter as tk

root = tk.Tk()

root.title("Illy Restaurant")

root.config(bg="#fff8e1")

label = tk.Label(root, text="Welcome to Illy Restaurant", font=('Arial', 25, "italic"), bg="#fbe9e7")
label.pack(pady=25)

menu = {
    
    "Pizza": 40.00,
    "Tacos": 49.00,
    "Sandwich": 30.00,
    "Burger": 32.00,
    "Frites": 15.00,
    "Nuggets": 35.00,
    "Soda": 15.00,
}

orders = {}

def ajouter_commande(item_name, price):
    if item_name in orders:
        orders[item_name]["quantity"] += 1
    else:
        orders[item_name] = {"quantity": 1, "price": price}
    mise_a_jour_commande()

def mise_a_jour_commande():
    order_list.delete(0, tk.END)
    total_price = 0
   
    for item, details in orders.items():
        order_list.insert(tk.END, f"{item}: {details['quantity']} * {details['price']} MAD")
        total_price += details["quantity"] * details["price"]  # Additionner chaque total de produit
    total_label.config(text=f"Total: {total_price} MAD")

def supprimer_commandes():
    global orders
    orders = {}
    mise_a_jour_commande()


def ajouter_commande_menu(item, price):
    ajouter_commande(item, price)

menu_frame = tk.Frame(root, bg="#fff8e1")
menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

tk.Label(menu_frame, text="Menu", bg="#fff8e1", font=("Arial", 16, "bold"), fg="#d84315").pack(pady=10)

for item, price in menu.items():
    frame = tk.Frame(menu_frame, bg="#fff8e1")
    frame.pack(pady=5, fill=tk.X)

    tk.Label(frame, text=f"{item} : {price} MAD", bg="#fff8e1", font=("Arial", 12), fg="#6d4c41").pack(side=tk.LEFT, padx=10)
    tk.Button(frame, text="Ajouter", command=lambda i=item, p=price: ajouter_commande_menu(i, p), bg="#d84315", fg="white", font=("Arial", 10, "bold")).pack(side=tk.RIGHT)

reset_button = tk.Button(menu_frame, text="Réinitialiser", command=supprimer_commandes, bg="#d84315", fg="white", font=("Arial", 12, "bold"))
reset_button.pack(pady=20)

order_frame = tk.Frame(root, bg="#ffffff", relief=tk.RIDGE, bd=2)
order_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10)

tk.Label(order_frame, text="Commandes", bg="#ffffff", font=("Arial", 16, "bold"), fg="#d84315").pack(pady=10)
order_list = tk.Listbox(order_frame, font=("Arial", 12), height=20, bg="#fbe9e7", fg="#6d4c41")
order_list.pack(pady=5, fill=tk.BOTH)

total_label = tk.Label(order_frame, text="Total: 0 MAD", bg="#ffffff", font=("Arial", 14, "bold"), fg="#d84315")
total_label.pack(pady=10)

root.mainloop()