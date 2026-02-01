class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        body = ""
        for item in self.ledger:
            body += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + body + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    spent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    percentages = []
    for s in spent:
        percent = (s / total_spent) * 100
        percentages.append(int(percent // 10) * 10)

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            chart += "o  " if percent >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i != max_len - 1:
            chart += "\n"

    return chart
