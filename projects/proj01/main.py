# Starting file for PROJECT 1
# Include your course number, student first and last name, and date in the comment header


#Greet the customer and introduce your sales program.

print("Hello Dreamer! Welcome to Dreamscape Travels! Where We Turn Dreams into Destinations.”")

startsale = input("Would you like to learn more about our travel packages? (yes/no): ")
print()

if startsale.lower() == "yes":
    print("Our Dreamscape packages include a variety of destinations across the United States, Europe, Asia, and the tropics.")
    print("We have standerized travel plans with realiable companies to ensure a smooth and enjoyable experience.")
    print("But if you have specific preferences or unique travel needs, we are happy to customize your itinerary to make your dream vacation truly unforgettable.")
    print()
    print("Would you like to book one of our exclusive travel packages today?")
    book = input("Please enter 'yes' or 'no': ")
    print()
    if book.lower() == "yes":
        print("Fantastic! Let's get started with your booking.")
        print ()
        print("United States Package")
        print("New York City · 4 days, 3 nights")
        print("Package includes: Hotel accommodation, selected sightseeing tours, and itinerary assistance.")
        print("day 1: Arrival and hotel check-in. Visit Times Square")
        print("day 2: Visit Central Park, The statue of Liberty, and enjoy a Broadway shows.")
        print("day 3: Free day for personal exploration.")
        print("day 4: Departure.")
    
        print("Europe Package") 
        print("")  
        print("day 1: Arrival and hotel check-in. Explore local attractions.")
        print("day 2: Sightseeing tours and cultural experiences.")
        print("day 3: Free day for personal exploration.")
        print("day 4: Departure.")
        print("Package includes: Hotel accommodation, selected sightseeing tours, and itinerary assistance.")
        print()
        
        print("Asia Packages")
        print("Package includes: Hotel accommodation, selected sightseeing tours, and itinerary assistance.")
        print("day 1: Arrival and hotel check-in. Explore local attractions.")
        print("day 2: Sightseeing tours and cultural experiences.")
        print("day 3: Free day for personal exploration.")
        print("day 4: Departure.")

        print("Tropical Packages")
        print(" day 1: Arrival and hotel check-in. Relax on the beach.")
        print("day 2: Enjoy water sports and local excursions.")
        print("day 3: Free day for personal exploration.")
        print("day 4: Departure.")
        print("Package includes: Hotel accommodation, selected sightseeing tours, and itinerary assistance.")
        print()

    elif book.lower() == "no":
        print("No problem! Feel free to explore our packages anytime.")
    else:
        print("Please enter 'yes' or 'no'.")

elif startsale.lower() == "no":
print()
    print("No worries! Have a wonderful day and safe travels!")
else:
    print()
    print("Please enter 'yes' or 'no'.")

#elsif 
#Ask if the user would like to learn more about your product or service.
#If yes, provide a short overview of the product or service.
#If no, end the conversation politely with a farewell message.

#If the customer continues:
#Provide a creative paragraph overview of your product or service.
#Make it engaging — serious or silly, your choice!
#Format long text nicely across multiple lines for readability.
#Ask if the user would like to make a purchase.
#If yes, continue with the sale.
#If no, display a farewell and end the program.

#Closing the sale:
#Ask for the customer’s first and last name and store them in variables.
#Ask for their email address and phone number (no validation needed at this point).
#Tell the customer how much the product or service costs.
#Ask how many items they want to purchase.
#Calculate and display the subtotal (quantity × price).
#Apply a 10% sales tax.
#Calculate and display the total amount due.

#Create a formatted receipt showing:
#Customer name, email, and phone number
#Quantity purchased and cost per item
#Subtotal, tax, and total amount due
#Nicely formatted output using line breaks and symbols
#End with a thank-you message and farewell.