import random

class Point():
    def basic_init(self):
        self.v = [0,0]
        self.personal_best = [0,0,-999]
        self.x = 0
        self.y = 0
        self.z = 0

    def __init__(self, x, y, z):
        self.basic_init()
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
    def __repr__(self):
        return self.__str__()

class PSO():
    def __init__(self, momentum = 0.8, localSpeed = 0.5, globalSpeed = 0.5):
        self.points = []
        self.global_best = [0,0,-999]
        self.momentum = momentum
        self.c1 = localSpeed
        self.c2 = globalSpeed
        self.random = random.SystemRandom()
    def genPoints(self, numPoints, min_x, max_x, min_y, max_y):
        x = lambda: self.random.uniform(min_x, max_x)
        y = lambda: self.random.uniform(min_y, max_y)
        self.points = [Point(x(), y(), 0) for i in range(0, numPoints)]
        return self.points
    def adjustZ(self, X, Y, Z):
        for p in self.points:
            x = min(range(len(X)), key=lambda i: abs(X[i] - p.x))
            y = min(range(len(Y)), key=lambda i: abs(Y[i] - p.y))
            p.z = Z[x][y] + 0.05
    def step(self, X, Y, Z):
        """
        v[] = v[] + c1 * rand() * (pbest[] - present[]) + c2 * rand() * (gbest[] - present[]) (a)
present[] = persent[] + v[] (b)
        """
        for p in self.points:
            if p.z > self.global_best[2]:
                self.global_best[2] = p.z
                self.global_best[1] = p.y
                self.global_best[0] = p.x
                print('new global best',str(self.global_best))
            if p.z > p.personal_best[2]:
                p.personal_best[2] = p.z
                p.personal_best[1] = p.y
                p.personal_best[0] = p.x
                #print('new personal best',str(p.personal_best),'for p:',p)
        for p in self.points:
            rnd1 = self.random.uniform(0.2, 0.8)
            local_vel =\
            [ self.c1 * rnd1 * (p.personal_best[0] - p.x),
              self.c1 * rnd1 * (p.personal_best[1] - p.y)
            ]
            rnd2 = self.random.uniform(0.2, 0.8)
            global_vel = \
            [ self.c2 * rnd2 * (self.global_best[0] - p.x),
              self.c2 * rnd2 * (self.global_best[1] - p.y)
            ]
            for i in range(len(p.v)):
                p.v[i] = self.momentum * p.v[i] + local_vel[i] + global_vel[i]
            p.x += p.v[0]
            p.y += p.v[1]
        self.adjustZ(X,Y,Z)
