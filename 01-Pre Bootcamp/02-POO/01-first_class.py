class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Saldo: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)

matias = user("Matias", "mmedelm@gmail.com")
james = user("James", "james@smth.com")
rex = user("Rex", "rex@smth.com")

matias.make_deposit(300)
matias.make_deposit(200)
matias.make_deposit(100)
matias.display_user_balance()

james.make_deposit(200)
james.make_deposit(100)
james.make_withdrawal(50)
james.make_withdrawal(100)
james.display_user_balance()

rex.make_deposit(500)
rex.make_withdrawal(100)
rex.make_withdrawal(100)
rex.make_withdrawal(100)
rex.display_user_balance()

matias.transfer_money(rex, 100)
matias.display_user_balance()
rex.display_user_balance()