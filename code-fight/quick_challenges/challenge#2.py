def bankRequests(accounts, requests):
    def withdraw(account, amount):
        try:
            accounts[account - 1] -= amount
        except IndexError:
            raise PaymentException
        if accounts[account - 1] < 0:
            raise PaymentException

    def transfer(account_from, account_to, amount):
        try:
            accounts[account_from - 1] -= amount
            accounts[account_to - 1] += amount
        except IndexError:
            raise PaymentException
        if accounts[account_from - 1] < 0:
            raise PaymentException

    def deposit(account, amount):
        try:
            accounts[account - 1] += amount
        except IndexError:
            raise PaymentException

    actions = {f.__name__: f for f in [withdraw, transfer, deposit]}

    for index, request in enumerate(requests):
        try:
            action_name, args = request.split(' ', 1)
            action = actions[action_name]
            action(*[int(arg) for arg in args.split()])
        except PaymentException:
            return '-{}'.format(index)

    return accounts


class PaymentException(Exception):
    pass


accounts = [10, 100, 20, 50, 30]
requests = [
    "withdraw 2 10", "transfer 5 1 20", "deposit 5 20", "transfer 3 4 15"
]
print bankRequests(accounts, requests)
