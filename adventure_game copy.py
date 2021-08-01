import time
import random
from pyfiglet import Figlet
custom_fig = Figlet(font="big")


def dice_roll(roomlist):
    print("you unlocked a chance roll!!\n")
    print_pause("If you roll an even number you're still in the game!")
    rolling = random.randint(1, 6)
    print_pause(rolling)
    if rolling % 2 == 0:
        print_pause("You rolled an even number! You're still in the game!")
        play_game(roomlist)
    else:
        print("You rolled an odd number, better luck next time.")
        game_over(roomlist)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def game_over(roomlist):
    print_pause(custom_fig.renderText("Game Over"))
    response = input("Do you want to play again?\nYes or No\n").lower()
    if "yes" in response:
        print_pause("Great, you got this Rookie!\n")
        roomlist.clear()
        intro(roomlist)
    elif "no" in response:
        print_pause("What a strange game,"
                    "The only winning move is not to play.\n")
        goodbye()
    else:
        print_pause("HUH?!\n")
        game_over(roomlist)


def intro(roomlist):
    print_pause(custom_fig.renderText("Escape Room: Special Agent"))
    print_pause("You arrive to your job interview "
                "at a secret government agency.\n")
    print_pause("They give you a folder that says README on the front and "
                "lock you in a room with a terminal prompt up on "
                "a computer.\n")
    print_pause("You open the folder you were given and read the contents.\n")
    print_pause("It appears as though they want you to play this "
                "weird text-based game "
                "to figure out the 10 digit passcode "
                "to the door of the room you are locked in!\n")
    print_pause("You will need to figure out the first 7 digits "
                "from the rooms.\n")
    print_pause("The last 3 digits change every 60 seconds, "
                "so be sure to complete all the rooms in the correct order "
                "to unlock the final 3 digit code and break free!\n")
    print_pause("If you succeed, you will be a special agent, "
                "but if you fail, who knows what will happen.\n")
    print_pause("Goodluck Rookie!\n")
    pre_game(roomlist)


def pre_game(roomlist):
    print_pause("Greetings Rookie! My name is Joshua.\n")
    response = input("Shall we play a game?\nYes or No \n").lower()
    if "yes" in response:
        print_pause("Special agent escape room it is!\n")
        play_game(roomlist)
    elif "no" in response:
        print_pause("A strange game, The only winning move is not to play.\n")
        print_pause("Computer will self-destruct in 3 seconds.\n3\n2\n1\n")
        game_over(roomlist)
    else:
        print_pause("Huh? Sorry, I dont understand\n")
        pre_game(roomlist)


def play_game(roomlist):
    print_pause("There are three rooms, each room represents a "
                "specialized division witin the agency.\n")
    response = input("Which room would you like to enter?\n"
                     "Cyber Crime Division\nWhite Collar Division\n"
                     "High Profile Division\n").lower()
    if "cyber" in response:
        cyber(roomlist)
    elif "white" in response:
        white_collar(roomlist)
    elif "high" in response:
        high_profile(roomlist)
    else:
        print_pause("Sorry, I don't understand your input.\n")
        play_game(roomlist)


def cyber(roomlist):
    if "23" in roomlist:
        print_pause("You already caught the cyber criminal.")
        play_game(roomlist)
    else:
        print_pause("You are assigned to your first case, you need "
                    "to track a cyber criminal on the dark web!\n")
        print_pause("You found the person of interest bidding on a "
                    "stolen famous piece of art.\n")
        response = input("What do you do next??\n1.Trace the criminals IP\n"
                         "2.Send this off to the cyber division, because "
                         "cyberspace scares me?\nPlease "
                         "enter 1 or 2\n").lower()
        if "1" in response:
            print_pause("You’re in luck!\n")
            print_pause("This criminal forgot to use VPN!\n")
            print_pause("You successfully traced his IP, tracked him down, "
                        "and just as you burst into his basement to take "
                        "him into custody...\n")
            print_pause("His bitcoin transaction cleared to the art thief.\n")
            print_pause("While searching through the basement, you find out "
                        "something is hidden in a locker at the downtown "
                        "train staion.\n")
            print_pause("You need to find out that locker number!\n")
            response = input("What do you do next?\n"
                             "1.Do you question this suspect?\n"
                             "2.Do you send him straight to jail?\n"
                             "Please enter 1 or 2\n").lower()
            if "1" in response:
                print_pause("You walk in the room and notice the cyber "
                            "criminal keeps mumbling 23, over and over.\n")
                print_pause("He is furious the art thief crossed him "
                            "again, the art thief took his bitcoins and "
                            "already posted the stolen art online "
                            "again to sell.\n")
                print_pause("You ask him what locker number the art was "
                            "going to be hidden in,\nbut it seems as though "
                            "he isn’t listening, or is he?\n")
                print_pause("He continuously mumbles 23. He stops, "
                            "makes eye contact and says,\nthere is no "
                            "honor among thieves.\n")
                print_pause("You won’t find the art in the locker,\n"
                            "but you will find "
                            "information to take down the art thief once "
                            "and for all!\n")
                roomlist.append("23")
                print_pause("Nice work Rookie, Let's add 23 to our list!\n")
                play_game(roomlist)
            elif "2" in response:
                print_pause("Your supervising officer is upset.\n"
                            "Turns out the cyber criminal had valueable "
                            "information you needed.\n")
                dice_roll(roomlist)
            else:
                print_pause("Sorry, I have no idea what you just said.\n")
                cyber(roomlist)

        elif "2" in response:
            print_pause("Sorry, this was a direct order Rookie.")
            dice_roll(roomlist)
        else:
            print_pause("Sorry, I am not built with NLU or NLP.\n"
                        "Blame my dev, and please try again.\n")
            cyber(roomlist)


def white_collar(roomlist):
    if "00" in roomlist:
        print_pause("You already caught the art thief.")
        play_game(roomlist)
    else:
        print_pause("This white collar ciminal is an art thief, "
                    "and he is making headlines EVERYWHERE!\n")
        print_pause("Be sure you gathered the missing information from "
                    "the cyber criminal before entering.\n")
        if "23" in roomlist[0:1]:
            print_pause("Ahh, yes you did find locker 23!\n")
            print_pause("Now you can get the last bit of information you "
                        "need to lock the art thief away for good,\n"
                        "Well done!!")
            print_pause("You are now face to face with the art thief, "
                        "what do you tell him?\n")
            response = input("1.Do you tell him about the evidence found "
                             "in the locker at the train station?\n"
                             "2.Tell him he is free to go, so you can follow "
                             "him back to his art stash?\n"
                             "Please enter 1 or 2\n").lower()
            if "1" in response:
                print_pause("The art thief panics when you mention a locker, "
                            "and he says, whatever was in locker 00 "
                            "wasn't mine!!\n")
                print_pause("Apperntly, he had some stolen items in "
                            "locker 00.\nHe just mistakenly told you about a "
                            "new locker assuming you were referring to it, "
                            "OOPS!.\n")
                print_pause("Add 00 to the list.\n")
                roomlist.append("00")
                play_game(roomlist)
            elif "2" in response:
                print_pause("Oh no! You lost the art thief while tailing him. "
                            "Sorry, Rookie!\n")
                dice_roll(roomlist)
            else:
                print_pause("Uh, I think you meant to say something else, "
                            "Let's try this again.\n")
                white_collar(roomlist)
        else:
            print_pause("Sorry, you don’t you have enough experience "
                        "yet Rookie.\n")
            play_game(roomlist)


def high_profile(roomlist):
    if "00" in roomlist[1:2]:
        response = input("Decypher the riddle to get a three digit code, "
                         "are you ready?\nPlease enter Yes or No\n").lower()
        if "yes" in response:
            print_pause("If what you seek is what you find, "
                        "this will release you from your bind.\n")
            print_pause("The mind bends twists and turns, for this is "
                        "what you will learn.\n")
            print_pause("Ask a question, go ahead four you will only "
                        "hurt your head.\n")
            print_pause("1 comes first before them all, if you miss this, "
                        "for you will fall.\n")
            print_pause("Six feet down below, for this is where people go, "
                        "but only at the very end.\n")
            response = input("What is the 3 digit code?\n")
            if "146" == response:
                roomlist.append("146")
                print_pause("Great work Rookie!\n")
                final(roomlist)
            else:
                print_pause("Sorry, thats not right.\n")
                high_profile(roomlist)
        else:
            print_pause("Ok, no problem Rookie.\n")
            play_game(roomlist)
    else:
        print_pause("This room is restricted to seasoned special agents that "
                    "can handle this criminals mind games.\n")
        play_game(roomlist)


def final(roomlist):
    codelist = ["348", "222", "777", "314", "110", "629",
                "208", "713", "512", "715", "215"]
    final_code = random.choice(codelist)
    roomlist.append(final_code)
    print_pause(roomlist)
    print_pause("Now rearrange the numbers from least to greatest and "
                "enter the code to break free!\n")
    response = input("Passcode:\n")
    if "0023146" in response:
        if final_code in response:
            print_pause("Congratulations! You have escaped the room "
                        "special agent!\n")
            print_pause("You have a bright future ahead of you.\n")
            game_over(roomlist)
        else:
            print_pause("Oof, nope. Try again. Remember the code changes "
                        "every 30 seconds\n")
            roomlist.remove(final_code)
            final(roomlist)
    else:
        print_pause("Oof, nope. Try again. Remember the code changes "
                    "every 30 seconds\n")
        roomlist.remove(final_code)
        final(roomlist)


def goodbye():
    print_pause(custom_fig.renderText("Goodbye, Special Agent!"))
    exit()


def initiate_game():
    roomlist = []
    intro(roomlist)
    pre_game(roomlist)
    play_game(roomlist)


initiate_game()
