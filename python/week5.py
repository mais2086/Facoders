s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
s1_sum=sum(s1[1:6])
s2_sum=sum(s2[1:6])
s3_sum=sum(s3[1:6])
name = input("Enter student's name: ")
if name in s1:
        print(s1[0], s1_sum)
elif name in s2:
        print(s2[0], s2_sum)
elif name in s3:
        print(s3[0], s3_sum)
else:
        print('Student is not recorded 0')
