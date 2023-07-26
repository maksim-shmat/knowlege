"""OOP Dataclasses about."""

#1

from dataclasses import dataclass

@dataclass
class Body:
    '''Class to represent a phisical body.'''
    name: str
    mass: float = 0.  # kg
    speed: float = 1.  # m/s

    def kinetic_energy(self) -> float:
        return (self.mass * self.speed ** 2) / 2

body = Body('Ball', 19, 3.1415)
print(body.kinetic_energy())  # 93.755711375 Joule
print(body)  # Body(name='Ball', mass=19, speed=3.1415)

93.755711375
Body(name='Ball', mass=19, speed=3.1415)
