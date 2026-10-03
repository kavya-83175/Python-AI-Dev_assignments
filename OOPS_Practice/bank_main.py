from bank import *

def main():
    print(bank.bank_name)
    b1=bank("Ravi Kumar","Savings",5000,"1256")
    b2=bank("Sravya","Current",20000,"4589")

    print(b1)
    print(b2)


    print(bank.total_accounts)

    print("Deposit: 1500 ->", b1.deposit(1500))
    print("Withdrw : 5000 ->",b2.withdraw(5000,"4589"))

    print("Interest added : ",b1.add_annual_interest())
    print("Balance now: ",b1.balance)
    print(b1.change_pin("1256","1234"))
    print(b2.change_pin("1458","1245"))




if __name__==("__main__"):
    main()

#As the balance only have the property as read if it is able to change anybody can change there balance which is invalid
#as holder name doesn't need any privacy as changing the name doesnt affect the financial things 
