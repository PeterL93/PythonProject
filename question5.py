import iso8601
import matplotlib.pyplot as plt

from common_functions import get_csv_reader

def run(f):
    csv_reader = get_csv_reader(f)
    x = biggest_transaction_amount_day = {}
    y = biggest_transaction_amount = 0
    for row in csv_reader:
        date = iso8601.parse_date(row[1])
        key = str(date.year) + "-0" + str(date.month) + "-0" + str(date.day) + " 0"
        biggest_transaction_amount_day.setdefault(key, 0)
        biggest_transaction_amount_day[key] += 1
        amount = float(row[5])
    
        if biggest_transaction_amount < amount:
            biggest_transaction_amount = amount
    for item in biggest_transaction_amount_day.items():
        fig = plt.scatter(biggest_transaction_amount,biggest_transaction_amount_day)
        plt.show(fig)
        print(x, y)

        


