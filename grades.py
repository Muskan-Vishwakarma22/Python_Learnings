#GRADING SYSTEM
#If the student has submitted the project, grade them correctly else reduce the grade by one
marks = float(input("Enter the marks: "))
proj = bool(input("Have you submitted the project (True or False)"))
if marks>=90 and proj == True:
    print("A+ Grade")
elif marks>= 90 and proj == False:
    print("A Grade")
elif marks>= 80 and marks < 90 and proj == True:
    print("A Grade")
elif marks>= 80 and marks < 90 and proj == False:
    print("B Grade") 
elif marks>= 70 and marks < 80 and proj == True:
    print("B Grade")
elif marks>= 70 and marks < 80 and proj == False:
    print("C Grade")
elif marks>= 60 and marks < 70 and proj == True:
    print("C Grade")
elif marks>= 60 and marks < 70 and proj == False:
    print("D Grade")
elif marks<60:
    print("F Grade")
else:
    print("Invalid Input")

        