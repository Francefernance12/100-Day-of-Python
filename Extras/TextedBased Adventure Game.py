import sys

# Number of steps
steps = 0
steps_limits = 5


# define a function to increment the step count
# if the user keep on going to the wrong direction, the steps number will raise by 1 until it reach the limit.
def increment_steps():
    global steps
    steps += 1


# story
def beginning():
    while steps < steps_limits:  # I am using while loops to let the user the chance to type in their inputs again if they type in the wrong input or they went to the wrong direction
        print("""
        You were relaxing in your home. 
        It is a regular room filled with ordinary stuff. 
        Suddenly, a mail came from the imperial castle. 
        You were summoned by the king! 
        You immediately prepared to set yourself to your quest! 
        The castle is straight ahead.

        Type right, left, forward, or backward to choose the direction you want to go.
        """)

        directions = ["left", "right", "forward", "backward"]
        player = input("")

        if player in directions:
            if player == "left":
                print("You ran into a wall. You can't progress from there. Type in your directions again")
                increment_steps()
            elif player == "right":
                print("You ran into a wall. You can't progress from there. Type in your directions again")
                increment_steps()
            elif player == "forward":
                print("""
                This is the castle, where the king and queen live. 
                It is filled with luxurious things.
                Inside, you greeted the king and the queen.
                They both ask you a very important task.
                They want you to eliminate a monster that has been terrorizing adventurers inside the dungeon.
                Without complaints, you went out.
                """)
                break  # Exit the loop when the player chooses "forward"
            elif player == "backward":
                print("You ignored the king's letter then you went back to bed to sleep. GAME OVER!")
                sys.exit()  # the program will stop when the user unlocks this secret ending
            else:
                print("Invalid input. Please try again: ")
        else:
            print("Invalid input. Please try again: ")


def middle_story():
    while steps < steps_limits:
        print("""
        After the king and Queen gave you the full story. 
        You prepared armor, and weapons to be prepared to head out to the dungeon.
        You saw that there was an exit to the right that leads towards a forest.
    
        type right, left, forward, backward to choose the direction you want to go.
    
        """)
        directions = ["left", "right", "forward", "backward"]
        player = input("")

        if player in directions:
            if player == "left":
                print("You ran into a wall. You can't progress from there. Type in your directions again")
                increment_steps()
            elif player == "right":
                print("""
                You exited through the door to your right. 
                You were greeted with a beautiful forest with beautiful creatures and trees.
                You venture towards the dungeon.
                """)
                break
            elif player == "forward":
                print("""
                You went closer to the King and Queen. They both smiled then they gave you their blessings.
                """)
                increment_steps()
            elif player == "backward":
                print("You felt like it was too much work then you left the castle and never came back. GAME OVER!")
                sys.exit()
            else:
                print("Invalid input. Please try again: ")
        else:
            print("Invalid input. Please try again: ")


def middle_story2():
    while steps < steps_limits:
        print("""
        You progressed through the forest.
        You have encountered many slimes and mythical creatures.
        Nothing harmful have been detected.
        Not until the you have finally reached the gate of a dungeon that was guarded.
        two giants, tripled your size, is guarding the gate.

        type right, left, forward, backward to choose the direction you want to go.

        """)
        directions = ["left", "right", "forward", "backward"]
        player = input("")

        if player in directions:
            if player == "left":
                print("""
                Before doing anything, you looked around to your left.
                luckily you spotted what looks like a hidden entrance to the dungeon!
                You quickly went in
                """)
                break
            elif player == "right":
                print("You ran into a wall. You can't progress from there. Type in your directions again")
                increment_steps()
            elif player == "forward":
                print("""
                With great courage, you showed yourself to the two giants.
                You have taken out your weapon and a slingshot.
                eventually the two beast is finally brought down.
                You went through the front gate
                """)
                break
            elif player == "backward":
                print("\"NOPE!\". You said as you ran back to your sweet home. GAME OVER!")
                sys.exit()
            else:
                print("Invalid input. Please try again: ")
        else:
            print("Invalid input. Please try again: ")


def middle_story3():
    while steps < steps_limits:
        print("""
        As you made it in the dungeon.
        You sense a bunch of monsters inside.
        You ran through the dungeon.
        slaying hungry looking monsters left and right.
        You then stopped and came by two paths with two signs.
        one of the sign reads \"boss room is straight ahead\".
        The other sign reads \"treasure room to your right!\"
        You chose to go....

        type right, left, forward, backward to choose the direction you want to go.

        """)
        directions = ["left", "right", "forward", "backward"]
        player = input("")

        if player in directions:
            if player == "left":
                print("You are staring at the wall for some reason... (Type in again)")
                increment_steps()
            elif player == "right":
                print("""
                You were entrance by the word \"treasure\"
                You thought it wouldn't hurt to take a look.
                You turned right towards the treasure room.
                The sign was right! There was a mountain of gold in front of you!
                But as you went towards the treasure, a pitfall trap activated.
                Then you fell inside deeper in the dark abyss.
                GAME OVER!
                """)
                sys.exit()
            elif player == "forward":
                print("""
                You were smart enough to know that it might have been a trap.
                You went forward until you encountered a giant door that leads to the boss.
                You prepared mentally then you went in
                """)
                break
            elif player == "backward":
                print("\"NOPE!\". You said as you ran back to your sweet home. GAME OVER!")
                sys.exit()
            else:
                print("Invalid input. Please try again: ")
        else:
            print("Invalid input. Please try again: ")


def the_end():
    while steps < steps_limits:
        print("""
        You entered the door.
        You saw the evil monster sitting on a giant throne.
        The monster stood up and he readies his fists.
        You both faced each other.
        The monster raised its large muscular right arms.
        It is attempting to use a slam attack!
        How do you react?!
        hint: it would be better to keep a good distance between him

        type right, left, forward, backward to choose where you are going to dodge:
        """)
        dodge = ["left", "right", "forward", "backward"]
        player = input("")

        if player in dodge:
            if player == "left":
                print("""
                You dodged to the right.
                You succeeded in dodging but he suddenly did a sweep attack 
                then you were gravely damaged.
                GAME OVER!
                """)
                sys.exit()
            elif player == "right":
                print("""
                You dodged to the right which succeeded
                but you did not pay attention to his other hand that was going to squash you
                You ended up getting squashed like a bug
                GAME OVER!
                """)
                sys.exit()
            elif player == "forward":
                print("""
                You wanted to show him who's boss by going forward and confronting him
                But that went badly as you were not ready for his fast smash attack.
                You ended up being squashed like a bug.
                GAME OVER!
                """)
                sys.exit()
            elif player == "backward":
                print("""
                You did a back flip which enabled you to dodge his smash attack
                You did it again as the monster did it again with its other arm.
                As the arm was stuck to the ground you ran up his arms like stepping on stairs
                then you strike him down using a rock with a slingshot.
                After the very hard fight against the monster,
                You went back to the castle
                The king and queen rewarded you with a title of a knight and gold
                The world is saved due to your bravery and choices.
                THE END.
                """)
                break
            else:
                print("Invalid input. Please try again: ")
        else:
            print("Invalid input. Please try again: ")


if steps >= steps_limits:
    print("You've reached the step limit. The game is over.")
    sys.exit()


beginning()
middle_story()
middle_story2()
middle_story3()
the_end()
