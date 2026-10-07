
#CS 31 Lab Activity 2 
# Michelle Najera
#October 7, 2026

#Begining
RED = "\033[31m" # wrong answers
GREEN = "\033[32m"  # right answers
YELLOW = "\033[33m"  #  else answers
MAGENTA = "\033[35m"  # main color for text
CYAN = "\033[36m"  # for titles and questions
RESET = "\033[0m"  # normal color - white :(

print(MAGENTA)
print()
print("* " * 40)
print()
print(CYAN +"                       THE DISNEY MOVIES QUIZZ! "+ MAGENTA)
print()
print("* " * 40)

print()
name= input("Name:")
print()
print (f"Hello,{name}! Welcome to my DISNEY MOVIES QUIZZ!")
print()

# START 

print ('Do you want to start? (Yes or No)')
print()
start_quiz = input ("   Answer: ")
if start_quiz== "Yes" or start_quiz== "yes" :
#.upper makes the responce uppercase and the same goes for .lower 
        print()
        print("Great! Lets's get started!")

    #START OF QUIZZ

        #Question 1 (open question)

        counter =0
        print()
        print("-" * 40)
        print()
        print("             Question 1")
        print()
        print("2 + 2 =")
        print()
        q1= int (input ("   Answer:"))
        if q1 == 4:
            counter += 1
            print("Yes that is correct!")
        else:
            print("sorry that is incorrect ")

        #Question 2 mcq

        print("             Question 2")
        print ("?")
        print ("    A -")
        print ("    B -")
        print ("    C -")
        print ("    D- ")
        q2= input("Your Answer- Choose A/B/C/D :")
        if q2.upper == "B": 
            counter += 1
            print("Yes that is correct!")
        else:
            print("sorry that is incorrect ")
        
        # Question 3 

        print("             Question 3")
        print()
        print("2 + 2 =")
        print()
        q3= int (input ("   Answer:"))
        if q3 == 4:
            counter += 1
            print("Yes that is correct!")
        else:
            print("sorry that is incorrect ")

        # Question 4

        print("             Question 4")
        print ("?")
        print ("    A -")
        print ("    B -")
        print ("    C -")
        print ("    D- ")
        q4= input("Your Answer- Choose A/B/C/D :")
        if q4.upper == "B": 
            counter += 1
            print("Yes that is correct!")
        else:
            print("sorry that is incorrect ")

        # Question 5

        print("             Question 5")
        print ("?")
        print ("    A -")
        print ("    B -")
        print ("    C -")
        print ("    D- ")
        q5= input("Your Answer- Choose A/B/C/D :")
        if q5.upper == "B": 
            counter += 1
            print("Yes that is correct!")
        else:
            print("sorry that is incorrect ")
        
        # END OF QUESTIONS 
       
        print()
        print("-" * 40)
        print ()
        print("* * * * Your Final Score * * * *")
        print()
        print (f"Your Final Score is: {counter}")
        
        if counter == 5:
            print()
            print("You got it All correct YAYYAYA")
        elif counter >3 and counter<5:
            print()
            print("Great work!")
        elif counter <3 :
            print()
            print ("keep studying and try again later!")   
            
        #END OF QUIZZ

elif start_quiz == "No" or start_quiz == "no":
    print()
    print ("No worries! Come back when your ready!")
    print( )
    print ("Bye Bye!")        
else:
    print()
    print(YELLOW + f"Oops! Your answer '{start_quiz}' is an invalid response, Please try again!")

print()
print("* " * 20)
print()
print("             THE END")
print()
print("* " * 20)
