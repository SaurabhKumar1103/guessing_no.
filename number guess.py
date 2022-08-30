import random
import os
import time

def menu():

    print()
    print()
    print()
    print("                                 NUMBER GUESSING")
    print()
    print()
    print("     1.To Play                                                           2.To Exit")
    print()

menu()
play=True
score=0.0
opt=input("Press 1.To play Or Any Key to Exit:")
if(opt=="1"):
    
    print("                                                                             Score is ",score)
    
    while(play):
        print("Hint-1:It is a number between 0 and 100")
        num=(random.randint(1,100))
        attempt=0
        print("Hint-2: ",end="")
        check=True
        
        if num > 2:
            # check for factors
            count=0
            for i in range(2,num):
                if (num % i) == 0:
                    print(i,end=", ") 
                    count+=1
                    if(count==2):
                        break
                    
            if(count==0):
                print("It is a prime number")
            else:
                print("is the multiple")
        elif num==2:
                print("It is an even prime number")       
                # if input number is less than
                # or equal to 1, it is not prime
        else:
                    print("is not a prime number")
        while(check):
            guess_no=int(input("                Enter the Guessing Number:"))
            if(num==guess_no):
                    print("Congrulation You guess the right Number")
                    if(attempt<=3):
                        score+=1
                        break
                    
            elif num>guess_no:
                    print("Guess Number is less than Actual Number")
                    print("Try Again")
                    attempt+=1
            else:
                    print("Guess Number is greater than Actual Number")
                    print("Try Again")
                    attempt+=1
            if attempt>3:
                print("Sorry!!! Score is deducted")
                print("Right answer is ",num)
                score-=0.5
                break
        
        time.sleep(2)
        # Clearing the Screen
        os.system('cls')
        menu()
        print()
        print("                                                                             Score is ",score)
        print( )
        opt=input("Press 1.To play Or Any Key to Exit:")
        if(opt!="1"):
            play=False
            os.system('cls')
            print("                                                                Your Score is ",score)
            time.sleep(1)
            print(exit())
        
        
else:
    os.system('cls')
    print("                                                                Your Score is ",score)
    time.sleep(1)
    print(exit())
