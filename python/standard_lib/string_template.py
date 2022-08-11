"""Formating strings with templates."""

import string

values = {'var': 'foo'}

t = string.Template("""
        Variable        : $var
        Escape          : $$  # double $ for excape from spec charactre
        Variable in text: ${var}iable
        """)
print('TEMPLATE:', t.substitute(values))

# Results:
#TEMPLATE: 
#        Variable        : foo
#        Escape          : $
#        Variable in text: fooiable
  
#2
s = """
Variable           : %(var)s
Escape             : %%  # double % for escape
Variable in text   : %(var)siable
"""
print('INTERPOLATION:', s % values)

# Results:
#INTERPOLATION: 
#Variable           : foo
#Escape             : %
#Variable in text   : fooiable

#3
f = """
Variable           : {var}
Escape             : {{}}  # double {} for escpape spec character
Variable in text   : {var}iable
"""
print('FORMAT:', f.format(**values))

# Results:
#FORMAT:
#Variable           : foo
#Escape             : {}
#Variable in text   : fooiable
