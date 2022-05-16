"""Analize for matplotlib from apple.csv."""

import csv
from datetime import datetime

from matplotlib import pyplot as plt


filename = '/home/jack/django2/knowlege/python/apple.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Read data and date from file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        try:
            high = float(row[2])  # or int
            low = float(row[1])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#print(highs)

# Put data on the diagramm
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# formating the diagramm
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
