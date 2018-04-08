import question1
import question4

def run():
    with open('trades_march_to_april_2018.csv', encoding='utf-8') as f:
        print_question_separator('1. What is the highest size of a transaction between March and April 2018 (BTC)')
        question1.run(f)
        print_question_separator('4. Average sale and buy price per day for the most bought currency')
        question4.run(f)

def print_question_separator(question_number):
    print('\nQuestion ' + str(question_number), end='\n' + 100 * '-' + '\n')


run()
# It is really bugging me that you have to define function before you call it, so I wrapped everything in run()
# Thanks to that I can order functions as they are called, so you can read code from top to bottom
