tip_calculator = float(input("Total cost of purchases? "))
purchase = str(input("Is it a joint purchase or singular purchase? "))
if purchase == ("joint"):
    print(tip_calculator * 0.003)
elif purchase == ("singular"):
    print(tip_calculator * 0.003)
else:
    print("Invalid.!")
     

