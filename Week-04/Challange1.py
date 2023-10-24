#10 locations 

#10 items 

#5 puzzles 

#All python techniques of week 1-3 

#No errors 

#No copies of work from fellow students or adventures found on the internet 

#Theme must be SPACE TRAVE
import sys
import time

inventory = []
visited = []
not_visited = ["Toi","Wolf"]

username = input("Enter your Astronaut name: ")

def intro():
    dialogue("<System message>\n"+
           "It's 2034/03/17,\n\n"+
           "You are one of the very few people who have been recruited for a mission by Terragroup.\n"+
           "Terragroup is the biggest abbreviation agency in the world.\n"+
           "The ground center Commander for this mission is Nikita Buyanov.\n\n"+
           "<Nikita Buyanov>\n"+
           "Your mission is to visit the planets that have been recently discoverd.\n"+
           "Astronaut " + username + " we wish you the best of luck on your voyage!\n\n"+
           "<System message>\n"+
           "You're on your way to the launch site and one of the Terragroup workers hands you a key.\n"+
           "The key is needed to initiate the launch protocol.\n\n")
    
    print("An item has been added to your inventory.\n"+
          "[+1 Launch Key]\n\n")
    
    inventory.append("Launch Key")

    time.sleep(2)

    dialogue("<Sytem message>\n"+
           "You arrive in the cockpit of the rocket.\n\n"+
           "<Nikita Buyanov>\n"+
           "Put the launch key into the key hole.\n")
    is_ready = input("Are you ready? [Yes/No] ")
    while is_ready != "Yes" and is_ready != "yes":
        if is_ready == "No" or is_ready == "no":
            dialogue("Oh? I'll give you some time then, go take a breather for 10 sec!\n")
            for i in range(1,11):
                time.sleep(1)
                print(i)

            is_ready = input("Are you ready now? [Yes/No] ")
        else:
            dialogue("I didn't hear you clearly can you repeat?\n")
            is_ready = input("Are you ready? [Yes/No] ")
    
    print("\n<Nikita Buyanov>")
    dialogue("Good now turn the key to activate the launch protocol\n\n"+
             "<System message>\n"+
             "Launch protocol activated\n"+
             "Launching in 10\n")
    for i in range(9,0, -1):
        time.sleep(1)
        print(i)
    print("\n<Nikita Buyanov>")
    dialogue("We have a lift off\n\n"+
             "- 2 Hours later -\n")
    print("\n<NikitaBuyanov>")
    dialogue("Now that you're oficialy in space you need decide what planet you want to go to.\n"+
             "Go up to the terminal to choose your first destination.\n")
    
    travel = input("What planet do you want to travel to first? " + str(not_visited))
    while travel != "Toi":
        dialogue("<System message>\n"+
                 "Destination not found\n")
        travel = input("What planet do you want to travel to? " + str(not_visited))
    dialogue("\n<System message>\n"+
             "Destination is set to "+ travel +".\n"+
             "have a safe journey!\n")
    load_level(travel)

def wolf():
    flight_to_wolf()

def flight_to_wolf():
    dialogue("\n<System message>\n"+
             "!ERROR!\n"+
             "Loose feul gauge detected!\n\n"+
             "You remember there is a wrench to tighten the gauge in the toolcabinet but it's locked with a code lock.\n"+
             "But you don't remeber the code, A tells you there is a hint about the code on a note"+
             "but he doesn't know where it is\n\n")
    search_note = input("Where do you want to search for the note? [Filling cabinet, Desk drawers]")
    if search_note == "Filling cabinet":
        print("An item has been added to your inventory.\n"+
              "[+1 Note]\n\n")
        inventory.append("Note code")
        time.sleep(2)
    else:
        print("You can't find the note check somewhere else before you lose to much fuel!")
        search_note = input("Where do you want to search for the note? [Filling cabinet, Desk drawers]") 

            

def toi():
    dialogue("\n<System message>\n"+
             "[8 hours have passed]\n"+
             "You have now arrived on planet TOI-1338b\n"+
             "This planet was discovered by an intern who has been here for 3 days.\n"+
             "Wolf Cukier discovered this beautiful planet which orbits 2 suns.\n"+
             "Its mass is 33 Earths, it takes 95.2 days to complete one orbit of its stars\n\n")

    time.sleep(1.5)

    dialogue("<Nikita Buyanov>\n"+
             "Astronaut " + username + ", I see you guys have arrived on planet TOI-1338b, be carefull on this planet please,\n"+
             "Put your mask on tightly, this planet contains of methane and ammonia, it will stink.\n"+
             "On top of that, never start a fire here, this planet also contains dense sources of hydrogen and helium.\n"+
             "It will explode...\n\n")

    print("Two items has been added to your inventory.\n"+
          "[+1 Tightly Fitted Helmet]\n"+
          "[+1 Oxygen Tank (100%)]")

    inventory.append("Tightly Fitted Helmet")
    inventory.append("Oxygen Tank")
    visited.append("Toi")
    not_visited.remove("Toi")
    travel()

def flight_home():
    print("\nEnd")


def reset_game():
    inventory = []

def dialogue(text):
     for i in text:
          sys.stdout.write(i)
          sys.stdout.flush()
          #time.sleep(0.03)

def travel():
    if not not_visited:
        dialogue("\n<system message>\n" +
                 "Welcome back in the cockpit!\n" +
                 "Now that you guys have completed all of your misions we are gonna safely go back home\n"+
                 "You put in the key to start the final launch protocol of the expedition\n"+
                 "\n<System message>\n"+
                 "Launch protocol activated\n"+
                 "Launching in 10\n")
        for i in range(9,0, -1):
            time.sleep(1)
            print(i)
        flight_home()
    else:
        dialogue("\n<system message>\n" +
                "Welcome back in the cockpit!\n" +
                "Now that you are done with your mission here. Go up to the terminal to select your next destination.\n")    
        travel = input("What planet do you want to travel to? " + str(not_visited))
        while travel not in not_visited:
            if travel in visited:
                dialogue("\n<System message>\n" +
                        "You already traveled to this place and have no mission there!")
                travel = input("What planet do you want to travel to? " + str(not_visited))
            else:
                dialogue("\n<System message>\n" +
                        "Destination not found\n")
                travel = input("What planet do you want to travel to? " + str(not_visited))
        dialogue("\n<System message>\n" +
                "Destination is set to " + travel + ".\n" +
                "have a safe journey!\n")
        load_level(travel)

def load_level(level):
    locations = {
        "intro": intro,
        "Toi": toi,
        "Wolf": wolf,
    }
    locations[level]()

load_level("intro")