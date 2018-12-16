mark = [19,10,8,17,9]

marks = 5

while True:
    print(mark)
    flag = False
    for pointer in range(0, marks-1):
        if mark[pointer] > mark[pointer+1]:
            num1 = mark[pointer]
            num2 = mark[pointer+1]
            mark[pointer] = num2
            mark[pointer+1] = num1
            flag = True
    marks = marks -1
    if flag == False or marks == 1:
        break

print(mark)