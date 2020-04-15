from math import fabs, sqrt
from RoadTypes import Point
import random

def point_distance(pointa, pointb):
    return sqrt((pointa.x - pointb.x) ** 2 + (pointa.y - pointb.y) ** 2)


def line(p1, p2):
    A = (p1.y - p2.y)
    B = (p2.x - p1.x)
    C = (p1.x*p2.y - p2.x*p1.y)
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return Point(x,y)
    else:
        return False

def line_cross(line1, line2):
    L1 = line(line1[0], line1[1])
    L2 = line(line2[0], line2[1])

    return intersection(L1, L2)
    
def min_intersect_degree(d1, d2):
    diff = abs(d1 - d2) % 180
    return min(diff, abs(diff-180))

def point_dot(a, b):
    return a.x * b.x + a.y * b.y

def point_projection(a, b, p):
    ap = Point(p.x-a.x, p.y-a.y)
    ab = Point(b.x-a.x, b.y-a.y)
    k = point_dot(ap,ab)/point_dot(ab,ab)
    result = Point(
        a.x + ab.x * k,
        a.y + ab.y * k
    )
    return result

def rand_in_limit(limit):
    # rand in [-limit, limit]
    return limit * (random.random() - 0.5) * 2

def rand_hit_thershold(thershold):
    if random.random() < thershold:
        return True
    else:
        return False