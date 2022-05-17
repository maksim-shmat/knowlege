"""How many colors is in plotly?"""

from plotly import colors

for key in colors.PLOTLY_SCALES.keys():
    print(key)

Results:
    Greys
    YlGnBu  # Yellow -> Green -> Blue
    Greens
    YlOrRd
    Bluered
    RdBu
    Reds
    Blues
    Picnic
    Rainbow
    Portland
    Jet
    Hot
    Blackbody
    Earth
    Electric
    Viridis
    Cividis
