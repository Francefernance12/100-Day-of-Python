print('''        __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
      ''')
choice1 = input("Welcome to Treasure Island. \n"
                "Your mission is to find the treasure. \n"
                "You started walking until you came across a cross road. Type \"left\" or \"right\"\n").lower()

if choice1 == "left":
    choice2 = input("You have arrived to a lake. There is an island in the middle of the lake. \n"
                    "type \"wait\" to wait for a boat. \n"
                    "type \"swim\" to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You got on the boat then, you arrived at the island safely. "
                        "You spotted a house with 3 doors. One red, one yellow and one blue. "
                        "which color do you choose?\n").lower()
        if choice3 == "blue":
            print("You went into the blue door. You were greeted by a bunch of monsters. You get eaten by the beasts.\n"
                  "Game Over!")
        elif choice3 == "yellow":
            print("You went through the yellow door. luckily, it was safe. You realize that this is a treasure room! \n"
                  "You cheered with happiness as you dive into the pool of treasure. \n"
                  "You Win!")
        elif choice3 == "red":
            print("You went through the red door. You notice that you were falling then you landed in a pool of fire \n"
                  "Game Over!")
        else:
            print("You were hesitant to open any door so you tried to go back to the boat but it left! \n"
                  "You can only do nothing but starve here. \n"
                  "Game Over!")
    else:
        print("You swam until a giant shark came out of nowhere then it ate you. \n"
              "Game Over!")
else:
    print("You fell into a hole. \n"
          "Game Over!")
