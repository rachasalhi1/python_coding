price= float(input("please in a price: "))
if price >0 :
    dinars = int(price)  
    centimes = round((price - dinars) * 100)  
    
    print(f"Dinars: {dinars}")
    print(f"Centimes: {centimes}")
 
