# Super class or function (Shape)
class Shape:
    def __init__(self,color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
      print(f"It is {self.color}  {'filled' if self.is_filled else 'not_filled'} ")    
 
class Circle(Shape):
    def __init__(self,color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
        

class Squre(Shape):
  def __init__(self,color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
      
class Triangle(Shape):
   def __init__(self,color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


circle = Circle(color = "red", is_filled = True, radius = 5)
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

       
squre = Squre(color = "yellow", is_filled = False, width = 6)
print(squre.color)
print(squre.is_filled)
print(f"{squre.width}cm")

triangle = Triangle(color = "blue", is_filled = True, width = 6 , height = 8)
print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")


circle.describe()
squre.describe()
triangle.describe()



### output ----->
## red True 5cm
## yellow  False  6cm
## blue  True  6cm  8cm
##  It is red  filled 
##  It is yellow  not_filled 
##  It is blue  filled 
