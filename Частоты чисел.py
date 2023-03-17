list1 = [1, 2, 3, 1, 2, 5, 7, 8, 2, 3, 0, 9, 9, 9, 0]

freq_dict = {}

for i in range(10):
    freq_dict[i] = 0
for num in list1:
    freq_dict[num] += 1

for num, freq in freq_dict.items():
    print(f"{num}: {freq}")