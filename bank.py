class bank:
    bank_name="State bank of India"
    total_accounts=0
    interest_rate=4.0
    MIN_BALANCE=500
    next_acc_num=1001
    def __init__(self,holder_name,acc_type,balance,pin):
        self.holder_name=holder_name
        self._acc_type=acc_type
        if(balance<self.MIN_BALANCE):
            raise ValueError("Invalid Balance")
        self.__balance=balance
        self.__pin=pin
        self._acc_num=bank.next_acc_num
        bank.next_acc_num+=1
        bank.total_accounts+=1

    @property
    def acc_num(self):
        return self._acc_num

    @property
    def balance(self):
        return self.__balance

    def deposit(self,amount):
        if(amount<=0):
            raise ValueError("Invalid amount")
        else:
            self.__balance= self.__balance+amount
            return self.__balance
        
    def withdraw(self,amount,pin):
        if( (self.__verify_pin(pin)) and (amount>0) and (self.__balance-amount)>=self.MIN_BALANCE):
            self.__balance-=amount
            return self.__balance
        else:
            raise ValueError("Invalid amount")

    def __verify_pin(self,pin):
        if(self.__pin==pin):
            return True
        else:
            return False

    def change_pin(self,old_pin,new_pin):
        if(self.__verify_pin(old_pin) and len(new_pin)==4):
            self.__pin=new_pin
            return "Pin changed Successfully"
        else:
            raise ValueError("Invalid Pin")

        
    def add_annual_interest(self):
        p= self.balance*bank.interest_rate/100
        self.__balance+=p
        return p
    
    @classmethod
    def get_total_acc(cls):
        return cls.total_accounts

    @staticmethod
    def is_valid_amount(amount):
        if(amount>0):
            return True
        else:
            return False

    def __str__(self):
        return (f"Account Number : {self._acc_num} |"
            f"Holder Name : {self.holder_name} |"
            f"Type : {self._acc_type} |"
            f"Balance : {self.__balance}")

    