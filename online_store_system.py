from pprint import pprint
store_dict = {}
"""
		"laptops": {"price": 1200, "quantity": 5},
		"headphones": {"price": 150, "quantity": 10},
		"mouse": {"Price": 40, "quantity": 20}"""
	
SHOULD_EXECUTE = True

def start():
	while SHOULD_EXECUTE:
		print("""
		1. Add Product
		2. Update stock
		3. Sell product
		4. Display inventory
		5. Most expensive product
		6. Total potential product
		7. Exit
		>>>""")

		choice = int(input("Enter choice (1-7):\n>>> "))
		call_function(choice)


def call_function(user_choice):
	if user_choice == 1:
		name = input("Name of product:\n>> ")
		price = float(input("Price of Product:\n>> "))
		quantity = int(input("Quantity of product:\n>> "))
		pprint(add_product(store_dict, name, price, quantity))
	elif user_choice == 2:
		name = input("Enter product name to update: ")
		quantity = int(input("Enter quantity to add: "))
		print(update_stock(store_dict, name, quantity))
	elif user_choice == 3:
		name = input("Enter product name to sell: ")
		quantity = int(input("Enter quantity to sell: "))
		print(sell_product(store_dict, name, quantity))
	elif user_choice == 4:
		#display_inventory(store_dict)
		print(display_inventory(store_dict))
	elif user_choice == 5:
		print(most_expensive_product(store_dict))

	elif user_choice == 6:
		print(total_potential_sales(store_dict))

	elif user_choice == 7:
		Exit()
	else:
		print("\nInvalid choice. Please enter 1-7.")


# Add product function

def add_product(store_dict, name, price, quantity):

	if name in store_dict:
		return f"\nProduct '{name}' already exists.."
	else:
		if quantity > 0:
			store_dict[name] = {"price": price, "quantity": quantity}
			return f"\nProduct '{name}' added successfully!"
		else:
			return "Quantity of a product must be greater than or equal to 1"

# 2. Update stock function

def update_stock(store_dict, name, quantity):
	if name not in store_dict:
		return f"\nError: Product '{name}' does not exist."
	else:
		store_dict[name]["quantity"] += quantity
		return f"\nStock for '{name}' updated. New quantity: {store_dict[name]['quantity']}"

# 3. Sell product function

def sell_product(store_dict, name, quantity):
	if name not in store_dict:
		return f"\nError: '{name}' not available in the store..Please check back later.."
	if store_dict[name]["quantity"] < quantity:
		return f"Error: Not enough stock of '{name}'. Only {store_dict[name]['quantity']} left."
	else:
		store_dict[name]["quantity"] -= quantity
		total_price = store_dict[name]["price"] * quantity
		return f"Sold {quantity} '{name}' for ${total_price}. Remaining stock: {store_dict[name]['quantity']}"

# Display Inventory function

def display_inventory(store_dict):
	if len(store_dict) == 0:
		return("Inventory is empty.")
	else:
		total_no = 0
		for name, items in store_dict.items():

			#	total_no += 1
			print( f"{name}: Price = {items['price']}, Quantity = {items['quantity']}")
			total_no +=1
		return f"\nTotal Number of product in the store is: {total_no}"


def most_expensive_product(store_dict):
	if len(store_dict) != 0:
		highest_price = 0
		highest_product = {}
		for name, item in store_dict.items():
			if item["price"] >= highest_price:
				highest_price = item["price"]
		highest_product["name"] = name
		return f"The Highest Product is: '{highest_product['name']}' And the Price is: ${highest_price}"
	else:
		return "Inventory is Empty"

def total_potential_sales(store_dict):
	if len(store_dict) != 0:
		total_value = 0
		for products in store_dict:
			quantity = store_dict[products]["quantity"]
			price = store_dict[products]["price"]
			total_value += price * quantity
		return f"Total Potential sale for {products} is: ${total_value}"
	else:
		return "Inventory is empty!!"


def Exit():
	global SHOULD_EXECUTE
	print("Good Bye!!")
	SHOULD_EXECUTE = False
	

start()
