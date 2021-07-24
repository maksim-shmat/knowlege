"""Count percent from number."""

# area_of_country("Russia", 17098242) -> "Russia is 11.48% of the total world's landmass"

def area_of_country(name, area):
    return "{} is {:.2%} of the total world's landmass".format(name, area / 148940000)

name = "Russia"
area = 17098242

######

def area_of_country(country: str, area: int) -> str:
    percent = round(area / 1489400, 2)
    return f"{country} is {percent} % of the total world's landmass"


