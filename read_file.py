from Student import Student

def read_class_file(class_file):
  with open(class_file) as file:
    students_list = []
    for row in file: 
      arr = row.split(", ")
      students_list.append(Student(arr[0], arr[1], arr[2]))
    return(students_list)
    