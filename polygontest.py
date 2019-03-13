from matplotlib import pyplot as plt
from shapely.geometry import LinearRing, Polygon, Point



# 1: valid ring

#poly = Polygon([(0, 0), (0, 2), (1, 1),
#                (2, 2), (2, 0), (1, 0.8), (0, 0)])
#x,y = poly.exterior.xy

ring = LinearRing([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 0.8), (0, 0)])
x, y = ring.xy

fig = plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
ax.plot(x, y)

ring = LinearRing([(3,3),(9,3),(9,200),(3,200)])
x, y = ring.xy

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title('Polygon Edges')

polygon = Polygon([(3,3),(9,3),(9,200),(3,200)])
p = Point([3,3])

print(p.within(polygon))
