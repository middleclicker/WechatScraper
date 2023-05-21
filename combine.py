import csv
import os

folder_path = os.getcwd()
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

def combine_csv_files(output_file):
    unique_records = []

    for file in csv_files:
        with open(file, mode='r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row not in unique_records:
                    unique_records.append(row)

    # Write unique records to the output file
    with open(output_file, 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)

        # Write headers
        headers = ['Date', 'Time', 'Author', 'Msg']
        writer.writerow(headers)

        for msg in unique_records:
            writer.writerow(msg)

combine_csv_files("combined.csv")
