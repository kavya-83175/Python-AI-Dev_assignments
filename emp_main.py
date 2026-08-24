from emp import *

def main():
    print("Company Name: ",employee.company_name)
    print("Employees Before : ",employee.total_employees)
    e1=employee("Divya",125,"HR",15000,12345)
    e2=employee("Ramesh",154,"Testing",25000,58965)
    print("Employees After : ",employee.total_employees)
    print("pf for e1: ",e1.calculate_pf())
    print("apply_hike for e1 : ",e1.apply_hike(10))
    e1.transfer_department("Testing")
    # print(e1)
    e1.salary=500
    # print(e1._salary)
    print(e1.__str__())


if __name__==("__main__"):
    main()