class Subject:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"{self.name}"


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.subjects = []

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def add_subject(self, subject: Subject):
        self.subjects.append(subject)

    def print_subjects(self):
        return f"{self.name} {self.surname} - Subjects: {self.subjects}"

    def __repr__(self):
        return f"{self.name} {self.surname}"


class KOS:

    def __init__(self):
        self.students = []
        self.subjects = []

    def add_student(self, name, surname):
        try:
            if self.get_student(name, surname):
                raise StudentPresentError()
        except StudentMissingError:
            self.students.append(Student(name, surname))

    def get_student(self, name, surname):
        for student in self.students:
            if student == Student(name, surname):
                return student
        raise StudentMissingError()

    def remove_student(self, name, surname):
        student = self.get_student(name, surname)
        self.students.remove(student)

    def add_subject(self, subject_name):
        try:
            if self.get_subject(subject_name):
                raise SubjectPresentError()
        except SubjectMissingError:
            self.subjects.append(Subject(subject_name))

    def get_subject(self, subject_name):
        for subject in self.subjects:
            if subject == Subject(subject_name):
                return subject
        raise SubjectMissingError()

    def remove_subject(self, subject_name):
        self.subjects.remove(Subject(subject_name))

    def assign_subject(self, subject_name, name, surname):
        student = self.get_student(name, surname)
        subject = self.get_subject(subject_name)
        student.add_subject(subject)

    def __repr__(self):
        return f"KOS:\n- Students: {self.students}\n- Subjects: {self.subjects}\n"


class StudentMissingError(Exception):
    def __init__(self):
        super().__init__("Student not in KOS")


class StudentPresentError(Exception):
    def __init__(self):
        super().__init__("Student already in KOS")


class SubjectMissingError(Exception):
    def __init__(self):
        super().__init__("Subject not in KOS")


class SubjectPresentError(Exception):
    def __init__(self):
        super().__init__("Subject already in KOS")


kos = KOS()
print(kos)
kos.add_student("Alice", "Smith")
# kos.add_student("Alice", "Smith")
kos.add_student("Bob", "Smith")
print(kos)
kos.remove_student("Alice", "Smith")
print(kos)

kos.add_subject("Math")
# kos.add_subject("Math")
kos.add_subject("OOP")
print(kos)
kos.remove_subject("Math")
print(kos)

kos.add_student("Alice", "Smith")
kos.assign_subject("OOP", "Alice", "Smith")
# kos.assign_subject("Math", "Alice", "Smith")
print(kos)

print(kos.get_student("Alice", "Smith"), kos.get_student("Alice", "Smith").subjects)
