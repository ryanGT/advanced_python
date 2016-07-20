import csv

mysniff = csv.Sniffer()

def get_dialect(filename,delimiters=[',','\t',' '], samplelines=5):
    f = open(filename,'r')
    all_list = f.readlines()
    sample_list = all_list[0:samplelines]
    sample_str = ''.join(sample_list)
    f.close()
    
    out = mysniff.sniff(sample_str, delimiters=delimiters)
    return out    


def read_to_list(filename, dialect):
    f = open(filename,'r')
    myreader = csv.reader(f, dialect=dialect)

    outlist = []
    
    for row in myreader:
        outlist.append(row)

    return outlist

fn1 = 'data_file_1.csv'
fn2 = 'data_file_1t.csv'
dialect1 = get_dialect(fn1)
dialect2 = get_dialect(fn2)

rows1 = read_to_list(fn1, dialect1)
rows2 = read_to_list(fn2, dialect2)

## f = open('data_file_1t.csv','r')
## list2 = f.readlines()
## f.close()
