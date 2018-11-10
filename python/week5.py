s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
s1_num= [18, 17, 19.5, 8, 25]
s2_num=[20, 20, 19, 9, 28]
s3_num=[14.5, 16, 13, 7, 23]
name = input("Enter student's name: ")
while True:
    if name in s1:
        print(s1[0], sum(s1_num))
    elif name in s2:
        print(s2[0], sum(s2_num))
    elif name in s3:
        print(s3[0], sum(s3_num))
    else:
        print('Student is not recorded 0')
    break
