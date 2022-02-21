"""A sample template system."""

import fileinput, re

# Matches fields enclosed in square brackets:
field_pat = re.compile(r'\[(.+?)\]')

# We'll collect variables in this:
scope = {}

# This is used in re.sub:
def replacement(match):
    code = match.group(1)
    try:
        # if the field can be evaluated, return it:
        return str(eval(code, scope))
    except SynatxError:
        # Otherwise, execute the assignment in the same scope ... exec code in scope
        # ...and return an empty string:
        return ''
    # Get all the text as a single string:
    # (There are other ways of doing this:
    lines = []
    for line in fileinput.input():
        lines.append(line)
    text = ''.join(lines)
    # Substitute all the occurrences of the field pattern:
    print(field_pat.sub(replacement, text))

    text = ''
    for line in fileinput.input():
        text += line
    print(field_pat.sub(replacement, text))

