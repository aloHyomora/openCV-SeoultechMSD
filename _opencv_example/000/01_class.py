
class Number:
    def __init__(self):
        self.value = 0
        
    def show(self):
        print(self.value)
        
num = Number()
num.show()
        
    
class Student:
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade
        
    def show(self):
        print(f'name: {self.name}, id: {self.id}, grade: {self.grade}')
        
student = Student('jack', 431284, 4)
student1 = Student('dssk', 56156784, 3)
student.show()

class School:
    def __init__(self):
        self.students = []
        
    def add(self, student):
        self.students.append(f'{student.name},{student.id},{student.grade}')
    
    def show(self):
        print(self.students)
        
school = School()
school.add(student)
school.add(student1)
school.show()