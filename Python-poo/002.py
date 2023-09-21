class Parrot:


  def __init__(self, name, age):
   self.name = name
   self.age = age


  def sing(self, song):
   return '{} sings {}'.format(self.name, song)

  def dance(self):
   return '{} is now dancing'.format(self.name)
pass

# instantiate the object
blu = Parrot('Blu', 10)
# call our instance methods
print(blu.sing('Happy'))
print(blu.dance())


class Cat:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  def meow(self, song):
    return '{} he is now meow {}'.format(self.name, song)
pass

myCat = Cat('Shizu', 'Street', 1)
print(myCat.meow('MIAU CARAIO'))




# arr = [1, 2, 3, 4, 5, 6]

# i = 0
# while i <= 5:
#   new = int(input(('Digite o proximo valor do array: ')))
#   arr.append(new)
#   print(arr)
#   i += 1


# for valor in arr:
#     res = valor * 5
#     print(res)
