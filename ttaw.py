import pickle

List1 = [i for i in range(100, 1000) if i % 6 == 0 and i % 7 == 0]

filtered_numbers = [num for num in List1 if str(num).endswith('4')]

with open('numbers.bin', 'wb') as f:
    pickle.dump(filtered_numbers, f)

print("Дані записано у файл numbers.bin")

with open('numbers.bin', 'rb') as f:
    result = pickle.load(f)

print("Зчитані дані з файлу numbers.bin:")
print(result)
