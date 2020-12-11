re.match(r": (?P<phone>(\+\d{2}-)?(\d\d\d-)?\d\d\d\d)", ":\
        +01-111-222-3333")
or

re.match(r": (?P<phone>(\+\d{2}-)?(\d{3}-\d{4})", ":\
        +01-111-222-3333")

for country codes insert from 1 to 3 numbers

re.match(r": (?P<phone>(\+\d{1,3}-)?(\d{3}-\d{4})", ":\
        +011-111-222-3333")
