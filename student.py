class student:
    college_name="Aditya Institute of technology"
    total_students=0
    PASS_MARKS=35
    MAX_SUBJECTS=5
    def __init__(self,name,roll_number,branch):
        self.name=name
        self._roll_number=roll_number
        self._branch=branch
        self.__marks={}
        student.total_students+=1

    @property
    def roll_number(self):
        return self._roll_number

    @property
    def branch(self):
        return self._branch

    def student_enter_marks(self,subject,score):
        if((score>=0 and score<=100) and len(self.__marks)<self.MAX_SUBJECTS):
            self.__marks[subject]=score
        else:
            raise ValueError("Invalid Number of subjects")

    def display(self):
        return self.__marks

    @property
    def avg_marks(self):
        if(len(self.__marks)==0):
            return 0;
        else:
            sum=0.0
            for i in self.__marks.values():
                sum+=i
            return sum/len(self.__marks)

    @property 
    def grade(self):
        if(self.avg_marks>=90):
            return "A+"
        elif(self.avg_marks>=75 and self.avg_marks<=89.99):
            return "A"
        elif(self.avg_marks>=60 and self.avg_marks<=74.99):
            return "B"
        elif(self.avg_marks>=35 and self.avg_marks<=59.99):
            return "PASS MARK"
        else:
            return "FAIL"

    @property
    def has_passed(self):
        for i in self.__marks.values():
            if(i<35):
                return False
        return True

    def change_branch(self,new_branch):
        self._branch=new_branch
        return self._branch

    @classmethod
    def total_num_students(cls):
        return cls.total_students

    @staticmethod
    def is_valid_marks(mark):
        if(mark>=0 and mark<=100):
            return True
        else:
            return False

    def __str__(self):
        return (f"roll no : {self.roll_number} |"
                f"name : {self.name} |"
                f"branch : {self._branch} |"
                f"avg_marks : {self.avg_marks}")


    