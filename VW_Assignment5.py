ship_weight = float(input("Hello! Please enter the weight of the spaceship on Earth in kilograms: "))
print("Select from the list of planets (and one moon)to determine the weight on it")
print("1: Moon")
print("2: Mars")
print("3: Venus")
print("4: Pluto")
planet_selection = int(input("Please type the number associated with the celestial body you want to select: "))
if planet_selection == 1:
    #made this a string even though im taking a number input. wanted the user to be able to input whatever without it breaking
    rock_decision = (input("Type '1' if you have any rocks aboard the ship. If not, press Enter: "))
    if (rock_decision) == "1":
            rock_weight = float(input("Please input the weight of the rocks that you collected: "))
    else:
         rock_weight = 0
    adjusted_ship_weight = (ship_weight+rock_weight) *.166
    print(f"The weight of the spaceship on the Moon would be {adjusted_ship_weight:,.2f} kilograms")
elif planet_selection == 2:
    rock_decision = (input("Type '1' if you have any rocks aboard the ship. If not, press Enter: "))
    if (rock_decision) == "1":
        rock_weight = float(input("Please input the weight of the rocks that you collected: "))
    else:
         rock_weight = 0
    adjusted_ship_weight = (ship_weight+rock_weight) *.377
    print(f"The weight of the spaceship on Mars would be {adjusted_ship_weight:,.2f} kilograms")
elif planet_selection == 3:
    adjusted_ship_weight = ship_weight *.907
    print(f"The weight of the spaceship on Venus would be {adjusted_ship_weight:,.2f} kilograms")
    venus_time = float(input("How many minutes was your shaceship on Venus?: "))
    if venus_time > 127:
         print("Your spaceship lasted longer on Venus than any other spacecraft so far!")
elif planet_selection == 4:
    adjusted_ship_weight = ship_weight *.067
    print(f"The weight of the spaceship on Pluto would be {adjusted_ship_weight:,.2f} kilograms")
else:
    print("Planet selection invalid. Please restart program to try again.")
