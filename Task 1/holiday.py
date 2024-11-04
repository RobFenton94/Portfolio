#  A list of destinations for the user to choose from.
city_flight = ["Milan", "Prague", "Berlin", "Warsaw", "Madrid"]
print(city_flight)

#  The user selects the destination of their choice.
destination_choice = input("Please select a listed destination: ")

#  The user chooses the amount of nights they wish to stay at a hotel.
num_nights = int(input("How many nights would you like to stay? (1 to 7): "))
while num_nights < 1 or num_nights > 7:
    print("Invalid input. Please enter a number between 1 and 7.")
    num_nights = int(input("How many nights would you like to stay? (1 to 7): "))

#  The user selects the number of car rental days.
rental_days = int(input("How many days do you wish to rent a car?: "))
while rental_days < 1 or rental_days > 7:
    print("Invalid input. Please enter a number between 1 and 7.")
    rental_days = int(input("How many days do you wish to rent a car? (1 to 7): "))

#  The program prints the users choices.
print("Destination Chosen: ", destination_choice)
print("Number of nights: ", num_nights)
print("Number of car rental days: ", rental_days)


def plane_cost(city_flight):
    #  A list of the destinations and their respective flight prices.
    if city_flight == "Milan":
        return 290
    elif city_flight == "Prague":
        return 260
    elif city_flight == "Berlin":
        return 285
    elif city_flight == "Warsaw":
        return 210
    elif city_flight == "Madrid":
        return 300
    else:
        print("Invalid city name.")
        return None


def car_rental(rental_days):
    #  I have entered a standard car rental cost per day.
    car_rental_cost_per_day = 50
    return rental_days * car_rental_cost_per_day


def hotel_cost(num_nights):
    #  Again I have entered a standard hotel cost per night.
    hotel_cost_per_night = 99
    return num_nights * hotel_cost_per_night


def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental


total_cost = holiday_cost(hotel_cost(num_nights), plane_cost(destination_choice), car_rental(rental_days))
print("Your holiday is going to cost: ", total_cost)
