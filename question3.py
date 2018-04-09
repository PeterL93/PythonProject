from common_functions import get_csv_reader

def run(f):
    csv_reader = get_csv_reader(f)
    buycounter = 0
    sellcounter = 0
    for row in csv_reader:
        if row[6] == "BUY":
            buycounter +=1
        if row[6] == "SELL":
            sellcounter +=1
    if buycounter>=sellcounter:
        print( "The most common is Buy which was: ")
        print(buycounter)
    else:
        print("the most common is Sell which was: ")
        print(sellcounter)




    
    
        