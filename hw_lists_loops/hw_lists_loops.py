# hw_lists_loops.py

# Завдання 1
numbers = [1, 5, 2, 8, 3, 7]

max_num = max(numbers)
min_num = min(numbers)
sum_num = sum(numbers)

print("Завдання 1:")
print("Найбільше число:", max_num)
print("Найменше число:", min_num)
print("Сума всіх чисел:", sum_num)

# Завдання 2
grades = [10, 8, 12, 7, 9]

average_grade = sum(grades) / len(grades)
above_average = [grade for grade in grades if grade > average_grade]

print("\nЗавдання 2:")
print("Середній бал:", average_grade)
print("Оцінки вище середнього:", above_average)
