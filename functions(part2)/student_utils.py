def calculate_average(scores):
    """Return the average score."""
    a=sum(scores)/len(scores)
    return a
    
    
def get_highest_score(scores):
    """Return the highest score in the list."""
    return max(scores)
    
    
def get_lowest_score(scores):
    """Return the lowest score in the list."""
    return min(scores)
    
    
def process_students(student_list):
    """Display each student name and the total number of students"""
    print("Students:")
    for i in student_list:
        print(i)
    print('Total Students: '+ str(len(student_list)))
    
    
def register_students(*students):
    """Prints the list of registered students and the total count."""
    print("Registered Students:")
    for i in students:
        print(i)
    print('Total: '+ str(len(students)))





  
