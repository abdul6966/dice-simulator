import random
num = True
while num:
  print(random.randint(1,6))
  another_num = input("Do you want to roll dice again? (y/n): ")
  if another_num.lower() == "y":
    continue
  else:
    break
