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
    def __init__(self):
        self.points = []
        self.global_best = [0,0,-999]
        self.c1 = 0.2
        self.c2 = 0.6
    def genPoints(self, numPoints, min_x, max_x, min_y, max_y):
        self.points = [Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y), 0) for i in range(0, numPoints)]
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
        global_best = -999
        for p in self.points:
            if p.z > global_best:
                global_best = p.z
            if p.z > p.personal_best[2]:
                p.personal_best[2] = p.z
        for p in self.points:
            rnd1 = random.uniform(0.1, 0.9)
            local_vel =\
            [ self.c1 * rnd1 * (p.personal_best[0] - p.x),
              self.c1 * rnd1 * (p.personal_best[1] - p.y)
            ]
            rnd2 = random.uniform(0.1, 0.9)
            global_vel = \
            [ self.c2 * rnd2 * (self.global_best[0] - p.x),
              self.c2 * rnd2 * (self.global_best[1] - p.y)
            ]
            p.v = p.v + local_vel + global_vel
