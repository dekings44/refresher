# Working with dictionaries and lists in python


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing somehting over and over again"
}

programming_dictionary["List"] = "a data type that takes any lyst of other data type"


programming_dictionary["Bug"] = "A moth in your computer"

for thing in programming_dictionary:

    print(thing)
    print(programming_dictionary[thing])