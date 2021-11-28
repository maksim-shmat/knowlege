"""Pickle serialization about."""

######1 Python pichling or serializing

import pickle

marks = {'Alex': 87, 'Lenin': 98, 'Kuwabara': 90}
picklefile = open('marks', 'wb')
pickle.dump(marks, picklefile)
picklefile.close()

######2 Python unpacking or deserializing

import pickle

picklefile = open('marks', 'rb')
marks = pickle.load(picklefile)
picklefile.close()
print(marks)
print(type(marks))

######
