import csv
file_path = 'data/country.csv'
with open(file_path, encoding='utf8') as f:
    csv_reader = csv.reader(f, delimiter=',')

#     next(csv_reader)

#     for line in csv_reader:
#         print(line) 
    
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print("Header: ")
            print(line)
            print('Data')
        else:
            print(line)

# #opening csv as a dictionary
# with open(file_path, encoding='utf8')as f:
#     csv_reader = csv.DictReader(f)

#     next(csv_reader)

#     for dict in csv_reader:
#         print(f'The are of {dict['name']} is {dict['area']} km2')

# # use custom filed name for dictionary
# field_names = ['Country Name', 'Area', 'Code2', 'Code3']
# with open(file_path, encoding='utf8') as f:
#     csv_reader = csv.DictReader(f, field_names)
#     for dict in csv_reader:
#         print(dict)