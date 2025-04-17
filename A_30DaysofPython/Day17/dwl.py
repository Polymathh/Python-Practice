classroom = {
    "Grade 1": ["Alice", "Ben", "Chris"],
    "Grade 2": ["Diana", "Eva"]
}

print(classroom["Grade 1"][1])  # Output: Ben

for grade, students in classroom.items():
    print(f"{grade} has {len(students)} students: {', '.join(students)}")
 
 