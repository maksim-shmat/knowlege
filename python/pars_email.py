"""Regular expression parser email: jill.eml."""

# $ python3 parse_email.py jill.eml
# Search name from How sent email

import fileinput, re

pat = re.compile('From:(.*)<.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m:
        print(m.group(1))  # not work, but why?

pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+',re.IGNORECASE)
addresses = set()
for line in fileinput.input():
    for address in pat.findall(line):
        addresses.add(address)
for address in sorted(addresses):
    print(address)

# If need find the addres in header of file use fileinput.close() if you find empty line
# Alternatively you can use fileinput.nextfile() to start processing the next file, if there is more than one.
