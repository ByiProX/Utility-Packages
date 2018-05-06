
import csv
import os

'''
Removes the header from all CSV files in the current
working directory.
'''

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('./removeCsvHeader'):
    if not csvFilename.endswith('.csv'):
        continue  # skip non-csv files

    print('Removing header from ' + csvFilename + ' ...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open('./removeCsvHeader/' + csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:  # Reader对象只能遍历一次，要再次读取CSV文件时，必须调用csv.reader创建一个对象
        if readerObj.line_num == 1:
            continue  # skip first row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
