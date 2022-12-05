import csv

range_overlaps = 0

with open('camps.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        camp_range_1 = range(int(line[0].split('-')[0]), int(line[0].split('-')[1]) + 1)  # +1 because ranges are inclusive in their example
        camp_range_2 = range(int(line[1].split('-')[0]), int(line[1].split('-')[1]) + 1)
        
        if not set(camp_range_1).isdisjoint(set(camp_range_2)):
            range_overlaps += 1

print(f'There are {range_overlaps} camp ranges partially contained within another')
