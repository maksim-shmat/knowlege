"""How six dices is True."""

from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

# Make six dices D6

dice_1 = Dice()
dice_2 = Dice()
dice_3 = Dice()
dice_4 = Dice()
dice_5 = Dice()
dice_6 = Dice()

# Make a line of throwings with saving of results into a list.
results = []
for roll_num in range(1001):
    result = dice_1.roll() + dice_2.roll() + dice_3.roll() + dice_4.roll() + dice_5.roll() + dice_6.roll()
    results.append(result)

# Analitics of results
frequencies = []
max_results = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides + dice_4.num_sides + dice_5.num_sides + dice_6.num_sides
for value in range(6, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualisation of results with plotly
x_values = list(range(6, max_results+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling six D6 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='six_d6.html')

print(frequencies)
