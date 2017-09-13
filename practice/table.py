from beautifultable import BeautifulTable
Student = ["A", "B", "C", "D", "E"]
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]

avg_score = [0, 0, 0, 0, 0]
for i in range(0, 5):
    avg_score[i] = (kor_score[i] + math_score[i] + eng_score[i]) / 3
# midterm_score = [Student, kor_score, math_score, eng_score, avg_score]
# print(midterm_score.)

table = BeautifulTable()
table.column_headers = Student
table.append_row(kor_score)
table.append_row(math_score)
table.append_row(eng_score)
table.append_row(avg_score)
print(table)
