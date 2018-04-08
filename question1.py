from common_functions import get_csv_reader


def run(f):
    csv_reader = get_csv_reader(f)
    biggest_transaction_amount = 0
    for row in csv_reader:
        amount = float(row[5])
        if biggest_transaction_amount < amount:
            biggest_transaction_amount = amount
    print(biggest_transaction_amount)
