import sort
import Student
import read_file
import time

student_list = read_file.read_class_file(input("Enter file nime:\n"))

start_time = time.time()
sort.buble_sort(student_list)
print("Time: ", time.time() - start_time, "\nResult:")
for i in student_list:
  print(i, "\n")

print("------------------------------------------")

start_time = time.time()
sort.quick_sort(0, len(student_list), student_list)
print()
print("QuickSort  \nComparasion times: ", sort.comparasion_times, "\nSwap times: ", sort.swap_times, "\nTime: ", time.time() - start_time, "\nResult:")
for i in student_list:
  print(i, "\n")
