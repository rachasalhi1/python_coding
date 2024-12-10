name =input ("Please enter ur name :")
if name != "VIP":
    n_ticket=int(input ("how many tickets would u like to buy :"))
    cost = n_ticket*15.50
    print(f"the total cost {cost}") 
    print("Enjoy ur tickets")
else:
    print("enjoy ur time for free")