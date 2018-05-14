dimensions = (200, 50)
##print(dimensions[0])
##print(dimensions[1])

#dimensions[0] = 250

for each in dimensions:
    print(each)
    
    
dimensions = (300, 60)
print(dimensions)

for each in dimensions:
    print(each)
    
    
dimensions = (900, 632)
print(dimensions)



###4-11 OUR PIZZAS & 4-12
##
##pizzas = [ "pepperoni", "sausage", "cheese", "deluxe", "veggie" ]
##
##buddy_pizzas = pizzas[ : ]
##
##pizzas.append("mushroom")
##buddy_pizzas.append("garlic")
##
##print(pizzas)
##print(buddy_pizzas)
##
##
##for pizza in pizzas:
##    print(pizza)
##    
##print("\n")
##    
##for pizza in buddy_pizzas:
##    print(pizza)
##    
    


###4-10 SLICES
##
##some_list = ["bing", "bong", "ving", "vong", "sing", "song"]
##
##print(len(some_list))
##
##print(some_list[ 0:3 ])
##print(some_list[ -3 : -1])
##print(some_list[ -1 : ])
##print(some_list[ : -1 ])
##print(some_list[:])
##
##print("The first three items in this list, are: ")
##print(some_list[ : 3 ])
##
##print("\n")
##
##print("Three items from the middle of this list, are: ")
##print(some_list[ 2:5 ])
##
##print("The last three items of this list, are: ")
##print(some_list[-3:])



##my_foods = ["pizza", "falafel", "carrot cake"]
##
##friend_foods = my_foods
##
##my_foods.append("cannoli")
##friend_foods.append("ice cream")
##
##print(my_foods)
##
##print(friend_foods)

##friend_foods = my_foods[ : ]
##friend_foods.append("ice cream")
##my_foods.append("cannoli")
##
##print("My favorite foods are: ")
##print(my_foods)
##
##print("\n")
##
##print("My friend's favorite foods are:")
##print(friend_foods)



##players = ["charles", "martina", "michael", "eli"]
## 
## 
##for player in players[ :2 ]:
##    print(player)
 
##print(players[1:2])
#print(players[ :2 ])
#print(players[ 2: ])
#print(players[ : -2 ] )

###4-9 LIST COMPREHENSION
##cubes = [value ** 3 for value in range(1, 11)]
##print(cubes)

###4-8 CUBES
##cubes = []
##
##for each in range(1, 11):
##    cubes.append(each ** 3)
##
##print(cubes)
##
##for each in cubes:
##    print(each)

###4-7 THREES
##threes = []
##
##for each in range(3, 31):
##    if each % 3 == 0:
##        threes.append(each)
##        print(each)
##
##print(threes)

###4-6 ODD NUMBERS
##my_input = list(range(1,21))
##
##for each in my_input:
##    if each % 2 != 0:
##        print(each)


#4-4 ONE MILLION
##numz = list(range(1, 1001))
####
####print(numz)
####
####for number in numz:
####    print(number)
##    
##total = 0
##
##total = sum(numz)
##print(total)
##
##print(min(numz))
##
##print(max(numz))





##m = list(range(1, 1000000))
##print(m) (This made my computer choke...)


###4-3 COUNTING TO TWENTY
##for number in range(1, 21):
##    print(number)
    

##squares = [value**2 for value in range(1,11)]
##
##print(squares)

##digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##
##print(min(digits))
##
##print(max(digits))
##
##print(sum(digits))

##for digit in digits:
##    print(digit ** 6)
    

##squares = []
##
##for value in range(1,11):
##    squares.append(value ** 2)
##
##print(squares)


##cubes = []
##for i in range(10, 20, 3):
##    print(i)


##squares = []
##
##for value in range(1,11):
##    square = value ** 2
##    squares.append(square)
##    print(squares)



##skippy = list(range(2, 8, 2))
##
##print(skippy)


##numbers = list(range(10, 100))
####print(numbers)
##
##for number in numbers:
##    if number % 10 == 0:
##        print( str(number) + " Is an even number, divisible by ten!")
##    
##    else:
##        print("Nope.")
  


##numbers = list(range(1,6))
##print(numbers)

##for each in range(1,6):
##    print(each)


###4-2 ANIMALS
##animals = ["dog", "cat", "python", "fish"]
##
##proper = sorted(animals)
##print(proper)
##
##for animal in animals:
##    #print(animal)
##    print("A " + animal + " would make a great pet.")
##
##print("What do these animals have in common?  They're animals.")

###4-1 PIZZAS
##
##pizzas = ["cheese", "sausage", "mushroom"]
##pizzas.append("pepperoni")
##
##for pizza in pizzas:
##    #print(pizza)
##    print("I like " + pizza + " pizza!")
##
##print("As you can see, I really like pizza!")


##magicians = ["alice", "david", "carolina"]
##
##for magician in magicians:
##    print(magician.title() + ", that was a great trick!")
##    print("I can't wait to see your next trick, " + magician.title() + ".\n")
##
##    print("Thank you, everyone...that was a great magic show!")
  
  
  
##cats = ["jade", "barack", "cali", "otis", "kizzy"]
##
##for cat in cats:
##    print(cat)
    
    