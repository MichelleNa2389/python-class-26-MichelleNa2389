
# CS 31 Project 1 
# Michelle Najera
# October 23, 2026

usa_cost = float(4976.00)
euro_cost =float(3400.00)
tropics_cost =float(2600.00)
asia_cost =float(3148.00)
sales_tax = 0.10

BLUE = "\033[34m"
RESET = "\033[0m"
chatbox = f"{BLUE}Dreamer:{RESET}"

#Greet the customer and introduce your sales program.
def greet_user():
    print()
    print("* " * 50)
    print(chatbox, "Hello! Welcome to Dreamscape Travels! Where We Turn Dreams into Destinations.”")

    print(f"""
{chatbox} Dreamscape offers travel packages across the United States, Europe, Asia, and the tropics. 
         Our trusted partners help ensure a smooth, enjoyable trip. We also customize itineraries 
         to fit your preferences and create your dream vacation.""")
    print()

def booking():
    print (chatbox, "Would you like to book one of our exclusive travel packages today?")
    booking_response =  input("Please enter 'yes' or 'no': ")

    if booking_response.lower() == "yes":
        print()
        print(chatbox,"Fantastic! Let's get started with your booking.")
        print("* " * 40)
        print("""
        Each package includes:
            - Airport transfers
            - Travel insurance
            - Guided tours and activities
            - Food Recommendations

            
        United States Package - New York"
            Day 1: Arrival, Check-in, Times Square
            Day 2: Central Park & Museums
            Day 3: Downtown & Statue of Liberty
            Day 4: Grand Central, Hudson Yards & Broadway
            Day 5: Free day for exploration
            Day 6: Free day for exporation
            Day 7: Check-out and Departure
            
        Europe Package - England and France
            Day 1: Arrival to England, Check-in, London sightseeing
            Day 2: Visting royal palaces and historic sites in London
            Day 3: Museums and cultural experiences in London
            Day 4: Arrival to France, Check-in, Paris sightseeing
            Day 5: Museums, Palaces, and Cafes
            Day 6: Free day for exploration in France
            Day 7: Departure

        Asia Package- Japan 
            Day 1: Arrival, Check-in, Shibuya & Shinjuku (Skyline views and neon streets)
            Day 2: Traditional Tokyo sightseeing (temples, gardens, and historic districts)
            Day 3: Anime, gaming & futuristic Tokyo (Akihabara, Odaiba, and themed cafes)
            Day 4: Mount Fuji day trip
            Day 5: free day for exploration
            Day 6: Spa And Wellness Day
            Day 7: Departure

        Tropics Package- Bahamas
            Day 1: Arrival and city tour
            Day 2: Swimming pigs in Exuma
            Day 3: Nassau culture and local food
            Day 4: Rose Island boat excursion
            Day 5: Snorkeling or scuba diving
            Day 6: Resort day + Cable Beach
            Day 7: Departure
            """)
        print("* " * 40)
        print("")
        #sales math 
        
    elif booking_response.lower() == "no":
        print(chatbox,"No problem! Feel free to explore our packages anytime.")
    else:
        print("Please enter 'yes' or 'no'.")

def sales():
    print(chatbox,"Before you choose your package, let's gather some details.")
    print()
    name= input("Enter your name: ")
    print()
    email= input("Enter your email: ")
    print()
    phone= input("Enter your phone number: ")
    print()
    package_choice = input(f"{chatbox}Which package would you like to book? (USA, Euro, Asia, Tropics): ")
    print()
    quantity = int(input(f"{chatbox}How many packages would you like to book? "))

    if package_choice.lower() == "usa":
        package_cost = usa_cost*quantity
        print()
        print(f"{chatbox}Package cost for {quantity} USA package(s): ${package_cost:.2f}")

    elif package_choice.lower() == "euro":
        package_cost = euro_cost*quantity
        print()
        print(f"{chatbox}Package cost for {quantity} Euro package(s): ${package_cost:.2f}")

    elif package_choice.lower() == "asia":
        package_cost = asia_cost*quantity
        print()
        print(f"{chatbox}Package cost for {quantity} Asia package(s): ${package_cost:.2f}")

    elif package_choice.lower() == "tropics":
        package_cost = tropics_cost*quantity
        print()
        print(f"{chatbox}Package cost for {quantity} Tropics package(s): ${package_cost:.2f}")
    else:
        print("Invalid package choice.")
        package_cost = 0
        #sales math 
    receipt(name, email, phone, package_choice, quantity, package_cost)


def receipt(name, email, phone, package_choice, quantity, package_cost):

    print("= " * 23)
    print("------------------ Receipt ------------------")
    print("= " * 23)
    print()
    print(f"                Name: {name}")
    print(f"               Email: {email}")
    print(f"               Phone: {phone}")
    print()
    print("-" * 43)
    print()
    print(f"             Package: {package_choice} ")
    print(f"            Quantity: {quantity}")
    subtotal = package_cost
    tax = subtotal * sales_tax
    total = subtotal + tax
    print("-" *43)
    print(f"            Subtotal: ${subtotal:.2f}")
    print(f"                 Tax: ${tax:.2f}")
    print("=" *43)
    print(f"               Total: ${total:.2f}")
    print("= " * 23)
    print()
    print("          Thank you for your purchase!")
    print()
    print("= " * 23)
   

def main():
    greet_user()
    booking()
    sales()
    receipt()
    
if __name__ == "__main__":
    main()
