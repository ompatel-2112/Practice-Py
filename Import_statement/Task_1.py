f1=open("studentInfo.txt","w+")
f2=open("studentMarks.txt","w+")
f3=open("Avrage.txt","w+")
f4=open("Agrade.txt","w+")
f5=open("Bgrade.txt","w+")
f6=open("Cgrade.txt","w+")

def write_data(num):
    data1 = []
    data2 = []
    for i in range(num):
        roll_no = int(input("Enter Roll No. :"))
        name = str(input("Enter Name :"))
        info1 = (str(roll_no) + "-" + name + "\n")
        data1.append(info1)
        mark = []
        for j in range(3):
            marks = str(input("Enter Marks :"))
            mark.append(marks)
        info2 = (str(roll_no) + "-" + mark[0] + "-" + mark[1] + "-" + mark[2] + "\n")
        data2.append(info2)

    f1.writelines(data1)
    f2.writelines(data2)
    return data1, data2


def read_data(data_1, data_2):
    print(data_1, end="")
    print(data_2)
    f1.seek(0)
    read1 = f1.readlines()
    f2.seek(0)
    read2 = f2.readlines()
    return read1, read2


def cal_avg(str_1, str_2):
    ls1 = []
    ls2 = []
    for ls in str_1:
        x = ls.strip("\n")
        y = x.split("-")
        ls1.append(y)
    print("roll no and name:", ls1)

    for ls in str_2:
        z = ls.strip("\n")
        w = z.split("-")
        ls2.append(w)

    avg = []
    for i in range(len(ls2)):
        new = []
        new.append(str(ls2[i][0]))
        avg1 = round((int(ls2[i][1]) + int(ls2[i][2]) + int(ls2[i][3])) / 3)
        new.append(str(avg1))
        avg.append(new)
    print("roll no and  avg:", avg)
    return ls1, avg


def grade(data3, data4):

    list_avg = []
    for i in data4:
        list_avg.append(int(i[1]))


    average_set = set(list_avg)
    average_set.add(0)
    print("averageSet", average_set)

    sorted_list = sorted(average_set, reverse=True)
    f3.writelines(str(sorted_list))
    print("sortedList", sorted_list)


    final = []
    for info in data3:
        rollno= info[0]
        name = info[1]
        for marks in data4:
            if marks[0] == rollno:
                avg = marks[1]
                final.append([rollno, name, avg])
                break
    print("roll no , name and Avg:", final)

    for i in final:
        for j in range(len(data3)):
            if int(data3[j][0]) == i:
                for str1 in range(len(list_avg)):
                    j = int(list_avg[str1])
                    if 80 <= j <= 100:
                        f4.write(str(data3[str1][0])+ "-" + str(data3[str1][1]) + "-" + str(j) + "\n")
                    elif 60 <= j < 80:
                        f5.write(str(data3[str1][0]) + "-" + str(data3[str1][1]) + "-" + str(j) + "\n")
                    elif 40 <= j < 60:
                        f6.write(str(data3[str1][0]) + "-" + str(data3[str1][1]) + "-" + str(j) + "\n")
                    else:
                        print("average is lower than 40")

stu = int(input("Enter the No of Students :"))
d1, d2 = write_data(stu)
x1, x2 = read_data(d1, d2)
d3, d4 = cal_avg(x1, x2)
grade(d3, d4)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
