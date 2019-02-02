
# Investigating multiple reflections of a laser beam
# Problem 144 
# https://projecteuler.net/problem=144
# 

import math
import logging
logger = logging.getLogger('p144')

def SolveQuadratic(a, b, c):
    assert(a != 0)
    t = math.sqrt(b*b-4*a*c)
    return ((-b-t)/2/a, (-b+t)/2/a)

class Beam:
    def __init__(self, point, direction):
        x0, y0 = point
        dx, dy = direction
        d = math.sqrt(dx*dx+dy*dy)
        assert(d>0)
        dx, dy = dx/d, dy/d
        self.point = (x0, y0)
        self.direction = (dx, dy)

    def reflect(self, N):
        # R = 2(N.L)N - L
        nx, ny = N
        dn = math.sqrt(nx*nx+ny*ny)
        nx, ny = nx/dn, ny/dn
        dx, dy = self.direction
        nl = nx*dx + ny*dy
        r = (dx-2*nl*nx, dy-2*nl*ny)
        return r
    
class Ellipse:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def hit(self, b):
        # calculate the point the beam hit with ellipse
        x0, y0 = b.point
        dx, dy = b.direction
        if dy == 0:
            y = y0
            x = math.sqrt((self.c-self.b*y*y)/self.a)
            if dx < 0:
                x = -x
        elif dx == 0:
            x = x0
            y = math.sqrt((self.c-self.a*x*x)/self.b)
            if dy < 0:
                y = -y
        else:
            d = dy/dx
            a_ = self.a + self.b*d*d
            b_ = self.b*2*d*(y0-d*x0)
            c_ = self.b*(d*x0-y0)**2-self.c
            r1, r2 = SolveQuadratic(a_, b_, c_)
            if dx < 0:
                x = r1
            else:
                x = r2
            y = d*x-d*x0+y0
        return (x, y)

    def getNorm(self, point):
        x, y = point
        if x == 0:
            return (0, -y)
        else:
            return (-x, -self.b*y/self.a)

def main(args):

    if args.test:
        N = 10
    else:
        K = 1000
        N = K*K

    ellipse = Ellipse(4, 1, 100)
    b = [Beam((0.0, 10.1), (1.4, -19.7))]
    h = []
    n = []

    answer = 0
    for i in range(N):
        h.append(ellipse.hit(b[i]))
        x, y = h[i]
        if -0.01 <= x and x <= 0.01 and y > 0:
            answer = i
            break
        #logger.debug("hit:{}".format(h[i]))
        n.append(ellipse.getNorm(h[i]))
        #logger.debug("Norm:{}".format(n[i]))
        r = b[i].reflect(n[i])
        #logger.debug("reflect:{}".format(r))
        b.append(Beam(h[i], r))

    logger.debug(h)

    logger.info("answer: {}".format(answer))
