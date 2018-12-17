class Student:
    def __init__(self, name, age, subject1, subject2, subject3, birthCity, birthState):
        self.name = name
        self.age = age
        self.subjects = [subject1, subject2, subject3]
        self.birthPlace = [birthCity, birthState]

    def details(self):
        print("All about", self.name)
        print(self.name, "is", self.age, "years old")
        print(self.name, "studies", self.subjects[0] + ",", self.subjects[1] + ", and", self.subjects[2])
        print(self.name, "was born in", self.birthPlace[0] + ",", self.birthPlace[1])

mary = Student("Mary", 14, "Digital Technology", "Maths", "English", "Cairns", "Qld")
michael = Student("Michael", 16, "Digital Solutions", "Specialist Maths", "English", "Brisbane", "Qld")

mary.details()
print("")
michael.details()