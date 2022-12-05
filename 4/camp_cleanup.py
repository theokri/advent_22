import csv

range_subsets = 0

with open('camps.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        camp_range_1 = range(int(line[0].split('-')[0]), int(line[0].split('-')[1]) + 1)  # +1 because ranges are inclusive in their example
        camp_range_2 = range(int(line[1].split('-')[0]), int(line[1].split('-')[1]) + 1)
        
        print(camp_range_1, camp_range_2)
        if set(camp_range_1).issubset(set(camp_range_2)) or set(camp_range_2).issubset(set(camp_range_1)):
            range_subsets += 1
            print(range_subsets)

print(f'There are {range_subsets} camp ranges contained fully within another')
