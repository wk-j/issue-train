import logging


def loaddata(foldername):
    logging.info(f"import data in - {foldername}")

    DataTitle = []
    DataDescription = []
    DataLabel = []
    import csv
    import os
    for filename in os.listdir(foldername):
        if filename.endswith(".csv"):
            with open(os.path.join(foldername+"/", filename), mode='r') as csv_file:
                logging.info(f"process file - {filename}")
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        #print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    # print(f'\t{row["Title"]}')
                    DataTitle.append(row["Title"])
                    DataDescription.append(row["Description"])
                    DataLabel.append(row["Label"])
                    line_count += 1
                logging.info(f"processed lines - {line_count}")
    return DataTitle, DataDescription, DataLabel
