import csv


def read_out_csv(path):
    with open(path) as csvfile:

        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        return [row for row in csv_reader]
