def calculate_total_expenses(expense_list):
    """Return the total of all monthly expenses."""
    return sum(expense_list)


def calculate_income_needed(total_expenses):
    """
    Return a dictionary containing:
      - net_needed: the total monthly expenses
      - gross_needed: the gross income required assuming 25% tax withholding
    """
    net_needed = total_expenses
    gross_needed = total_expenses / 0.75  # approximates take-home pay after taxes

    return {
        "net_needed": net_needed,
        "gross_needed": gross_needed
    }
