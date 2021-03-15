""" Methods Arguments: Default, optional, *args, **kwargs."""

###### Python method definition and call syntax with * and **

def address(city,state,country):
    print(city)
    print(state)
    print(country)

address('San Diego','CA','US')
address('Vancouver','BC','US')

us_address = ('San Diego','CA','US')
address(*us_address)

canada_address = {'country':'US','city':'San Diego','state':'CA'}
address(**canada_address)

###### Python method optional arguments

def address_with_default(city,state,country='US'):
    print(city)
    print(state)
    print(country)

address_with_default('San Diego','CA')
address_with_default('Vancouver','BC','CA')
address_with_default(**{'state':'CA','city':'San Diego'})

#####
