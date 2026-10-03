from student import *
def main():
    print(student.college_name)
    print(student.total_students)
    s1=student("Kavya",151,"DS")
    s2=student("Siri",85,"ECE")
    s1.student_enter_marks("Python",80)
    s1.student_enter_marks("cpp",80)
    s1.student_enter_marks("Java",80)
    s1.student_enter_marks("c",80)
    s1.student_enter_marks("DBMS",80)

    s2.student_enter_marks("Python",55)
    s2.student_enter_marks("cpp",35)
    s2.student_enter_marks("Java",40)
    s2.student_enter_marks("c",30)
    s2.student_enter_marks("DBMS",10)

    print(s1.display())
    print("Is s1 passed : ",s1.has_passed)
    print("Is s2 Passed : ",s2.has_passed)
    # s1.student_enter_marks("R",80)
    # s1.roll_number=147
    # s1.avg_marks=151
    # print(s1.name)
    print("Is 151 a valid_mark : ",s1.is_valid_marks(151))
    print(f"old branch : {s1.branch} new branch : {s1.change_branch("AIML")}")
    # print(s1.branch)
    
    print(s1)

if __name__==("__main__"):
    main()
