import csv

li = []
with open('result.csv','wb') as wf:
    writer = csv.writer(wf)

    with open('test.csv','rb') as f:
        reader = csv.reader(f)
        for row in reader:
            li.append(row)
            writer.writerow(row)
            
print li