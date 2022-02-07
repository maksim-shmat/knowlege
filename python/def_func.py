"""All about def in examples."""
'''
#1

def hello(name):
    return 'Hello, ' + name + '!'

print(hello('world'))  # Hello, world
print(hello('Jackie'))  # Hello, Jackie

#2

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

#2a with *args

def store(data, *full_names):  # *
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

#3 more *args, **kwargs

def story(**kwds):
    return 'Once upon a time, there was a '\
            '{job} calles {name}.'.format_map(kwds)

def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
        return pow(x, y)

    def interval(start, stop=None, step=1):
        'Imitates range() for step > 0'
        if stop is None:  # if the stop is not supplied shuffle the parameters
            start, stop = 0, start
        result = []
        i = start  # We start counting at the start index
        while i < stop:  # Unitl the index reaches the stop index
            result.append(i)  # append the index to the result
            i += step  # increment the index with the step (>0)
        return result

#4

def combine(parameter): print(parameter + external)  # Shrubberry

external = 'berry'
combine('Shrub')

#5 for global

def combine(parameter):
    print(parameter + globals()['parameter'])  # Bilberry

parameter = 'berry'
combine('Bil')
'''
#5 Binary search

def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)

seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)  # [4, 8, 34, 67, 95, 100, 123]
print(search(seq, 34))  # 2
print(search(seq, 100))  # 5

#6 
