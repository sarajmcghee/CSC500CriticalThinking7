#Part 1
while True:
    try:
        years = int(input("Enter the number of years: "))
        if years <= 0:
            print("Please enter a positive number greater than zero.") 
        else:
            break
      
    except ValueError:
        print("Please enter a positive integer value.")

total_months = 0
total_rainfall = 0.0

months = [ "Januaray", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for year in range (1, years +1 ):
    print(f"\nFor Year {year} : ")
    for month in months:
        while True:
            try:
                month_rainfall = float(input(f"Enter rainfall (in inches) for {month}: "))
                if month_rainfall < 0:
                   print("Please enter a positive number greater than zero.") 
                else:
                  break
            except ValueError:
                print("Please enter a positive value.")
        total_months += 1
        total_rainfall += month_rainfall
average_rainfall = total_rainfall / total_months

print("\nResults of Calculations:")
print(f"Total months: {total_months}" )
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f}")


#Part 2
while True:
     try:
       books = float(input(f"Enter the number of books purchased this month: "))
       if books < 0:
          print("Please enter a positive number greater than zero.") 
       else:
          break
     except ValueError:
          print("Please enter a positive integer value.")

match books :
    case 0:
        points_earned = 0 
    case 2:
        points_earned = 5 
    case 4:
        points_earned = 15 
    case 6:
        points_earned = 30
    case _ if books > 8:
        points_earned = 60 
    case _:
        points_earned = 0

print(f"Total points you awarded: {points_earned} ")