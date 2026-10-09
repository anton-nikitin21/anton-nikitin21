# # class Triangle:
# #     """Для треугольников"""
# #     n_dots=3
# #     def __init__(self,a,b,c):
# #         self.a=a
# #         self.b=b
# #         self.c=c
# #         if not (a + b > c and a + c > b and b + c > a):
# #              raise ValueError("triangle inequality does not hold")
# #         self.p = (a + b + c) / 2

# #     def area(self):
# #           return (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5

# # tr_1= Triangle(7,8,9)
# # tr_2=Triangle(4,5,6)

# # square_1 = tr_1.area()
# # square_2 = tr_2.area()

# # class Rectangle(Triangle):
# #     n_dots=4
# #     """Для прямоугоульников"""
# #     def __init__(self, a, b):
# #         self.a=a
# #         self.b=b
# #     def area(self):
# #          return self.a*self.b
    
# # rc1=Rectangle(5,4)
# # print(rc1.area())

# class BaseFigure:
#     """Для всех фигур"""

#     n_dots = None

#     def __init__(self):
#         self.validate()

#     def area(self):
#         raise NotImplementedError("area() без реализации")
    
#     def validate(self):
#         raise NotImplementedError("validate() без реализации")

# class Triangle(BaseFigure):
#     """Для треугольников"""
#     n_dots = 3

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.p = (a + b + c) / 2
#         super().__init__()

#     def validate(self):
#         if not (self.a + self.b > self.c and
#                 self.a + self.c > self.b and
#                 self.b + self.c > self.a):
#             raise ValueError("triangle inequality does not hold")
#         return self.a, self.b, self.c

#     def area(self):
#         return (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5


# class Rectangle(BaseFigure):
#     """Для прямоугоульников"""
#     n_dots = 4

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         super().__init__() 

#     def validate(self):
#         return self.a, self.b

#     def area(self):
#         return self.a * self.b


# tr_1=Triangle(3,4,5)
# print(tr_1.validate(),tr_1.area())

# rc_1=Rectangle(3,4)
# print(rc_1.validate(),rc_1.area())

# class Circle(BaseFigure):
#     """Для кругов"""
#     n_dots = float('inf')

#     def __init__(self,r):
#         self.r=r
#         super().__init__()
#     def validate(self):
#         pass

#     def area(self):
#         return 3.14*self.r**2
    
# cl=Circle(4)
# print(cl.area())


class Vector:
    def __init__(self, coords):
        self.coords = coords

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self.coords) != len(other.coords):
            raise ValueError(
                f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}"
            )

        new_coords = [a + b for a, b in zip(self.coords, other.coords)]
        return Vector(new_coords)
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ValueError(
                    f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}"
                )
            return sum(a * b for a, b in zip(self.coords, other.coords))

        if isinstance(other, (int, float)):
            return Vector([a * other for a in self.coords])

        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.coords == other.coords

    def __abs__(self):
        return sum(x*x for x in self.coords) ** 0.5

    def __repr__(self):
        return f"Vector({self.coords})"
    
    def __str__(self):
        return str(self.coords)


print(abs(Vector([-12, 5])))



