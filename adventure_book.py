name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    print("You are on a road and the road ends in a fork that goes 'left' or 'right' that has no signage. Which way would you like to go: ")).lower()

if answer == "left": #nested if statements begin
    answer = input("You see a bandit camp on the road ahead of you. Type 'continue' to continue down the road or 'forest' to avoid the camp in the forest: ").lower()

    if answer == "continue":
        print("The bandits came out of their cam and killed you.")
    elif answer == "forest":
        answer = input("You walk for a day and reach a city. Type 'enter' to enter the city, or 'rest' to rest for the rest of the day: ").lower()
    else:
        print("Not a valid option. Try again")

elif answer == "right":
    answer = input("You come to a bridge that looks worn down from heavy use. Type 'over' to go over the bridge, or 'under' to go under the bridge: ").lower()

    if answer == "over":
        print("The bridge collapsed under your weight killing you.")
    elif answer == "under":
        answer = input("You find a lost child under the bridge. Type 'help' to help the child, or 'leave' to leave the child be: ").lower()

        if answer == "leave":
            print("The child pulled out a knife and killed you.")
        elif answer == "help":
            print("You help the child back to their home and their rich parents pay you back with lots of gold. You Win!")
        else:
            print("Not a valid option. Try again")

    else:
        print("Not a valid option. Try again")

else:
    print("Not a valid option. Try again")

print("Thanks for trying my story.")
