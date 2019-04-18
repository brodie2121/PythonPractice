bye_count = 0 

while bye_count <3:
    should_run = True

    while should_run: 
        user_input = input("What? ")
        print("%s" % (user_input,))
        if user_input == "bye":
            should_run = False

            bye_count = bye_count + 1
        print(bye_count)





