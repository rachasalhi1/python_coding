number_of_people= int(input("how many people need a ride ? "))
n_one_taxi= int(input("how many people fit on one taxi ? "))
number =number_of_people // n_one_taxi
if number_of_people % n_one_taxi ==0   :
  print(f"the  numnber of taxi needed {number}")
else :
  print(f"the  numnber of taxi needed {number+1}")
  print(f"the last taxi contains only {number_of_people % n_one_taxi}")
