import csv
import os

# Define input and output file paths
input_file_path = 'SupplementalFile4.csv'
output_file_path = 'GenomeInitiativeCountries.csv'

# Open the input CSV file for reading
with open(input_file_path, mode='r') as input_file:
    the_file = input_file.read().split('\n')

output_file = open(output_file_path, mode='w')

for row in the_file[:-1]:
    line = row.split(',')
    # print(line)
    modified_row = "{},{},{},{},".format(line[0].strip(), line[1].strip(), line[4].strip(), line[5].strip())
    output_file.write(modified_row + '\n')