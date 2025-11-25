






def snowball_order(debt_list):
    """Return the debts sorted from smallest balance to largest."""
    return sorted(debt_list, key=lambda d: d["balance"])









def snowball_plan(debt_list, extra_amount):
    """Return a snowball payoff plan based on smallest-balance-first strategy."""
    # sort debts smallest to largest
    ordered = sorted(debt_list, key=lambda d: d["balance"])
    
    
    working = []
    for debt in ordered:
        working.append({
            "name": debt["name"],
            "balance": debt["balance"],
            "min_payment": debt["min_payment"],
            "rate": debt["rate"],
        })    
            # Step 3: prepare plan results list
    plan = []

    # monthly payoff loop structure
    month = 1
    max_months = 1000

    while any(d["balance"] > 0 for d in working) and month <= max_months:

        # add monthly interest before payments
        for debt in working:
            if debt["balance"] > 0:
                interest = debt["balance"] * debt["rate"] / 12
                debt["balance"] += interest

        # apply minimum payments
        for debt in working:
            if debt["balance"] > 0:
                debt["balance"] -= debt["min_payment"]
                if debt["balance"] < 0:
                    debt["balance"] = 0


        # apply snowball extra payment to smallest remaining debt
        active_debts = [d for d in working if d["balance"] > 0]
        if active_debts:
            smallest = active_debts[0]
            smallest["balance"]-= extra_amount
            if smallest["balance"] < 0:
                smallest["balance"] = 0  
                
    # record snapshot of balances for each month
    snapshot = {
        "month": month,
        "balances": [d["balance"] for d in working]
    }
    plan.append(snapshot)                
                    
          
    month += 1


    # build final summary for return
    total_months = month - 1 #(because month increments after final payment)
    
    summary = {
        "total_months": total_months,
        "final_balances": [d["balance"] for d in working],
        "monthly_plan": plan
    }
    
    return summary

