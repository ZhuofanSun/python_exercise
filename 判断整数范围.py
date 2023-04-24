grade = float(input('please input the grade: '))
if grade >= 90:
    print(grade,',A')
elif grade >= 80 and grade < 90:
    print(grade, ',B')
elif grade >= 70 and grade < 80:
    print(grade, ',C')
elif grade >= 60 and grade < 70:
    print(grade, ',C')
else: print('you failed')
