import csv

# with open('customers.csv','r') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     print(csv_reader)
#     for line in csv_reader:
#         print(line[1])


with open('customers.csv','a')as file:
    new_customers_list = [
    [13, "Fatima Noor", "fatima.noor@example.com", 24, "Pakistan"],
    [14, "Liam O'Brien", "liam.obrien@example.com", 37, "Ireland"]
]
    csv_writer = csv.writer(file)
    csv_writer.writerows(new_customers_list)