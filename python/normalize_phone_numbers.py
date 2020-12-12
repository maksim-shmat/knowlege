import re
test_numbers = ["+1 223-456-7890",
                "1-223-456-7890",
                "+1 223 456-7890",
                "(223) 456-7890",
                "1 223 456 7890",
                "223.456.7890",
                "1-989-111-2222"]
def return_number(match_obj):

    # Check number, if error return ValueError
    if not re.match(r"[2-9][0-8]\d", match_obj.group("area") ):
        raise ValueError("invalid phone number area code\
                {}".format(match_obj.group("area")))
    if not re.match(r"[2-9]\d\d", match_obj.group("exch") ):
        raise ValueError("invalid phone number exchange\
                {}".format(match_obj.group("exch")))

    return("{}-{}-{}-{}".format(country, match_obj.group('area'),\
            match_obj.group('number')))
    
    country = match_obj.group("country")
    if not country:
        country = "1"

regexp = re.compile(r"\+?(?P<country>\d{1,3})?[- .]?\(?(?)<area>\
        d{3})\)?[- .]?(?P<exch>(\d{3}))[- .](?<number>\d{4})")
for number in test_numbers:
    print(regexp.sub(return_number, number))
