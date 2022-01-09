"""Matplotlib examples."""

#1

import numpy as np
import matplotlib.pyplot as plt
'''
x = np.linspace(0, 10, 100)
y = (6 * x - 30) ** 2

plt.plot(x, y)
plt.show()


#2 generate 100 numbers from 0 to 10
numbers = 10 * np.random.random(100)
plt.plot(numbers, 'bo')  # bo - blue and dots
plt.show()

#3 Multiple graphs

x = np.linspace(0, 5, 200)
y1 = 2 * x
y2 = x ** 2
y3 = np.log(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()

#4 Subplots, e.g. two graphs

x = np.linspace(0, 5, 200)
y1 = np.sin(x)
y2 = np.sqrt(x)

plt.subplot(211)
plt.plot(x, y1, 'r-')  # red one line

plt.subplot(212)
plt.plot(x, y2, 'g--') # greem line ----

plt.show()

#5 Multiple Plotting Windows

x = np.linspace(0, 7, 186)
y1 = np.sin(x)
y2 = np.sqrt(x)

plt.figure(1)
plt.plot(x, y1, 'r-')

plt.figure(2)
plt.plot(x, y2, 'g--')

plt.show()

#6 Plotting Styles

#from matplotlib import style
#style.use('ggplot')
'''
#7 Setting the titles of out graphs and windows

x = np.linspace(0, 50, 100)
y = np.sin(x)

plt.title("Sine Function")
plt.suptitle("Data Science")
#plt.figure("MyFigure")
plt.grid(True)
plt.plot(x,y)

plt.show()

#8 Labeling Axes
