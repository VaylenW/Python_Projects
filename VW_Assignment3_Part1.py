#Program_1
gc_balance = float(input("Hello! Please input the starting balance of your giftcard: "))
print("The current balance on your gift card is $" + str(round(gc_balance)) + ".")
gc_purchase1 = float(input("What is the cost of your first purchase?: $"))
gc_purchase1 = gc_purchase1 + gc_purchase1*.06
gc_balance = gc_balance - gc_purchase1
print("The total amount of money subtracted from your giftcard after tax is: $" + str(round(gc_purchase1,2)) + ".")
print("The current balance on your gift card is $" + str(round(gc_balance,2)) + ".")
gc_purchase2 = float(input("What is the cost of your second purchase?: $"))
gc_purchase2 = gc_purchase2 + gc_purchase2*.06
gc_balance = gc_balance - gc_purchase2
print("The total amount of money subtracted from your giftcard after tax is: $" + str(round(gc_purchase2,2)) + ".")
print("The current balance on your gift card is $" + str(round(gc_balance)) + ".")