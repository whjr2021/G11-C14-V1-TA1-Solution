# TA1a-Step 1: Create a class "Dog"
class Dog:
  # TA1a-Step 2: Add the two properties to the 'Dog' class using variables.
  owner = True
  happy_wagging_tail = True

  # TA1a-Step 3: Add the two methods "run()" and "bark()" inside the 'Dog' class.
  def run(self):
      print("Yes")
  def bark(self):
      print("Woof-Woof")
      
# TA1a-Step 4: Create an instance or object of the 'Dog' class. Name them as 'tommy', 'scooby', 'dodo' 
tommy = Dog()
scooby  = Dog()
dodo = Dog()

# TA1b-Step 1: Access the properties and methods of 'tommy'
# 1. Print all properties of the 'tommy' object.
print(tommy.owner)
print(tommy.happy_wagging_tail)
# 2. Print the value returned by the 'run()' function of 'tommy'.
tommy.run()
# 3. Print the value returned by the 'bark()' function  of 'tommy'.
tommy.bark()
print("-------------------")
# TA1b-Step 2: Access the properties and methods of 'dodo'
# 1. Print all properties of the 'dodo' object.
print(dodo.owner)
print(dodo.happy_wagging_tail)
# 2. Print the value returned by the 'run()' function  of 'dodo'.
dodo.run()
# 3. Print the value returned by the 'bark()' function  of 'dodo'.
dodo.bark()  