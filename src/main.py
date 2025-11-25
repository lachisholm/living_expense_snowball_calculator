from calculations import calculate_total_expenses, calculate_income_needed
from file_utils import read_expenses_file, read_debts_file
from snowball import snowball_plan


def main():
    """Main program function that coordinates the overall workflow."""
    print("Living Expense and Debt Snowball Calculator")
    print("-------------------------------------------")
    
    # read data from files
    expenses = read_expenses_file("data/expenses.txt")
    debts = read_debts_file("data/debts.txt")
    
    # calculate total expenses
    total_expenses = calculate_total_expenses(expenses)
    
    # calculate income needed
    income_info = calculate_income_needed(total_expenses)
    print("\nMonthly Income Needed:")
    print(f"  Net Income Needed: ${income_info['net_needed']:.2f}")
    print(f"  Gross Income Needed: ${income_info['gross_needed']:.2f}")
    
    #ask user for snowball amount
    extra = float(input("\nEnter the extra monthly amount for your snowball payment: "))
    
    plan = snowball_plan(debts, extra)
    
    #show the summary
    print(f"\nDebt-Free in {plan['total_months']} months!")

if __name__ == "__main__":
    main()
