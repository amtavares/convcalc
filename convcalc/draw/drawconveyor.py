import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import math

class Pulley():
    def __init__(self, x, y, r, name):
        self.radius = r
        self.x = x
        self.y = y
        self.name = name

p1 = Pulley(0, 0, 5, 'P1')
p2 = Pulley(10, 0, 2, 'P2')

pulleys =[]
pulleys.append(p1)
pulleys.append(p2)

# ========================================
def calc_h(r, d):
    h = math.sqrt(d*d - r*r)
    return h
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def calc_beta(h,d):
    sinbeta = h * math.sin(deg2rad(90))/d
    beta = math.asin( sinbeta )
    return beta

def deg2rad(deg):
    return deg*math.pi/ 180 

def rad2deg(rad):
    return rad*180/math.pi

def angle_from_dist(x1,y1,x2,y2, r1):
    pass

# ========================================

x1 = p1.x
y1 = p1.y
x2 = p2.x
y2 = p2.y
r1 = p1.radius
r2 = p2.radius

d = distance(x1,y1,x2,y2)
print('d:{}'.format(d))
h = calc_h(r1, d)
print('h:{}'.format(h))
beta = calc_beta(h, d)
print('beta:{}'.format(beta))


# ========================================
fig, ax = plt.subplots()

patches = []
for p in pulleys:
    circle = Circle((p.x, p.y), p.radius)
    patches.append(circle)

colors = 100*np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(np.array(colors))
ax.add_collection(p)
fig.colorbar(p, ax=ax)

plt.show()