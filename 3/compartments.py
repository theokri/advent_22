import csv
import string

item_priority_scores: dict[str, int] = {item: i + 1 for (i, item) in enumerate(string.ascii_lowercase + string.ascii_uppercase)}
sum_priority_scores: int = 0

with open('rugsacks.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rugsack = row[0]
        rugsack_delimiter = len(rugsack) // 2        
        first_compartment, second_compartment = rugsack[rugsack_delimiter:], rugsack[:rugsack_delimiter]
        common_items = set(first_compartment).intersection(set(second_compartment))

        sum_priority_scores += sum([item_priority_scores[item] for item in common_items])

print('The sum priority of misplaced items is', sum_priority_scores)
