print("You find yourself in a giant human size cage made from bronze and metal. As this cage hangs from a chain bolted to the celing of a rocky cavern, an army of \n"
"skeletons at the floor bow to a Lich sitting atop it's Golden Throne. Surronding you is other cages holding varios creatures, all looking in terror of the horrors below. \n" 
"you have no memory of your exsistance and or any one elnce. All you can recall is your skill in combat, even though you can't remember ever learning how. In the cage there is a door. \n"
"One of the bars surrounding the cage making it unable to leave looks damaged. A bigger cage swings back and forth, in that cage you see a ogre raging in furry swinging it's weight back \n"
"and forth. You see a rock on the floor of your cage. You pick it up and see a two headed human size seagull fly by your cage, it seems like a guard and is flying by all the cages.\n")

game = True
while game:
    Act1Choice = True
    Act1Choice = input("What do you do?\n"
    "1.Go to the door 2.Check the bar 3.Shift your attention to the ogre 4. peer your eye on the seagull 5.do nothing.\n"
    "Choose from (1, 2, 3, 4, 5): \n")
    print(Act1Choice)
    if Act1Choice == "1":
        print("*Act 1 Story Chosen* 'A Doorway Out'\n")
        Act1Choice = False
        TheDoor = True
        while TheDoor:
            TheDoor = input("You walk to the door a see a lock on it. What do you do?\n"
            "1. Try to Break the lock with your rock 2. Try to kick the Door Open 3.Charge at the door to break it open 4.Jiggle the handle to open it 5. This it to complicated and give up.\n"
            "Choose from (1, 2, 3, 4, 5): ")
            print(TheDoor)
            if TheDoor == "1":
                print("You Hold the Rock up above you and in one fast motion, you strike it down onto the Lock. The lock shatters onto the ground and the Rock crumbles in his your hand. the Door swings open.")
                TheDoor = False

    elif Act1Choice == "2":
        print("*Act 1 Story Chosen* 'Metal Bonds\n")
        Act1Choice = False

    elif Act1Choice == "3":
        print("*Act 1 Story Chosen* 'Man & monster'\n")
        Act1Choice = False

    elif Act1Choice == "4":
        print("*Act 1 Story Chosen* 'Winged Hope'\n")
        Act1Choice = False

    elif Act1Choice == "5":
        print("*Act 1 Story Chosen* 'Waiting On Luck\n")
        Act1Choice = False
