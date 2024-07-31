class Student:
    def hi(self,name,id):
        self.name=name
        self.id=id
    def printd(self):
        print(self.name,self.id)

p=Student("Digvijay",1)
p.printd()