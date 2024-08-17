class Bank_Acc:

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password


    def login(self):

        print("Login Successful")


class Customer_detail(Bank_Acc):

    def __init__(self, name, phone_no, email_add, address, user_id, password):
        super().__init__(user_id, password)
        self.name = name
        self.phone_no = phone_no
        self.email_add = email_add
        self.address =address

    def view(self):

        print("Customer Details ")


class Account_Detail(Bank_Acc):

    def __init__(self, acc_no,  user_id, password):
        super().__init__(user_id, password)

        self.acc_no = acc_no
        self.acc_balance = 0
        self.routing_no = None


    def acc_view(self):
        print("Acc_no is ", self.acc_no)




class Transaction(Account_Detail):

     def __init__(self, acc_no, user_id, password, withdraw_amt, deposit_amt):
           super().__init__(acc_no,  user_id, password)
           self.withdraw_amt = withdraw_amt
           self.deposit_amt = deposit_amt
           self.transfer_amt = 60
           self.new_acc_bal = 0


     def deposit(self):
         self.deposit_amt = int(input("Enter the amount to be deposit: "))
         self.acc_balance += self.deposit_amt

         print(" The current Acc balance is :", self.acc_balance)


     def withdraw(self):
         self.withdraw_amt = int(input("Enter the amout to be withdrwan: "))
         if self.acc_balance > self.withdraw_amt:
             self.acc_balance = self.acc_balance - self.withdraw_amt

             print("Acc balance is :", self.acc_balance)
         else:
             print("not sufficient balance")


     def transfer(self):

         if self.acc_balance > self.transfer_amt:
             self.acc_balance = self.acc_balance - self.transfer_amt
             print("Acc balance is :", self.acc_balance)
         else:
             print("not sufficient balance")

     def updated_acc_bal(self):
         return self.acc_balance



class Bill_Payment(Transaction):

     def __init__(self,acc_no, user_id, password, withdraw_amt, deposit_amt, sdge,credit_card ):
         super().__init__(acc_no, user_id, password,withdraw_amt, deposit_amt)
         self.sdge = sdge
         self.credit_card = credit_card
         self.withdraw_amt = withdraw_amt
         self.deposit_amt = deposit_amt
         self.current_acc_bal= self.updated_acc_bal()






     def bill_payment(self):
         self.sdge = int(input("Enter the amount to be paid: "))
         if self.current_acc_bal > self.sdge:
             self.current_acc_ball -= self.sdge
             print(f"The SDGE bill of {self.sdge} has been paid. Your account balance is now {self.current_acc_bal}")
         else:
             print("Not sufficient balance to make the payment")







cust_detail = Customer_detail("Abhi", 9878766779, "abc@gm.com", "hjhiikll", "abhi", "iujdhu")
acc_detail = Account_Detail(56767678,  "abhi", "gugsgu")
transac = Transaction(56767678,  "abhi", "gugsgu", None, None)
bill = Bill_Payment(56767678,  "abhi", "gugsgu", None, None, None, None)



transac.deposit()
transac.updated_acc_bal()
bill.updated_acc_bal()

print(transac.withdraw())
print(bill.bill_payment())