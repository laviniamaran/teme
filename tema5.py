from math import cos, acos, degrees, radians


class AngleOutOfRande(Exception):
    def __init__(self, angle):
        self.angle = angle

    def __str__(self):
        return f'{self.angle} is not in rage (0, 180)'


class UndefinedAngle(Exception):
    def __init__(self, angle):
        self.angle = angle

    def __str__(self):
        return f'{self.angle} is not defined'


class SizeOutOfRande(Exception):
    def __init__(self, meters):
        self.meters = meters

    def __str__(self):
        return f'{self.meters} is smaller than 0'


class UndefinedSide(Exception):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'{self.side} is not defined'


class Triangle():

    def __init__(self, A=1, B=1, C=1, AB=60, BC=60, AC=60):
        self.A = A
        self.B = B
        self.C = C
        self.AB = radians(AB)
        self.BC = radians(BC)
        self.AC = radians(AC)

    def __str__(self):
        return f"A= {round(self.A, 2)}, B= {round(self.B, 2)}, C= {round(self.C, 2)}, AB= {round(degrees(self.AB), 2)}, BC= {round(degrees(self.BC), 2)}, AC= {round(degrees(self.AC), 2)}"

    def modify_angle(self, angle, adegrees):

        if (angle == "AB"):
            if (adegrees + degrees(self.AB) > 180 or adegrees + degrees(self.AB) < 0):
                raise AngleOutOfRande(adegrees + degrees(self.AB))
            else:
                self.AB += radians(adegrees)
                self.C = (self.A ** 2 + self.B ** 2 - 2 * self.A * self.B * cos(self.AB)) ** (1 / 2)
                self.BC = acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C))
                self.AC = acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A))


        elif (angle == "BC"):
            if (adegrees + degrees(self.BC) > 180 or adegrees + degrees(self.BC) < 0):
                raise AngleOutOfRande(adegrees + degrees(self.BC))
            else:
                self.BC += radians(adegrees)
                self.A = (self.B ** 2 + self.C ** 2 - 2 * self.B * self.C * cos(self.BC)) ** (1 / 2)
                self.AC = acos((self.A ** 2 + self.C ** 2 - self.B ** 2) / (2 * self.A * self.C))
                self.AB = acos((self.A ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B))


        elif (angle == "AC"):
            if (adegrees + degrees(self.AC) > 180 or adegrees + degrees(self.AC) < 0):
                raise AngleOutOfRande(adegrees + degrees(self.AC))
            else:
                self.AC += radians(adegrees)
                self.B = (self.A ** 2 + self.C ** 2 - 2 * self.A * self.C * cos(self.AC)) ** (1 / 2)
                self.AB = acos((self.A ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B))
                self.BC = acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C))

        else:
            raise UndefinedAngle(angle)

    def modify_side(self, side, meters):

        if (side == "A"):
            if (meters + self.A <= 0):
                raise SizeOutOfRande(meters + self.A)
            else:
                self.B = ((self.A + meters) / self.A) * self.B
                self.C = ((self.A + meters) / self.A) * self.C
                self.A += meters

        elif (side == "B"):
            if (meters + self.B <= 0):
                raise SizeOutOfRande(meters + self.B)
            else:
                self.A = ((self.B + meters) / self.B) * self.A
                self.C = ((self.B + meters) / self.B) * self.C
                self.B += meters

        elif (side == "C"):
            if (meters + self.C <= 0):
                raise SizeOutOfRande(meters + self.C)
            else:
                self.B = ((self.C + meters) / self.C) * self.B
                self.A = ((self.C + meters) / self.C) * self.A
                self.C += meters

        else:
            raise UndefinedSide


# 10P
# Create an object from your class with default constructor values and modify angle AB by +30 degrees and side A by +1.5

triangle = Triangle()
print(triangle)
triangle.modify_angle("AB", 30)
print(triangle)
triangle.modify_side("A", 1.5)
print(triangle)