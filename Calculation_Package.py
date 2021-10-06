import csv
class Calculation():

    def __init__(self,i_csv):
        self.i_csv = i_csv

    def taxCalculation(self):
        
        with open(self.i_csv,'r') as n:
            csv_reader = csv.DictReader(n)

    
            with open('result2.csv','w') as m:
                fieldnames = ['Product-name','Product-CostPrice','Product-salesTaxPercentage','Country','Product-Finalprice']
                csv_writer = csv.DictWriter(m,fieldnames=fieldnames)

                csv_writer.writeheader()


    
        with open(self.i_csv,'r') as o:
            csv_read = csv.reader(o)
            next(csv_read)


            with open('result2.csv','a') as p:
                csv_w = csv.writer(p)
    
                for line in csv_read:
                    finalPrice = int(line[1]) + int(line[1])*int(line[2])/100
                    
                    csv_w.writerow([line[0],line[1],line[2],line[3],finalPrice])