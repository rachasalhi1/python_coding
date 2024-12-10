print("Runner 1:")
name1 =input("Name:")
time1 = int(input("Time (in seconds:"))
print("Runner 2:")
name2 =input("Name:")
time2 = int(input("Time (in seconds:"))
if time1<time2:
   print(f"{name1} is faster")

if time1>time2:
   print(f"{name2} is faster")
else:
  print("they are same ")