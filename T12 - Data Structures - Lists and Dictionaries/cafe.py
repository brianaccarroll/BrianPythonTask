menu = ['Chocolate Brownie', 'Omelette', 'Tea', 'Coffee']
stock = {'Chocolate Brownie': 5,
         'Omelette': 10,
         'Tea': 50,
         'Coffee': 120}
price = {'Chocolate Brownie': 6.95,
         'Omelette': 7.95,
         'Tea': 1.4,
         'Coffee': 1.9}
total_stock = 0.0
# Calculate the total stock of the cafe by adding up each item value from the menu.
# Item value is the item stock * item price
for item in menu:
    total_stock += stock[item] * price[item]
print(f"The total stock in the cafe is {total_stock}")

