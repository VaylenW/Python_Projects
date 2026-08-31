#Program 2
day_length = int(input("Hello! Please type '1' if you are wanting to rent for one day or '2' if you are renting for a half day: "))
if day_length == 1:
    subtotal = 150
elif day_length == 2:
    subtotal = 80
else:
    print("Invalid input. Please restart program.")
total_rider_count = int(input("Please type in the total number of riders: "))
charged_riders = total_rider_count - 2
#trying to avoid a negative number for life jacket charge, in case rider count is 1
if charged_riders < 0:
    charged_riders = 0
subtotal = charged_riders * 5 + subtotal
total = subtotal * .06 +subtotal
tax = subtotal * .06
print(f"Your subtotal before tex is ${subtotal} and your tax is ${format(tax, ",.2f")}, your grand total price of the rental is ${format(total, ",.2f")}")