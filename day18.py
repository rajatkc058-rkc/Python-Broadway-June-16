class Test:
    a = 10
    __b = 1
    # print(__b)

    c = __b + 1

    def display(self):
        return self.__b

    def __data(self):
        return self.a


obj = Test()
print(obj.a)
# print(obj.__b)
print(obj.c)
print(obj.display())
# print(obj.__data())


class Test:
    a = 10
    __b = 1
    c = __b + 1
    def display(self):
        return self.__b

    def __data(self):
        return self.a

    def send_data(self):
        return self.__data
class Test2:
    def display_all(self):
        return self.display()

    # def display2 (self):
    # return self.send_data()


obj = Test()
print(obj.a)
# print(obj.__b)
print(obj.c)
print(obj.display())
# print(obj.__data())
# print(obj.display2())


class Account:
    account_holder = "Hari Sharma"
    account_number = 143578960
    __total_balance = 20000
    __pin = 1234

    def deposit_money(self):
        deposited_amount = 10000
        self.__new_total_balance = self.__total_balance + deposited_amount
        # print(self.__new_total_balance)
        return f" Deposited : {deposited_amount}"

    def get_balance(self):
        return self.__new_total_balance

    def verify_pin(self):
        user_pin = 1235
        if user_pin == self.__pin:
            return "Proceed Transaction"
        else:
            return "Sorry! Transaction pin invalid"

    def withdraw_money(self):
        withdraw = 30000
        if withdraw <= self.__new_total_balance:
                self.newbalance_afterwithdraw = self.__new_total_balance - withdraw
                return self.newbalance_afterwithdraw
        else:
                return "Insufficent Balance"


class Saving_account(Account):
    interest_rate = 0.05

    def calc_year_interest(self):
        interest = self.get_balance() * 0.05
        return interest

    def display_info(self):
        return f"""accountholder_name : {self.account_holder}
    account_number : {self.account_number}
    Deposit_made : {self.deposit_money()}
    AvailableBalance: {self. withdraw_money()}
    Interest rate : {self.interest_rate}
    Interest_amount : {self.calc_year_interest()}"""


obj = Saving_account()
print(obj.deposit_money())
print(obj.get_balance())
print(obj.verify_pin())
print(obj.withdraw_money())
print(obj.calc_year_interest())
print(obj.display_info())
