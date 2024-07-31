class Point:

    #  def __init__(self, x, y):
  #      self.x = x
   #     self.y = y
    # def __str__(self):
     #   return f"({self.x}, {self.y})"
    #def __repr__(self):
     #   return f"Point({self.x}, {self.y})"

#e=Point(1,3)
#print(e)

    def __init__(self, dictionary):
        self.dictionary = dictionary
    def __setitem__(self, key, value):
         self.dictionary[key]=value

e=Point({'a':1, 'b':2,'c':3,'d':4})
print(e.dictionary)
e['b'] = 0
print(e.dictionary)