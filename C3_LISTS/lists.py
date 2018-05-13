motorcycles = []

motorcycles.append("Harley-Davidson")
motorcycles.append("Honda")
motorcycles.append("Suzuki")

##motorcycles[0] = "harley-davidson"
##motorcycles[1] = "honda"
##motorcycles[2] = "suzuki"
##
##print(motorcycles)

motorcycles.insert(0,"indian")

##print(motorcycles)
##print(motorcycles[0].title())

motorcycles.insert(2, "moped")

print(motorcycles)
first_owned = motorcycles.pop(1)
print(first_owned)
message = "The first motorcycle I owned was a " + first_owned.title() + "."
print(message)

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
