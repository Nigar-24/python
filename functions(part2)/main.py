from student_utils import *

students = ["Ali", "Leyla", "Kamran", "Aysel"]
scores = [78, 91, 85, 67, 95, 88]

print("Average Score:", calculate_average(scores))
print("Highest Score:", get_highest_score(scores))
print("Lowest Score:", get_lowest_score(scores))
process_students(students)
register_students("Ali", "Leyla", "Kamran")
