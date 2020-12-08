import time
import random

intro_text = ["\nOh no!", "Oh you there! Yeah You! My name is Sasha",
              "I seem to be lost and that's a problem because I am really hungry.",
              "Oh, I know, how about you help me.",
              "Will you help me?"]
confirm_1 = ["\nThank you so much for helping me.", "But, um...",
             "I don't know where my home is.",
             "So, you need to pick where we go.",
             "Are we going to the city or the country?"]
deny_1 = ["\nI don't know why you won't help me.", "Now I am sad.",
          "I am going to lay down and cry.", "The game is now over.\n"]
city_text = ["\nWow, the city is so big!",
             "That means it will be harder to find home.",
             "...and food. :(", "Hey, do you smell that?",
             "It smells like food!", "Can we go there?", "Please?"]
country_text = ["\nAw man... I don't recognize any of this.",
                "We should go to the city.", "Let's go!"]
cafe_text = ["\nBAM!",
             "SPLAT!", "CRASH!", "SNARF - SNARF - SNARF - SNARF - SNARF...",
             "Buuuuuuuuuuuurp..."]
building_text = ["\nLet's go explore!", "Hey! I recognize that place!",
                 "I think it is my apartment building.", "Let's go in!",
                 "Dagnabbit... there are 3 doors.",
                 "I don't remember which one is mine.", "Which one should we try?"]
door_1A_text = ["\nNO!", "This is waaaaay too pink.",
                "Let's get out of here, quick!", "SLAM!"]
door_1B_text = ["\nWOAH!", "Way too many other cats in here for me.",
                "Lets skedaddle, quietly.", "(click)"]
door_1C_text = ["\nWHAT?", "How are we back in the country?",
                "Let's go, quick!", "SLAM!"]
door_2A_text = ["\nYIKES!", "Can we agree not to talk about this?", "SLAM!"]
door_2B_text = ["\nTHAT'S A BIG BAG OF NOPE!", "SLAM!"]
door_2C_text = ["\nSLAM!!!"]
door_3A_text = ["\nWOW!!!!", "You win!", "This is my apartment!",
                "I can't believe we found it.", "I can't thank you enough for this.",
                "But... I'm hungry now and the refrigerator looks lonely,",
                "so I will see you in other games.", "Goodbye!\n"]
door_3B_text = ["\nThe fire escape?", "This doesn't make any sense.", "SLAM!"]
door_3C_text = ["\nDOGS! DOGS! DOGS! DOGS! DOOOOOOGGGGGSSSSS!", "SLAM!"]
exit_text = ["\nI don't know why you have to be that way.",
             "I am just a cat that wants some help!\n",
             "Ok...", "Have a good day.", "I will lay down and cry now.\n"]


def pause():
    time.sleep(1)


def text(list):
    for sentence in list:
        print(sentence)
        pause()


def help():
    response = input("(Please enter Y or N)\n").lower()
    pause()
    if response == 'y':
        text(confirm_1)
    elif response == 'n':
        text(deny_1)
        game_over()
    else:
        print("\nHmmmm...\n")
        pause()
        help()


def city_country():
    response = input("(Please enter City or Country)\n").lower()
    pause()
    if 'city' in response:
        text(city_text)
        cafe()
    elif 'country' in response:
        text(country_text)
        print("Zoooooom...")
        pause()
        text(city_text)
        cafe()
    else:
        print("\nHmmm...\n")
        pause()
        city_country()


def cafe():
    response = input("(Please enter Y or N)\n").lower()
    pause()
    if response == 'y':
        print("\nWOO-HOO!")
        pause()
        text(cafe_text)
        pause()
        text(building_text)
        building()
    elif response == 'n':
        print("\nReally? Ok...")
        pause()
        text(building_text)
        building()
    else:
        print("Hmmm...")
        pause()
        cafe()


def building():
    response = input("(Please enter 1, 2, or 3)\n")
    pause()
    if '1' in response:
        door_1_choice = random.choice([door_1A_text, door_1B_text,
                                       door_1C_text, door_3A_text])
        door_1(door_1_choice)
        if door_1_choice == door_3A_text:
            game_over()
        building()
    elif '2' in response:
        door_2_choice = random.choice([door_2A_text, door_2B_text,
                                       door_2C_text, door_3A_text])
        door_2(door_2_choice)
        if door_2_choice == door_3A_text:
            game_over()
        building()
    elif '3' in response:
        door_3_choice = random.choice([door_3A_text, door_3B_text])
        door_3(door_3_choice)
        if door_3_choice == door_3A_text:
            game_over()
        building()


def door_1(choice):
    text(choice)


def door_2(choice):
    text(choice)


def door_3(choice):
    text(choice)


def game_over():
    response = input("Play again?\n(Please enter Y or N)\n").lower()
    if response == 'y':
        play_game()
    elif response == 'n':
        text(exit_text)
        exit()
    else:
        game_over()


def play_game():
    text(intro_text)
    help()
    city_country()


play_game()
