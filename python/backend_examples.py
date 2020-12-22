""" Tuples, lists and dictionaries."""

"""
# 069
# Create a tuple containing the names of five countries and display the whole
# tuple. Ask the user to enter one of the countries that have been shown to 
# them and then display the index number(i.e. position in the list) of that
# item in the tuple.

country_tuple = ("France", "England", "Spain", "Germany", "Australia")
print(country_tuple)
print()
country = input("Please enter one of the countries from above: ")
print(country, "has index number", country_tuple.index(country))

# 070
# Add to program 069 to ask the user to enter a number and display the 
# country in that position.

country_tuple = ("France", "England", "Spain", "Germany", "Australia")
print(country_tuple)
print()
country = input("Please enter one of the countries from above: ")
print(country, "has index number", country_tuple.index(country))
print()
num = int(input("Enter a number between 0 and 4: "))
print(country_tuple[num])
"""
# 071
# Create a list of two sports. Ask the user what their favourite sport is
# and add this to the end of the list. Sort the list and display it.

sports_list = ["tennis", "football"]
sports_list.append(input("What is your favourite sport? "))
sports_list.sort()
print(sports_list)

# 072

