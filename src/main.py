# Main game file

import zork

#zork.Play_Zork()

#def PrintOutput(s):
    #print("OUTPUT", s)

itemList = []
isdead = False
room_num = 4
while isdead == False:
    if room_num == 4:
        print("---------------------------------------------------------")
        print("You are standing in an open field west of a white house, with a boarded front door.")
        print("You can see a small lake to the north.")
        print("(A secret path leads southwest into the forest.)")
        print("There is a Small Mailbox.")
        second = input("What do you do? ")
        temlist =  zork.front_of_house(second, itemList)
        isdead = temlist[1]
        room_num = temlist[0]
