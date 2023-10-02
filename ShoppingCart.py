import time
def showOptions():
    options = [
        "1. Add New Item To Shopping List",
        "2. Update Item Amount In Shopping List",
        "3. View All Items In Shopping List",
        "4. Delete An Item In Shopping List",
        "5. Clear Shopping List",
        "'quit'. Leave and print Shopping List.",
    ]
    [print("\t" + option) for option in options]
    choice = input("Enter A value or type 'quit' TO LEAVE: ").lower().strip()
    return choice
 
def AddToCart():
    name = input("Enter name of Item: ").lower().strip()
    quantity = int(input("Enter quantity: "))
    price = float(input(f"Enter Price of {name}: $"))
    newItem = {"name": name, "price": price, "quantity": quantity, "total": round(quantity*price, 2)}
    shoppingCart[name] = newItem
#     print(shoppingCart)


def UpdateCount():
    name = input("Enter name of Item: ")
    if name in shoppingCart:
        print("Item Found!")
        newQuantity = int(input("Enter new quantity: "))
        shoppingCart[name]["quantity"] = newQuantity
        price = shoppingCart[name]["price"]
        shoppingCart[name]["total"] = round(newQuantity*price, 2)
        print(f"Quantity has been Updated to {newQuantity}")
    else:
        itemNotFound()
#     print(shoppingCart)


def itemNotFound():
    print("Item is not in shopping cart! Please try again later")
    
def viewCart():
    if len(shoppingCart) == 0:
        print("\tShopping list is empty!!")
        return
    total = 0
    print("="*20)
#     print(shoppingCart)
    for key, value in shoppingCart.items():
        total += value.get("total", 0)
        print(f'''\t{key.title()}
        \tPrice:     {value.get("price", "Undefined")}
        \tQuantity:  {value.get("quantity", "Undefined")}
        \tTotal:     ${value.get("total", "0")}''')
        time.sleep(1)
    print("="*20)
    print(f"\tThe total of the list is: ${round(total, 2)}")
    print("="*20)
        
def deleteItem():
    name = input("Enter name of Item: ").lower().strip()
    if name in shoppingCart:
        del shoppingCart[name]
        print(f"{name} has just been removed from the shopping cart")
    else:
        itemNotFound()
        
def clearList():
    if len(shoppingCart) == 0:
        print("SHOPPING CART IS ALREADY EMPTY")
    choice = input(f"***ARE YOU SURE YOU WANT TO CLEAR YOUR LIST? IT HAS {len(shoppingCart)} items! TYPE 'CLEAR' to continue press ENTER to cancel: ")
    if choice == "CLEAR":
        print("Clearing list...")
        time.sleep(2)
        print("Shopping LIST has been CLEARED!!!!")
        shoppingCart.clear()
    else:
        print("List not cleared. You are SAFE!!")

inputDict = {"1": AddToCart, "2": UpdateCount, "3": viewCart, "4": deleteItem, "5": clearList }
shoppingCart = {}

def main():
    while True:
        print('\n')
        print(f"{'='*10}Welcome to BESTMART!{'='*10}")
        print("\tHow can I help you today?")
        choice = showOptions()
        if choice == "" or choice == "quit":
            break
        else:
            inputDict[choice]()
    
    print("Printing Shopping List...")
    time.sleep(2)
    viewCart()
    
    print("GoodBye, thanks for shopping".title())
    
main()