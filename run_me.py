import question1

def run():
    with open('trades_march_to_april_2017.csv', encoding='utf-8') as f:
        print_question_separator('1. What is the transaction with the highest volume in the timespan')
        question1.run(f)


def print_question_separator(question_number):
    print('\nQuestion ' + str(question_number), end='\n' + 100 * '-' + '\n')


run()
# It is really bugging me that you have to define function before you call it, so I wrapped everything in run()
# Thanks to that I can order functions as they are called, so you can read code from top to bottom
