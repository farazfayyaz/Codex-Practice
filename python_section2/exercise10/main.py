import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]


try:
    with open('packing_list.csv', 'r') as file:
    # Work with files here
        csv_reader = csv.reader(file)

        for row in csv_reader:
            print(row)
except FileNotFoundError:
# Catch errors here
    print('Packing list file not found. Creating a new one.')
    with open('packing_list.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)

        csv_writer.writerows(data)