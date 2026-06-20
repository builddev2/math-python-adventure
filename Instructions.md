# Python + Math Adventure 🎮
### A step-by-step program for young coders who love math

Welcome! You are going to learn two amazing things at the same time:
- **Python** — a real programming language used by scientists, game makers, and engineers
- **High School Math** — algebra, geometry, statistics, trigonometry, and more!

Each stage is like a level in a video game. Finish one, unlock the next.
You will need **Python 3** installed on your computer. Ask a grown-up to help you install it from [python.org](https://python.org) if you haven't already.

---

## How to Run Your Code
1. Open a program called **IDLE** (it comes with Python) or any text editor
2. Type your code into a new file and save it as something like `stage1.py`
3. Press **F5** (in IDLE) or type `python stage1.py` in the terminal to run it

---

---

# Stage 1 — Your First Programs
## Python: `print`, Variables, Operators, `if/else`
## Math: Arithmetic, Order of Operations, Inequalities

---

### 1.1 Say Hello to Python

The very first thing every programmer learns is how to make the computer say something.
The `print()` command tells Python to show words or numbers on the screen.

```python
print("Hello! I am learning Python and Math!")
print("2 + 3 =", 2 + 3)
print("10 - 4 =", 10 - 4)
print("3 x 7 =", 3 * 7)
print("20 / 4 =", 20 / 4)
```

Run this and you will see the answers! Notice:
- `*` means multiply
- `/` means divide
- Python calculates the math for you automatically!

---

### 1.2 Order of Operations (PEMDAS / BODMAS)

In math class you learn **PEMDAS**: Parentheses, Exponents, Multiply/Divide, Add/Subtract.
Python follows the exact same rules!

```python
# Without parentheses
print(2 + 3 * 4)       # Python does 3*4 first = 12, then 2+12 = 14

# With parentheses
print((2 + 3) * 4)     # Python does 2+3 first = 5, then 5*4 = 20

# Exponents (powers)
print(2 ** 3)           # 2 to the power of 3 = 8
print(5 ** 2)           # 5 squared = 25
```

The `**` symbol means "to the power of". So `2 ** 3` means 2³ = 8.

---

### 1.3 Variables — Giving Names to Numbers

In algebra, letters like `x` or `y` hold numbers. Python uses the same idea, called **variables**.

```python
apples = 5
oranges = 3

total_fruit = apples + oranges
print("Total fruit:", total_fruit)

# You can change a variable
apples = 10
print("Now I have", apples, "apples")
```

A variable is like a labeled box — you put a value in the box and use the label to find it later.

---

### 1.4 If/Else — Making Decisions with Inequalities

In math, inequalities use symbols like `>` (greater than), `<` (less than), `>=` (greater than or equal to).
Python uses these same symbols to make decisions!

```python
age = 8

if age >= 13:
    print("You are a teenager!")
elif age >= 10:
    print("Almost a teenager!")
else:
    print("You are still a kid — enjoy it!")

# Number comparison
x = 15
y = 20

if x > y:
    print(x, "is bigger")
elif x < y:
    print(y, "is bigger")
else:
    print("They are equal!")
```

**The math connection:** `x > y` is an inequality. Python checks if it's True or False, then decides what to do.

---

### Stage 1 Challenges

1. Write a program that calculates `(5 + 3) ** 2 - 10` and prints the answer. What do you expect it to be?
2. Make a variable called `score` equal to 85. Use `if/elif/else` to print "A" if score ≥ 90, "B" if score ≥ 80, "C" if score ≥ 70, and "Try again" otherwise.
3. Print the result of `7 ** 2 + 24 ** 2`. Do you notice anything special about the number you get? (Hint: What is 25 ** 2?)

---

---

# Stage 2 — Loops, Lists, and Functions
## Python: `for` loops, `while` loops, Lists, `def`
## Math: Sequences, Patterns, Mathematical Functions

---

### 2.1 For Loops — Repeating with Sequences

In math, a **sequence** is a list of numbers with a pattern, like 1, 2, 3, 4, 5 or 2, 4, 6, 8.
A `for` loop lets you do something for each number in a sequence.

```python
# Count from 1 to 10
for number in range(1, 11):
    print(number)

# Print the first 8 even numbers
for i in range(1, 9):
    print(i * 2)

# Print squares: 1, 4, 9, 16, 25
for i in range(1, 6):
    print(i, "squared is", i ** 2)
```

`range(1, 11)` generates numbers 1, 2, 3 ... 10 (stops BEFORE 11).

---

### 2.2 While Loops — Repeating Until Something is True

A `while` loop keeps going as long as something is true. It's great for counting up or down.

```python
# Count down from 10
countdown = 10
while countdown > 0:
    print(countdown)
    countdown = countdown - 1  # or: countdown -= 1
print("Blast off!")

# Sum of numbers 1 through 100 (a famous math puzzle!)
total = 0
number = 1
while number <= 100:
    total = total + number
    number = number + 1
print("Sum of 1 to 100:", total)  # The answer is 5050!
```

The sum 1+2+3+...+100 = 5050. This was famously solved by mathematician Carl Friedrich Gauss when he was a kid!

---

### 2.3 Lists — Storing Many Values

A **list** stores many values together. It's like a row in a spreadsheet.

```python
grades = [92, 85, 78, 95, 88]

print("All grades:", grades)
print("First grade:", grades[0])   # Lists start at index 0!
print("Last grade:", grades[-1])   # -1 means the last item

# Loop through a list
print("My grades are:")
for grade in grades:
    print(grade)
```

---

### 2.4 Functions — Your Own Reusable Commands

In math, a **function** takes an input and gives an output. For example, f(x) = x² means "square whatever you put in."
In Python, you create a function with `def`.

```python
# Define a function (like writing the rule for f(x))
def square(x):
    return x ** 2

# Call the function (like calculating f(5))
print(square(5))    # Output: 25
print(square(12))   # Output: 144

# A more useful function
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

print(celsius_to_fahrenheit(0))    # 32.0 (freezing)
print(celsius_to_fahrenheit(100))  # 212.0 (boiling)
```

**The math connection:** `def square(x): return x ** 2` is exactly like writing f(x) = x².

---

### Stage 2 Challenges

1. Write a `for` loop that prints the first 10 numbers in the sequence 3, 6, 9, 12 ... (the 3 times table).
2. Write a function called `area_of_rectangle(width, height)` that returns width × height. Test it with a few different sizes.
3. Use a `while` loop to find the first number whose square is greater than 200. Print that number.

---

---

# Stage 3 — Smarter Lists and the Math Module
## Python: List Comprehensions, `import math`
## Math: Statistics — Mean, Median, Standard Deviation

---

### 3.1 List Comprehensions — Shortcuts for Building Lists

Instead of writing a loop to build a list, Python lets you do it in one line!

```python
# Old way (using a loop)
squares = []
for i in range(1, 11):
    squares.append(i ** 2)

# New way (list comprehension) — much shorter!
squares = [i ** 2 for i in range(1, 11)]
print(squares)

# Only keep even squares
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(even_squares)
```

`i % 2` means "remainder when divided by 2." If the remainder is 0, the number is even.

---

### 3.2 The Math Module

Python has a built-in toolbox called `math` full of powerful math tools.

```python
import math

print(math.sqrt(144))    # Square root of 144 = 12.0
print(math.pi)           # Pi ≈ 3.14159...
print(math.floor(3.9))   # Round DOWN = 3
print(math.ceil(3.1))    # Round UP = 4
print(math.log(100, 10)) # log base 10 of 100 = 2.0
```

---

### 3.3 Mean, Median, and Standard Deviation

**Mean** (average) = add all numbers, divide by how many there are.
**Median** = the middle number when sorted.
**Standard Deviation** = how "spread out" the numbers are.

```python
import math

scores = [72, 85, 91, 68, 95, 88, 76, 90, 84, 79]

# Mean
mean = sum(scores) / len(scores)
print("Mean:", mean)

# Median
sorted_scores = sorted(scores)
n = len(sorted_scores)
if n % 2 == 0:
    median = (sorted_scores[n//2 - 1] + sorted_scores[n//2]) / 2
else:
    median = sorted_scores[n//2]
print("Median:", median)

# Standard Deviation (how spread out the scores are)
variance = sum((x - mean) ** 2 for x in scores) / n
std_dev = math.sqrt(variance)
print("Standard Deviation:", round(std_dev, 2))
```

**What does standard deviation mean?** A small standard deviation means most scores are close to the mean. A large one means they are spread out far apart.

---

### Stage 3 Challenges

1. Use a list comprehension to create a list of all numbers from 1 to 50 that are divisible by 3. Print it.
2. Create a list of 5 test scores of your choosing. Calculate and print the mean and median.
3. What is `math.sqrt(math.pi)`? Print it and write down what you notice.

---

---

# Stage 4 — Dictionaries and Algebra
## Python: Dictionaries, f-strings
## Math: Algebra — Linear and Quadratic Equations

---

### 4.1 Dictionaries — Labels for Your Data

A **dictionary** stores data as key-value pairs, like a real dictionary where a word (key) has a definition (value).

```python
student = {
    "name": "Alex",
    "age": 8,
    "grade": 3,
    "favorite_subject": "Math"
}

print(student["name"])      # Alex
print(student["age"])       # 8

# Add a new entry
student["score"] = 98
print(student)

# Loop through a dictionary
for key, value in student.items():
    print(key, ":", value)
```

---

### 4.2 F-Strings — Pretty Printing

F-strings let you put variables directly inside a string. Much nicer than lots of commas!

```python
name = "Alex"
score = 95
grade = "A"

# Old way
print("Student:", name, "got a score of", score, "which is a", grade)

# F-string way (starts with f before the quote)
print(f"Student: {name} got a score of {score} which is a {grade}")
print(f"5 squared is {5 ** 2}")   # You can put math inside {}
```

---

### 4.3 Solving Linear Equations

A **linear equation** looks like: `ax + b = c`. Solving for x means finding: `x = (c - b) / a`.

```python
def solve_linear(a, b, c):
    """Solves ax + b = c for x"""
    if a == 0:
        print("No solution! (a cannot be zero)")
        return
    x = (c - b) / a
    print(f"{a}x + {b} = {c}")
    print(f"x = ({c} - {b}) / {a} = {x}")
    return x

solve_linear(3, 5, 20)   # 3x + 5 = 20  →  x = 5
solve_linear(2, -4, 10)  # 2x - 4 = 10  →  x = 7
```

---

### 4.4 Solving Quadratic Equations

A **quadratic equation** looks like: `ax² + bx + c = 0`.
To solve it, we use the **quadratic formula**: x = (-b ± √(b²-4ac)) / 2a

The part under the square root, `b²-4ac`, is called the **discriminant**:
- If it's positive: two solutions
- If it's zero: one solution
- If it's negative: no real solutions

```python
import math

def solve_quadratic(a, b, c):
    """Solves ax^2 + bx + c = 0"""
    print(f"Solving: {a}x² + {b}x + {c} = 0")
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Two solutions: x = {round(x1, 4)} and x = {round(x2, 4)}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"One solution: x = {x}")
    else:
        print("No real solutions (discriminant (b**2 - 4*a*c) is negative)")

solve_quadratic(1, -5, 6)    # x² - 5x + 6 = 0  →  x=2, x=3
solve_quadratic(1, -2, 1)    # x² - 2x + 1 = 0  →  x=1
solve_quadratic(1, 0, 4)     # x² + 4 = 0        →  no real solutions
```

**Wow!** You just wrote a program that solves one of the most important equations in all of high school math!

---

### Stage 4 Challenges

1. Create a dictionary for your 3 favorite animals with their names as keys and their top speed (in mph) as values. Print each one using an f-string.
2. Use `solve_linear` to find x if `5x + 12 = 47`.
3. Use `solve_quadratic` to solve `x² + x - 6 = 0`. Check your answers by plugging them back into the equation!

---

---

# Stage 5 — Classes and Geometry
## Python: Classes and Objects
## Math: Geometry — Pythagorean Theorem, Shapes, Areas, Volumes

---

### 5.1 Classes — Blueprints for Objects

A **class** is a blueprint. Just like an architect draws a house plan and you can build many houses from it, a class is a plan for creating many objects.

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def info(self):
        print(f"{self.name} is a {self.breed}, {self.age} years old")

# Create two Dog objects from the class
dog1 = Dog("Buddy", "Labrador", 3)
dog2 = Dog("Max", "Poodle", 5)

dog1.bark()
dog2.info()
```

`__init__` is the "setup" method — it runs when you create a new object.

---

### 5.2 Shape Classes — Geometry Comes Alive

Now let's use classes to do real geometry!

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def describe(self):
        print(f"Circle with radius {self.radius}")
        print(f"  Area = {round(self.area(), 4)}")
        print(f"  Circumference = {round(self.circumference(), 4)}")


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


c = Circle(5)
c.describe()

r = Rectangle(4, 7)
print(f"\nRectangle {r.width}x{r.height}:")
print(f"  Area = {r.area()}")
print(f"  Perimeter = {r.perimeter()}")
print(f"  Is it a square? {r.is_square()}")
```

---

### 5.3 The Pythagorean Theorem

The most famous theorem in geometry: **a² + b² = c²**
In a right triangle, if `a` and `b` are the two shorter sides, then `c` (the hypotenuse) satisfies this equation.

```python
import math

class RightTriangle:
    def __init__(self, a, b):
        self.a = a   # one leg
        self.b = b   # other leg
        self.c = math.sqrt(a**2 + b**2)   # hypotenuse!

    def area(self):
        return 0.5 * self.a * self.b

    def describe(self):
        print(f"Right triangle with legs {self.a} and {self.b}")
        print(f"  Hypotenuse = {round(self.c, 4)}")
        print(f"  Area = {self.area()}")
        # Verify Pythagoras
        print(f"  Check: {self.a}² + {self.b}² = {self.a**2} + {self.b**2} = {self.a**2 + self.b**2}")
        print(f"         c² = {round(self.c**2, 4)}  ✓")

# Famous Pythagorean triples (all whole numbers!)
t1 = RightTriangle(3, 4)     # hypotenuse = 5
t1.describe()

print()
t2 = RightTriangle(5, 12)    # hypotenuse = 13
t2.describe()
```

**Pythagorean triples** are special triangles where all three sides are whole numbers: (3,4,5), (5,12,13), (8,15,17)...

---

### 5.4 3D Volumes

```python
import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

earth = Sphere(6371)   # Earth's radius in km
print(f"Earth's volume: {earth.volume():.2e} km³")   # scientific notation!

can = Cylinder(4, 12)
print(f"Cylinder volume: {round(can.volume(), 2)} cubic units")
```

`:.2e` formats a number in scientific notation — great for very large numbers!

---

### Stage 5 Challenges

1. Add a `Triangle` class with `base` and `height` that calculates area (½ × base × height).
2. Create a `RightTriangle(8, 15)`. What is the hypotenuse? Is this another Pythagorean triple?
3. Add a `diagonal()` method to the `Rectangle` class. The diagonal of a rectangle uses the Pythagorean theorem: d = √(width² + height²).

---

---

# Stage 6 — Recursion and Trigonometry
## Python: Recursion
## Math: Trigonometry — sin, cos, tan, the Unit Circle

---

### 6.1 Recursion — A Function That Calls Itself

**Recursion** is when a function calls itself to solve a smaller version of the same problem.
Think of Russian nesting dolls — each doll contains a smaller version of itself.

```python
def factorial(n):
    """n! = n × (n-1) × (n-2) × ... × 1"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)   # calls itself!

print(factorial(5))   # 5! = 5×4×3×2×1 = 120
print(factorial(10))  # 10! = 3628800
```

How it works for `factorial(4)`:
- factorial(4) = 4 × factorial(3)
- factorial(3) = 3 × factorial(2)
- factorial(2) = 2 × factorial(1)
- factorial(1) = 1  ← base case, stop!

---

### 6.2 The Fibonacci Sequence

The **Fibonacci sequence** is 1, 1, 2, 3, 5, 8, 13, 21 ... Each number is the sum of the two before it.
It appears in nature: sunflower seeds, pinecones, spiral shells!

```python
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

---

### 6.3 Trigonometry — Angles and Triangles

**Trigonometry** studies the relationship between angles and side lengths in triangles.
The three main functions are:
- **sin(θ)** = opposite / hypotenuse
- **cos(θ)** = adjacent / hypotenuse
- **tan(θ)** = opposite / adjacent  (= sin/cos)

In Python, the `math` module uses **radians**, not degrees. 180° = π radians.
To convert: `radians = degrees × π / 180`

```python
import math

def deg_to_rad(degrees):
    return degrees * math.pi / 180

# Values at famous angles
angles = [0, 30, 45, 60, 90]

print(f"{'Angle':>6} | {'sin':>8} | {'cos':>8} | {'tan':>8}")
print("-" * 40)
for deg in angles:
    rad = deg_to_rad(deg)
    s = round(math.sin(rad), 4)
    c = round(math.cos(rad), 4)
    t = round(math.tan(rad), 4) if deg != 90 else "undefined"
    print(f"{deg:>5}° | {str(s):>8} | {str(c):>8} | {str(t):>8}")
```

You'll see the famous values: sin(30°) = 0.5, cos(60°) = 0.5, sin(45°) = cos(45°) ≈ 0.707!

---

### 6.4 The Unit Circle — Finding Points with Trig

The **unit circle** has radius 1. Any point on it can be written as (cos θ, sin θ).
This connects geometry, algebra, and trigonometry all at once!

```python
import math

def point_on_unit_circle(degrees):
    """Returns (x, y) coordinates on the unit circle for a given angle"""
    rad = degrees * math.pi / 180
    x = round(math.cos(rad), 4)
    y = round(math.sin(rad), 4)
    return (x, y)

# Trace the circle at every 45 degrees
print("Points on the unit circle:")
for angle in range(0, 360, 45):
    point = point_on_unit_circle(angle)
    print(f"  At {angle:>3}°: (x={point[0]:>7}, y={point[1]:>7})")

# The most important identity in trig: sin²(θ) + cos²(θ) = 1
angle = 37
r = math.radians(angle)
identity_check = round(math.sin(r)**2 + math.cos(r)**2, 10)
print(f"\nsin²(37°) + cos²(37°) = {identity_check}  ← always equals 1!")
```

`sin²(θ) + cos²(θ) = 1` is called the **Pythagorean Identity** — it connects the unit circle back to the Pythagorean theorem!

---

### Stage 6 Challenges

1. Write a recursive function `power(base, exp)` that calculates base^exp without using `**`. (Hint: base^exp = base × base^(exp-1))
2. What is the Fibonacci number at position 15? Use your `fibonacci` function to find out.
3. What angle gives sin(θ) = cos(θ)? Check your answer using Python.

---

---

# Stage 7 — Graphing with NumPy and Matplotlib
## Python: `numpy`, `matplotlib`
## Math: Linear Regression, Data Distributions

---

### Setup
First, install the libraries. Open your terminal and type:
```
pip install numpy matplotlib
```

---

### 7.1 NumPy — Fast Math on Arrays

**NumPy** lets you do math on entire lists of numbers at once — much faster than a loop!

```python
import numpy as np

# Create an array
data = np.array([10, 20, 30, 40, 50])
print(data * 2)          # [20 40 60 80 100] — multiplied every number!
print(data + 5)          # [15 25 35 45 55]

# Stats with NumPy
scores = np.array([72, 85, 91, 68, 95, 88, 76, 90])
print(f"Mean:   {np.mean(scores):.2f}")
print(f"Median: {np.median(scores):.2f}")
print(f"Std Dev:{np.std(scores):.2f}")
print(f"Min:    {np.min(scores)},  Max: {np.max(scores)}")

# Create 100 evenly spaced numbers between 0 and 10
x = np.linspace(0, 10, 100)
print(x[:5])   # First 5 values
```

---

### 7.2 Your First Graph!

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)    # 200 points from -5 to 5

# Plot several functions at once
plt.figure(figsize=(10, 6))

plt.plot(x, x,       label="f(x) = x",    color="blue")
plt.plot(x, x**2,    label="f(x) = x²",   color="red")
plt.plot(x, x**3,    label="f(x) = x³",   color="green")

plt.title("Three Math Functions")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.ylim(-30, 30)    # Limit y-axis so it doesn't get too big
plt.show()
```

You just drew the graphs of three functions! Notice how x² is a U-shape (parabola) and x³ is an S-shape.

---

### 7.3 Graphing Trig Functions

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4 * np.pi, 400)   # 0 to 4π (two full rotations)

plt.figure(figsize=(12, 5))
plt.plot(x, np.sin(x), label="sin(x)", color="blue")
plt.plot(x, np.cos(x), label="cos(x)", color="red")

plt.axhline(y=0, color="black", linewidth=0.5)   # x-axis line
plt.title("Sine and Cosine Waves")
plt.xlabel("x (radians)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
```

See how sine and cosine are the same wave but shifted? This is called a **phase shift**.

---

### 7.4 Linear Regression — Finding the Best Fit Line

**Linear regression** finds the straight line that best fits a set of data points.
It's one of the most important tools in statistics and machine learning!

```python
import numpy as np
import matplotlib.pyplot as plt

# Hours studied vs. test score (made-up data)
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
scores = np.array([55, 60, 65, 70, 72, 78, 82, 85, 90, 95])

# NumPy finds the best-fit line: score = m * hours + b
coefficients = np.polyfit(hours, scores, 1)
m = coefficients[0]   # slope
b = coefficients[1]   # y-intercept
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
```

**The math connection:** The best-fit line `score = m × hours + b` is a linear equation! The slope `m` tells you how many points you gain per extra hour of study.

---

### Stage 7 Challenges

1. Plot `y = sin(x)` and `y = sin(2x)` on the same graph. What is different about `sin(2x)`?
2. Add a `y = x²` curve to the polynomial graph. Does it go up faster or slower than `x³`?
3. In the regression example, what is the predicted score if a student studies 0 hours? Does this make real-world sense?

---

---

# Stage 8 — Algorithms, Logarithms, and Growth
## Python: Sorting and Searching Algorithms
## Math: Logarithms, Exponential Growth, Intro to Limits

---

### 8.1 Logarithms — The Opposite of Exponents

If `2^10 = 1024`, then `log₂(1024) = 10`. Logarithms answer the question: **"What power do I raise the base to?"**

```python
import math

# log base 10
print(math.log10(100))      # 2.0  (because 10² = 100)
print(math.log10(1000))     # 3.0  (because 10³ = 1000)

# log base 2 (important in computer science!)
print(math.log2(8))         # 3.0  (because 2³ = 8)
print(math.log2(1024))      # 10.0 (because 2^10 = 1024)

# Natural log (base e ≈ 2.718)
print(math.log(math.e))     # 1.0
print(math.e)               # 2.71828...

# Convert between bases: log_b(x) = log(x) / log(b)
def log_base(x, base):
    return math.log(x) / math.log(base)

print(log_base(27, 3))      # 3.0  (because 3³ = 27)
```

---

### 8.2 Exponential Growth vs. Logarithmic Growth

Exponential growth gets BIG very fast. Logarithmic growth is its opposite — it gets big very slowly.

```python
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
```

Notice that exponential `2^x` grows MUCH faster than quadratic `x²`, which grows faster than linear `x`.
Logarithmic growth is the slowest of all.

---

### 8.3 Binary Search — Logarithms in Action

**Binary search** is an algorithm that finds a number in a sorted list by cutting the search in half each time.
If you have 1,024 numbers, it takes at most 10 steps (because log₂(1024) = 10)!

```python
def binary_search(sorted_list, target):
    """Find target in sorted_list. Returns index or -1 if not found."""
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
            low = mid + 1    # search the right half
        else:
            high = mid - 1   # search the left half

    print(f"Not found. Took {steps} steps.")
    return -1

# Search through 1000 numbers
numbers = list(range(0, 2000, 2))   # [0, 2, 4, 6, ... 1998]
binary_search(numbers, 742)
binary_search(numbers, 1000)
```

**The math connection:** Binary search takes at most `ceil(log₂(n))` steps for `n` items. That's why logarithms are so important in computer science!

---

### 8.4 Introduction to Limits

A **limit** asks: "What value does a function approach as x gets close to some number?"
This is the foundation of calculus!

```python
# What does (x² - 1) / (x - 1) approach as x → 1?
# (It's 0/0 at x=1 exactly, but what happens near 1?)

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
```

You can **see** the limit happening in the numbers! This is exactly what mathematicians do when they study calculus.

---

### 8.5 Bubble Sort — A Classic Algorithm

**Bubble sort** repeatedly compares adjacent numbers and swaps them if they're in the wrong order.

```python
def bubble_sort(arr):
    """Sorts a list in ascending order using bubble sort"""
    n = len(arr)
    comparisons = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   # swap!

    print(f"Sorted in {comparisons} comparisons")
    return arr

data = [64, 34, 25, 12, 22, 11, 90]
print("Before:", data)
sorted_data = bubble_sort(data[:])   # data[:] makes a copy
print("After: ", sorted_data)
```

For n items, bubble sort takes about n² comparisons. Binary search is much smarter — showing that the right **algorithm** matters as much as the code itself!

---

### Stage 8 Challenges

1. How many steps does binary search need to find a number in a list of 1,000,000 items? Calculate `math.ceil(math.log2(1000000))`.
2. Plot `y = 10^x` (exponential) and `y = log10(x)` on the same graph from x=0.1 to x=3. What do you notice about the two curves?
3. Investigate the limit of `sin(x)/x` as x → 0. Try very small values like 0.1, 0.01, 0.001. What does it approach?

---

---

# Stage 9 — Calculus I: Derivatives & Rates of Change
## Python: Helper Functions, Numerical Methods
## Math: Slope, Average vs. Instantaneous Rate of Change, Derivatives

> ⚡ **Difficulty is going up!** In Stage 8 you watched a function *approach* a value (a limit). Now you'll use that exact idea to measure how fast things change. This is the first big idea of **calculus** — the math that powers physics, engineering, and even video game animation.

---

### 9.1 Slope — How Steep Is a Line?

You already know **slope** from algebra. It measures how steep a line is:

```
slope = rise / run = (change in y) / (change in x)
```

If you have two points, the slope between them is `(y2 - y1) / (x2 - x1)`.

```python
def slope(x1, y1, x2, y2):
    """Slope of the line through two points."""
    return (y2 - y1) / (x2 - x1)

print("Slope from (0,0) to (3,6):", slope(0, 0, 3, 6))    # 2.0  (goes up 2 for every 1 across)
print("Slope from (1,1) to (4,2):", slope(1, 1, 4, 2))    # 0.333...
print("Slope from (2,5) to (6,5):", slope(2, 5, 6, 5))    # 0.0  (flat line!)
```

A big slope means steep. A slope of 0 means flat. A negative slope means going downhill.

---

### 9.2 Average Rate of Change on a Curve

A straight line has the **same** slope everywhere. But a curve like `f(x) = x²` is steeper in some places than others! 

The slope between two points *on a curve* is called the **average rate of change**. We pick two x-values, find their y-values with the function, and take the slope:

```python
def f(x):
    return x ** 2

# Average rate of change of x² between x=1 and x=3
x1, x2 = 1, 3
y1, y2 = f(x1), f(x2)
average_slope = (y2 - y1) / (x2 - x1)
print(f"Between x={x1} and x={x2}, the curve rises at an average rate of {average_slope}")
# (1, 1) and (3, 9)  →  (9 - 1) / (3 - 1) = 4
```

But what if we want the steepness at *one exact point*, not the average over a gap? That's where the magic happens. 👇

---

### 9.3 The Derivative — Instantaneous Rate of Change

Here's the trick: make the two points **closer and closer together** until the gap is almost zero. Remember limits from Stage 8? We shrink the run (`h`) toward 0:

```
slope at x ≈ (f(x + h) - f(x)) / h        ... where h is a tiny number
```

This "slope at a single point" is called the **derivative**. Let's write a function that estimates it:

```python
def derivative(f, x, h=0.000001):
    """Estimate the slope of f at the point x (the derivative)."""
    return (f(x + h) - f(x)) / h

def f(x):
    return x ** 2

print("Slope of x² at x=3:", round(derivative(f, 3), 4))    # very close to 6
print("Slope of x² at x=5:", round(derivative(f, 5), 4))    # very close to 10
print("Slope of x² at x=0:", round(derivative(f, 0), 4))    # very close to 0 (the bottom is flat!)
```

Notice the slope changes depending on *where* you are on the curve. That's what makes a curve curvy!

---

### 9.4 Checking the Famous Power Rule

Mathematicians discovered a shortcut: the derivative of `x²` is exactly `2x`, and the derivative of `x³` is exactly `3x²`. This is called the **power rule**. Let's check our numerical derivative against the rule with a table:

```python
def derivative(f, x, h=0.000001):
    return (f(x + h) - f(x)) / h

def f(x):
    return x ** 2          # the rule says its derivative should be 2*x

print(f"{'x':>4} | {'our estimate':>14} | {'rule (2x)':>10}")
print("-" * 36)
for x in range(1, 6):
    estimate = round(derivative(f, x), 3)
    rule = 2 * x
    print(f"{x:>4} | {estimate:>14} | {rule:>10}")
```

When your estimate matches the rule, you've just *experimentally proven* a calculus law with Python! 🎉

**The math connection:** A derivative tells you the slope at every point. Where the derivative is 0, the curve is momentarily flat — that's a **peak** or a **valley** (super useful for finding the highest or lowest point of something).

---

### Stage 9 Challenges

1. Use your `derivative` function on `f(x) = x ** 3` at `x = 2`. The power rule says the answer should be `3 * x²`. Does your estimate match? Try a couple of other x-values too.
2. The derivative of `sin(x)` is famously `cos(x)`. Use your `derivative` function (with `math.sin`) to estimate the slope of `sin(x)` at `x = 0`. Then compare it to `math.cos(0)`. Are they close?
3. A ball's height is `h(t) = -5*t**2 + 20*t`. The ball is at its highest point when its rate of change (slope) is 0. Estimate the derivative at `t = 1`, `t = 2`, and `t = 3`. Between which times does the slope cross zero?

---

---

# Stage 10 — Calculus II: Integrals & Area Under a Curve
## Python: Accumulation Loops (Riemann Sums)
## Math: Area Under a Curve, Integration, Convergence

> ⚡ **Even harder now!** Stage 9 measured how things *change*. Stage 10 does the opposite — it *adds up* tiny pieces to measure a whole. This is the second great idea of calculus: the **integral**.

---

### 10.1 The Big Idea — Slicing Area Into Rectangles

How do you find the area under a curvy line? You can't use a simple rectangle formula because the top is curved. The clever trick: **chop the area into many thin rectangles**, find each rectangle's area, and add them all up.

The more (and thinner) the rectangles, the better the estimate. This is called a **Riemann sum**.

```
area ≈ rectangle1 + rectangle2 + rectangle3 + ...
each rectangle area = height × width
```

The height of each rectangle comes from the function; the width is the same small number for all of them.

---

### 10.2 Building a Riemann Sum with a Loop

Let's write a function that estimates the area under any curve `f` between `a` and `b`, using `n` rectangles:

```python
def integrate(f, a, b, n):
    """Estimate the area under f from a to b using n rectangles."""
    width = (b - a) / n        # how wide each rectangle is
    total_area = 0

    for i in range(n):
        x = a + i * width      # left edge of this rectangle
        height = f(x)          # the curve's value there
        total_area += height * width

    return total_area

def f(x):
    return x ** 2

# Area under x² from 0 to 1, using 10 rectangles
print("With 10 rectangles:", round(integrate(f, 0, 1, 10), 5))
```

Each loop adds one skinny rectangle's area to the running total. That `total_area += ...` is an **accumulation** pattern — building up an answer piece by piece.

---

### 10.3 More Rectangles = Better Accuracy (Convergence!)

Watch what happens as we use more and more rectangles. The exact area under `x²` from 0 to 1 is exactly **1/3 ≈ 0.33333**. Our estimate should sneak up on it — just like a limit from Stage 8!

```python
def integrate(f, a, b, n):
    width = (b - a) / n
    total_area = 0
    for i in range(n):
        x = a + i * width
        total_area += f(x) * width
    return total_area

def f(x):
    return x ** 2

print(f"{'rectangles':>12} | {'area estimate':>14}")
print("-" * 30)
for n in [1, 10, 100, 1000, 100000]:
    estimate = integrate(f, 0, 1, n)
    print(f"{n:>12} | {round(estimate, 6):>14}")

print("\nThe exact answer is 1/3 =", round(1/3, 6))
```

See the estimates converge toward 0.3333? That's the integral revealing itself. The same "approach a value" idea from limits is doing the work again.

---

### 10.4 A Real-World Use — Distance From Speed

Integrals aren't just about abstract curves. If you know how fast something is moving at every moment, the **area under the speed graph is the total distance traveled**.

```python
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
```

You just used calculus to turn a *speed* into a *distance* — exactly what a car's odometer does!

**The math connection:** Derivatives (Stage 9) and integrals (Stage 10) are **opposites**. A derivative breaks a quantity down into its rate of change; an integral builds a quantity up from its pieces. Together they are the heart of calculus.

---

### Stage 10 Challenges

1. Use `integrate` to estimate the area under `f(x) = x ** 3` from 0 to 2. Try `n = 10`, `n = 1000`, and `n = 100000`. The exact answer is 4 — how close do you get?
2. The area under a flat line `f(x) = 5` from 0 to 3 should be a simple rectangle (width 3, height 5 = area 15). Confirm your `integrate` function agrees. Why doesn't the number of rectangles matter here?
3. A runner's speed is `speed(t) = 2*t + 1` meters per second. Estimate how far they run between `t = 0` and `t = 5` seconds. (Hint: it's the area under the speed curve.)

---

---

# Stage 11 — Probability & Random Simulations  ✨ *New Concept!*
## Python: The `random` Module, Monte Carlo Simulation
## Math: Probability, Expected Value, the Law of Large Numbers

> ✨ **A brand-new concept!** Until now your programs always gave the *same* answer every time. Now you'll teach the computer to roll dice, flip coins, and throw darts — and use that randomness to *discover* math. This is how scientists model weather, how games stay fun, and how banks measure risk.

---

### 11.1 Teaching Python to Be Random

Python has a built-in toolbox called `random`. Here are its most useful tools:

```python
import random

print(random.randint(1, 6))        # a whole number from 1 to 6 (like a dice roll)
print(random.randint(0, 1))             # a decimal between 0.0 and 1.0
print(random.choice(["heads", "tails"]))   # picks one item at random
print(random.choice(["🍎", "🍌", "🍇"]))     # works on any list!
```

Run it a few times — you'll get different answers each time. That's the point! Each run is like a fresh roll of the dice.

---

### 11.2 Simulating Many Coin Flips

**Probability** measures how likely something is, from 0 (never) to 1 (always). A fair coin has a 0.5 (50%) chance of heads. Let's test that by flipping a *simulated* coin thousands of times and counting:

```python
import random

flips = 1000
heads = 0

for i in range(flips):
    if random.choice(["H", "T"]) == "H":
        heads += 1

print(f"Out of {flips} flips, {heads} were heads.")
print(f"That's a probability of {heads / flips}")   # should be close to 0.5
```

The `heads / flips` is the **experimental probability** — what actually happened. It won't be exactly 0.5, but it should be close.

---

### 11.3 The Law of Large Numbers

Here's something beautiful: **the more times you try, the closer your experiment gets to the true probability.** This is called the **Law of Large Numbers**. Let's watch it happen by rolling a die and counting how often we get a 6 (the true probability is 1/6 ≈ 0.1667):

```python
import random

print(f"{'rolls':>10} | {'fraction that were 6':>22}")
print("-" * 38)
for rolls in [10, 100, 1000, 100000]:
    sixes = 0
    for i in range(rolls):
        if random.randint(1, 6) == 6:
            sixes += 1
    print(f"{rolls:>10} | {round(sixes / rolls, 4):>22}")

print("\nThe true probability is 1/6 =", round(1/6, 4))
```

With few rolls the fraction jumps around. With many rolls it settles right near 0.1667. The randomness "averages out."

---

### 11.4 Monte Carlo — Estimating π With Darts! 🎯

Now the showstopper. We can estimate **π** (pi!) using nothing but random darts. Here's the idea:

- Imagine a square that is 2 units wide, with a circle of radius 1 inside it.
- Throw random darts at the square.
- The fraction of darts that land *inside the circle* relates to π by: `area of circle / area of square = π / 4`.

A point `(x, y)` is inside the circle if `x² + y² ≤ 1` (that's the Pythagorean theorem from Stage 5!).

```python
import random

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
print(f"Real π     ≈ {3.14159}")
```

This trick — using random chance to compute a real answer — is called a **Monte Carlo simulation**, named after a famous casino. Real scientists use it to solve problems too hard for a formula!

**The math connection:** Geometry (the circle), the Pythagorean theorem (`x² + y² ≤ 1`), and probability all team up to reveal π. Math is connected. 🌐

---

### Stage 11 Challenges

1. Roll **two** dice (each `random.randint(1, 6)`) thousands of times and add them. Estimate the probability that the sum is exactly 7. Is 7 more or less likely than 2? (Try counting a few sums to see.)
2. Run the π-estimating program with `darts = 100`, then `10000`, then `1000000`. Does the estimate get closer to 3.14159 as you throw more darts? Connect this to the Law of Large Numbers.
3. Simulate a "lucky spinner" with `random.choice(["win", "lose", "lose", "lose"])`. After many spins, what fraction are wins? Does it match what you'd expect from the list?

---

---

# Stage 12 — Matrices & Vectors  ✨ *New Concept!*
## Python: NumPy Arrays as Vectors and Matrices
## Math: Linear Algebra — Vectors, Matrices, Solving Systems of Equations

> ✨ **The final boss — a brand-new concept!** Back in Stage 4 you solved *one* equation for *one* unknown. Now you'll solve *many* equations with *many* unknowns at once, using grids of numbers called **matrices**. This is **linear algebra**, the math behind 3D graphics, machine learning, and Google's search engine.

*(This stage uses NumPy. If you skipped Stage 7, run `pip install numpy` first.)*

---

### 12.1 Vectors — Arrows With Math

A **vector** is just a list of numbers that we treat as a single object — like an arrow pointing in space. We store one in a NumPy array. Vectors can be added, scaled, and more — all at once:

```python
import numpy as np

a = np.array([3, 4])
b = np.array([1, 2])

print("Add:        ", a + b)        # [4 6]  — adds matching parts
print("Scale by 2: ", 2 * a)        # [6 8]  — multiplies every part
print("Subtract:   ", a - b)        # [2 2]
```

The **magnitude** (length) of a vector uses — surprise! — the Pythagorean theorem from Stage 5:

```python
import numpy as np

a = np.array([3, 4])
length = np.sqrt(a[0]**2 + a[1]**2)     # √(3² + 4²) = √25 = 5
print("Length of vector [3, 4]:", length)

# NumPy has a shortcut for this:
print("Length (the easy way):", np.linalg.norm(a))
```

---

### 12.2 The Dot Product — Multiplying Vectors

The **dot product** multiplies matching parts of two vectors and adds the results. It tells you how much two vectors point in the same direction:

```python
import numpy as np

a = np.array([3, 4])
b = np.array([1, 2])

dot = a[0]*b[0] + a[1]*b[1]      # 3*1 + 4*2 = 11
print("Dot product (by hand):", dot)

print("Dot product (NumPy):  ", np.dot(a, b))    # 11 — same answer
```

The dot product even lets you find the **angle** between two vectors (used constantly in video game physics!):

```python
import numpy as np

a = np.array([1, 0])
b = np.array([1, 1])

cos_angle = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle_degrees = np.degrees(np.arccos(cos_angle))
print(f"Angle between the vectors: {round(angle_degrees, 1)}°")    # 45.0°
```

---

### 12.3 Matrices — Grids of Numbers

A **matrix** is a 2D grid of numbers (rows and columns). In NumPy it's an array of arrays:

```python
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
print("Shape (rows, columns):", matrix.shape)    # (2, 3) — 2 rows, 3 columns
print("Top-left number:", matrix[0, 0])          # 1   (row 0, column 0)
print("Bottom-right number:", matrix[1, 2])      # 6   (row 1, column 2)
```

You can multiply two matrices together using the `@` symbol. Matrix multiplication combines information in a special way — it's how a computer rotates a 3D model or runs a layer of a neural network:

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("A @ B =")
print(A @ B)        # combines rows of A with columns of B
```

---

### 12.4 Solving Systems of Equations — The Grand Finale

Here's the real power. Suppose you have **two equations with two unknowns**:

```
2x + 1y = 8
1x + 3y = 9
```

Solving this by hand takes work. NumPy solves it in one line! We put the left-side numbers in a matrix and the right-side numbers in a vector:

```python
import numpy as np

# coefficients (the numbers in front of x and y)
A = np.array([[2, 1],
              [1, 3]])

# the answers on the right side
b = np.array([8, 9])

solution = np.linalg.solve(A, b)
print(f"x = {solution[0]}")     # 3.0
print(f"y = {solution[1]}")     # 2.0
```

Let's **check** it — plug the answers back in:

```python
import numpy as np

A = np.array([[2, 1], [1, 3]])
b = np.array([8, 9])
solution = np.linalg.solve(A, b)
x, y = solution

print("Check equation 1:", 2*x + 1*y, "should be 8")
print("Check equation 2:", 1*x + 3*y, "should be 9")
```

Back in Stage 4 you solved one equation. Now you can solve a whole *system* of them at once — even with 10, 100, or 1000 unknowns. That's the power of linear algebra. 🚀

**The math connection:** Vectors, the Pythagorean theorem, dot products, and equation-solving all live together in linear algebra. It's the language computers use to handle data, graphics, and AI.

---

### Stage 12 Challenges

1. Create two vectors `np.array([2, 5])` and `np.array([4, 1])`. Compute their dot product two ways (by hand and with `np.dot`) and confirm they match. Then find the angle between them.
2. Solve this system of equations with `np.linalg.solve`, then verify your answer by plugging it back in:
   ```
   3x + 2y = 16
   1x - 1y = 2
   ```
3. Build two 2×2 matrices of your choice and multiply them with `@`. Then swap the order (`B @ A` instead of `A @ B`). Do you get the same answer? (Matrix multiplication has a surprise in store!)

---

---

---

# 🔥 Grand Challenges — For True Math Wizards
### These 5 puzzles combine many stages at once. No code is given — figure it out! Take your time, they are the hardest yet.

1. **Hunt for a square root (Stages 9 + 4).** Without ever using `math.sqrt`, can you find the square root of 2 on your own? Start from a guess and repeatedly use your `derivative` tool from Stage 9 to nudge the guess closer to where `f(x) = x**2 - 2` hits zero. How many nudges until your guess stops changing? (This famous trick has a name — look up "Newton's method" once you've tried it.)

2. **Measure a circle by adding up slices (Stages 10 + 5).** The top edge of a circle of radius 1 follows a curve you can write with the Pythagorean theorem. Use your `integrate` tool from Stage 10 to find the area trapped under that curve. Can you predict the answer from the area of a full circle *before* you run it? How close does your estimate come?

3. **A surprising party (Stage 11).** In a room of just 23 people, how likely is it that two of them share a birthday? Most people guess "very unlikely." Simulate many random rooms and count for yourself. Were you surprised?

4. **A ratio hidden in the rabbits (Stages 6 + 3).** Take your Fibonacci numbers and divide each one by the number just before it. Keep going for bigger and bigger Fibonacci numbers. Do the answers settle toward a single value? Research what that number is called — it shows up in art and nature everywhere.

5. **Distance in 3D (Stages 12 + 5).** Stage 5's Pythagorean theorem worked for flat triangles. Invent your own version that finds the straight-line distance between two points floating in 3D space, then check your hand-built formula against what NumPy's vector tools give you. Do they agree?

---

---

# You Did It! 🏆

Congratulations! You have learned:

| Python | Math |
|--------|------|
| print, variables, operators, if/else | Arithmetic, inequalities |
| Loops, lists, functions | Sequences, mathematical functions |
| List comprehensions, math module | Statistics: mean, median, std deviation |
| Dictionaries, f-strings | Linear & quadratic equations |
| Classes and objects | Geometry: Pythagorean theorem, shapes, volumes |
| Recursion | Trigonometry: sin, cos, tan, unit circle |
| NumPy, Matplotlib | Linear regression, data visualization |
| Sorting & searching algorithms | Logarithms, exponential growth, limits |
| Helper functions, numerical methods | Calculus I: derivatives & rates of change |
| Accumulation loops (Riemann sums) | Calculus II: integrals & area under a curve |
| The `random` module, Monte Carlo simulation | Probability, expected value, law of large numbers |
| NumPy arrays as matrices & vectors | Linear algebra: vectors, matrices, solving systems |

### What to Learn Next
- **Python:** Try building a text adventure game, a website with Flask, or dive into machine learning with scikit-learn
- **Math:** Multivariable calculus, statistics & data science, or the math behind 3D graphics and AI

Keep going — you are already thinking like a real programmer and mathematician!
