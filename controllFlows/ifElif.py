# Write an if/elif/else statement for a college with a grading system as shown below:

# If grade is 90 or higher, print "A"
# Else if grade is 80 or higher, print "B"
# Else if grade is 70 or higher, print "C"
# Else if grade is 60 or higher, print "D"
# Else, print "F"


marks = {}
marks["Maths"] = int(input('Maths: '))
marks["Physics"] = int(input('Physics: '))
marks["Chemistry"] = int(input('Chemistry: '))
marks["Biology"] = int(input('Biology: '))
marks["Computer"] = int(input('Computer: '))

print(marks)

def grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

for subject, mark in marks.items():
    print(f"{subject}: {grade(mark)}")