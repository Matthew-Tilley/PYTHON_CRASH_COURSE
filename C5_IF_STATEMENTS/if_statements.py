alien_0 = {
    "color": "green",
    "points": 5
}

alien_0 = {
    "x_position": 0,
    "y_position": 25,
    "speed": "medium"
    
    }

print("Original X position was: " + str(alien_0["x_position"]))

if alien_0["speed"] == "slow":
    x_increment = 1
    
elif alien_0["speed"] == "medium":
    x_increment = 2

else:
    x_increment = 3
    
alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New x-position: " + str(alien_0["x_position"]))



#print(alien_0['color'])

##print(alien_0["color"])
##
##new_points = alien_0["points"]
##
##print("You just earned " + str(new_points) + " points!")
##
##
##alien_0['x_position'] = 0
##alien_0['y_position'] = 25
##print(alien_0)

##alien_0["color"] = "yellow"
##print("The alien is now: " + alien_0["color"])



        


###5-11 ORDINAL NUMBERS
##
##numz = [1,2,3,4,5,6,7,8,9]
##
##for num in numz:
##    
##    if num == 1:
##        print(str(num) + "st")
##    
##    if num == 2:
##        print(str(num) + "nd")
##    
##    if num == 3:
##        print(str(num) + "rd")
##        
####    if num == 4 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9:
####        print(str(num) + "th")
##    if num >= 4 and num < 10:
##        print(str(num) + "th")



###5-10 CHECKING USERNAMES
##
##current_users = ["joe", "jeff", "jane", "jill", "randy", "jean"]
##
##new_users = ["bill", "bob", "lynette", "angie", "george", "joe", "randy"]



##for newUser in new_users:
##    
##    for currUser in current_users:
##        
##        if newUser == currUser:
##            
##            print("Sorry, " + newUser.title() + " ...that login is already in use; please choose another username.")
##            new_users.remove(newUser)
##            pass
##           
##        
##        else:
##            pass
##
##    print(newUser.title() + ": Available")
        
        




###5-8 HELLO ADMIN
##
##username = ["joe", "jane", "jeff", "jenny", "ralph", "admin"]
##
####username = []
##
##if username == []:
##    print("Your login information does not match our records.")
##
##else:
##    for user in username:
##        
##        if user == "admin":
##            print("Hello, ADMIN...would you like to see a status report?")
##        
##        else:
##            print("Hello " + user.title() + " glad you stopped by!")
##        

##for user in username:
##    print("Removing " + user.title())
##    username.remove(user)



##available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
##
##requested_toppings = ["mushrooms", "french fries", "extra cheese"]
##
##for requested_topping in requested_toppings:
##    
##    if requested_topping in available_toppings:
##        
##        print("Adding " + requested_topping)
##        
##    else:
##        print("Sorry, we don't have " + requested_topping + " as an available topping.")
##        
##print("\n\nFinished making your pizza!")
##        
        

#requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
##requested_toppings = []
##
##if requested_toppings:
##    for requested_topping in requested_toppings:
##        print("Adding " + requested_topping + ".")
##else:
##    print("Are you sure you want a plain pizza?")


##for requested_topping in requested_toppings:
##    
##    if requested_toppings == undefined:
##        print("Are you sure you want a plain pizza?")
##    
##    if requested_topping == "green peppers":
##        print("Sorry, we are out of green peppers right now.")
##    
##    #else:
##        #print("Adding " + requested_topping + ".")
##    
    

#print("\nFinished making your pizza!")



##depleted_toppings = ["bacon", "sausage", "anchovies", "green peppers"]
##
##requested_items = ["extra cheese", "green peppers", "mushrooms"]
##
##withheld_items = []
##
##for RI in requested_items:
##    
##    for DP in depleted_toppings:
##        
##        if DP == RI:
##            print(DP + " - not available.")
##            
##            x = withheld_items.append(DP)
##            
##            requested_items.pop(DP)
##            
    
    
           

            




##requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
##
##for topping in requested_toppings:
##    
##   if requested_topping == "green peppers":
##       print("Sorry, we're out of green peppers at the moment.")
##       
##    else:
##        print("Adding " + requested_topping + ".")
      

##requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
##
##for each in requested_toppings:
##    print("Adding " + each + ".")
##    
##print("\nFinished making your pizza!")


##cars = ["chevy", "toyota", "pontiac", "bmw"]
##
##for car in cars:
##    if car == "bmw":
##        print(car.upper())


###5-7 FAVORITE FRUIT
##
##veggies = ["broccoli", "avacado", "tomato", "onion", "potato"]
##
##if "broccoli" in veggies:
##    print("I love broccoli.")
##    
##if "avacado" in veggies:
##    print("I adore avacado.")
##    
##if "tomato" in veggies:
##    print("I really like tomato.")
##    
##if "onion" in veggies:
##    print("Onion is terrific!")
##
##if "potato" in veggies:
##    print("Love, love, love me some potatoes!!!")
##

###5-6 STAGE OF LIFE TESTER
##
##def ageChecker(age):
##    
##    if age < 2:
##        print("You're just a baby!")
##    
##    elif age >= 2 and age < 4:
##        print("You're a toddler.")
##        
##    elif age >= 4 and age < 13:
##        print("You're a kid.")
##    
##    elif age >= 13 and age < 20:
##        print("You are a teenager.")
##    
##    elif age >= 20 and age < 65:
##        print("You're an adult.")
##    
##    elif age > 65:
##        print("You're a senior-citizen!")
##
##ageChecker(66)


###5-3 ALIEN SPACESHIPS
##spaceship = "green"
##spaceship = "yellow"
##spaceship = "red"
##
##if "green" in spaceship:
##    print("You earned FIVE points.")
##
##elif "yellow" in spaceship:
##    print("You earned TEN points.")
##    
##else:
##    print("You earned FIFTEEN points!!!")

          

##requested_toppings = ["mushrooms", "extra cheese"]
##requested_toppings.append("pepperoni")
##
##if "mushrooms" in requested_toppings:
##    print("Adding mushrooms!")
##    
##if "pepperoni" in requested_toppings:
##    print("Adding pepperoni.")
##    
##print("\n Finished making your pizza!")
##    



##def checker(age):
##    if age < 4:
##        print("Admission is free!")
##    
##    elif age >= 4 and age <18:
##        print("Admission is five dollars.")
##        
##    elif age > 18 and age >= 65:
##        print("You get a discount...admission is five dollars.")
##    
##    else:
##        print("Admission is ten dollars.")
##    
##checker(84)

##bird = "has feathers."

##if "has feathers" in bird:
##    print(True)
    
##turtle = "has shell"
##if "has shell" in turtle:
##    print("Turtles have shells.")
    
##inventory = ["bmw", "chevrolet", "ford", "nissan"]

##if "ford" in inventory:
##    print("Gobble-gobble!")

##if "toyota" not in inventory:
##    print("No 'Yota's here!")

##if "bmw" and "nissan" in inventory:
##    print("Yep, we've got 'em in stock!")

##if "pontiac" or "oldsmobile" not in inventory:
##    print("We ain't got them-there vee-hickles in stock, partner!")
##    
##else:
##    print("How many you want?")

##for item in inventory:
##    if "chevrolet" in inventory:
##        print("YAY!")

##if "oldsmobile" not in inventory:
##    print("Nadazipzilch, bro.")
    


###5-1 CONDITIONAL TESTS
##car = 'pontiac'
##
##if car != "toyota":
##    print("It ain't a 'Yota!")


##banned_users = ["andrew", "carolina", "david"]
##
##user = "marie"
##
##if user not in banned_users:
##    print("Hello " + user + " your comment will be submitted.")


##toppings = ["mushrooms", "onions", "pineapple"]
##
##if "sausage" in toppings:
##    print(True)
##    
##elif "mushrooms" in toppings:
##    print("No sausage here!")


##thing_1 = "blue"
##
##thing_2 = "orange"
##
##if thing_1 == "blue" or thing_2 == "orange":
##    print("Yep.")
##    
##if (thing_1 != "purple") or (thing_2 != "red"):
##    print("Blurrpppsszzz.")


##flub = 63
##dub = 99
##
##if flub % 2 >0 and dub % 2 >0:
##    print("Yay!")


##answer = 17
##
##if answer != 42:
##    print("Nada.")


##age = 18
##
##if age == 18:
##    print("You are allowed.")
##else:
##    print("Nope.")



##requested_topping = "mushrooms"
##
##if requested_topping != "anchovies":
##    print("Hold the anchovies!")

    
##tester = "Apple"
##
##if tester.lower() == "apple":
##    print(True);
##    
##print(tester)


##if "Audi" == 'audi':
##        print(True)
##else:
##    print(False)


##a = 3
##
##
##b = 3
##
##if a == b:
##    print(True);


##cars = ['audi', 'bmw', 'subaru', 'toyota']
##
##for car in cars:
##        if car == "bmw":
##            print(car.upper())
##        
##        else:
##            print(car.title())