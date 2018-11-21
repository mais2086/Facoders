#يظهر في البداية التعليمات للمعلمة، كالتالي:
while True:
    ch=input("Choose one: students_names, student_score, students_count: ")

#٢- ثم يطلب من المعلمة ادخال المعلومات المطلوبة: اسم الطالب٫ اسم الصف٫ او كلاهما، بحسب المطلوب في ال function.
    if ch == 'students_names':

        def students_names(grade):
            grade = list(grade.keys())
            print('grade')
        grade=input("Enter grade: ")

    elif ch == 'student_score':
        def student_score(grade,name):
            sc=sum(grade.get("name"))
            print('sc')
        grade, name = input('Enter grade: '), input('Enter name: ')

    elif ch == 'students_count':
    
        def students_count(grade):
            ct=len(grade.keys())
            print('ct')
        grade = input('Enter grade: ')

    finish=input('Are you Done(Y/N): ')
    if finish == 'Y':
        break
    else:
        continue
grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}
