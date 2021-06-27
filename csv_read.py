import csv

def read_csv(filename):
  list_data   =  list()
  with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row)
        list_data.append(' '.join(row).strip())
  return list_data[1:]

# filename = 'schedule.csv'

# print(read_csv(filename))