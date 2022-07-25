"""Count air_mass.

In astronomy air mass is a measure of the amount of atmosphere between the
observer and the object bing observed. It is a function of the zenith angle
(the angle between the line of sight a vertical) and the altitude of the
observer. It is defined as teh integral of the atmospheric density along
the line of sight and is usually expressed relative to the air mass at zenith.
Thus, looking straight up gives an air mass of one (regardless of observer's
altitude) and viewing at any zenith angle greater than zero gives higher
values.

You will need to integrate p(h(a,z,x)) where p(h) is the atmospheric density
for a given height above sea level, and h(a,z,x) is the height above sea level
for a point at distance x along the line of sight. Determining this last
function requires some trigonometry.

For this task you can assume:
    - The density of Earth's atmosphere is proportional to exp(-a/8500 meters)
    - The Earth is a perfect sphere of radius 6731 km

Task:
    - Write a function that calculates the air mass for an observer at <a> given
    altitude a above sea level and zenith angle <z>.
    - Show the air mass for zenith angles 0 to 90 in steps of 5 degrees for an
    observer at sea level.
    - Do the same for the NASA SOFIA infrared telescope, which has a cruising
    altitude of 13,700 meters (about 8.3 miles),
    it flies in a specially retrofitted Boing 747 about four flights a week.
"""

from math import sqrt, cos, exp

DEG = 0.0174532925199432957592369236907684886127134  # degree to radiants
RE = 6371000  # Earth radius in meters
dd = 0.001  # intergrate in this fraction of the distance already covered
FIN = 10000000  # intergrate only to a height of 10000km, effectively ininity

def rho(a):
    """The density of air as a function of height above sea level."""
    return exp(-a / 8500.0)

def height(a, z, d):
    """
    a = altitude of observer
    z = zenith angle (in degrees)
    d = distance along line of sight
    """
    return sqrt((RE + a)**2 + d**2 - 2 * d * (RE + a) * cos((180 -z) * DEG)) - RE

def column_density(a, z):
    """Integrates density along the line of sight."""
    dsum, d = 0.0, 0.0
    while d < FIN:
        delta = max(dd, (dd)*d)  # adaptive step size to avoid it taking forever:
        dsum += rho(height(a, z, d + 0.5 * delta)) * delta
        d += delta
    return dsum

def airmass(a, z):
    return column_density(a, z) / column_density(a, 0)

print('Angle            0 m             13700 m/n', '-' * 36)
for z in range(0, 91, 5):
    print(f"{z: 3d}        {airmass(0, z): 12.7f}    {airmass(13700, z): 12.7f}")
