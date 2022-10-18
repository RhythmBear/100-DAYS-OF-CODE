import random

# num = "angela"
# new_num = [n for n in num]
# print(new_num)
#
# new_range = [n * 2 for n in range(1, 5)]
# print(new_range)
#
# numbers = [1, 1, 2, 3, 5, 8, 11, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]

students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {name: random.randint(1, 100) for name in students}

students_passed = {name: score for (name, score) in students_scores.items() if score >= 50}
print(students_scores)
print(students_passed)

# print(result)
