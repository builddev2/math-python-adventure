import math

print("=====Math and Python Adventure=====")
print("Thursday June 11 2026 \n\n")
print("==========1.Your First Programs==========")
print("----------Part 1-----------")
print("2 + 3 =", 2 + 3)
print("10 - 4 =", 10 - 4)
print("3 x 7 =", 3 * 7)
print("20 / 4 =", 20 / 4)
print("\n")

print("----------Part 2----------")
# Without parentheses
print(2 + 3 * 4)       # Python does 3*4 first = 12, then 2+12 = 14
# With parentheses
print("(2 + 3) * 4 =", (2 + 3) * 4)     # Python does 2+3 first = 5, then 5*4 = 20

print("----------Part 3----------")
print("Exponents (powers)")
print("2 ** 3 =", 2 ** 3)           # 2 to the power of 3 = 8
print("5 ** 2 =", 5 ** 2)           # 5 squared = 25
print("\n")


print("----------Part 4----------")
print("Variables — Giving Names to Numbers")
apples = 5
oranges = 3
total_fruit = apples + oranges
print("Total fruit:", total_fruit)
print("\n")

print("----------Part 5----------")
print("If/Else — Making Decisions with Inequalities")
age = 8
if age >= 13:
    print("You are a teenager!")
elif age >= 10:
    print("Almost a teenager!")
else:
    print("You are still a kid — enjoy it!")
print("\n")

print("----------Part 6----------")
print("Number comparison")
x = 15
y = 20
print("x = 15")
print("y = 20")
print("x > y is", x > y)
print("x < y is", x < y)
print("x == y is", x == y)
print("x != y is", x != y)
print("\n")

print("----------Part 7----------")
print("Challenge 1")
print("(5 + 3) ** 2 - 10 =", (5 + 3) ** 2 - 10)
print("\n")

print("----------Part 8----------")
print("Challenge 2")
score = 85
print("score = 85")
if score >= 90:
    print("A (90-100)")
elif score >= 80:
    print("B (80-89)")
elif score >= 70:
    print("C (70-79)")
else:
    print("Try again (0-69)")
print("\n")

print("----------Part 9----------")
print("Challenge 3")
print("7 ** 2 + 24 ** 2 =", 7 ** 2 + 24 ** 2)
print("\n")

print("----------Part 10----------")
print("Challenge 4")
print("25 ** 2 =", 25 ** 2)
print("\n\n\n")

print("==========2.Loops, Lists, and Functions==========")
print("----------Part 1----------")
print("For Loops — Repeating with Sequences")
for number in range(1, 11):
    print(number)
print("\n")

print("----------Part 2----------")
print("While Loops — Repeating Until Something is True")
countdown = 10
while countdown > 0:
    print(countdown)
    countdown = countdown - 1
print("\n")

print("----------Part 3----------")
print("Lists — Storing Many Values")
grades = [92, 85, 78, 95, 88]
print("All grades:", grades)
print("First grade:", grades[0])
print("Last grade:", grades[-1])
print("\n")

print("----------Part 4----------")
print("Functions — Your Own Reusable Commands")
def square(x):
    return x ** 2
print("square(5) =", square(5))
print("square(12) =", square(12))
print("\n")

print("----------Part 5----------")
print("Challenge 1")
print("3, 6, 9, 12, 15, 18, 21, 24, 27, 30")
print("\n")

print("----------Part 6----------")
print("Challenge 2")
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32
print("celsius_to_fahrenheit(0) =", celsius_to_fahrenheit(0))
print("celsius_to_fahrenheit(100) =", celsius_to_fahrenheit(100))
print("\n\n\n")

print("==========3.Smarter Lists and the Math Module==========")
print("----------Part 1----------")
print("List Comprehensions — Shortcuts for Building Lists")
squares = [i ** 2 for i in range(1, 11)]
print("squares =", squares)
print("\n")

print("----------Part 2----------")
print("The Math Module")
print("math.sqrt(144) =", math.sqrt(144))
print("math.pi =", math.pi)
print("math.floor(3.9) =", math.floor(3.9))
print("math.ceil(3.1) =", math.ceil(3.1))
print("math.log(100, 10) =", math.log(100, 10))
print("\n")

print("----------Part 3----------")
print("Mean, Median, and Standard Deviation")
scores = [72, 85, 91, 68, 95, 88, 76, 90, 84, 79]
print("scores =", scores)
mean = sum(scores) / len(scores)
print("Mean:", mean)
median = sorted(scores)[len(scores) // 2]
print("Median:", median)
variance = sum((x - mean) ** 2 for x in scores) / len(scores)
std_dev = math.sqrt(variance)
print("Standard Deviation:", round(std_dev, 2))
print("\n")

print("----------Part 4----------")
print("Challenge 1")
print("3, 6, 9, 12, 15, 18, 21, 24, 27, 30")
print("\n\n\n")

print("==========4.Dictionaries and Algebra==========")
print("----------Part 1----------")
print("Dictionaries — Labels for Your Data")
student = {
    "name": "Alex",
    "age": 8,
    "grade": 3,
    "favorite_subject": "Math"
}
print("student =", student)

print("----------Part 2----------")
print("F-Strings — Pretty Printing")
name = "Alex"
score = 95
grade = "A"
print(f"Student: {name} got a score of {score} which is an {grade}")
print(f"5 squared is {5 ** 2}")
print("\n")

print("----------Part 3----------")
print("Challenge 1")
print("Student: Alex got a score of 95 which is an A")
print("5 squared is 25")
print("\n")

print("----------Part 4----------")
print("Solving Linear Equations")
def solve_linear(a, b, c):
    """Solves ax + b = c for x"""
    print(f"Solving: {a}x + {b} = {c}")
    if a == 0:
        print("No solution! (a cannot be zero)")
        return
    x = (c - b) / a
    print(f"{a}x + {b} = {c}")
    print(f"x = ({c} - {b}) / {a} = {x}")
    return x
print("solve_linear(3, 5, 20) =", solve_linear(3, 5, 20))
print("solve_linear(2, -4, 10) =", solve_linear(2, -4, 10))
print("\n")

print("----------Part 5----------")
print("Solving Quadratic Equations")
def solve_quadratic(a, b, c):
    """Solves ax^2 + bx + c = 0"""
    print(f"Solving: {a}x^2 + {b}x + {c} = 0")
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"2 real solutions: x = {round(x1, 4)} and x = {round(x2, 4)}")
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"1 real solution: x = {x}")
        return x
    else:
        print("0 real solutions (discriminant (b² - 4*a*c) is negative)")
        return 0 # for no real solutions
print("solve_quadratic(1, -5, 6) =", solve_quadratic(1, -5, 6))
print("solve_quadratic(1, -2, 1) =", solve_quadratic(1, -2, 1))
print("solve_quadratic(1, 0, 4) =", solve_quadratic(1, 0, 4))
print("\n\n\n")

print("==========5.Classes and Geometry==========")
print("----------Part 1----------")
print("Classes — Blueprints for Objects")
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    def bark(self):
        print(f"{self.name} says: Woof!")
    def info(self):
        print(f"{self.name} is a {self.breed}, {self.age} years old")

dog1 = Dog("Buddy", "Labrador", 3)
dog2 = Dog("Max", "Poodle", 5)
dog1.bark()
dog2.info()
print("\n")

print("----------Part 2----------")
print("Shape Classes — Geometry Comes Alive")
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def circumference(self):
        return 2 * math.pi * self.radius
    def describe(self):
        print(f"Circle with radius {self.radius}")
        print(f"  Area = {self.area()}")
        print(f"  Circumference = {self.circumference()}")

c = Circle(5)
c.describe()
print("\n")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def is_square(self):
        return self.width == self.height
    def describe(self):
        print(f"Rectangle with width {self.width} and height {self.height}")
        print(f"  Area = {round(self.area(), 4)}")
        print(f"  Perimeter = {round(self.perimeter(), 4)}")
        print(f"  Is it a square? {self.is_square()}")

r = Rectangle(4, 7)
r.describe()
print("\n")

print("----------The Pythagorean Theorem----------")
class RightTriangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = math.sqrt(a**2 + b**2)
    def area(self):
        return 0.5 * self.a * self.b
    def describe(self):
        print(f"Right triangle with legs {self.a} and {self.b}")
        print(f"  Hypotenuse = {self.c}")
        print(f"  Area = {self.area()}")
        print(f"  Check: {self.a}² + {self.b}² = {self.a**2} + {self.b**2} = {self.a**2 + self.b**2}")
        print(f"         c² = {self.c**2}  ✓")

t1 = RightTriangle(3, 4)
t1.describe()

t2 = RightTriangle(5, 12)
t2.describe()
print("\n")

print("----------3D Volumes----------")
class Sphere:
    def __init__(self, radius):
        self.radius = radius
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3
    def surface_area(self):
        return 4 * math.pi * self.radius ** 2
    def describe(self):
        print(f"Sphere with radius {self.radius}")
        print(f"  Volume = {round(self.volume(), 4)}")
        print(f"  Surface Area = {round(self.surface_area(), 4)}")

s = Sphere(5)
s.describe()
print("\n")

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def volume(self):
        return math.pi * self.radius ** 2 * self.height
    def surface_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2
    def describe(self):
        print(f"Cylinder with radius {self.radius} and height {self.height}")
        print(f"  Volume = {self.volume()}")


earth = Sphere(6371)
print(f"Earth's volume: {earth.volume():.2e} km³")
print("\n")

can = Cylinder(4, 12)
print(f"Cylinder volume: {can.volume()} cubic units")
print("\n")

print("----------Part 3----------")
print("Challenge 1")
print("(The Earth is a sphere, so the volume is calculated using the formula for the volume of a sphere.)")
print("Sphere with radius 6371")
print("  Volume = 1.0832e+12 km³")
print("\n\n\n")

print("==========6.Recursion and Trigonometry==========")
print("----------Part 1----------")
print("Recursion — A Function That Calls Itself")
def factorial(n):
    """n! = n × (n-1) × (n-2) × ... × 1"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("factorial(5) =", factorial(5))
print("factorial(10) =", factorial(10))
print("\n")

print("----------Part 2----------")
print("The Fibonacci Sequence")
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("fibonacci(0) =", fibonacci(0))
print("fibonacci(1) =", fibonacci(1))
print("fibonacci(2) =", fibonacci(2))
print("fibonacci(3) =", fibonacci(3))
print("fibonacci(4) =", fibonacci(4))
print("fibonacci(5) =", fibonacci(5))
print("fibonacci(6) =", fibonacci(6))

for i in range(16):
    print(f"F({i}) = {fibonacci(i)}")
print("\n")

print("----------Part 3----------")
def deg_to_rad(degrees):
    return degrees * math.pi / 180

angles = [0, 30, 45, 60, 90]

print(f"{'Angle':>6} | {'sin':>8} | {'cos':>8} | {'tan':>8}")
print("-" * 40)
for deg in angles:
    rad = deg_to_rad(deg)
    s = round(math.sin(rad), 4)
    c = round(math.cos(rad), 4)
    t = round(math.tan(rad), 4) if deg != 90 else "undefined"
    print(f"{deg:>5}° | {str(s):>8} | {str(c):>8} | {str(t):>8}")

print("\n")

print("----------Part 4----------")
print("The Unit Circle")
def point_on_unit_circle(degrees):
    """Returns (x, y) coordinates on the unit circle for a given angle"""
    rad = degrees * math.pi / 180
    x = round(math.cos(rad), 4)
    y = round(math.sin(rad), 4)
    return (x, y)

print(f"{'Angle':>6} | {'x':>8} | {'y':>8}")
print("-" * 40)
for deg in angles:
    point = point_on_unit_circle(deg)
    print(f"{deg:>5}° | {str(point[0]):>8} | {str(point[1]):>8}")
print("\n")

print("==========7.Graphing with NumPy and Matplotlib==========")
print("----------Part 1----------")
print("NumPy — Fast Math on Arrays")
import numpy as np
data = np.array([10, 20, 30, 40, 50])
print(data * 2)
print(data + 5)
scores = np.array([72, 85, 91, 68, 95, 88, 76, 90])
print(f"Mean:   {np.mean(scores):.2f}")
print(f"Median: {np.median(scores):.2f}")
print(f"Std Dev:{np.std(scores):.2f}")
print(f"Min:    {np.min(scores)},  Max: {np.max(scores)}")
x = np.linspace(0, 10, 100)
print(x[:5])
print("\n")

print("----------Part 2----------")
print("Your First Graph!")
import matplotlib.pyplot as plt
x = np.linspace(-20, 20, 200)
plt.figure(figsize=(10, 6))
plt.plot(x, x,       label="y = x",    color="blue")
plt.plot(x, x**2,    label="y = x²",   color="red")
plt.plot(x, x**3,    label="y = x³",   color="green")
plt.title("Three Math Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.xlim(-20, 20)
plt.ylim(-50, 50)
plt.show()
print("\n")

print("----------Part 3----------")
print("Graphing Trig Functions")
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4 * np.pi, 400)

plt.figure(figsize=(12, 5))
plt.plot(x, np.sin(x), label="sin(x)", color="blue")
plt.plot(x, np.cos(x), label="cos(x)", color="red")
plt.axhline(y=0, color="black", linewidth=0.5)
plt.title("Sine and Cosine Waves")
plt.xlabel("x (radians)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
print("\n")

print("----------Part 4----------")
print("Linear Regression — Finding the Best Fit Line")
import numpy as np
import matplotlib.pyplot as plt

hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
scores = np.array([55, 60, 65, 70, 72, 78, 82, 85, 90, 95])

coefficients = np.polyfit(hours, scores, 1)
m = coefficients[0]
b = coefficients[1]
print(f"Best fit line: score = {m:.2f} × hours + {b:.2f}")
# Predict score for 11 hours of study
predicted = m * 11 + b
print(f"Predicted score for 11 hours: {predicted:.1f}")

# Plot it
best_fit_line = m * hours + b

plt.figure(figsize=(8, 5))
plt.scatter(hours, scores, color="blue", label="Data points", s=60)
plt.plot(hours, best_fit_line, color="red", label=f"Best fit: y = {m:.1f}x + {b:.1f}")
plt.title("Study Hours vs. Test Score")
plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.legend()
plt.grid(True)
plt.show()
print("\n\n\n")

print("==========8.Algorithms, Logarithms, and Growth==========")
print("----------Part 1----------")
print("Logarithms — The Opposite of Exponents")
import math
print("log base 10")
print("log10(100) =", math.log10(100))
print("log10(1000) =", math.log10(1000))
print("log base 2")
print("log2(8) =", math.log2(8))
print("log2(1024) =", math.log2(1024))
print("Natural log")
print("log(e) =", math.log(math.e))
print("e =", math.e)
print("\n")
print("Convert between bases")
def log_base(x, base):
    return math.log(x) / math.log(base)
print(log_base(27, 3))
print("\n")

print("----------Part 2----------")
print("Exponential Growth vs. Logarithmic Growth")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 20, 200)

plt.figure(figsize=(10, 6))
plt.plot(x, x,             label="Linear: y = x",      color="blue")
plt.plot(x, 2**x,          label="Exponential: y = 2^x", color="red")
plt.plot(x, np.log2(x),    label="Logarithmic: y = log₂(x)", color="green")
plt.plot(x, x**2,          label="Quadratic: y = x²",  color="orange")
plt.ylim(0, 100)
plt.title("Growth Rates Compared")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
print("\n")

print("----------Part 3----------")
print("Binary Search — Logarithms in Action")
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if sorted_list[mid] == target:
            print(f"Found {target} at index {mid} in {steps} steps!")
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Not found. Took {steps} steps.")
    return -1

numbers = list(range(0, 2000, 2))
binary_search(numbers, 742)
binary_search(numbers, 1000)
print("\n")

print("----------Part 4----------")
print("Introduction to Limits")
def f(x):
    return (x**2 - 1) / (x - 1)

print("x → 1 from below:")
for x in [0.9, 0.99, 0.999, 0.9999]:
    print(f"  f({x}) = {f(x):.6f}")

print("\nx → 1 from above:")
for x in [1.1, 1.01, 1.001, 1.0001]:
    print(f"  f({x}) = {f(x):.6f}")

print("\nThe limit appears to approach: 2")
print("(Because (x²-1)/(x-1) = (x+1)(x-1)/(x-1) = x+1  →  1+1 = 2)")

print("\n")

print("----------Part 5----------")
print("Bubble Sort — A Classic Algorithm")
def bubble_sort(arr):
    """Sorts a list in ascending order using bubble sort"""
    n = len(arr)
    comparisons = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(f"Sorted in {comparisons} comparisons")
    return arr

data = [64, 34, 25, 12, 22, 11, 90]
print("Before:", data)
sorted_data = bubble_sort(data[:])
print("After: ", sorted_data)
print("\n")

print("----------Part 6----------")
print("Challenge 1")
print("How many steps does binary search need to find a number in a list of 1,000,000 items? Calculate math.ceil(math.log2(1000000))")
print("................\n" * 20)
print("log2(1000000) = ", math.log2(1000000))

print("\n\n\n")
print("==========9.Calculus I==========")

print("----------Slope - How Steep Is a Line?----------")

def slope(x1, y1, x2, y2):
    """Slope of the line through 2 points."""
    return (y2 - y1)/ (x2 - x1)

print("Slope from (0,0) to (3,6):", slope(0, 0, 3, 6))    # 2.0  (goes up 2 for every 1 across)
print("Slope from (1,1) to (4,2):", slope(1, 1, 4, 2))    # 0.333...
print("Slope from (2,5) to (6,5):", slope(2, 5, 6, 5))    # 0.0  (flat line!)


def f(x):
    return x ** 2

# Average rate of change of x² between x=1 and x=3
x1, x2 = 1, 3
y1, y2 = f(x1), f(x2)
average_slope = (y2 - y1) / (x2 - x1)
print(f"Between x={x1} and x={x2}, the curve rises at an average rate of {average_slope}")
# (1, 1) and (3, 9)  →  (9 - 1) / (3 - 1) = 4

def derivative(f, x, h=0.000001):
    """Estimate the slope of f at the point x (the derivative)."""
    return (f(x+h) - f(x)) / h

print("Slope of x² at x=3:", round(derivative(f, 3), 4))    # very close to 6
print("Slope of x² at x=5:", round(derivative(f, 5), 4))    # very close to 10
print("Slope of x² at x=0:", round(derivative(f, 0), 4))    # very close to 0 (the bottom is flat!)

def derivative(f, x, h=0.000001):
    return (f(x + h) - f(x)) / h

print(f"{'x':>4} | {'our estimate':>14} | {'rule (2x)':>10}")
print("-" * 36)
for x in range(1, 6):
    estimate = round(derivative(f, x), 3)
    rule = 2 * x
    print(f"{x:>4} | {estimate:>14} | {rule:>10}")

print("==========10.Calculus II: Integrals & Area Under a Curve==========")

def integrate(f, a, b, n):
    """Estimate the area under f from a to b using n rectangles."""
    width = (b - a) / n        # how wide each rectangle is
    total_area = 0

    for i in range(n):
        x = a + i * width      # left edge of this rectangle
        height = f(x)          # the curve's value there
        total_area += height * width

    return total_area

print("With 10 rectangles:", round(integrate(f, 0, 1, 10), 5))

def integrate(f, a, b, n):
    width = (b - a) / n
    total_area = 0
    for i in range(n):
        x = a + i * width
        total_area += f(x) * width
    return total_area

print(f"{'rectangles':>12} | {'area estimate':>14}")
print("-" * 30)
for n in [1, 10, 100, 1000, 100000]:
    estimate = integrate(f, 0, 1, n)
    print(f"{n:>12} | {round(estimate, 6):>14}")

print("\nThe exact answer is 1/3 =", round(1/3, 15))

def integrate(f, a, b, n=100000):
    width = (b - a) / n
    total = 0
    for i in range(n):
        x = a + i * width
        total += f(x) * width
    return total

# A car's speed (in meters per second) at time t seconds: speed(t) = 3*t
def speed(t):
    return 3 * t


# How far does the car travel between t=0 and t=4 seconds?
distance = integrate(speed, 0, 4)
print(f"Distance traveled from 0 to 4 seconds: {round(distance, 2)} meters")

import random

print(random.randint(1, 6))        # a whole number from 1 to 6 (like a dice roll)
print(random.randint(0, 1))             # a decimal between 0.0 and 1.0
print(random.choice(["heads", "tails"]))   # picks one item at random
print(random.choice(["🍎", "🍌", "🍇"]))     # works on any list!

flips = 1000
heads = 0

for i in range(flips):
    if random.choice(["H", "T"]) == "H":
        heads += 1

print(f"Out of {flips} flips, {heads} were heads.")
print(f"That's a probability of {heads / flips}")   # should be close to 0.5

print(f"{'rolls':>10} | {'fraction that were 6':>22}")
print("-" * 38)
for rolls in [10, 100, 1000, 100000]:
    sixes = 0
    for i in range(rolls):
        if random.randint(1, 6) == 6:
            sixes += 1
    print(f"{rolls:>10} | {round(sixes / rolls, 4):>22}")

print("\nThe true probability is 1/6 =", round(1/6, 15))

darts = 100000
inside = 0

for i in range(darts):
    x = random.random()      # 0 to 1
    y = random.random()      # 0 to 1
    if x**2 + y**2 <= 1:     # is the dart inside the quarter-circle?
        inside += 1

# fraction inside ≈ π/4, so multiply by 4 to estimate π
pi_estimate = 4 * inside / darts
print(f"Threw {darts} darts, {inside} landed inside the circle.")
print(f"Estimated π ≈ {pi_estimate}")
print(f"Real π ≈ {3.14159}")

a = np.array([3, 4])
b = np.array([1, 2])

print("Add:        ", a + b)        # [4 6]  — adds matching parts
print("Scale by 2: ", 2 * a)        # [6 8]  — multiplies every part
print("Subtract:   ", a - b)        # [2 2]

a = np.array([3, 4])
length = np.sqrt(a[0]**2 + a[1]**2)     # √(3² + 4²) = √25 = 5
print("Length of vector [3, 4]:", length)

# NumPy has a shortcut for this:
print("Length (the easy way):", np.linalg.norm(a))

a = np.array([3, 4])
b = np.array([1, 2])

dot = a[0]*b[0] + a[1]*b[1]      # 3*1 + 4*2 = 11
print("Dot product (by hand):", dot)

print("Dot product (NumPy):  ", np.dot(a, b))    # 11 — same answer

a = np.array([1, 0])
b = np.array([1, 1])

cos_angle = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle_degrees = np.degrees(np.arccos(cos_angle))
print(f"Angle between the vectors: {round(angle_degrees, 1)}°")    # 45.0°

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
print("Shape (rows, columns):", matrix.shape)    # (2, 3) — 2 rows, 3 columns
print("Top-left number:", matrix[0, 0])          # 1   (row 0, column 0)
print("Bottom-right number:", matrix[1, 2])      # 6   (row 1, column 2)

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("A @ B =")
print(A @ B)        # combines rows of A with columns of B

# coefficients (the numbers in front of x and y)
A = np.array([[2, 1],
              [1, 3]])

# the answers on the right side
b = np.array([8, 9])

solution = np.linalg.solve(A, b)
print(f"x = {solution[0]}")     # 3.0
print(f"y = {solution[1]}")     # 2.0

A = np.array([[2, 1], [1, 3]])
b = np.array([8, 9])
solution = np.linalg.solve(A, b)
x, y = solution

print("Check equation 1:", 2*x + 1*y, "should be 8")
print("Check equation 2:", 1*x + 3*y, "should be 9")

print("THE END")
print("Done on Tuesday June 16, 2026")
print("Goodbye!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")