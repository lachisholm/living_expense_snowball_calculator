def calculate_total_expenses(expenses_list):
    """Return the sum of all expenses in the list."""
    total = 0
    for amount in expenses_list:
        total+= amount
    return total






def calculate_total_debt_payments(debt_list):
    """Return the sum of all minimum debt payments."""
    total = 0
    for debt in debt_list:
        total += debt["min_payment"]
    return total









def calculate_net_needed(total_expenses, total_debt_payments):
    """Return the net amount needed by summing total expenses and total debt payments."""
    return total_expenses + total_debt_payments













def calculate_total_expenses(net_needed, tax_rate):
    """Return the gross income required to produce the net needed."""
    if tax_rate < 0 or tax_rate >= 1:
        raise ValueError("Tax rate must be between 0 and 1 (Tax rate must be between 0 and 1.")
    return net_needed / (1 - tax_rate)







    


def calculate_monthly_interest(balance, rate):
    """Return the monthly interest amount for a debt."""
    return balance * rate / 12











    
def calculate_months_to_payoff(balance, monthly_payment, rate):
    """Return an estimate of how many months it will take to pay off a debt."""
    if monthly_payment <= 0:
        raise ValueError("Monthly payment must be greater than zero.")
    
    months = 0 
    current_balance = balance
    
    while current_balance > 0 and months < 1000:
        interest = current_balance * rate / 12
        current_balance = current_balance + interest - monthly_payment
        months += 1
        
    if months >= 1000:
        return None  # Payment to small to ever pay off
    
    return months