
#CS 31 Lab Activity 3.1, 
# Michelle Najera
# October 19, 2026

# display a welcome message
print("The Miles Per Gallon program")
print()

repeat_mpg = "y"

while repeat_mpg.lower() == "y":
# get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon of gas: "))

    if miles_driven <= 0:
     print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
    # calcate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        total_gas_cost = round(gallons_used * cost_per_gallon, 2)
        cost_per_mile = round(total_gas_cost / miles_driven, 2)

        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gas_cost)
        print("Cost per mile:             ", cost_per_mile)

    print()
    repeat_mpg = input("Do you want to calculate another MPG? (y/n): ")  

print()
print("Bye!")
