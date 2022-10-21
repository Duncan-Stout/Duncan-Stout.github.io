# main function
def coffee_bot():
  print("Welcome to the cafe!")
  drink_type = get_drink_type()
  size = get_size()
  print("Alright thats a " + size + ' ' + drink_type + "!")
  name = input("\nCan I get your name please?\n")
  print("\nThanks, " + name + "! your drink will be out shortly.")
#get size of drink 
def get_size():
  res = input("And what size would you like? \n [a] Small \n [b] Medium \n [c] Large \n")
  if res == "a":
    return "small"
  elif res == "b":
    return "medium"
  elif res == "c":
    return "large"
  else:
    print_message()
    return get_size()

# error message       
def print_message():
  print("I'm sorry, I didn't understand your selection. Please enter the letter next to our available choices.")  

# get type of drink 
def get_drink_type():
  res = input("What type of drink would you like? \n [a] Brewed Coffee \n [b] Mocha \n [c] Latte \n")
  if res == "a":
    return "brewed coffee"
  elif res == "b":
    return "mocha"
  elif res == "c":
    return order_latte()
  else:
    print_message()
    return get_drink_type() 

# customise latte 
def order_latte():
   res = input("What kind of milk for your latte? \n [a] 2% milk\n [b] Non-fat milk\n [c] Soy milk\n ") 
   if res == "a":
     return "latte"
   elif res == "b":
     return "non-fat latte"
   elif res == "c":
     return "soy-latte"
   else:
     print_message()
     return order_latte()                  


# Call coffee_bot()!
coffee_bot()
