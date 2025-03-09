from datetime import datetime


class Person:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def __str__(self):
        total = sum([transaction.amount for transaction in self.transactions])
        if total > 0:
            return f"{self.name} masih hutang ke aku {total}"
        return f"Aku masih hutang {total*-1} ke {self.name}"


class Transaction:
    """
    1. I lend money to my friend -> +amount on that person
    2. I ask money to my friend -> -amount on that person
    """

    # As lend function (1)
    def __init__(self, amount: int):
        self.amount = amount
        self.created_at = datetime.now()

    # As ask function (2)
    def ask(self):
        self.amount *= -1


class Me:
    def __init__(self):
        self.friends = []

    def add_friend(self, friend: Person):
        self.friends.append(friend)

    def friends_has_debt(self):
        return [friend for friend in self.friends if friend.transactions]
