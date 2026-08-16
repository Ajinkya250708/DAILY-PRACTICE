class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database...")
    def welcome(self):
        print("Welcome",self.name)

s1=student("Harshit",48)
print(s1.name,s1.marks)
s1.welcome()

s2=student("Dishita",56)
print(s2.name,s2.marks)
s2.welcome()
