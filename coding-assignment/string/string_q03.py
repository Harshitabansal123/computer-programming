#program to reverse each element of a string 
a="hello good night"
s=a.split()
for i in s:
    b=i[::-1]
    print(b, end=' ')
