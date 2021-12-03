"""Canvas about."""

g = Gui()

canvas = g.ca(width=500, height=500)    # make a canvas

canvas.config(bg='white')    # make canvas background, colors: white, black,
                             # red, green, blue, cyan, yellow, magenta

item = canvas.circle([0,0], 100, fill='red') # (centre, radius, color)

item.convig(fill='yellow', outline='orange', width=10)

canvas.rectangle([[0,0][200, 100]], fill='blue', outline='orange', width=10)

# make oval
canvas.oval([[0,0], [200,100]],outline='orange', width=10)

# make corner
canvas.line([[0,100], [100, 200], [200, 100]], width=10)

# make polygon
canvas.polygon([[0,100], [100, 200], [200, 100]], fill='red', outline='orange', width=10)

# make an entry
entry = g.en(text = 'Text to default')

# make a text vidget
text = g.te(width=100, height=5)

# insert text into vidget
text.insert(END, 'string of text')

####### make an event

def make_circle(event):
    pos = ca.canvas_cords([event.x, event.y])
    item = ca.circle(pos, 5, fill='red')

###### make drag-and-drop

def Dragable(item):
    def __init__(self):
        """Start event coordinates."""
        self.canvas = item.canvas
        self.tag = item.tag
        self.bind('<Button-3>', self.select) # push button
        self.bind('<Bs-Motion>', self.drag) # moving button
        self.bind('<Release-3>', self.drop) # repush button

    def select(self):
        """Change afterward to yellow."""
        self.dragx = event.x
        self.dragy = event.y
        self.fill = self.cget('fill')
        self.config(fill='yellow')
    
    def drag(self):
        """Push."""
        dx = event.x - self.dragx
        dy = event.y - self.dragy
        self.dragx = event.x
        self.dragy = event.y
        self.move(dx, dy)

    def drop(self):
        """Repush."""
        self.config(fill=self.fill)

    def make_circle(event):
        pos = ca.canvdas_coords([event.x, event.y])
        item = ca.circle(pos, 5, fill='red')
        item = Draggable(item)
