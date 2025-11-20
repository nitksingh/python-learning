# Object-Oriented Programming in Python

## Quick Summary

### Core OOP Concepts

| Concept | What It Is | Example |
|---------|-----------|---------|
| **Class** | Blueprint for creating objects | `class Dog:` |
| **Object** | Instance of a class | `my_dog = Dog()` |
| **Attribute** | Variable that belongs to an object | `my_dog.name = "Buddy"` |
| **Method** | Function that belongs to a class | `my_dog.bark()` |
| **Inheritance** | Creating new class from existing one | `class Puppy(Dog):` |
| **Encapsulation** | Hiding internal details | `@property` decorator |
| **Polymorphism** | Same method, different behavior | Method overriding |

### When to Use OOP vs Functions

| Use Functions When | Use Classes When |
|-------------------|------------------|
| Simple, independent operations | Related data and behavior together |
| Stateless transformations | Need to maintain state |
| One-time calculations | Creating multiple similar objects |
| Small utility operations | Building frameworks/libraries |

### Key Syntax Quick Reference

```python
# Basic class
class Person:
    def __init__(self, name):      # Constructor
        self.name = name           # Instance attribute
    
    def greet(self):               # Instance method
        return f"Hello, I'm {self.name}"

# Create object
person = Person("Alice")
print(person.greet())

# Inheritance
class Student(Person):             # Inherits from Person
    def __init__(self, name, grade):
        super().__init__(name)     # Call parent constructor
        self.grade = grade
```

---

## What is Object-Oriented Programming?

### The Problem: Code Without OOP

Imagine managing student data:

```python
# Without OOP - data and functions are separate
student1_name = "Alice"
student1_age = 20
student1_grades = [85, 90, 88]

student2_name = "Bob"
student2_age = 21
student2_grades = [78, 82, 85]

def calculate_average(grades):
    return sum(grades) / len(grades)

def print_student_info(name, age, grades):
    avg = calculate_average(grades)
    print(f"{name}, age {age}, average: {avg}")

print_student_info(student1_name, student1_age, student1_grades)
print_student_info(student2_name, student2_age, student2_grades)
```

**Problems:**
- Variables are scattered and unrelated
- Easy to pass wrong data (mixing up students)
- Hard to add new students
- No clear organization

---

### The Solution: With OOP

```python
# With OOP - data and behavior bundled together
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
    
    def print_info(self):
        avg = self.calculate_average()
        print(f"{self.name}, age {self.age}, average: {avg}")

# Create student objects
student1 = Student("Alice", 20, [85, 90, 88])
student2 = Student("Bob", 21, [78, 82, 85])

# Use them
student1.print_info()  # Alice, age 20, average: 87.67
student2.print_info()  # Bob, age 21, average: 81.67
```

**Benefits:**
- ✅ Data and behavior are bundled together
- ✅ Each student is independent
- ✅ Clear, organized structure
- ✅ Easy to create more students
- ✅ Easier to maintain and extend

---

## Classes and Objects: The Basics

### Understanding Classes and Objects

**Class** = Blueprint (like a cookie cutter)  
**Object** = Instance (like the actual cookie)

```python
# Class is the blueprint
class Dog:
    # This defines what ALL dogs have
    pass

# Objects are individual dogs created from the blueprint
dog1 = Dog()  # First dog object
dog2 = Dog()  # Second dog object
dog3 = Dog()  # Third dog object

# Each object is unique
print(dog1)  # <__main__.Dog object at 0x...>
print(dog2)  # <__main__.Dog object at 0x...> (different address)
print(dog1 == dog2)  # False (different objects)
```

---

### The Constructor: `__init__`

The `__init__` method is called automatically when creating an object. It initializes the object's attributes.

```python
class Dog:
    # __init__ is the constructor (initializer)
    # self refers to the object being created
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
        print(f"A dog named {name} is born!")

# When you create an object, __init__ is called automatically
dog1 = Dog("Buddy", 3)
# Output: A dog named Buddy is born!

print(dog1.name)  # Buddy
print(dog1.age)   # 3

# Create another dog with different data
dog2 = Dog("Max", 5)
# Output: A dog named Max is born!

print(dog2.name)  # Max
print(dog2.age)   # 5
```

**Key Points:**
- `__init__` is called automatically when creating an object
- `self` represents the instance being created
- `self.name` creates an attribute that belongs to that specific object
- Each object has its own copy of attributes

---

### Instance Methods

Methods are functions that belong to a class and operate on objects.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method - operates on the specific object (self)
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_age_in_dog_years(self):
        return self.age * 7
    
    def have_birthday(self):
        self.age += 1  # Modify the object's attribute
        return f"{self.name} is now {self.age} years old!"

# Create a dog
buddy = Dog("Buddy", 3)

# Call methods
print(buddy.bark())                    # Buddy says Woof!
print(buddy.get_age_in_dog_years())    # 21
print(buddy.have_birthday())           # Buddy is now 4 years old!
print(buddy.age)                       # 4 (attribute was modified)
```

**Why `self` is needed:**
```python
# When you call: buddy.bark()
# Python internally translates it to: Dog.bark(buddy)
# That's why we need 'self' - it receives the object itself!

# You can see this explicitly:
print(Dog.bark(buddy))  # Buddy says Woof! (same result)
```

---

### Real-World Example: Bank Account

```python
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance  # Default value of 0
        self.transactions = []  # Keep history
    
    def deposit(self, amount):
        """Add money to account."""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from account."""
        if amount > self.balance:
            return f"Insufficient funds. Balance: ${self.balance}"
        if amount > 0:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Invalid withdrawal amount"
    
    def get_balance(self):
        """Check current balance."""
        return f"Account {self.account_number} balance: ${self.balance}"
    
    def get_transaction_history(self):
        """Show all transactions."""
        if not self.transactions:
            return "No transactions yet"
        return "\n".join(self.transactions)

# Create accounts
alice_account = BankAccount("001", "Alice", 1000)
bob_account = BankAccount("002", "Bob")  # Uses default balance=0

# Use the accounts
print(alice_account.get_balance())        # Account 001 balance: $1000
print(alice_account.deposit(500))         # Deposited $500. New balance: $1500
print(alice_account.withdraw(200))        # Withdrew $200. New balance: $1300
print(alice_account.withdraw(2000))       # Insufficient funds. Balance: $1300

print("\nTransaction History:")
print(alice_account.get_transaction_history())
# Output:
# Deposit: +$500
# Withdrawal: -$200
```

---

## Class Attributes vs Instance Attributes

### Instance Attributes

Each object has its own copy.

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute - unique to each dog

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name)  # Buddy
print(dog2.name)  # Max

dog1.name = "Charlie"  # Changes only dog1
print(dog1.name)  # Charlie
print(dog2.name)  # Max (unchanged)
```

---

### Class Attributes

Shared by all objects of the class.

```python
class Dog:
    # Class attribute - shared by ALL dogs
    species = "Canis familiaris"
    total_dogs = 0  # Track total number of dogs
    
    def __init__(self, name):
        self.name = name  # Instance attribute
        Dog.total_dogs += 1  # Increment class attribute

# All dogs share the same species
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris
print(Dog.species)   # Canis familiaris (can access via class too)

# Both see the same total_dogs
print(Dog.total_dogs)  # 2
print(dog1.total_dogs) # 2
print(dog2.total_dogs) # 2

# Changing class attribute affects all instances
Dog.species = "Canis lupus familiaris"
print(dog1.species)  # Canis lupus familiaris
print(dog2.species)  # Canis lupus familiaris
```

---

### Real-World Example: Employee Counter

```python
class Employee:
    # Class attributes
    company_name = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, position, salary):
        # Instance attributes
        self.name = name
        self.position = position
        self.salary = salary
        self.employee_id = Employee.employee_count + 1
        
        # Update class attribute
        Employee.employee_count += 1
    
    def get_info(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Position: {self.position}"

# Create employees
emp1 = Employee("Alice", "Developer", 80000)
emp2 = Employee("Bob", "Designer", 75000)
emp3 = Employee("Charlie", "Manager", 90000)

print(f"Total employees at {Employee.company_name}: {Employee.employee_count}")
# Output: Total employees at TechCorp: 3

print(emp1.get_info())  # ID: 1, Name: Alice, Position: Developer
print(emp2.get_info())  # ID: 2, Name: Bob, Position: Designer
print(emp3.get_info())  # ID: 3, Name: Charlie, Position: Manager
```

---

## Special Methods (Magic Methods)

Special methods (also called "dunder" methods for double underscore) allow your objects to work with Python's built-in operations.

### `__str__` and `__repr__`

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    # __str__ for human-readable string (print, str())
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
    
    # __repr__ for developer-friendly representation (debugging)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

book = Book("1984", "George Orwell", 1949)

print(book)          # '1984' by George Orwell (1949)  [uses __str__]
print(str(book))     # '1984' by George Orwell (1949)  [uses __str__]
print(repr(book))    # Book('1984', 'George Orwell', 1949)  [uses __repr__]

# In Python console or debugging
book  # Shows __repr__: Book('1984', 'George Orwell', 1949)
```

---

### Comparison Methods

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
    # __eq__ for equality (==)
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    # __lt__ for less than (<)
    def __lt__(self, other):
        return self.age < other.age
    
    # __le__ for less than or equal (<=)
    def __le__(self, other):
        return self.age <= other.age

alice = Person("Alice", 30)
bob = Person("Bob", 25)
alice2 = Person("Alice", 30)

# Equality
print(alice == alice2)  # True (same name and age)
print(alice == bob)     # False

# Comparison
print(bob < alice)      # True (25 < 30)
print(alice < bob)      # False

# Sorting works now!
people = [alice, bob, Person("Charlie", 35)]
sorted_people = sorted(people)  # Sorts by age
for person in sorted_people:
    print(person)
# Output:
# Bob (25)
# Alice (30)
# Charlie (35)
```

---

### Container Methods

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    # __len__ for len()
    def __len__(self):
        return len(self.songs)
    
    # __getitem__ for indexing playlist[0]
    def __getitem__(self, index):
        return self.songs[index]
    
    # __contains__ for 'in' operator
    def __contains__(self, song):
        return song in self.songs
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __str__(self):
        return f"Playlist '{self.name}' with {len(self)} songs"

# Create playlist
my_playlist = Playlist("Favorites")
my_playlist.add_song("Song A")
my_playlist.add_song("Song B")
my_playlist.add_song("Song C")

# Use built-in functions
print(len(my_playlist))        # 3 (uses __len__)
print(my_playlist[0])          # Song A (uses __getitem__)
print("Song B" in my_playlist) # True (uses __contains__)

# Can iterate because of __getitem__
for song in my_playlist:
    print(song)
# Output:
# Song A
# Song B
# Song C
```

---

### Common Special Methods Reference

| Method | Operation | Example |
|--------|-----------|---------|
| `__init__` | Constructor | `obj = MyClass()` |
| `__str__` | String for print() | `print(obj)` |
| `__repr__` | Developer string | `repr(obj)` |
| `__len__` | Length | `len(obj)` |
| `__getitem__` | Index access | `obj[key]` |
| `__setitem__` | Set item | `obj[key] = value` |
| `__contains__` | Membership test | `item in obj` |
| `__eq__` | Equality | `obj1 == obj2` |
| `__lt__` | Less than | `obj1 < obj2` |
| `__add__` | Addition | `obj1 + obj2` |
| `__call__` | Call as function | `obj()` |

---

## Inheritance

Inheritance allows you to create a new class based on an existing class, inheriting its attributes and methods.

### Basic Inheritance

```python
# Parent class (Base class)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return "Some generic sound"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Child class (Derived class) - inherits from Animal
class Dog(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} says Woof!"
    
    def fetch(self):  # New method specific to Dog
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} says Meow!"
    
    def scratch(self):  # New method specific to Cat
        return f"{self.name} is scratching the furniture"

# Create objects
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

# Use inherited methods
print(dog.sleep())         # Buddy is sleeping (from Animal)
print(cat.sleep())         # Whiskers is sleeping (from Animal)

# Use overridden methods
print(dog.make_sound())    # Buddy says Woof! (overridden in Dog)
print(cat.make_sound())    # Whiskers says Meow! (overridden in Cat)

# Use child-specific methods
print(dog.fetch())         # Buddy is fetching the ball
print(cat.scratch())       # Whiskers is scratching the furniture
```

---

### Using `super()` to Extend Parent Functionality

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

class Student(Person):
    def __init__(self, name, age, student_id, major):
        # Call parent's __init__ to set name and age
        super().__init__(name, age)
        # Add student-specific attributes
        self.student_id = student_id
        self.major = major
    
    def introduce(self):
        # Extend parent's introduce method
        parent_intro = super().introduce()
        return f"{parent_intro}. I'm studying {self.major}"

class Teacher(Person):
    def __init__(self, name, age, subject, years_experience):
        super().__init__(name, age)
        self.subject = subject
        self.years_experience = years_experience
    
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro}. I teach {self.subject}"

# Create objects
student = Student("Alice", 20, "S12345", "Computer Science")
teacher = Teacher("Dr. Smith", 45, "Physics", 20)

print(student.introduce())
# Output: Hi, I'm Alice and I'm 20 years old. I'm studying Computer Science

print(teacher.introduce())
# Output: Hi, I'm Dr. Smith and I'm 45 years old. I teach Physics
```

---

### Real-World Example: Payment System

```python
class Payment:
    """Base payment class"""
    def __init__(self, amount):
        self.amount = amount
        self.status = "pending"
    
    def process(self):
        """To be implemented by subclasses"""
        raise NotImplementedError("Subclass must implement process()")
    
    def get_receipt(self):
        return f"Payment of ${self.amount} - Status: {self.status}"

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number, cvv):
        super().__init__(amount)
        self.card_number = card_number[-4:]  # Store only last 4 digits
        self.cvv = cvv
    
    def process(self):
        # Simulate payment processing
        print(f"Processing credit card ending in {self.card_number}...")
        self.status = "completed"
        return f"Credit card payment of ${self.amount} successful"

class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    
    def process(self):
        print(f"Processing PayPal payment for {self.email}...")
        self.status = "completed"
        return f"PayPal payment of ${self.amount} successful"

class CryptoPayment(Payment):
    def __init__(self, amount, wallet_address, crypto_type):
        super().__init__(amount)
        self.wallet_address = wallet_address
        self.crypto_type = crypto_type
    
    def process(self):
        print(f"Processing {self.crypto_type} payment to {self.wallet_address}...")
        self.status = "completed"
        return f"{self.crypto_type} payment of ${self.amount} successful"

# Use different payment methods
def process_payment(payment):
    """Process any type of payment - polymorphism in action!"""
    result = payment.process()
    print(result)
    print(payment.get_receipt())
    print()

# Create different payment types
credit_payment = CreditCardPayment(100, "1234567812345678", "123")
paypal_payment = PayPalPayment(50, "user@example.com")
crypto_payment = CryptoPayment(200, "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb", "Bitcoin")

# Process all payments using the same function
process_payment(credit_payment)
process_payment(paypal_payment)
process_payment(crypto_payment)

# Output:
# Processing credit card ending in 5678...
# Credit card payment of $100 successful
# Payment of $100 - Status: completed
#
# Processing PayPal payment for user@example.com...
# PayPal payment of $50 successful
# Payment of $50 - Status: completed
#
# Processing Bitcoin payment to 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb...
# Bitcoin payment of $200 successful
# Payment of $200 - Status: completed
```

---

## Polymorphism

Polymorphism means "many forms" - same method name, different behavior.

### Method Overriding (Runtime Polymorphism)

```python
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c

# Create different shapes
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(3, 4, 5)
]

# Same method call, different behavior!
for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")

# Output:
# Rectangle:
#   Area: 50.00
#   Perimeter: 30.00
# Circle:
#   Area: 153.94
#   Perimeter: 43.98
# Triangle:
#   Area: 6.00
#   Perimeter: 12.00
```

---

### Duck Typing (Python's Polymorphism)

"If it walks like a duck and quacks like a duck, it's a duck."

```python
# No common parent class needed!
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop!"

# Function works with ANY object that has a speak() method
def make_it_speak(thing):
    print(thing.speak())

# All work, even though they're unrelated classes
dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)    # Woof!
make_it_speak(cat)    # Meow!
make_it_speak(robot)  # Beep boop!
```

---

## Encapsulation and Properties

### Private Attributes (Convention)

Python uses naming conventions for "private" attributes (name mangling with `__`).

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner           # Public
        self._balance = balance      # Protected (convention: don't access directly)
        self.__pin = "1234"          # Private (name mangled)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def get_balance(self):
        return self._balance

account = BankAccount("Alice", 1000)

# Public - OK to access
print(account.owner)  # Alice

# Protected - can access but shouldn't (convention)
print(account._balance)  # 1000 (works but not recommended)

# Private - name mangled to prevent access
# print(account.__pin)  # AttributeError

# But still accessible (Python doesn't truly enforce privacy)
print(account._BankAccount__pin)  # 1234 (name mangling)

# Proper way to access balance
print(account.get_balance())  # 1000
```

---

### Properties with `@property`

Properties let you use getter/setter methods like attributes.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    # Getter - allows reading like an attribute
    @property
    def celsius(self):
        return self._celsius
    
    # Setter - allows setting like an attribute
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Use like attributes, but validation happens!
temp = Temperature(25)
print(temp.celsius)     # 25 (calls getter)
print(temp.fahrenheit)  # 77.0

temp.celsius = 30       # Calls setter
print(temp.celsius)     # 30
print(temp.fahrenheit)  # 86.0

temp.fahrenheit = 32    # Calls fahrenheit setter
print(temp.celsius)     # 0.0

# Validation works
try:
    temp.celsius = -500  # Raises ValueError
except ValueError as e:
    print(e)  # Temperature below absolute zero!
```

---

### Real-World Example: User Account with Validation

```python
class UserAccount:
    def __init__(self, username, email):
        self._username = username
        self._email = email
        self._is_active = True
        self._login_attempts = 0
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters")
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric")
        self._username = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format")
        self._email = value
    
    @property
    def is_active(self):
        return self._is_active
    
    def deactivate(self):
        self._is_active = False
    
    def record_failed_login(self):
        self._login_attempts += 1
        if self._login_attempts >= 3:
            self.deactivate()
            return "Account locked due to too many failed attempts"
        return f"Failed login attempt {self._login_attempts}/3"

# Create account
user = UserAccount("alice123", "alice@example.com")

print(user.username)  # alice123
print(user.email)     # alice@example.com
print(user.is_active) # True

# Validation works
try:
    user.username = "ab"  # Too short
except ValueError as e:
    print(e)  # Username must be at least 3 characters

try:
    user.email = "invalid"  # No @ or .
except ValueError as e:
    print(e)  # Invalid email format

# Track failed logins
print(user.record_failed_login())  # Failed login attempt 1/3
print(user.record_failed_login())  # Failed login attempt 2/3
print(user.record_failed_login())  # Account locked due to too many failed attempts
print(user.is_active)              # False
```

---

## Class Methods and Static Methods

### Instance Methods

Regular methods that operate on instance (`self`).

```python
class MyClass:
    def instance_method(self):
        return f"Called on {self}"
```

---

### Class Methods

Methods that operate on the class itself, not instances.

```python
class Employee:
    company = "TechCorp"
    raise_percentage = 1.05
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def apply_raise(self):
        """Instance method - operates on instance"""
        self.salary = int(self.salary * Employee.raise_percentage)
    
    @classmethod
    def set_raise_percentage(cls, percentage):
        """Class method - operates on class"""
        cls.raise_percentage = percentage
    
    @classmethod
    def from_string(cls, emp_string):
        """Alternative constructor using class method"""
        name, salary = emp_string.split('-')
        return cls(name, int(salary))

# Use class method to change class attribute
Employee.set_raise_percentage(1.10)

emp1 = Employee("Alice", 50000)
emp1.apply_raise()
print(emp1.salary)  # 55000 (10% raise)

# Use class method as alternative constructor
emp2 = Employee.from_string("Bob-60000")
print(emp2.name)    # Bob
print(emp2.salary)  # 60000
```

---

### Static Methods

Methods that don't operate on instance or class - just regular functions inside the class.

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        """Static method - no self or cls needed"""
        return x + y
    
    @staticmethod
    def is_even(num):
        return num % 2 == 0
    
    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

# Call without creating instance
print(MathOperations.add(5, 3))        # 8
print(MathOperations.is_even(4))       # True
print(MathOperations.is_prime(17))     # True

# Can also call from instance (but unusual)
math = MathOperations()
print(math.add(10, 20))                # 30
```

---

### When to Use Each

| Method Type | Use When | Access To |
|-------------|----------|-----------|
| **Instance Method** | Need to access/modify instance data | `self` (instance) |
| **Class Method** | Need to access/modify class data or create alternative constructors | `cls` (class) |
| **Static Method** | Logically belongs to class but doesn't need instance or class data | Nothing special |

---

## Practical Design Patterns

### Factory Pattern (Using Class Methods)

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def __str__(self):
        return f"Pizza with {', '.join(self.ingredients)}"
    
    @classmethod
    def margherita(cls):
        """Factory method for Margherita pizza"""
        return cls(['mozzarella', 'tomatoes', 'basil'])
    
    @classmethod
    def pepperoni(cls):
        """Factory method for Pepperoni pizza"""
        return cls(['mozzarella', 'tomatoes', 'pepperoni'])
    
    @classmethod
    def hawaiian(cls):
        """Factory method for Hawaiian pizza"""
        return cls(['mozzarella', 'tomatoes', 'ham', 'pineapple'])

# Easy to create standard pizzas
pizza1 = Pizza.margherita()
pizza2 = Pizza.pepperoni()
pizza3 = Pizza.hawaiian()

print(pizza1)  # Pizza with mozzarella, tomatoes, basil
print(pizza2)  # Pizza with mozzarella, tomatoes, pepperoni
print(pizza3)  # Pizza with mozzarella, tomatoes, ham, pineapple

# Can also create custom
custom = Pizza(['mozzarella', 'olives', 'mushrooms'])
print(custom)  # Pizza with mozzarella, olives, mushrooms
```

---

### Singleton Pattern

```python
class DatabaseConnection:
    _instance = None  # Class attribute to store single instance
    
    def __new__(cls):
        """Control object creation"""
        if cls._instance is None:
            print("Creating new database connection...")
            cls._instance = super().__new__(cls)
            cls._instance.connected = True
        return cls._instance
    
    def query(self, sql):
        return f"Executing: {sql}"

# Multiple calls return the same instance
db1 = DatabaseConnection()  # Creating new database connection...
db2 = DatabaseConnection()  # (no message, reuses existing)
db3 = DatabaseConnection()  # (no message, reuses existing)

print(db1 is db2)  # True (same object)
print(db2 is db3)  # True (same object)

# All share the same state
db1.connected = False
print(db2.connected)  # False (same object)
```

---

## Common Interview Problems Using OOP

### Problem 1: LRU Cache (Design)

```python
class Node:
    """Doubly linked list node"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """Least Recently Used Cache implementation"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # Dummy head and tail for easier list manipulation
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_front(self, node):
        """Add node right after head (most recently used)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Remove node from its current position"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get(self, key):
        """Get value and mark as recently used"""
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_to_front(node)
            return node.value
        return -1
    
    def put(self, key, value):
        """Put key-value pair, evict LRU if needed"""
        if key in self.cache:
            # Update existing
            self._remove_node(self.cache[key])
        
        node = Node(key, value)
        self._add_to_front(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            # Remove least recently used (node before tail)
            lru = self.tail.prev
            self._remove_node(lru)
            del self.cache[lru.key]

# Test
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # 1
cache.put(3, 3)        # Evicts key 2
print(cache.get(2))    # -1 (not found)
cache.put(4, 4)        # Evicts key 1
print(cache.get(1))    # -1 (not found)
print(cache.get(3))    # 3
print(cache.get(4))    # 4
```

---

### Problem 2: Design a Parking Lot

```python
from enum import Enum
from datetime import datetime

class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    TRUCK = 3

class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class ParkingSpot:
    def __init__(self, spot_number, vehicle_type):
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type
        self.vehicle = None
        self.is_available = True
    
    def park_vehicle(self, vehicle):
        if self.is_available and self.vehicle_type == vehicle.vehicle_type:
            self.vehicle = vehicle
            self.is_available = False
            return True
        return False
    
    def remove_vehicle(self):
        vehicle = self.vehicle
        self.vehicle = None
        self.is_available = True
        return vehicle

class Ticket:
    def __init__(self, ticket_id, vehicle, spot, entry_time):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = entry_time
        self.exit_time = None
        self.fee = 0

class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []
        self.tickets = {}
        self.ticket_counter = 1
    
    def add_spot(self, spot):
        self.spots.append(spot)
    
    def find_available_spot(self, vehicle_type):
        for spot in self.spots:
            if spot.is_available and spot.vehicle_type == vehicle_type:
                return spot
        return None
    
    def park_vehicle(self, vehicle):
        spot = self.find_available_spot(vehicle.vehicle_type)
        if spot is None:
            return None, "No available spots"
        
        if spot.park_vehicle(vehicle):
            ticket = Ticket(
                self.ticket_counter,
                vehicle,
                spot,
                datetime.now()
            )
            self.tickets[ticket.ticket_id] = ticket
            self.ticket_counter += 1
            return ticket, f"Parked at spot {spot.spot_number}"
        return None, "Failed to park"
    
    def unpark_vehicle(self, ticket_id):
        if ticket_id not in self.tickets:
            return "Invalid ticket"
        
        ticket = self.tickets[ticket_id]
        ticket.exit_time = datetime.now()
        
        # Calculate fee (e.g., $5 per hour)
        duration = (ticket.exit_time - ticket.entry_time).seconds / 3600
        ticket.fee = round(duration * 5, 2)
        
        ticket.spot.remove_vehicle()
        return f"Fee: ${ticket.fee}"

# Test the parking lot
parking_lot = ParkingLot("Main Street Parking")

# Add spots
parking_lot.add_spot(ParkingSpot(1, VehicleType.CAR))
parking_lot.add_spot(ParkingSpot(2, VehicleType.CAR))
parking_lot.add_spot(ParkingSpot(3, VehicleType.MOTORCYCLE))
parking_lot.add_spot(ParkingSpot(4, VehicleType.TRUCK))

# Park vehicles
car1 = Vehicle("ABC123", VehicleType.CAR)
ticket1, msg1 = parking_lot.park_vehicle(car1)
print(msg1)  # Parked at spot 1

car2 = Vehicle("XYZ789", VehicleType.CAR)
ticket2, msg2 = parking_lot.park_vehicle(car2)
print(msg2)  # Parked at spot 2

motorcycle = Vehicle("MOTO123", VehicleType.MOTORCYCLE)
ticket3, msg3 = parking_lot.park_vehicle(motorcycle)
print(msg3)  # Parked at spot 3

# Try to park when full
car3 = Vehicle("FULL123", VehicleType.CAR)
ticket4, msg4 = parking_lot.park_vehicle(car3)
print(msg4)  # No available spots

# Unpark
import time
time.sleep(2)  # Simulate some time passing
print(parking_lot.unpark_vehicle(ticket1.ticket_id))  # Fee: $0.0 (less than an hour)
```

---

### Problem 3: Design a Library System

```python
from datetime import datetime, timedelta

class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_available = True
    
    def __str__(self):
        status = "Available" if self.is_available else "Checked out"
        return f"'{self.title}' by {self.author} ({status})"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        self.fines = 0
    
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    
    def add_fine(self, amount):
        self.fines += amount

class Transaction:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.checkout_date = datetime.now()
        self.due_date = self.checkout_date + timedelta(days=14)  # 2 weeks
        self.return_date = None

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}  # isbn -> Book
        self.members = {}  # member_id -> Member
        self.transactions = []
        self.fine_per_day = 1.0  # $1 per day late
    
    def add_book(self, book):
        self.books[book.isbn] = book
    
    def add_member(self, member):
        self.members[member.member_id] = member
    
    def checkout_book(self, isbn, member_id):
        if isbn not in self.books:
            return "Book not found"
        if member_id not in self.members:
            return "Member not found"
        
        book = self.books[isbn]
        member = self.members[member_id]
        
        if not book.is_available:
            return f"'{book.title}' is not available"
        
        # Create transaction
        transaction = Transaction(book, member)
        self.transactions.append(transaction)
        
        # Update book and member
        book.is_available = False
        member.borrow_book(book)
        
        due = transaction.due_date.strftime("%Y-%m-%d")
        return f"'{book.title}' checked out to {member.name}. Due: {due}"
    
    def return_book(self, isbn, member_id):
        if isbn not in self.books or member_id not in self.members:
            return "Book or member not found"
        
        book = self.books[isbn]
        member = self.members[member_id]
        
        # Find transaction
        transaction = None
        for t in self.transactions:
            if t.book == book and t.member == member and t.return_date is None:
                transaction = t
                break
        
        if transaction is None:
            return "No active checkout found"
        
        # Mark as returned
        transaction.return_date = datetime.now()
        book.is_available = True
        member.return_book(book)
        
        # Calculate fine if late
        if transaction.return_date > transaction.due_date:
            days_late = (transaction.return_date - transaction.due_date).days
            fine = days_late * self.fine_per_day
            member.add_fine(fine)
            return f"'{book.title}' returned. Late by {days_late} days. Fine: ${fine:.2f}"
        
        return f"'{book.title}' returned on time"
    
    def search_books(self, query):
        """Search books by title or author"""
        results = []
        query_lower = query.lower()
        for book in self.books.values():
            if query_lower in book.title.lower() or query_lower in book.author.lower():
                results.append(book)
        return results

# Test the library system
library = Library("City Library")

# Add books
library.add_book(Book("978-0-7475-3269-9", "Harry Potter", "J.K. Rowling"))
library.add_book(Book("978-0-261-10238-4", "The Hobbit", "J.R.R. Tolkien"))
library.add_book(Book("978-0-06-112008-4", "To Kill a Mockingbird", "Harper Lee"))

# Add members
library.add_member(Member("M001", "Alice"))
library.add_member(Member("M002", "Bob"))

# Checkout
print(library.checkout_book("978-0-7475-3269-9", "M001"))
# Output: 'Harry Potter' checked out to Alice. Due: 2025-12-03

# Try to checkout same book
print(library.checkout_book("978-0-7475-3269-9", "M002"))
# Output: 'Harry Potter' is not available

# Return
print(library.return_book("978-0-7475-3269-9", "M001"))
# Output: 'Harry Potter' returned on time

# Search
results = library.search_books("harry")
for book in results:
    print(book)
# Output: 'Harry Potter' by J.K. Rowling (Available)
```

---

## When to Use OOP vs Functions

### Use Functions When:

```python
# Simple, stateless operations
def calculate_tax(amount, rate):
    return amount * rate

def convert_temperature(celsius):
    return celsius * 9/5 + 32

# One-time calculations
def get_area_of_circle(radius):
    return 3.14159 * radius ** 2
```

### Use Classes When:

```python
# Need to maintain state
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
    
    def add_item(self, item, price):
        self.items.append(item)
        self.total += price

# Related data and behavior
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []
    
    def create_post(self, content):
        self.posts.append(content)

# Creating multiple similar objects
users = [
    User("alice", "alice@example.com"),
    User("bob", "bob@example.com")
]
```

---

## Best Practices

### 1. Single Responsibility Principle

Each class should have one job.

```python
# Bad - class does too much
class User:
    def __init__(self, name):
        self.name = name
    
    def save_to_database(self):
        # Database logic here
        pass
    
    def send_email(self):
        # Email logic here
        pass

# Good - separate concerns
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        # Database logic here
        pass

class EmailService:
    def send_welcome_email(self, user):
        # Email logic here
        pass
```

---

### 2. Composition Over Inheritance

Prefer "has-a" relationships over "is-a". Composition provides more flexibility and avoids the problems of deep inheritance hierarchies.

#### The Problem with Inheritance

```python
# Bad - Inheritance hierarchy becomes rigid and complex

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        return f"{self.name} is working"

class Manager(Employee):
    def manage_team(self):
        return f"{self.name} is managing"

class Developer(Employee):
    def write_code(self):
        return f"{self.name} is coding"

# What if someone is BOTH a Manager AND Developer?
# Can't inherit from both effectively (multiple inheritance is messy)

# What if a Manager needs to write code sometimes?
# Or a Developer needs to manage temporarily?
# Inheritance is too rigid!
```

---

#### Real-World Scenario 1: Employee Roles

**Problem:** An employee can have multiple roles that change over time.

```python
# Bad - Using inheritance
class EmployeeManagerDeveloper(Manager, Developer):
    # Multiple inheritance - confusing and hard to maintain
    pass

# What if they also need to be a Tester? Create another class?
# What if roles change? Create new objects?
```

**Solution:** Use composition with role objects.

```python
# Good - Using composition

class DevelopmentSkill:
    def write_code(self):
        return "Writing code"
    
    def review_code(self):
        return "Reviewing code"

class ManagementSkill:
    def manage_team(self):
        return "Managing team"
    
    def conduct_meetings(self):
        return "Conducting meetings"

class TestingSkill:
    def write_tests(self):
        return "Writing tests"
    
    def perform_qa(self):
        return "Performing QA"

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.skills = []  # Can have any combination of skills
    
    def add_skill(self, skill):
        self.skills.append(skill)
    
    def remove_skill(self, skill):
        self.skills.remove(skill)
    
    def perform_task(self, task_name):
        # Delegate to appropriate skill
        for skill in self.skills:
            if hasattr(skill, task_name):
                method = getattr(skill, task_name)
                return f"{self.name}: {method()}"
        return f"{self.name}: Cannot perform {task_name}"

# Create employees with different skill combinations
alice = Employee("Alice", 100000)
alice.add_skill(DevelopmentSkill())
alice.add_skill(ManagementSkill())

bob = Employee("Bob", 90000)
bob.add_skill(DevelopmentSkill())
bob.add_skill(TestingSkill())

charlie = Employee("Charlie", 85000)
charlie.add_skill(TestingSkill())

# Employees can perform tasks based on their skills
print(alice.perform_task("write_code"))      # Alice: Writing code
print(alice.perform_task("manage_team"))     # Alice: Managing team
print(bob.perform_task("write_tests"))       # Bob: Writing tests
print(charlie.perform_task("manage_team"))   # Charlie: Cannot perform manage_team

# Easy to add/remove skills
alice.remove_skill(ManagementSkill())  # Alice is no longer managing
bob.add_skill(ManagementSkill())       # Bob is promoted to manager
```

**Benefits:**
- ✅ Flexible: Skills can be added/removed dynamically
- ✅ No multiple inheritance complexity
- ✅ Easy to add new skills without changing existing code
- ✅ Employees can have any combination of skills

---

#### Real-World Scenario 2: GUI Components

**Problem:** UI components need different features (clickable, draggable, resizable).

```python
# Bad - Inheritance leads to explosion of classes

class Button:
    pass

class ClickableButton(Button):
    pass

class DraggableButton(Button):
    pass

class ResizableButton(Button):
    pass

class ClickableDraggableButton(Button):  # Combination 1
    pass

class ClickableResizableButton(Button):  # Combination 2
    pass

class DraggableResizableButton(Button):  # Combination 3
    pass

class ClickableDraggableResizableButton(Button):  # Combination 4
    pass

# 3 features = 7 extra classes!
# Add one more feature = 15 classes total!
```

**Solution:** Use composition with behavior objects.

```python
# Good - Using composition

class Clickable:
    """Behavior for clickable items"""
    def click(self):
        return "Clicked!"

class Draggable:
    """Behavior for draggable items"""
    def __init__(self):
        self.position = (0, 0)
    
    def drag(self, x, y):
        self.position = (x, y)
        return f"Dragged to {self.position}"

class Resizable:
    """Behavior for resizable items"""
    def __init__(self):
        self.size = (100, 50)
    
    def resize(self, width, height):
        self.size = (width, height)
        return f"Resized to {self.size}"

class UIComponent:
    """Base UI component using composition"""
    def __init__(self, name):
        self.name = name
        self.behaviors = {}
    
    def add_behavior(self, behavior_name, behavior):
        self.behaviors[behavior_name] = behavior
    
    def __getattr__(self, name):
        # Delegate to behaviors
        for behavior in self.behaviors.values():
            if hasattr(behavior, name):
                return getattr(behavior, name)
        raise AttributeError(f"No behavior supports '{name}'")

# Create components with any combination of behaviors
button = UIComponent("Submit Button")
button.add_behavior("clickable", Clickable())
print(button.click())  # Clicked!

window = UIComponent("Main Window")
window.add_behavior("draggable", Draggable())
window.add_behavior("resizable", Resizable())
print(window.drag(100, 200))      # Dragged to (100, 200)
print(window.resize(800, 600))    # Resized to (800, 600)

icon = UIComponent("App Icon")
icon.add_behavior("clickable", Clickable())
icon.add_behavior("draggable", Draggable())
print(icon.click())               # Clicked!
print(icon.drag(50, 50))          # Dragged to (50, 50)
```

**Benefits:**
- ✅ Mix and match behaviors freely
- ✅ No class explosion
- ✅ Add new behaviors without touching existing code
- ✅ Runtime flexibility

---

#### Real-World Scenario 3: Vehicle Systems

```python
# Instead of rigid inheritance hierarchies
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine started ({self.horsepower}hp)"

class ElectricMotor:
    def __init__(self, kilowatts):
        self.kilowatts = kilowatts
    
    def start(self):
        return f"Electric motor started ({self.kilowatts}kW)"

class GPSSystem:
    def navigate(self, destination):
        return f"Navigating to {destination}"

class EntertainmentSystem:
    def play_music(self, song):
        return f"Playing: {song}"

class AutoPilot:
    def engage(self):
        return "Autopilot engaged"

# Flexible vehicle composition
class Vehicle:
    def __init__(self, name):
        self.name = name
        self.power_source = None
        self.systems = {}
    
    def set_power_source(self, power_source):
        self.power_source = power_source
    
    def add_system(self, system_name, system):
        self.systems[system_name] = system
    
    def start(self):
        if self.power_source:
            return f"{self.name}: {self.power_source.start()}"
        return f"{self.name}: No power source"
    
    def use_system(self, system_name, method, *args):
        if system_name in self.systems:
            system = self.systems[system_name]
            if hasattr(system, method):
                return getattr(system, method)(*args)
        return f"System {system_name} not available"

# Create different vehicle configurations
# Basic gas car
basic_car = Vehicle("Basic Car")
basic_car.set_power_source(Engine(150))
print(basic_car.start())  # Basic Car: Engine started (150hp)

# Luxury gas car with features
luxury_car = Vehicle("Luxury Car")
luxury_car.set_power_source(Engine(400))
luxury_car.add_system("gps", GPSSystem())
luxury_car.add_system("entertainment", EntertainmentSystem())
print(luxury_car.start())
print(luxury_car.use_system("gps", "navigate", "Airport"))
print(luxury_car.use_system("entertainment", "play_music", "Highway to Hell"))

# Tesla-like electric car with autopilot
tesla = Vehicle("Tesla Model S")
tesla.set_power_source(ElectricMotor(670))
tesla.add_system("gps", GPSSystem())
tesla.add_system("entertainment", EntertainmentSystem())
tesla.add_system("autopilot", AutoPilot())
print(tesla.start())
print(tesla.use_system("autopilot", "engage"))

# Hybrid (could have both engine and electric motor!)
hybrid = Vehicle("Hybrid SUV")
hybrid.set_power_source(Engine(200))  # Primary power
# Could store electric motor separately
hybrid.add_system("gps", GPSSystem())
print(hybrid.start())
```

**Benefits:**
- ✅ Easy to swap power sources
- ✅ Add/remove systems independently
- ✅ Can create any vehicle configuration
- ✅ No rigid inheritance hierarchy

---

#### When to Use Inheritance vs Composition

| Use Inheritance When | Use Composition When |
|---------------------|---------------------|
| Clear "is-a" relationship | "Has-a" or "uses-a" relationship |
| Behavior rarely changes | Need flexibility to change behavior |
| Simple, shallow hierarchy | Multiple features that can be mixed |
| Few variations | Many possible combinations |
| Example: Dog IS-A Animal | Example: Car HAS-A Engine |

**Rule of Thumb:** 
- If you can say "X **IS A** Y" → Consider inheritance
- If you can say "X **HAS A** Y" → Use composition
- When in doubt → Use composition (more flexible)

---

#### Summary: Why Composition Wins

**Problems with Deep Inheritance:**
1. Rigid structure - hard to change
2. Class explosion - too many combinations
3. Tight coupling - changes cascade
4. Multiple inheritance complexity

**Benefits of Composition:**
1. ✅ Flexible - add/remove behaviors at runtime
2. ✅ Reusable - mix and match components
3. ✅ Maintainable - change one component without affecting others
4. ✅ Testable - test components independently
5. ✅ Scalable - add new features without modifying existing code

---

### 3. Use Meaningful Names

```python
# Bad
class D:
    def __init__(self, n, a):
        self.n = n
        self.a = a

# Good
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

### 4. Keep Methods Short and Focused

```python
# Bad - method does too much
def process_order(self, order):
    # 50 lines of code doing everything...
    pass

# Good - break into smaller methods
def process_order(self, order):
    self.validate_order(order)
    self.calculate_total(order)
    self.charge_payment(order)
    self.send_confirmation(order)
```

---

## Summary

### Key Takeaways:

1. **Classes** are blueprints, **objects** are instances
2. **`__init__`** initializes objects, **`self`** refers to the instance
3. **Instance attributes** are unique per object, **class attributes** are shared
4. **Special methods** (`__str__`, `__eq__`, etc.) integrate with Python operations
5. **Inheritance** allows code reuse and extension
6. **`super()`** calls parent class methods
7. **Polymorphism** enables same interface, different behavior
8. **Encapsulation** with properties provides controlled access
9. **Class methods** operate on class, **static methods** are utilities
10. **Use OOP** when you need state and related behavior together

### The OOP Mindset:

- Think in terms of **objects** (nouns) and **actions** (verbs)
- **Objects** have **attributes** (what they are) and **methods** (what they do)
- **Inheritance** models "is-a" relationships
- **Composition** models "has-a" relationships
- **Encapsulation** hides complexity
- **Polymorphism** provides flexibility

---

Happy coding! 🐍

