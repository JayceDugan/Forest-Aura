from game_generator import generateLocations, generateItems, generateBlockedPaths, generateHints

print("Setting up... \n");

forestMap = generateLocations()
blockedPathMessages = generateBlockedPaths()
hints = generateHints()
items, itemLocations = generateItems()

print("\n Setup complete! \n\n")

# set the player's start location
mapLoc = 4

#initialise game variables
playerInput=""
gameMessage=""
actionsIKnow = ["north","east","south","west", "q", "take", "use", "drop", "backpack", "help", "hint"]
action=""
endGame=False
backpack=[]
itemsIKnow = ["flute","stone","sword"]
item=""
def takeItem():
    global gameMessage, backpack, items, itemLocations, hints
    
    #find the index number of the item in the items array
    if item in items:
        itemIndexNumber = items.index(item)

        #Does the item exist in the game world and is it at the player's current location?
        if itemLocations[itemIndexNumber] == mapLoc:
            gameMessage="You take the "+item+"."
            #add it to your backpack
            backpack.append(item)
            #remove it from the game world
            items.remove(item)
            itemLocations.remove(mapLoc)
        else:
            #message if the player tries to take an item that isn't in the current location
            gameMessage = "You can't do that."
    else:
        if item in backpack:
            gameMessage = "You already have the "+item+" in your backpack."
        else:
            gameMessage = "You can't do that."
def dropItem():
    global gameMessage, backpack, itemLocations, items
    # only try to drop the item if the backpack isn't empty
    if len(backpack)>0:
        #If the item is in the backpack
        if item in backpack:
            # remove the item from the backpack
            backpack.remove(item)
            # and add it to the items at the current map location
            itemLocations.append(mapLoc)
            items.append(item)
            # tell the player the item has been dropped
            gameMessage="You drop the "+item
        else:
            #message if the player tries to drop something not in backpack
            gameMessage = "You can't do that."
    else:
        #messaage if the backpack is empty
        gameMessage = "You are not carrying anything."
        
def useItem():
    global gameMessage, items, itemLocations, backpack, endGame, hints

    #find out if the item is in the backpack
    if item in backpack:
        #figure out what to do with it
        if item == 'flute':
            if mapLoc == 8:
                gameMessage = "Beautiful music fills the air."
                gameMessage+=" A wizened old man steps outside"
                gameMessage+=" and hands you a sword!"
                #add the sword to the world
                items.append("sword")
                itemLocations.append(mapLoc)
                #reset the hint for this location
                hints[mapLoc]=""
            else:
                gameMessage = "You try and play the flute "
                gameMessage+=" but it makes no sound here."
        elif item == 'sword':
            if (mapLoc == 3):
                gameMessage = "You swing the sword and slay the dragon!"
                gameMessage+=" You've saved the forest of Lyrica!"
                endGame = True
            else:
                gameMessage = "You swing the sword listlessly."
        elif item == 'stone':
            if (mapLoc == 1):
                gameMessage = "You drop the stone in the well."
                # remove stone from backpack
                backpack.remove(item)
                gameMessage+=" A magical flute appears!"
                # add flute to game world
                items.append("flute")
                itemLocations.append(mapLoc)
                #reset the hint for this location
                hints[mapLoc]=""
            else:
                gameMessage = "You fumble with the stone in your pocket"
    else:
        #message if item is not in backpack
        if len(backpack)>0:
            gameMessage = "You're not carrying it."
        else:
            #message if backpack is empty
            gameMessage = "Your backpack is empty."
            
def playGame():
#retrieve and process player action
    
    #access global variables
    global mapLoc, endGame, gameMessage, action, item
    
    #reset game variables
    gameMessage = ""
    action = ""

    #get the player's input and convert it to lower case
    playersInput=input("Enter action or q to quit: ")
    playersInput.lower()

    #parse the player input to find a valid action
    actionCount=0
    actionList=[]
    for a in actionsIKnow:
        if a in playersInput:
            action = a
            actionList.append(action)
            actionCount+=1

    #parse the player input to find valid items
    itemCount=0
    itemList=[]
    for i in itemsIKnow:
        if i in playersInput:
            item = i
            itemList.append(item)
            itemCount+=1

    if actionCount==0:
        gameMessage = "I don't understand that."
    elif actionCount>1:
        gameMessage = "Do you mean "
        for a in actionList:
            gameMessage+=a+" or "
        gameMessage+="...?"
    else:
        #action count must be 1
        #process the action
        if action == 'north':
            if mapLoc >= 3:
                mapLoc -=3
            else:
                gameMessage = blockedPathMessages[mapLoc]
        elif action == 'east':
            if mapLoc % 3 != 2:
                mapLoc += 1
            else:
                gameMessage = blockedPathMessages[mapLoc]
        elif action == 'south':
            if mapLoc < 6:
                mapLoc +=3
            else:
                gameMessage = blockedPathMessages[mapLoc]
        elif action == 'west':
            if mapLoc % 3 != 0:
                mapLoc -=1
            else:
                gameMessage = blockedPathMessages[mapLoc]
        elif action == 'q':
            gameMessage = "\nYou have escaped the forest of Lyrica!"
            endGame=True
        elif action == 'use':
            if itemCount==1:
                useItem()
            elif itemCount == 0:
                gameMessage = "What do you want to use?"
            else:
                #itemCount > 0
                gameMessage = "Do you want to use a "
                for i in itemList:
                    gameMessage+=i+" or a "
                gameMessage+="...?" 
        elif action == 'take':
            if itemCount==1:
                takeItem()
            elif itemCount == 0:
                gameMessage = "What do you want to take?"
            else:
                #itemCount > 0
                gameMessage = "Do you want to take the "
                for i in itemList:
                    gameMessage+=i+" or the "
                gameMessage+="...?" 
        elif action == 'drop':
            if itemCount==1:
                dropItem()
            elif itemCount == 0:
                gameMessage = "What do you want to drop?"
            else:
                #itemCount > 0
                gameMessage = "Do you want to drop your "
                for i in itemList:
                    gameMessage+=i+" or your "
                gameMessage+="...?"
        elif action == 'backpack':
            if len(backpack)>0:
                gameMessage="You are carrying: "+', '.join(backpack)
            else:
                gameMessage="Your backpack is empty."
        elif action == 'help':
            gameMessage ="Possible actions: "+', '.join(actionsIKnow)
        elif action == 'hint':
            gameMessage = hints[mapLoc]
        else:
            gameMessage = "Error: This action is still in development"
        
def describeLocation():
    print("You can see",forestMap[mapLoc])
    for i in range(len(itemLocations)):
        if itemLocations[i] == mapLoc:
            print("You see a",items[i],"here.")
    
    
print("Welcome to the Forest of Lyrica!")
print("\n\nHere are all the locations you can discover!\n")

for loc in forestMap:
    print(" -", loc)

print("\n\nHere are all the items you can find! \n")

for item in items:
    print(" -", item)

print("\n\nYou can currently see", forestMap[mapLoc])

print("\n\nLet's play! Here are a list of actions you can take:");

for action in actionsIKnow:
    print(" -", action)

print("\n")

while not endGame:
    playGame()
    if gameMessage:
        print(gameMessage)
    else:
        describeLocation()
    
    
