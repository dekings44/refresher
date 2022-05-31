# Working with dictionaries and lists in python


# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected",
#     "Function": "A piece of code that you can easily call over and over again",
#     "Loop": "The action of doing somehting over and over again"
# }

# programming_dictionary["List"] = "a data type that takes any lyst of other data type"


# programming_dictionary["Bug"] = "A moth in your computer"

# for thing in programming_dictionary:

#     print(thing)
#     print(programming_dictionary[thing])

# # Nested dictionaries and lists
# travel_log = {
#     "France": ["Parise", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# travel_log1 = {
#     "France": {"cities_visited": ["Parise", "Lille", "Dijon"]},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"]}
# }

travel_list = [
    {
        "Country": "France",
        "cities_visited": ["Parise", "Lille", "Dijon"],
        "visits": 20
    },
    {
        "Country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "visits": 12
    }
]


def add_new_country(country, time_visited, cities):
    new_country = {}
    new_country['country'] = country
    new_country['visits'] = time_visited
    new_country['cities_visited'] = cities

    travel_list.append(new_country)


add_new_country('Nigeria', 50, ['Lagos', 'Abuja', 'Port Harcourt'])
print(travel_list)