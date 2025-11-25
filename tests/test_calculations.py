from src.calculations import calculate_total_expenses, calculate_income_needed

def test_calculate_total_expenses():
    """Verify total expenses are summed correctly."""
    expenses = [1200, 300.50, 89.99]
    assert calculate_total_expenses(expenses) == 1590.49


def test_calculate_income_needed():
    """Verify gross and net income needed are calculated correctly."""
    total = 2000  # total expenses
    result = calculate_income_needed(total)

    assert result["net_needed"] == 2000
    assert result["gross_needed"] == 2000 / 0.75
