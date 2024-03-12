# Initialise the flight price by city, hotel cost per night and car rental cost per day
barcelona_flight = 65.0
london_flight = 107.9
new_york_flight = 359
paris_flight = 258.5
hotel_per_night = 56.45
car_rental_per_day = 29.89


# Function to calculate the hotel cost
def hotel_cost(num_nights: int) -> float:
    return num_nights * hotel_per_night


# Function to calculate the car rental cost
def car_rental(rental_days: int) -> float:
    return rental_days * car_rental_per_day


# Function to calculate the plane cost
def plane_cost(city_flight: str) -> float:
    if city_flight == 'Barcelona':
        return barcelona_flight
    elif city_flight == 'London':
        return london_flight
    elif city_flight == 'Paris':
        return paris_flight
    elif city_flight == 'New York':
        return new_york_flight
    else:
        raise Exception("Invalid flight!")


# Ask for the city the user will be flying to, number of night they will be staying and the number
# of days they will be hiring a car
city_flight = input("Which city are you flying to? Please choose from Barcelona, London, New York and Paris: ")
num_nights = int(input("How many nights will you stay at the hotel? "))
rental_days = int(input("How many days will you rent the car? "))

# Holiday cost is the sum of plane, hotel and car rental cost.
holiday_cost = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)
print(f'The total holiday cost is {holiday_cost: .2f}')



