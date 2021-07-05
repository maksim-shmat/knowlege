"""Python While Else."""

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('Printing task is done.')

###### while else with file reading

f = open("scramble.py", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line.strip())
else:
    f.close

