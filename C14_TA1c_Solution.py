# TA1a-Step 1: Create a class "Dog"
class Dog:
  # TA1a-Step 2: Add the two properties to the 'Dog' class using variables.
  owner = True
  happy_wagging_tail = True
  
  # TA1c-Step 1: Initialise the instance variables through a constructor.
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
  
  # TA1a-Step 3: Add the two methods "run()" and "bark()" inside the 'Dog' class.
  def run(self):
      print("Yes")
  def bark(self):
      print("Woof-Woof")
      
# TA1c- Step 2: Create an object 'dog1' of class "Dog" and enter the values as 'Tommy', 'Labrador' inside the bracket.
dog1 = Dog("Tommy", "Labrador")
# 1. Print the name of 'dog1' object function.
print(dog1.name)
# 2. Print the breed of 'dog1' object function.
print(dog1.breed)
# 3. Print the owner and tail property values.
print(dog1.owner)
print(dog1.happy_wagging_tail)
# 4. Print the value returned by the 'run()' function of 'tommy'.
dog1.run()
# 5. Print the value returned by the 'bark()' function  of 'tommy'.
dog1.bark()