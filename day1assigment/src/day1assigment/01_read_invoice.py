import csv

total_invoices = 0
greater_than_100k = 0
invalid_amount = 0

with open("data/homework_invoices.csv") as src:
    data = csv.DictReader(src)
    for invoice in data:
        total_invoices = total_invoices + 1

        vendor = invoice["vendor"]
        amount = invoice["amount"]
        status = invoice["status"]
        try:
            amount = float(amount)
            if amount > 100000:
                greater_than_100k = greater_than_100k + 1
                print(
                    f"{invoice['invoice_id']} - "
                    f"{vendor} - "
                    f"{amount} - "
                    f"{status} - "
                    f"Greater than 100,000"
                )
        except ValueError:
            invalid_amount = invalid_amount + 1
            print(f" Invoice Id :: {invoice['invoice_id']} invalid amount {amount}")
    print(" Total invoice :", total_invoices)
    print(" Total invoice  greater than 10000:", greater_than_100k)
    print(" Total invoice with missing/invalid amount ", invalid_amount)
