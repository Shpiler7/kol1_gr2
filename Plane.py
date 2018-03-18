class Plane(object):
    angle = 90
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def tiltCorrection(self):
        self.angle = 90
    def currOrientation(self):
        print(self.angle)
   