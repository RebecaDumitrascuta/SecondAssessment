from cars import Cars
import csv
import json


def main():
    with open('input.csv', 'r') as csv_file:
        rows = csv.reader(csv_file)
        for row in rows:
            Cars({'brand': row[0], 'hp': row[2], 'price': row[3]}).evaluate_cars()

    for key, value in Cars.filter_cars.items():
        with open(r'output_data\\'+key + '.json', 'w') as file:
            file.write(json.dumps(value))
    for key, value in Cars.brands.items():
        with open(r'output_data\\'+key + '.json', 'w') as file:
            file.write(json.dumps(value))



if __name__ == '__main__':
    main()

