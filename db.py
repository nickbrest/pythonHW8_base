import csv

def read(data_base):
    with open(data_base, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter = ",")
        for row in file_reader:
            print(' '.join(row))


def write(data_base, data):
    with open(data_base, 'a', encoding='utf-8') as file:
        file_csv = csv.writer(file)
        file_csv.writerow(data)


def remove(data_base, data):
    with open(data_base, 'w', encoding='utf-8') as file:
        file
