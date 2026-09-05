#Program_1
card_balance = float(input("Hello! Please input the starting balance of your giftcard: $"))
#Watched a video that mentioned f-strings so i wanted to try them out here
print(f"The current balance on your gift card is ${card_balance:,.2f}.")
card_purchase1 = float(input("What is the cost of your first purchase?: $"))
card_purchase1 = card_purchase1 + card_purchase1*.06
card_balance = card_balance - card_purchase1
print(f"The total amount of money subtracted from your giftcard after tax is: ${card_purchase1:,.2f}.")
print(f"The current balance on your gift card is ${card_balance:,.2f}.")
card_purchase2 = float(input("What is the cost of your second purchase?: $"))
card_purchase2 = card_purchase2 + card_purchase2*.06
card_balance = card_balance - card_purchase2
print(f"The total amount of money subtracted from your giftcard after tax is: ${card_purchase2:,.2f}.")
print(f"The current balance on your gift card is ${card_balance:,.2f}.")