import csv

elf_kcal_buffer: list[int] = []
kcal_sums: list[int] = []

with open('calories.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 0:
            elf_kcal_buffer.append(int(row[0]))
        else:
            kcal_sums.append(sum(elf_kcal_buffer))
            elf_kcal_buffer.clear()

kcal_sums.sort(reverse=True)

print(f'Top 3 elves have {sum(kcal_sums[:3])} calories')
