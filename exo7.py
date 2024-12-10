year = int(input("please type in a year :"))
if year%4== 0 :
    print("it's a leap year")
elif year%100==0 and year %400==0:  
     print("it's a leap year")  
else: 
   print("it's not a leap year") 