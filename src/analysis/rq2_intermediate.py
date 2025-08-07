import csv

input_file = "data\\ClassEvalAnalysis\\benchmark_solution_code\\baseline.csv"
output_file = "data\\ClassEvalAnalysis\\benchmark_solution_code\\baselineProcessed.csv"

with open(input_file, mode='r', newline='', encoding="utf-8") as infile, open(output_file, mode='w', newline='', encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        if row[0].strip() == 'Class':
            writer.writerow(row)