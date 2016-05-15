'''
Created on May 15, 2016

@author: raydelto
'''
import csv;

csv_file = None
header_count = {}

def add(value):
    global header_count
    if value in header_count:
        header_count[value] += 1
    else:
        header_count[value] = 1

def init():
    global csv_file
    csv_file = open('files/Reporte.csv', 'rt')

def parse():
    global csv_file
    global header_count
    init()
    print "test"
    
    try:
        reader = csv.reader(csv_file)
        for row in reader:
            #print row[0]
            add(row[0])
    except:
        print "error"
    finally:
        csv_file.close()
    print header_count;
        
if __name__ == '__main__':
    parse()