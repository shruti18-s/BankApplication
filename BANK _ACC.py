class BankAccount:

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    def login(self, user_id_search):
        if user_id_search == self.user_id:
            pass_entered = input("Enter Password")
            if pass_entered == self.password:
                print("Login Successful")
        else:
            print("You are not an existing customer. Would you like to open an Account?")


class CustomerDetail(BankAccount):

    def __init__(self, name, phone_no, email_add, address, user_id, password):
        self.bank_acc = BankAccount(user_id, password)
        self.name = name
        self.phone_no = phone_no
        self.email_add = email_add
        self.address = address

    def view(self):
        print("Customer Details:\n", "Name of Customer:", self.name, "\nContact Detail of customer are:",
              self.phone_no, self.email_add, self.address)


class ExistingCustomer(CustomerDetail):

    def __init__(self, name, phone_no, email_add, address, user_id, password):
        super().__init__(name, phone_no, email_add, address, user_id, password)

    def get_account(self):
        return AccountDetail(56767678, self.bank_acc.user_id, self.bank_acc.password)


class NewCustomer(CustomerDetail):

    def __init__(self, name, phone_no, email_add, address, user_id, password):
        super().__init__(name, phone_no, email_add, address, user_id, password)

    def create_account(self):
        print("Click the link to create an account")


class AccountDetail(BankAccount):

    def __init__(self, acc_no, user_id, password):
        self.bank_acc = BankAccount(user_id, password)
        self.acc_no = acc_no
        self.acc_balance = 0
        self.routing_no = None

    def view(self):
        print("Acc_no is", self.acc_no)

    def deposit(self):
        deposit_amt = int(input("Enter the amount to be deposit: "))
        self.acc_balance += deposit_amt
        print("The current Acc balance is:", self.acc_balance)

    def withdraw(self):
        withdraw_amt = int(input("Enter the amount to be withdrawn: "))
        if self.acc_balance > withdraw_amt:
            self.acc_balance -= withdraw_amt
            print("Acc balance is:", self.acc_balance)
        else:
            print("Not sufficient balance")

    def transfer(self):
        transfer_amt = 60
        if self.acc_balance > transfer_amt:
            self.acc_balance -= transfer_amt
            print("Acc balance is:", self.acc_balance)
        else:
            print("Not sufficient balance")

    def get_balance(self):
        return self.acc_balance


login = BankAccount("Abhi", "Welcome_2022")
exist_cust_detail = ExistingCustomer("Abhi", 9878766779, "abc@gm.com", "San Diego", "abhi", "Welcome_2022")
acc_detail = exist_cust_detail.get_account()
transac = Transaction(acc_detail)

login.login("Abhi")
exist_cust_detail.view()
acc_detail.view()

transac.deposit()
transac.get_balance()
transac.withdraw()
transac.get_balance()
transac.transfer()
transac.get_balance()
