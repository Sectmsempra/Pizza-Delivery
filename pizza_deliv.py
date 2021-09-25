print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
  pay = 15
  if add_pepperoni == "Y":
    pay += 2
    if extra_cheese == "Y":
      pay += 1
   
elif size == "M":
  pay = 20
  if add_pepperoni == "Y":
    pay += 3
    if extra_cheese == "Y":
      pay += 1

elif size == "L":
  pay = 25
  if add_pepperoni == "Y":
    pay += 3
    if extra_cheese == "Y":
      pay += 1
 
print(f"Your final bill is ${pay}")