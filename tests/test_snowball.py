from src.snowball import snowball_order


def test_snowball_order_sorts_correctly():
    """Verify that debts are sorted from smallest balance to largest."""
    debts = [
        {"name": "Car", "balance": 5000, "min_payment": 200, "rate": 0.06},
        {"name": "Card", "balance": 800, "min_payment": 25, "rate": 0.18},
        {"name": "Loan", "balance": 1500, "min_payment": 75, "rate": 0.10},
    ]

    ordered = snowball_order(debts)

    # balances should come back as 800, 1500, 5000
    balances = [d["balance"] for d in ordered]

    assert balances == [800, 1500, 5000]
