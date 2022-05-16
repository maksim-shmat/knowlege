"""For analitics with plotly and matplotlib, from dice.py."""

from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice


# Make two dices D6
dice_1 = Dice()  # for D10 write Dice(10), D6(default) inf dice.py
dice_2 = Dice()

# Make a dice D6.
#dice = Dice()

# Make a line of throwings with saving of results into a list.
results = []
for roll_num in range(1000):
    #result = dice.roll()  # for one dice
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# Analitics of results.
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
#for value in range(1, dice.num_sides+1):  # for one dice
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualisation of results with plotly
#x_values = list(range(1, dice.num_sides+1))  # for one dice
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

#x_axis_config = {'title': 'Result'}  # for one dice
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='two_d6.html')

print(frequencies)
