"""
Calculate the number of points on a spirograph pattern
from the number of teeth on the ring and the number of 
teeth on the wheel.

----
Method

Take ring teeth r and difference between ring and wheel (r-w) 
as d.

Find the lowest common multiple LCM of r and d

Divide LCM by d

This is p, the number of points

Example
ring r = 96
wheel w = 52
d = (r - w) = 44
LCM of 96 and 44 is 1056
1056 / 44 = 24

We calculate 24 points for ring 96 and wheel 52

"""

# no imports required beyond standard ones
import math

rings = [96, 105, 144, 150]

wheels = [24, 30, 32, 40, 42, 45, 48, 52, 56, 60, 63, 72, 75, 80, 84]

for ring in rings:
    for wheel in wheels:
        print(
            f"Ring {ring} Wheel {wheel} Points {int(math.lcm(ring, ring-wheel)/(ring-wheel))}"
        )
    print()
