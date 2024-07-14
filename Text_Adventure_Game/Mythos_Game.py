#
# Python:   3.11.7
#
# Author:   Joe Lapinski
#
# Purpose:  The Tech Academy - Python Course. Creating our first computer game.
#           Demonstrating how to pass variables, from function to function,
#           while producing a functional game.
#
#           Remember, function_name(variable) means that we pass in the variable.
#           return variable means that we are returning the variable back
#           to the calling function.
#

def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again,{}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different characters. \nYou can choose to ask them for information \nor to engage them in battle.")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA mysterious creature approaches you along the path toward the castle. \nWill you ask them for information \nor challenge them to a fight? (info/fight) \n>>>: ").lower()
        if pick == "info":
            print("\nThe kind old traveler warns you about the castle in the distance. \nBut hands you a piece of a key. \n'Should you collect enough of these, you may find \nwhat you're looking for, afterall. Good luck, adventurer!' as they walk away smiling and you continue on along the path...")
            nice = (nice + 1)
            stop = False
        if pick == "fight":
            print ("\nThe creature removes its hood and reveals itself. \nThey are an evil and grotesque monster with green eyes and gnarly teeth. \nThey swipe at you with their sword and you take some damage \nbefore they, oddly, escape into the woods once they caught a glimpse of your face...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print ("\n{}, your current total: \n({}, Key Pieces) and ({}, Damage Taken)".format(name,nice,mean))

    

def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:       #else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    #Subsitute the {} wildcards with our variable values
    print("\n{}, the path you have traveled leads to an old wooden door at the base of the castle. \nNobody is around, as this is clearly not the main entrance. \nYou look at the door's keyhole, a golden light is shining through it, and wonder about the key pieces you collected along the way. \nDoubtful, you fit your key pieces together and atempt to unlock the door. \nIt unlocks with a surprising ease, revealing a room full of treasure and gold! Congratulations - you win! Now, what to do about that sleeping dragon?... ".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)



def lose(nice,mean,name):
    #Subsitute the {} wildcards with our variable values
    print("\nThat last poisonous slash seemed to be one too many and you fall to your knees, weakened and unable to go on.\nWith your last bit of draining energy, you wondered why those creatures were scared by your appearance. \nJust then you hear footsteps, and a enormous something standing over you. \n'Well, if it isn't the King's long-lost child {}, I didn't think you'd ever show your face around here again after what you did to me. \nYou look up, weakened, to see a larger, creepier, and more fearsome version of the beasts you encountered along the path.\nThis one had a large scar across its face, where one of its eyes had once been. \nWhehter a case of mistaken identity, or amnesia, you have no memory of this creature, or of any relation to a King. \nYou try to plead your case but a battle-axe, dripping with a blackened ooze, was already descending toward you. \nA moment later, everything goes black. Game Over".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)

    

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go! Come back to Mythos again soon.")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'Yes', ( N ) for 'No':\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)











if __name__ == "__main__":
    start()
