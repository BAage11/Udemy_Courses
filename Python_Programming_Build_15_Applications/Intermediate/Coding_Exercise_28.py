# Start off by creating the Result class

class Result():
    def __init__(self):
        self.studentMarks = {'A': 88, 'B': 71, 'C': 84, 'D': 95, 'E': 60, 'F': 89}

    def add_rslt(self, student, marks):
        self.studentMarks[student] = marks


class Student(Result):
    def __init__(self):
        Result.__init__(self)

    def sho_rslt(self, studentName):
        for k,v in self.studentMarks.items():
            if k == studentName:
                print(k + " got " + str(v) + " marks")


new = Student()

# Adding following results:
new.add_rslt('G', 85)
new.add_rslt('H', 67)

# Print result of students:
new.sho_rslt('A')
new.sho_rslt('B')
new.sho_rslt('D')
new.sho_rslt('F')
new.sho_rslt('H')
