class Bank_Acc:

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    def login(self, user_id_search):

        if user_id_search == self.user_id:

            pass_entered = input("Enter Password")
            if pass_entered == self.password:
                print("Login Successful")
            else:
                print("Wrong Password . Please enter again")
        else:
            print("You are not an existing customer. Would you like to open an Account?")


class Customer_detail(Bank_Acc):

    def __init__(self, name, phone_no, email_add, address, user_id, password):
        super().__init__(user_id, password)
        self.name = name
        self.phone_no = phone_no
        self.email_add = email_add
        self.address = address


class Existing_Customer(Customer_detail):

    def __init__(self, name, phone_no, email_add, address, user_id, password):
        super().__init__(name, phone_no, email_add, address, user_id, password)

    def view(self):
        if super().login("abhi"):
            print("Customer Details:\n ", "Name iof Customer:", self.name, "\n Contact Detail of customer are:",
                  self.phone_no, self.email_add, self.address)
        else:
            return


class New_Customer(Customer_detail):
    def __init__(self, name, phone_no, email_add, address, user_id, password):
        super().__init__(name, phone_no, email_add, address, user_id, password)

    def create_acc(self):
        print("Click the link to create an account")


class Account_Detail(Bank_Acc):

    def __init__(self, acc_no, user_id, password):
        super().__init__(user_id, password)

        self.acc_no = acc_no
        self.acc_balance = 0
        self.routing_no = None

    def view(self):
        print("Account Balance is ", self.acc_balance, " for Account no", self.acc_no)


class Transaction(Account_Detail):

    def __init__(self, acc_no, user_id, password, withdraw_amt, deposit_amt):
        super().__init__(acc_no, user_id, password)
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


login = Bank_Acc("abhi", "Welcome_2022")
exist_cust_detail = Existing_Customer("Abhi", 9878766779, "abc@gm.com", "San Diego", "abhi", "Welcome_2022")
acc_detail = Account_Detail(56767678, "abhi", "Welcome_2022")
transac = Transaction(56767678, "abhi", "Welcome_2022", None, None)

login.login("abhi")

exist_cust_detail.view()
transac.deposit()
transac.updated_acc_bal()
