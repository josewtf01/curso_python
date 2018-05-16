import csv
examplefile = open('example.csv')
examplereader = csv.reader(examplefile)
exampledata = list(examplereader)

for i in exampledata:
    print(i)

examplefile.close()
