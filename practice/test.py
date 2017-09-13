# recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n - 1))


print(factorial(int(input("input number for factorial: "))))

# from beautifultable import BeautifulTable
# Student = ["A", "B", "C", "D", "E"]
# kor_score = [49, 79, 20, 100, 80]
# math_score = [43, 59, 85, 30, 90]
# eng_score = [49, 79, 48, 60, 100]
#
# avg_score = [0, 0, 0, 0, 0]
# for i in range(0, 5):
#     avg_score[i] = (kor_score[i] + math_score[i] + eng_score[i]) / 3
# # midterm_score = [Student, kor_score, math_score, eng_score, avg_score]
# # print(midterm_score.)
#
# table = BeautifulTable()
# table.column_headers = Student
# table.append_row(kor_score)
# table.append_row(math_score)
# table.append_row(eng_score)
# table.append_row(avg_score)
# print(table)


# print("구구단 몇단을 계산할까요?")
# mult = input()
# i = int(mult)
#
# print("구구단 ", i, "단을 계산합니다")
#
# for j in range(1, 10):
#     print(i, "x ", j, " = ", i * j)
#     j += 1

# print("Year of birth")
# birth_year = input()
# age = 2017 - int(birth_year) + 1
#
# if 26 >= age and age >= 20:
#     print("University Student")
# elif age > 26:
#     print("older")
# else:
#     print("younger")
