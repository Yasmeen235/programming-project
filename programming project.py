from abc import ABC, abstractmethod


class IDataStorage(ABC):
    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def get_all(self):
        pass



class InMemoryStorage(IDataStorage):
    def __init__(self):
        self.data = []

    def add(self, entity):
        self.data.append(entity)

    def get_all(self):
        return self.data



class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Grade: {self.grade})"



class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Teacher(ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject})"


class Course:
    def __init__(self, course_id, name, teacher):
        self.course_id = course_id
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Course(ID: {self.course_id}, Name: {self.name}, Teacher: {self.teacher.name})"



class SchoolManagementSystem:
    def __init__(self, student_storage, teacher_storage, course_storage):
        self.student_storage = student_storage
        self.teacher_storage = teacher_storage
        self.course_storage = course_storage

    def add_student(self, student):
        self.student_storage.add(student)

    def add_teacher(self, teacher):
        self.teacher_storage.add(teacher)

    def add_course(self, course):
        self.course_storage.add(course)

    def list_students(self):
        return self.student_storage.get_all()

    def list_teachers(self):
        return self.teacher_storage.get_all()

    def list_courses(self):
        return self.course_storage.get_all()


if __name__ == "__main__":
   
    student_storage = InMemoryStorage()
    teacher_storage = InMemoryStorage()
    course_storage = InMemoryStorage()

   
    school_system = SchoolManagementSystem(student_storage, teacher_storage, course_storage)

    
    student1 = Student(1, "Ali", 10)
    student2 = Student(2, "Sara", 9)

    teacher1 = Teacher(1, "Mr. Ahmed", "Math")
    teacher2 = Teacher(2, "Ms. Layla", "Science")

    course1 = Course(1, "Algebra", teacher1)
    course2 = Course(2, "Biology", teacher2)

    course1.add_student(student1)
    course2.add_student(student2)

    school_system.add_student(student1)
    school_system.add_student(student2)
    school_system.add_teacher(teacher1)
    school_system.add_teacher(teacher2)
    school_system.add_course(course1)
    school_system.add_course(course2)

 
    print("Students:")
    for student in school_system.list_students():
        print(student)

    print("\nTeachers:")
    for teacher in school_system.list_teachers():
        print(teacher)

    print("\nCourses:")
    for course in school_system.list_courses():
        print(course)
        print("  Enrolled Students:")
        for student in course.students:
            print(f"    - {student.name}")