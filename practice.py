expenses = [
    {"amount" : 16.00, "category" : "pho"},
    {"amount" : 67.00, "category" : "pants"},
    {"amount" : 15.50, "category" : "sushi"},
    {"amount" : 25.50, "category" : "sushi"},
]
def total_spent(expense):
    total = 0
    for k in expense:
        total = total + k['amount']
    return total

def total_by_category(expense):
    totals = {}
    for k in expense:
        category = k['category']
        totals[category] = totals.get(category, 0) + k['amount']
    return totals
print(total_by_category(expenses))

