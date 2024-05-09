from abc import ABC
import uuid
flag=1
class User(ABC):
    def __init__(self, name, email, address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.user_list=[]
        self.total_balance=0
        self.total_loan_amount=0
        
class Create_Account(User):
    def __init__(self, name, email, address,account_type):
        super().__init__(name, email, address,account_type)
        self.balance=0
        self.history=[]
        self.account_id={}
        self.account_id[uuid.uuid4()]={self.name,self.balance}
        info=(name,email,address,account_type)
        self.user_list.append(info)
        

class Customer(Create_Account):          
    def deposit(self,dep_amount):
        self.balance+=dep_amount
        self.history.append(dep_amount)
        self.total_balance+=dep_amount
    def withdraw(self,wd_amount):
        if self.balance>0:
            self.balance-=wd_amount
            self.history.append(wd_amount)
            self.total_balance-=wd_amount
        else:
            "Bank is out of cash"
    def view_history(self):
        for trX in self.history:
            print(f'Deposit amount: {trX.dep_amount}')
            print(f'Withdraw amount: {trX.withdraw}')
    def take_loan(self, loan_amount):
        if flag==1:
            balance-=loan_amount
            self.total_loan_amount+=loan_amount
        else:
            print('Loan service not available now')
    def transfer_amount(self, transfer_account_id, transfer_amount):
        if transfer_account_id not in self.account_id:
            "Account does not exist"
        else: 
            self.balance-=transfer_amount
            transfer_account_id.balance+=transfer_amount
        
class Admin(Create_Account):
    
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address, account_type)
    def delete_account(self,info,account_info):
        remove(self.user_list.info)
        remove(self.account_id[account_info])
    def view_user_list(self):
        print(self.user_list)
    def Check_balance(self):
        print(self.total_balance)
    def Check_loan_amount(self):
        print(self.total_loan_amount)
    def loan_turnoff(self):
        flag==0
        print('Loan service turned off')
    def loan_turnon(self):
        flag==1
        print('Loan service turned on')

class Counter:
    def admin_interface():
       name=input('Enter your name: ') 
       email=input('Enter your email: ')
       address=input('Enter your address: ')
       account_type=input('Enter your account type: ')
       Choice=int(input('Enter your choice: '))
       admin = Admin(name=name,email=email,address=address,account_type=account_type)
       while True:
            print(f' **Welcome {admin.name}** ')
            print('1. View user list')
            print('2. Delete account')
            print('3. View user list')
            print('4. Check balance')
            print('5. Check loan amount')
            print('6. Loan Service Turn On')
            print('7. Loan Service Turn Off')
            print('8. Exit')
        
            if Choice==1:
                admin.view_user_list()
            elif Choice==2:
                admin.delete_account()
            elif Choice==3:
                admin.view_user_list()
            elif Choice==4:
                admin.Check_balance()
            elif Choice==5:
                admin.Check_loan_amount()
            elif Choice==6:
                admin.loan_turnon()
            elif Choice==7:
                admin.loan_turnoff()
            elif Choice==8:
                break
            else:
                print('Invalid Input')

    def customer_interface():
        name=input('Enter your name: ') 
        email=input('Enter your email: ')
        address=input('Enter your address: ')
        account_type=input('Enter your account type: ')
        Choice=int(input('Enter your choice: '))
        customer = Customer(name=name,email=email,address=address,account_type=account_type)
        while True:
            print(f'**Welcome {customer.name}**')
            print('1. Deposit Money')
            print('2. Withdraw Money')
            print('3. View Transaction History')
            print('4. Take Loan')
            print('5. Transfer Balance')
            print('6. Exit')
            if Choice==1:
                customer.deposit()
            elif Choice==2:
                customer.withdraw()
            elif Choice==3:
                customer.view_history
            elif Choice==4:
                customer.take_loan()
            elif Choice==5:
                customer.transfer_amount()
            elif Choice==6:
                break
            else:
                print('Invalid Input')

    while True:
        print('**Welcome to XYZ Banking System**')
        print('1.Admin')
        print('2.User')
        print('3.Exit')
        choice= int(input('Enter your choice: ')) 
        if choice==1:
            admin_interface()
        elif choice==2:
            customer_interface()
        elif choice==3:
            break
        else:
            print('Invalid choice')




        
        



  
  
  



