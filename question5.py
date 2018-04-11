import iso8601
import matplotlib.pyplot as plt

from common_functions import get_csv_reader

def run(f):
    csv_reader = get_csv_reader(f)
    transaction_counts = {}
    for row in csv_reader:
        date = iso8601.parse_date(row[1])
        key = str(date.year) + "-0" + str(date.month) + "-0" + str(date.day) + " 0" + str(date.hour) + ":00"
        transaction_counts.setdefault(key, 0)
        transaction_counts[key] += 1
        
    for item in transaction_counts.items():
        x = item[0]
        y = item[1]
        fig = plt.scatter(x, y, s=200)
        print(item[0], " -> ", item[1], " transactions")

    plt.title("Graph of a days transactions", fontsize=20)
    plt.xlabel("Hours", fontsize=14)
    plt.ylabel("Transaction numbers", fontsize=14)
    plt.show(fig)
    