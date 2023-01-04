students = ['John', 'Dias', 'Silvern', 'Victorious']
markedStudents = {}
while students:
    student = students.pop()
    mark = input(f" Enter {student.title()} ' mark: ")
    print(f"Marked {student.title()}")
    markedStudents[student] = mark
print(markedStudents)
print(markedStudents.keys())

