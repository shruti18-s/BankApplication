from Bank_Acc import Bank_Acc


class Customer_detail(Bank_Acc):

    def __init__(self, name, phone_no, email_add, address):
        self.name = name
        self.phone_no = phone_no
        self.email_add = email_add
        self.address =address

    def view(self):

        print("Customer Details ")



cust_detail = Customer_detail("Abhi", 9878766779, "abc@gm.com", "hjhiikll")

print(cust_detail.login())