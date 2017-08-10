def printAny(*what):
    if what:
        print("There are ", len(what), " arguments")
        for thing in what[0:]:
            print(thing)
        print("Done printing...")

printAny("Printing with three arguments:", "This thing", "Another thing")
printAny("Only printing this")

#Unnecessary comment to test git scripts
