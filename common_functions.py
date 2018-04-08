import csv


def get_csv_reader(f):
    f.seek(0)
    reader = csv.reader(f, delimiter=',')
    next(reader)
    return reader


def print_results_in_order(data, value_getter):
    i = 1
    for key in data:
        base_indentation = 40
        calculated_indentation = base_indentation - (len(key) + len(str(i)))
        print(str(i)+'.',
              key,
              calculated_indentation * '.',
              format(value_getter(key), ','),
              'Eur')
        i += 1


def find_biggest_sum_in_dict(data):
    biggest_sum = 0
    biggest_key = ''
    for key, count in data.items():
        if biggest_sum < count:
            biggest_key = key
            biggest_sum = count
    return {'name': biggest_key, 'sum': biggest_sum}

def find_second_biggest_sum_in_dict(data):
    biggest_sum = 0
    biggest_key = ''
    for key, count in data.items():
        if biggest_sum < count:
            biggest_key = key
            biggest_sum = count

    data[biggest_key] = 0;

    biggest_sum = 0
    second_biggest_key = ''

    for key, count in data.items():
        if biggest_sum < count:
            second_biggest_key = key
            biggest_sum = count

    return {'name': second_biggest_key, 'sum': biggest_sum}

