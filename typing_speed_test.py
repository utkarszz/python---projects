from time import *
import random as r
def mistake (partest,usertest) :
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error
def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)



test =["lorem  ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
"my name is utkarsh" , "helloooooooo"]
test1 = r.choice(test)
print("*****typing speed test*****")
print(test1)
print()
print()
time_1 = time()
# Taking user input
testinput=input("Enter :")
time_2 = time()

print('speed : ',speed_time(time_1,time_2,testinput),"words per second")
print("error : ",mistake(test1,testinput),"characters")