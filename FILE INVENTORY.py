import csv
import os
FILE_NAME = "students.csv"
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Python", "OOPS", "Web Tech", "Total", "Average", "Grade"])
def add_student():
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

       sid = input("Enter ID: ")
        name = input("Enter Name: ")
        p = int(input("Python Marks: "))
        o = int(input("OOPS Marks: "))
        w = int(input("Web Tech Marks: "))
total = p + o + w
        	avg = total / 3
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "Fail"
        writer.writerow([sid, name, p, o, w, total, avg, grade])
        print("Student added successfully!\n")
def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
def main():
    create_file()
    while True:
        print("\n1. Add Student\n2. View Students\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")
main()
