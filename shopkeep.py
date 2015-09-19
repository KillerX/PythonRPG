__author__ = 'DS'


global playercash
playercash = 200
value = {"apple": 10, "rope": 20, "bedroll": 100, "bomb": 30}
playerinventory = {"apple": 3, "rope": 7, "bedroll": 1, "bomb": 0}
shopkeepinventory = {"bomb": 20, "rope": 1}

singular = {"bomb": "Bomb", "apple": "Apple", "bedroll": "Bedroll", "rope": "Rope"}
plural = {"bomb": "Bombs", "apple": "Apples", "bedroll": "Bedrolls", "rope": "Ropes"}


def inventory():
    for item in playerinventory:
        if playerinventory[item] == 1:
            print singular[item] + ":", playerinventory[item]
        else:
            print plural[item] + ":", playerinventory[item]
    print "Gold:", playercash


def town():
    print "It's a quiet day in town, do you go to the shopkeep, the apple seller, the castle or open your inventory?"
    while True:
        choice = raw_input("> ")
        if "shopkeep" in choice:
            shopkeep()
        elif "apple" in choice:
            appleseller()
        elif "castle" in choice:
            castle()
        elif "inventory" in choice:
            inventory()
        elif "leave" in choice:
            print "You leave the town. Goodbye!"
            exit(0)
        else:
            print "You wander around aimlessly for a bit."


def shopkeep():
    print "Welcome stranger"
    while True:
        choice = raw_input("> ")
        if choice == "help":
            print "list: lists the items for sale"
            print "value <argument>: gives the sell value for given item"
            print "sell <item> <quantity>: sells the given item in given quantity from your inventory"
            print "buy <item> <quantity>: buys the given item in given quantity from the shop"
        elif choice == "list":
            for item in shopkeepinventory:
                if shopkeepinventory[item] == 1:
                    print shopkeepinventory[item], singular[item] + ", price:", int(round(value[item]*1.3))
                else:
                    print shopkeepinventory[item], plural[item] + ", price:", int(round(value[item]*1.3))
        elif choice == "inventory":
            inventory()
        elif "sell" in choice:
            splitchoice = choice.split(' ')
            if len(splitchoice) == 3:
                item = splitchoice[1]
                amount = splitchoice[2]
                try:

                    pass
                except KeyError:
                    print "Error: invalid arguments"
                global playercash

                print playercash
            elif len(splitchoice) < 3:
                print "Error: not enough arguments"
            else:
                print "Error: too many arguments"
        elif "bye" or "leave" in choice:
            town()
        else:
            print "Ehh can't say I know what you're tryin' to say, stranger."


def appleseller():
    pass


def castle():
    pass

town()



