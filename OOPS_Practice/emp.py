class employee:
    company_name="TechCorp Solutions"
    total_employees=0
    pf_percentage=12.0
    MIN_SALARY=15000
    MAX_SALARY=5000000
    def __init__(self,name,emp_id,department,salary,pan_number):
        self.name=name
        self._emp_id=emp_id
        self._department=department
        self._salary=salary
        self.__pan_number=pan_number
        employee.total_employees+=1

    @property
    def emp_id(self):
        return self._emp_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if(employee.is_valid_salary(value)):
            self._salary=value
        else:
            raise ValueError("Invalid Salary")

    def apply_hike(self,percentage):
        if(percentage>=0 and percentage<=50):
            self._salary+=(self._salary*percentage/100)
            return self.salary
        else:
            raise ValueError("Invalid Percentage")

    def calculate_pf(self):
        return self._salary*(self.pf_percentage)/100

    def transfer_department(self,new_dept):
        print("old department e1: ",self._department)
        self._department=new_dept
        print("New department e1 : ",self._department)

    @classmethod
    def get_total_employees(cls):
        return cls.total_employees

    @staticmethod
    def is_valid_salary(value):
        if(value>=15000 and value<=5000000):
            return True
        else:
            return False

    def __str__(self):
        return (f"Employee(ID={self._emp_id}, "
            f"Name={self.name}, "
            f"Department={self._department}, "
            f"Salary={self._salary})")

    
