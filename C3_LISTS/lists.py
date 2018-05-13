###LIST SORTING

places = ["New Zealand", "Australia", "Germany", "Great Brittan", "California", "Colorado"]
places.append("Wales")

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)







##alphabetical = sorted(places)
##print(alphabetical)
##print(places)
##
##r_alphabetical = sorted(places, reverse=True)
##print(r_alphabetical)
##print(places)



##cars = ["toyota", "chevrolet", "subaru", "honda", "bmw", "audi", "ford"]
##print(cars)
##cars.reverse()
##print(cars)
##cars.reverse()
##print(cars) #NOW BACK IN THE ORIGINAL SORTED ORDER
##print(len(cars))
##print("There are " + str(len(cars)) + " makes of cars in this list.")  #I just totally did this, right outta my own head.  :)
##
##example = "LKJASLKJASDLKJSADLKJ"
##
##print(len(example))

##print("Here is the original list: ")
##cars1 = ["toyota", "subaru", "bmw", "audi"]
##print(cars1)
##
##print("\n")
##
##print("Here is the temporarily-sorted list of cars: ")
##print(sorted(cars1))
##
##print("Here is the original list again.  Sorted() does *NOT* permenantly change the sort order of your original list!!!")
##print(cars1)
##
##print("\n")
##
####cars.sort(reverse=True)
##
##
##print("Here is the original list of numbers: ")
##numbers1 = [333, 22, 99, 11, 66, 43]
####numbers.sort(reverse=True)
##print(numbers1)
##
##print("Here is the temporarily-sorted list of numbers: ")
##print(sorted(numbers1))
##
##print("Here is your original list again.  Sorted() does *NOT* permenantly change the sort order of your original list!!!")
##print(numbers1)








##guests = ["einstein", "sagan", "hawking", "tyson" ]
##
###3-5 CHANGING GUEST LIST
####guests.remove("hawking")
####print(guests)
##
##not_coming = "hawking"
####guests.remove(not_coming)
####print(guests)
##
##guests.remove(not_coming)
##
####message = "Unfortunately, " + not_coming.title() + " cannot make it, because he is newly dead."
####print(message)
##
##guests.append("kaku")
##
##guests.append("manzier")
##guests.append("hawking")
##guests.append("smith")
##
##guests.insert(0, "nelson")
##guests.insert(3, "lewis")
##guests.append("winchell")
##
##
##print("I'm sorry " + guests.pop() + " but you are cordially uninvited.")
##print("I'm sorry " + guests.pop() + " but you are cordially uninvited.")
##print("I'm sorry " + guests.pop() + " but you are cordially uninvited.")
##print("I'm sorry " + guests.pop() + " but you are cordially uninvited.")
##print("I'm sorry " + guests.pop() + " but you are cordially uninvited.")
##print("I'm sorry " + guests.pop() + " but you are cordially uninvited.")
##print("I'm sorry " + guests.pop() + " but you are cordially uninvited.")
##print("I'm sorry " + guests.pop() + " but you are cordially uninvited.")
##
##print(guests)
##
##del(guests[1])
##print(guests)
##del(guests[0])
##
##print(guests)





##print("Hey " + guests[0].title() + "  " + "we found a bigger table; party on!!!")
##print("Hey " + guests[1].title() + "  " + "we found a bigger table; party on!!!")
##print("Hey " + guests[2].title() + "  " + "we found a bigger table; party on!!!")
##print("Hey " + guests[3].title() + "  " + "we found a bigger table; party on!!!")
##print("Hey " + guests[4].title() + "  " + "we found a bigger table; party on!!!")
##print("Hey " + guests[5].title() + "  " + "we found a bigger table; party on!!!")
##print("Hey " + guests[6].title() + "  " + "we found a bigger table; party on!!!")
##print("Hey " + guests[7].title() + "  " + "we found a bigger table; party on!!!")
##print("Hey " + guests[8].title() + "  " + "we found a bigger table; party on!!!")
##print("Hey " + guests[9].title() + "  " + "we found a bigger table; party on!!!")

      



##print(guests)
##
##print("Dear Mr. and / or Mrs. " + guests[0].title() + ", you are cordially invited to dinner at my estate.")
##print("Dear Mr. and / or Mrs. " + guests[1].title() + ", you are cordially invited to dinner at my estate.")
##print("Dear Mr. and / or Mrs. " + guests[2].title() + ", you are cordially invited to dinner at my estate.")
##print("Dear Mr. and / or Mrs. " + guests[3].title() + ", you are cordially invited to dinner at my estate.")



#3-4 GUEST LIST
##print("Dear Mr. and / or Mrs. " + guests[0].title() + ", you are cordially invited to dinner at my estate.")
##print("Dear Mr. and / or Mrs. " + guests[1].title() + ", you are cordially invited to dinner at my estate.")
##print("Dear Mr. and / or Mrs. " + guests[2].title() + ", you are cordially invited to dinner at my estate.")
##print("Dear Mr. and / or Mrs. " + guests[3].title() + ", you are cordially invited to dinner at my estate.")


##motorcycles = []
##
##motorcycles.append("Harley-Davidson")
##motorcycles.append("Honda")
##motorcycles.append("Suzuki")
##
####motorcycles[0] = "harley-davidson"
####motorcycles[1] = "honda"
####motorcycles[2] = "suzuki"
####
####print(motorcycles)
##
##motorcycles.insert(0,"indian")
##
####print(motorcycles)
####print(motorcycles[0].title())
##
##motorcycles.insert(2, "moped")
##
####print(motorcycles)
##
##motorcycles.append("ducati")
##
##print(motorcycles)
##
##too_expensive = "ducati"
##motorcycles.remove(too_expensive)
##print(motorcycles)
##
##message = "Those " + too_expensive + " bikes are a bit pricey for my tastes."
##print(message)



##print(motorcycles)
##
##motorcycles.remove('ducati')
##print(motorcycles)

##print(motorcycles)
##first_owned = motorcycles.pop(1)
##print(first_owned)
##message = "The first motorcycle I owned was a " + first_owned.title() + "."
##print(message)

##print(motorcycles)
##
##popped_motorcycles = motorcycles.pop()
##print(motorcycles)
##print(popped_motorcycles)


##print(motorcycles)
##
##del motorcycles[2]
##print(motorcycles)

##print(motorcycles)

##motorcycles = ["honda", "yamaha", "suzuki"]
##motorcycles.append("Ducati")
##print(motorcycles)


##print(motorcycles)
##motorcycles[1] = "harley-davidson"
##print(motorcycles)
##message = "I ride " + motorcycles[1].title() + " motorcycles.  I would rather eat worms, than ride a " + motorcycles[0].title() + "."
##print(message)

###3-3 YOUR OWN LIST
##vehicles = ["Harley", "Ford", "Honda", "Chevy"]
##models = ["Softail", "Transit Connect", "Civic Hybrid", "Volt"]
##
##message = "I would like to own a " + vehicles[1] + " " + models[1] + " someday."
##print(message)


##names = ["mike", "jeff", "john", "chris", "brandy", "shan"]

###3-2 GREETINGS
##greeting = "Hello " + names[0].title() + ", how are you today?"
##print(greeting)

###3-1 NAMES
##print(names[0].title())
##print(names[-1].title())



##bicycles = ["trek", "cannondale", "redline", "specialized", "huffy"]

##message = "My first bicycle was a " + bicycles[-1].title()
##
##print(message)

##print(bicycles)
##print(bicycles[0])
##print(bicycles[0].upper())
##print(bicycles[0].title())
##
##print(bicycles[-1].upper())
