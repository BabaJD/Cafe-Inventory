# create the list for the menu
menu_list = ["Pizza", "Burger", "Hotdog", "Cake"] 

# create a dictionary called "stock" and assign the amount of the stock is available in the cafe
stock = {"Pizza" : 20, "Burger" : 50, "Hotdog" : 35, "Cake" : 15}

# create another dictionary called "price" and assign price to each item in the menu
prices = {"Pizza" : 30, "Burger" : 10, "Hotdog" : 5, "Cake" : 25}

# Create a "total stock value" variable that starts at 0 
total_stock_value = 0

# calculate the value of each stock on the cafe's menu list by looping
# over the stock and prices of each item in the menu list to get the individual value of each item
for item in menu_list:
    item_value = stock[item] * prices[item]
    print(f"The value of the stock item for {item} is ${item_value}")
    #then add everything up to get the total stock value
    total_stock_value += item_value

print(f"\nThe total value of the cafe's inventory is ${total_stock_value}")
