from itertools import zip_longest
import string

item_priority_scores: dict[str, int] = {item: i + 1 for (i, item) in enumerate(string.ascii_lowercase + string.ascii_uppercase)}
sum_priority_scores: int = 0

with open('rugsacks.csv', newline='') as csvfile:
    for l_1, l_2, l_3 in zip_longest(*[csvfile] * 3):
        group_inventory = [set(line.strip()) for line in [l_1, l_2, l_3]]
        group_badge = list(set.intersection(group_inventory[0], group_inventory[1], group_inventory[2]))[0]        
        sum_priority_scores += item_priority_scores[group_badge]

print('The sum priority of badge items is', sum_priority_scores)
