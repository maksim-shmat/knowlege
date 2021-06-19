"""How to create PDF with python."""

pip install FPDF

import numpy as np
import pandas as pd
from fpdf import FPDF
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
pdf.add_page()
pdf.set_font('helvetica', 'bold', 10)
pdf.set_text_color(255, 255, 255)

# inserting images
pdf.image('C:/Users/.../image.png', x = 0, y = 0, w = 210, h = 297)

# Inserting Text and Numbers
pdf.text(x, y, txt)

pdf.set_xy(x, y)
pdf.cell(w, h, txt, border, align, fill)

# Visualizing Data

def bar_chart(creadit, debit, balance):
    
    x = [x[0:6] for (x,y) in balance]
    y1 = [y for (x,y) in credit]
    y2 = [y for (x,y) in debit]
    y3 = [y for (x,y) in balance]

    n = len(x)
    index = np.arange(n)

    fig, ax = plt.subplots(1, 1, figsize=(16,7), dpi= 96)
    plt.plot(x,y3,label='Balance',color='black',linewidth=2.0)
    b1=plt.bar(index-0.0625,y1,label='Credit',color=[(0.06667,0.5647,0.7951)],width=0.125)
    b2=plt.bar(index+0.0625,y2,label='Debit',color=[(1,0.4118,0.4118)],width=0.125)

    plt.xticks(fontsize=14, rotation = 45, horizontalalignment='center',color='darkgrey')
    plt.yticks(fontsize=14,color='darkgrey')
    plt.xlim(-1.0)
    ax.yaxis.grid(alpha=0.5)
    plt.yscale('log', basey=1.00001)

    for axis in [ax.yaxis]:
        axis.set_major_formatter(ScalarFormatter())

    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(0.5)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(0)
    plt.savefig('fig1.png', orientation='portrait',transparent=True, bbox_inches=None, pad_inches=0)

###
def donut_chart(value):

    if value >= 80:
        color = [0.4392,0.6784,0.2784]
    if (value < 80) and (value >= 60):
        color = [0.9569,0.6941,0.5137]
    if value < 60:
        color = [1.0000,0.4118,0.4118]
        
    my_circle_plt.Circle( (0,0), 0.8, color=[0.4902,0.8000,1.0000])

    if value > 0:
        values = [value, 100 - value]
        plt.pie(values,
                vidgeprops = { 'linewidth' : 0, 'edgecolor' : 'white' }, color=[color,[1,1,1]],labeldistance=1.1)

    if value < 0:
        values = [-value, 100 + value]
        plt.pie(values,
                wedgeprops = { 'linewidth' : 0, 'edgecolor' : 'white' }, colors=[color,color_b],labeldistance=1.1, counterclock=False)

    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.savefig('fig2.png',orientation='portrait',transparent=True, bbox_inches=None, pad_inches=0)

###
pdf.output('Automated PDF Report.pdf')
