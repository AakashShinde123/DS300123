class student:
    def __init__(self):
      self.name = None
      self.rollnumber = None

    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setRollNumber(self,rollnumber):
        self.rollnumber = rollnumber
    def getRollNumber(self):
        return self.rollnumber
a1 = student() 
a1.setName("Aakash")
print(a1.getName())
a1.setRollNumber(5)
print(a1.getRollNumber())
