with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(int(row.strip()))

max_temp = max(temperatures)
max_temp = min(temperatures)
mean_temp = sum(temperatures)/len(temperatures)

# we'll need to sort to get the median temp
temperatures.sort()
median_temp = temperatures[len(temperatures)//2]
print("max = {}".format(max_temp))
print("min = {}".format(min_temp))
print("mean = {}".format(mean_temp))
print("median = {}".format(median_temp))

# How many unique temperatures in list?
unique_temp = len(set(temperatures))
print("number of temp - {}".format(len(temperatures)))
print("number of temp - {}".format(unique_temps))
