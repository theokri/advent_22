import csv

elf_kcal_buffer: list[int] = []
max_kcal: int = 0

with open('calories.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 0:
            elf_kcal_buffer.append(int(row[0]))
        else:
            max_kcal = max(max_kcal, sum(elf_kcal_buffer))
            elf_kcal_buffer.clear()

print('Maximum kcal:', max_kcal)