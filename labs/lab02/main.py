
#CS 31 Lab Activity 2 
# Michelle Najera
#October 7, 2026

print("Math Quizz 1")
print("*" * 20)

print()
name= input("Name:")
print()

start_quiz = input (f"Are you sure you you want to continue with the quizz?")
if start_quiz.upper() == "Y":
#.upper makes the responce uppercase and the same goes for .lower 
        print("Great! Lets's get started!")
#start asking questions 
#Question 1 (open question)
        q1= int (input ())
        if q1 == 25:
            counter += 1
            print("Yes that is correct!")
        else:
            print("sorry that is incorrect ")

#Question 2 mcq
        print ("?")
        print ("    A -")
        print ("    B -")
        print ("    C -")
        print ("    D- ")
        q2= input("Your Answer- Choose A/B/C/D :")
        if q2.upper == B: 
            counter += 1
            print("Yes that is correct!")
        else:
            print("sorry that is incorrect ")
        

        print("**** Your Final Score ****")
        print (f"Your Final Score is: {counter}")

        if counter == 5:
            print("You got it All correct YAYYAYA")
        elif counter >3 and counter<5:
            print("Great work!")
        elif counter <3 :
            print ("keep studying and try again later!")    
elif start_quiz.upper() == "N":
        print ("No worries! Come back when your ready! Bye Bye!")        
else:
    print("Sorry that is an invalid responce, Please try again!")

print()
print("*" * 20)
