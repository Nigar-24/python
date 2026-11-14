def calculate_average(scores):
    """Return the avareage score."""
    a=sum(scores)/len(scores)
    return a
scores=[90,80,70]
print(calculate_average(scores))


def get_lowest_score(scores):
    """Return the lowest score in the list."""
    return min(scores)
scores=[90,80,70]
print(get_lowest_score(scores))


def process_students(student_lists):
    """Display each student name and the total number of students"""
    print("Students:")
    for i in student_lists:
        print(i)
    print('Total students: '+ str(len(student_lists)))
student_lists=['Ali','Leyla','Kamran','Aysel']
process_students(student_lists)



def register_students(*students):
    """Prints the list of registered students and the total count."""
    print("Registered Students:")
    for i in students:
        print(i)
    print('Total: '+ str(len(students)))
students=["Ali","Leyla","Kamran"]
register_students(*students)





