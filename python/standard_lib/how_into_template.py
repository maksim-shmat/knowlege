import string

t = string.Template('$var')
print(t.pattern.pattern)

# Results - regular expression:
#(?P<escaped>\$)  |   # Escape sequence of two delimiters

#(?P<named>(?a:[_a-z][_a-z0-9]*))       |   # delimiter and a Python identifier

#{(?P<braced>(?a:[_a-z][_a-z0-9]*))} |   # delimiter and a braced identifier

#(?P<invalid>)             # Other ill-formed delimiter exprs

# Make new string.Template with change re
import re
import string

class MyTemplate(string.Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}}|
    (?P<invalid>)
    )
    '''

t = MyTemplate('''
        {{{{
        {{var}}
        ''')
print('MATCHES:', t.pattern.findall(t.template))
print('SUBSTITUTED:', t.safe_substitute(var='replacement'))

# Results:
MATCHES: [('{{', '', '', ''), ('', 'var', '', '')]
SUBSTITUTED:
        {{
        replacement

