def read_expenses_file(path):
    """Read the expenses file and return a list of expense amounts."""
    expenses = []
     
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line: 
                expenses.append(float(line))
    return expenses







def read_debts_file(path):
    """Read the debts file and return a list of debt entries."""
    debts = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            # Expected format:
            # name, balance, min_payment, rate
            parts = line.split(",")
            
            debt = {
                "name": parts[0],
                "balance": float(parts[1]),
                "min_payment": float(parts[2]),
                "rate": float(parts[3])
            }
            
            debts.append(debt)
            
    return debts








def write_summary(path, summary_text):
    """write the summary text to a file."""
    pass #Implementation code here