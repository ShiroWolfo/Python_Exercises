#LISTA 4
#ZADANIE1-------------------------------------------------------------------------------
class Pupil:
    def __init__(self, name, surname):
        if len(name) < 3 or len(surname) < 3:
            raise ValueError("Name and surname should have at least 3 characters.")
        self.name = name
        self.surname = surname
        self.marks = {}

    def complete_marks(self):
        while True:
            subject = input("Enter subject name (or 'exit' to finish): ")
            if subject == "exit":
                break
            grade = float(input("Enter grade for {}: ".format(subject)))
            if grade not in [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]:
                print("Invalid grade. Please enter a valid grade.")
                continue
            self.marks[subject] = grade

    def print_marks(self):
        print("Marks:")
        for subject, grade in self.marks.items():
            print("{}: {}".format(subject, grade))

    def mean(self):
        if len(self.marks) == 0:
            return 0
        total = sum(self.marks.values())
        return total / len(self.marks)

    def __str__(self):
        return "{} {}: {:.2f}".format(self.name, self.surname, self.mean())


class Student(Pupil):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.weights = {}

    def complete_weights(self):
        while True:
            subject = input("Enter subject name (or 'exit' to finish): ")
            if subject == "exit":
                break
            weight = float(input("Enter weight for {}: ".format(subject)))
            if weight <= 0 or weight > 1:
                print("Invalid weight. Please enter a valid weight.")
                continue
            self.weights[subject] = weight

    def mean(self):
        if len(self.marks) == 0:
            return 0
        weighted_sum = sum(self.marks[subject] * self.weights[subject] for subject in self.marks)
        total_weights = sum(self.weights.values())
        return weighted_sum / total_weights

    def __str__(self):
        return super().__str__()

# Utworzenie obiektów klasy Pupil i Student
pupil = Pupil("Miłosz", "Szymański")
pupil.complete_marks()
pupil.print_marks()
print("Mean grade:", pupil.mean())
print()

student = Student("Adam", "Nowak")
student.complete_marks()
student.complete_weights()
student.print_marks()
print("Mean grade (weighted):", student.mean())
