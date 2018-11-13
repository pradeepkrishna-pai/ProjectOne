import csv

class A(object):
    
    def __init__(self, data):
        self.data = data
        
    def read_data(self):
        pass
    
    def write_to_csv(self):
        
        with open('CSVFile.csv', 'wb') as f:
            writer = csv.writer(f)
            for i in self.data:
                writer.writerow(i)
                

data = [['Pradeep', '1111'], ['Sneha', '2222'], ['Kruthika', '3333'], ['Shalini', '4444']]

obj = A(data)
obj.write_to_csv()