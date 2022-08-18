class Shoes:
    #This is the constructor of the class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #This function returns the cost of the product
    def get_cost(self):
        return self.cost

    #This function returns the quantity of the product
    def get_quanty(self):
        return self.quantity

    #This function returns the class object in string format
    def __str__(self):
        return f"""Country:\t {self.country}
Code:\t\t {self.code}
Product:\t {self.product}
Cost:\t\t {self.cost}
Quantity:\t {self.quantity}
____________________________________"""

shoes_list = []

#This function reads the text file info into a class object that then will be inserted into a list
def read_shoes_data():
    f = open("inventory.txt", "r")
    line_num = 0
    for line in f:
        line_num += 1 
        if line_num != 1:
            line_list = line.strip("\n").split(",")
            new_shoe_object = Shoes(line_list[0], line_list[1], line_list[2], line_list[3], line_list[4])
            shoes_list.append(new_shoe_object)
        else:
            pass 
    f.close()   

#This function takes in info of a shoe and then inputs it into the list of all shoes objects
def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product name: ")
    cost = input("Enter the cost of the product: ")
    quantity = input("Enter the quantity of the product: ")
    new_shoe_object = Shoes(country, code, product, cost, quantity)
    shoes_list.append(new_shoe_object)

#This function prints all shoes objects info
def view_all():
    for shoe in shoes_list:
        print(shoe.__str__())

#This function will restock a product to the amount the user inputs
def re_stock():
    f = open("inventory.txt", "w+")
    f.close()
    quantity_list = []
    for shoe in shoes_list:
        quantity_list.append(int(shoe.get_quanty()))
    smallest_quantity = min(quantity_list)
    index = quantity_list.index(smallest_quantity)
    shoe_obj = shoes_list[index] 
    is_restock = input(f"Do you want to restock on the {shoe_obj.product} prodduct. [y/n]").lower()
    f = open("inventory.txt", "a")
    if is_restock == "y":
        restock_to = int(input(f"Enter the number of {shoe_obj.product} you want to restock to: "))
        line_count = 0
        for shoe in shoes_list:
            line_count += 1
            if line_count == 1:
                f.write("Country,Code,Product,Cost,Quantity\n")
            if shoe.code == shoe_obj.code:
                shoe.quantity = restock_to
                print(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
                f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
            else:
                f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

    elif is_restock == "n":
        pass
    else:
        print("Wrong input!\nReturning to main menu.")
    f.close()

#This function returns a certain shoe object through a code that will then be printed in a string format
def search_shoe():
    shoe_code = input("Enter the code of the shoe: ")
    for shoe in shoes_list:
        if shoe_code == shoe.code:
            return shoe.__str__()

def value_per_item():
    for shoe in shoes_list:
        result = int(shoe.cost) * int(shoe.quantity)
        print(f"{shoe.product} value \t= {result}")

#This function returns the product with the highest quantity
def highest_qty():
    quantity_list = []
    for shoe in shoes_list:
        quantity_list.append(int(shoe.get_quanty())) 
    
    biggest_num = max(quantity_list)
    index = quantity_list.index(biggest_num)
    product = shoes_list[index].product
    print(product, "is for sale")
    print(shoes_list[index].__str__())

read_shoes_data()
while True:
    program_input = input("""Choose a option from the below choices
"add": Adds a shoe to the list
"va  : Views all the shoes
"rs" : Restocks on the lowest quantity shoe
"se" : View a shoe through a code
"vv  : View value of each item"
"vh" : View the highest quantity shoe
"q"  : Quits the program
""")
    if program_input == "add":
        capture_shoes()        
    elif program_input == "va":
        view_all()
    elif program_input == "rs":
        re_stock()
    elif program_input == "se":
        print(search_shoe())
    elif program_input == "vv":
        value_per_item()
    elif program_input == "vh":
        highest_qty()
    elif program_input == "q":
        exit()
