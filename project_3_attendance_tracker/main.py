import csv

def add_attendance(name, status):
    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, status])

add_attendance("John", "Present")
add_attendance("Anna", "Absent")
add_attendance("Mark", "Present")

print("Attendance updated")