import csv

def read_csv(filename):
  list_data   =  list()
  with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(len(''.join(row)))
        # print(row)
        if len(''.join(row)) == 0:
          continue
        list_data.append(' '.join(row).strip())
  return list_data[1:]
