want_coins = True
coins = 0

while want_coins: 
    user_input = input("You have " + str(coins) +  " coins, do you have another? ")
    if user_input == "yes":
        coins += 1 
    else:
        user_input == "no"
        should_run = False  
       
        print("bye") 
    