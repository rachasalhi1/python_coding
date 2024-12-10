total=int(input("Total amount :"))
number=int(input("Number of item :"))
day=input("Day of weeek :")
price = total* number
if day== "Saturday" or day== "Sunday":
    price=price*0.2
    if number >5:
        price =price*0.05
        print(f"total price after discount {price}dinars")
    else:
         print(f"total price after discount {price}dinars")   
else :
    price=price*0.1
    if number >5:
        price =price*0.05
        print(f"total price after discount {price}dinars")
    else:
         print(f"total price after discount {price}dinars")   




