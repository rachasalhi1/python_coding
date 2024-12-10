print("please type in the name of the ceveral cities (one by one)")
i=1

name=input(f"please type in the  name  of the  city number {i} ")
if name !="stop":
  length = len(name)
  print(f"the city {name} have {length} letters so its population is {length},000,000")
while name !="stop" :
    i=i+1
    name=input(f"please type in the  name  of the  city number {i} ")
    if name !="stop":
     length = len(name)
     print(f"the city {name} have {length} letters so its population is {length},000,000")
    