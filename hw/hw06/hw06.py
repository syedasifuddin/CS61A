# Object Oriented Programming


class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0, previous=1, nextvalue=1):
        self.value = value
        self.previous = previous
        self.nextvalue = nextvalue

    def next(self):
        "*** YOUR CODE HERE ***"
        return (Fib(self.previous, self.nextvalue, self.previous + self.nextvalue))

    def __repr__(self):
        return str(self.value)


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, artifact, cost):
        self.artifact = artifact
        self.cost = cost
        self.quantity = 0
        self.balance = 0

    def vend(self):
        if self.quantity <= 0:
            return 'Machine is out of stock.'
        elif self.balance < self.cost:
            return 'You must deposit ${0} more.'.format(self.cost - self.balance)
        elif self.balance == self.cost:
            self.quantity -= 1
            self.balance -= self.cost
            return 'Here is your {0}.'.format(self.artifact)
        else:
            self.quantity -= 1
            self.balance -= self.cost
            change = self.balance
            self.balance = 0
            return 'Here is your {0} and ${1} change.'.format(self.artifact, change)

    def deposit(self, value):

        if self.quantity <= 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(value)
        else:
            self.balance += value
            return 'Current balance: ${0}'.format(self.balance)

    def restock(self, value):
        self.quantity += value
        return 'Current {0} stock: {1}'.format(self.artifact, self.quantity)
