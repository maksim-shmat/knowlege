"""Matplotlib examples."""

'''
#1

import numpy as np
import matplotlib.pyplot as plt

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

# check available styles
>>> import matplotlib.pyplot as plt
>>> plt.style.available
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
plt.style.use('seaborn')
or
#from matplotlib import style
#style.use('ggplot')

#7 Setting the titles of out graphs and windows, and labeling axes

x = np.linspace(0, 50, 100)
y = np.sin(x)

plt.title("Sine Function")
plt.suptitle("Data Science")
#plt.figure("MyFigure")
plt.grid(True)
plt.plot(x,y)
plt.xlabel("x-values")
plt.ylabel("y-values")

plt.show()

#8 Legends

x = np.linspace(10, 50, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.log(x/3)

plt.plot(x, y1, 'b-', label="Sine")  # blue
plt.plot(x, y2, 'r-', label="Cosine")  # red
plt.plot(x, y3, 'g-', label="Logarithm")  # green
plt.legend(loc = 'upper left')

plt.show()
# plt.savefig("functions.png")  # save it

#9 Histograms

mu, sigma = 172,4

x = mu + sigma * np.random.randn(10000)
plt.hist(x, 100, density = True, facecolor = "blue")
plt.xlabel("Height")
plt.ylabel("Probability")
plt.title("Height of Students")
plt.text(160, 0.125, "greec.mu.char = 172, greec.sigma.char = 4")
plt.axis([155, 190, 0, 0.15])
plt.grid(True)

plt.show()

#10 Bar chart

bob = (90, 67, 87, 76)
charles = (80, 80, 47, 66)
daniel = (40, 95, 76, 89)

skills = ("Python", "Java", "Networking", "Machine Learning")

width = 0.2
index = np.arange(4)
plt.bar(index, bob, width=width, label="Bob")
plt.bar(index + width, charles, width=width, label="Charles")
plt.bar(index + width * 2, daniel, width=width, label="Daniel")

plt.xticks(index + width, skills)
plt.ylim(0, 120)
plt.title("IT Skill Levels")
plt.ylabel("Skill Level")
plt.xlabel("IT Skill")
plt.legend()

plt.show()

#11 Pie chart

labels = ('American', 'German', 'French', 'Other')
values = (47, 23, 20, 10)
plt.pie(values, labels=labels, autopct="%.2f%%", shadow=True)
plt.title("Student Nationalities")
plt.show()

#12 Scatter plots

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x,y)
plt.show()

#13 Boxplot diagrams

mu, sigma = 172,4

values = np.random.normal(mu, sigma, 200)

plt.boxplot(values)
plt.title("Student's Height")
plt.ylabel("Height")
plt.show()

#14 3d plots

from mpl_toolkits import mplot3d

z = np.linspace(0, 20, 100)
x = np.sin(z)
y = np.cos(z)
ax = plt.axes(projection = '3d')
ax.plot3D(x, y, z)

plt.show()

#15 Surface plots

from mpl_toolkits import mplot3d

ax = plt.axes(projection = '3d')

def z_function(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)
Z = z_function(X,Y)

ax.plot_surface(X,Y,Z)

plt.show()

#16 Matplotlib with Pandas

import pandas as pd
import matplotlib.pyplot as plt

data = {'Name': ['Anna', 'Bob', 'Charles', 'Daniel', 'Evan', 'Fiona', 'Gerald', 'Henry', 'Intuition'],
        'Age': [ 17, 28, 35, 23, 32, 89, 76, 110, 11],
        'Height': [123, 321, 234, 32, 35, 534, 234, 22, 2]}

df = pd.DataFrame(data)
df.sort_values(by = ['Age', 'Height'])
df.hist()
df.plot()

plt.plot(df['Age'], 'bo')  # dots on the line if use with df.plot() 
plt.show()

#17 squares in a line

import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set header and marks of axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

plt.show()
'''
# 18 squares with dots

import matplotlib.pyplot as plt


x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set header and mark of axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set font value for ticks on the axes.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
