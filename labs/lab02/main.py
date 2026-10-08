
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
BLUE = "\033[34m"

print(MAGENTA)
print()
print("* " * 40)
print()
print(CYAN +"                       ✨THE DISNEY MOVIES QUIZZ!✨ "+ MAGENTA)
print()
print("* " * 40)

print()
name= input("Name: ")
print()
print (f"Hello,{name}! Welcome to THE DISNEY MOVIES QUIZZ!")
print()

# START 

print (CYAN+'Would you like to get started? (Yes or No)'+ MAGENTA)
print()

start_quiz = input ("   Answer: ")
if start_quiz== "Yes" or start_quiz== "yes"  or start_quiz== "YES":
#.upper makes the responce uppercase and the same goes for .lower 
        print()
        print("AWESOME! Let's start!")
        print()

    #START OF QUIZZ

        #Question 1 (open question)

        counter =0
        print("-" * 80)
        print()
        print("                                 ✨Question 1✨")
        print()
        print(CYAN +"What is the first Disney movie ever made?" + MAGENTA)
        print()
        q1= input ("   Answer: ")
        if q1 == "Snow White and the Seven Dwarfs" or q1 == "snow white and the seven dwarfs" or q1 == "Snow White" or q1 == "snow white":
            counter += 1
            print()
            print(GREEN +"Correct! Snow White and the Seven Dwarfs was the first movie Walt Disney made in 1937!🧹 👸 🪞 🏰 " + MAGENTA)
        else:
            print()
            print(RED + "sorry that is incorrect "+MAGENTA)

        #Question 2 mcq
        print()
        print("                                 ✨Question 2✨")
        print()
        print (CYAN +"What animal is Mushu in the movie Mulan?")
        print()
        print ("Choose A/B/C/D"+ BLUE)
        print ("    A - A Lizard 🦎")
        print ("    B - A Dragon 🐉")
        print ("    C - A Snake 🐍")
        print ("    D - A Cricket 🦗"+ MAGENTA)
        print()

        q2= input("   Answer: ")
        if q2 == "B" or q2 == "b": 
            counter += 1
            print()
            print(GREEN + "Correct! Mushu is a Dra-GON!" + MAGENTA)
        else:
           print()
           print(RED + "sorry that is incorrect "+MAGENTA)
        
        # Question 3 
        print()
        print("                                 ✨Question 3✨")
        print()
        print(CYAN+ "Who was the first Disney princess that was a person of color?"+MAGENTA)
        print()
        q3= input ("   Answer: Princess ")
        if q3 == "Jasmine" or q3 == "jasmine":
            counter += 1
            print()
            print(GREEN + "That is correct! Jasmine is the first P.O.C. princess. Aladdin made its dabute in 1992!🧞‍♂️ 🕌 🐯 "+ MAGENTA)
        else:
            print()
            print(RED + "sorry that is incorrect "+MAGENTA)

        # Question 4
        print()
        print("                                 ✨Question 4✨")
        print()
        print (CYAN+"In the early 2000 Disney made 2 spin off movies from their show Mickey's House of Mouse. What were the names of those movies?🐭")
        print()
        print ("  Choose A/B/C/D" + BLUE)
        print ("    A - Mickey's House of Villains👻🎃🕸️🕷️")
        print ("    B - Mickey's House of Mouse: A Valentine's Day Mix-Up 💐❤️🍫")
        print ("    C - Mickey's House of Mouse: The Grand Reopening Gala🥂🎉🥳")
        print ("    D - Mickey's Magical Christmas: Snowed in at the House of Mouse 👻🎃🕸️🕷️"+MAGENTA)

        q4= input("   Answer: ")
        if q4 == "A and D" or q4 == "D and A"or q4 == "a and D" or q4 == "D and a" or q4 == "A and d" or q4 == "d and A" or q4 == "a and d" or q4 == "d and a": 
            counter += 1
            print()
            print(GREEN +"Correct! They only made a Christmas and Halloween specials." + MAGENTA)
        else:
            print()
            print(RED + "sorry that is incorrect "+MAGENTA)

        # Question 5
        print()
        print("                                 ✨Question 5✨")
        print()
        print (CYAN+ "In Monsters, Inc., what is the company motto of the factory where Sulley and Mike work?🚪😳🧦🛌")
        print()
        print ("  Choose A/B/C/D"+ BLUE)
        print ("    A - Optimizing Nightmares, Powering Tomorrows")
        print ("    B - Your Worst Nightmare is Our Best Asset.")
        print ("    C - We Scare Because We Care")
        print ("    D - It's laughter we're after"+ MAGENTA)
        print()
        q5= input("   Answer:")
        if q5 == "C" or q5 == "c": 
            counter += 1
            print()
            print(GREEN + "Yes that is correct! Before Mike changed it to, It's laughter we're after" + MAGENTA)
        else:
            print()
            print(RED + "sorry that is incorrect "+MAGENTA)
        
        # END OF QUESTIONS 
       
        print()
        print("-" * 80)
        print ()
        print(CYAN + "* * * * * * * * Your Final Score * * * * * * * *"+ MAGENTA)
        print()
        print (f"Your Final Score is: {counter}")
        print()
        
        if counter == 5:
            print()
            print(CYAN+"You got All the questions correct! YAYYAYA"+ MAGENTA)
        elif counter >3 and counter<5:
            print()
            print(CYAN+"Great work!"+MAGENTA)
        elif counter <3 :
            print()
            print (YELLOW+"Looks like you need to brush up on your Disney knowledge! Don't worry, you can always try again!"+MAGENTA)   
            
        #END OF QUIZZ

elif start_quiz == "No" or start_quiz == "no" or start_quiz == "NO":
    print()
    print ("No worries! Come back when your ready!")
    print( )
    print ("Bye Bye!")        
else:
    print()
    print(YELLOW + f"Oops! Your answer '{start_quiz}' is an invalid response, Please try again!"+ MAGENTA)

print()
print("* " * 40)
print()
print(CYAN +"                      ✨ THE END✨"+ MAGENTA)
print()
print("* " * 40)
