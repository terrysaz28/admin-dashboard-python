import os

def create_invoice(customer, item, amount):
    if not os.path.exists("invoices"):
        os.makedirs("invoices")

    filename = f"invoices/{customer}.txt"

    with open(filename, "w") as file:
        file.write("INVOICE\n")
        file.write("-----------------\n")
        file.write(f"Customer: {customer}\n")
        file.write(f"Item: {item}\n")
        file.write(f"Amount: £{amount}\n")

create_invoice("John", "Printer Paper", 25)
create_invoice("Anna", "Office Chair", 120)
create_invoice("Mark", "Laptop Stand", 45)

print("Invoices created")