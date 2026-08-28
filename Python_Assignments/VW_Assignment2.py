print("Hello! Welcome to the store!")
soda_price = float(input("Please give the price of the soda in decimal form: "))
chips_price = float(input("Please give the price of the chips in decimal form: "))
gum_price = float(input("Please give the price of the gum in decimal form: "))
chocolate_price = float(input("Please give the price of the chocolate in decimal form: "))
subtotal = soda_price + chips_price + gum_price + chocolate_price
total = subtotal + subtotal*.06
print("Your subtotal is $" + str(round(subtotal, 2)) + " and your grand total after tax is $" + str(round(total, 2)) + ".")