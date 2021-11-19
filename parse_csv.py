import csv

with open('InputDataSample.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_data.csv', 'w') as new_file:
        fieldnames = ['Column A', 'Column B']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
