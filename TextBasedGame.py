# A short prototype text based game 
# Noah Law

import random
import time

answer = input("Start the game? (yes/no)")

def snooze():
    time.sleep(3)
    return

def fileJump(start, end):
    fp = open("GameText.txt")
    for i, line in enumerate(fp):
            if i > start:
                snooze()
                print(line[:-1])
            if i > end:
                break
    fp.close()
    return


def carScenario():
    # Offer the player the first decision they will have to make in the game as a small demo of what's to come
    print("What will you do? (Stay in the left lane/Let the car pass)")
    carChoice = input().lower()
    

    while carChoice != "stay in the left lane" or carChoice != "let the car pass":
        if carChoice == "stay in the left lane":
            snooze()
            print("The car quickly switches lanes before abruptly cutting back into yours. You barely swipe it before it speeds off.")
            break
        elif carChoice == "let the car pass":
            snooze()
            print('You get over into the right lane allowing the speeding car to pass you.\nAs it does, you see the driver give you a thumbs up out the window.')
            break 
        else:
            print("What will you do? (Stay in the left lane/Let the car pass)")
            carChoice = input().lower()
    
    #Once the choice has been made, continue on the predetermined path of the game
    fileJump(23,26)
    #print("Car Scenario End")
    return
   
def hotelScenario():
    fileJump(27,32)
    lookChoice = input().lower()
    if lookChoice == "look":
       fileJump(34,40)
    else:
        print("You let out a yawn and make your way towards the hotel's entrance.")
    
    #print("Hotel Parking lot Scenario End")
    return

def insideHotel():
    fileJump(42,43)
    lookLobby = input().lower()
    if lookLobby == "look":
        fileJump(44,47)
        lookLobbyAgain = input().lower()
        if lookLobbyAgain == "look":
            fileJump(48,50)
    
    fileJump(52,64)
    #print("Past here")
    #Take in user input for going around the room
    metCondition = 0 #Do not let the player advance until all the prerequisites are fulfilled
    isDark = 0 #If the room is dark then prompt then to turn on the lights!
    roomInput = input().lower()
    while metCondition != 1:
        if roomInput == "look" and isDark == 0:
            fileJump(65,66)
            #print("Should tell you it's dark here ^")
            fileJump(63,64)
            turnOn = input().lower()
        else:
            print("Due to your incompetency of handling the simple task your mother has arrived to assist you")
            fileJump(74,79)
            break 
        
        if turnOn == "turn on lights" or turnOn == "turn on the lights" or turnOn == "turn on lights" or turnOn == "turn on light" or turnOn == "look" or turnOn == "look for a light":
            fileJump(67,69)
            fileJump(63,64)
            isDark = 1
            cleanRoom = input().lower()
        else:
            print("Due to your incompetency of handling the simple task your mother has arrived to assist you")
            fileJump(74,79)
            break
            
        if (roomInput == "clean room" or roomInput == "clean" or roomInput == "clean up your room" or roomInput == "look") and isDark == 1:
            fileJump(70,79)
            leosNotes = open("LeosNotes.txt", "w")
            metCondition = 1
        else:
            print("Due to your incompetency of handling the simple task your mother has arrived to assist you")
            fileJump(74,79)
            break

    return 

def nightWalk():
    jonathanRemark = 0
    fileJump(80,82)
    lookInput = input().lower()
    if lookInput == "look":
        fileJump(83,85)
    fileJump(86, 91)
    #print(lookInput)
    lookInput = input().lower()
    #print(lookInput)
    if lookInput == "run" or lookInput == "run away":
        fileJump(96,99)
        jonathanRemark = 1
    elif lookInput == "stand ground" or lookInput == "stand your ground":
        fileJump(94,95)
        jonathanRemark = 2
    else:
        fileJump(92,93)

    #print("We're here now")
    fileJump(100,107)
    lookInput = input().lower()
    if lookInput == "look":
        fileJump(108,111)
    
    
    if jonathanRemark == 1:
        fileJump(113,115)
    elif jonathanRemark == 2:
        fileJump(116,118)
    else:
        fileJump(119, 121)
    
    fileJump(125,142)
    

        
    
   










def begin_game():
    #Open the file with the game's beginning story
    fileJump(-1, 22)
    carScenario()
    hotelScenario()
    insideHotel()
    nightWalk()
    
    


    return


if answer == "yes":
    snooze()
    begin_game()

elif answer == "no":
    print("Oh man! :(")

