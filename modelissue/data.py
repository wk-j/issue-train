def loaddata(foldername):
    print(foldername)
    DataTitle = []
    DataDescription = []
    DataLabel = []
    import csv
    import os
    for filename in os.listdir(foldername):
        if filename.endswith(".csv"):
            with open(os.path.join(foldername+"/", filename), mode='r') as csv_file:
                print(filename)
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        #print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    #print(f'\t{row["Title"]}')
                    DataTitle.append(row["Title"])
                    DataDescription.append(row["Description"])
                    DataLabel.append(row["Label"])
                    line_count += 1
                print(f'Processed {line_count} lines.')
    return DataTitle,DataDescription,DataLabel

if __name__ == "__main__":
    print('')
    #loaddata('Documents')
    