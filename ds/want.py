def findenemy(couple,teacher):#student teacher#
    for i in range(len(couple)):
        if teacher in couple[i]:
            return couple[i][0]
def incouple(couple,teacher):
    for i in range(len(couple)):
        if teacher in couple[i]:
            return True
    return False
def iwantyou(studentdata,teacherdata,studentname,index,couple):
    nowname = []
    nowwant = []
    manyround = []
    for i in range(len(couple)):
        nowname.append(couple[i][0])
        nowwant.append(couple[i][1])
    for i in range(len(studentname)):
        if studentname[i] not in nowname:
            teacher = studentdata[studentname[i]][index]
            if incouple(manyround,teacher):
                myvalue = teacherdata[teacher].index(studentname[i])#small good#
                enemyvalue = teacherdata[teacher].index(findenemy(manyround,teacher))
                if enemyvalue > myvalue:
                    manyround.remove([findenemy(manyround,teacher),teacher])
                    manyround.append([studentname[i],teacher])
                else:
                    pass
            else:
                manyround.append([studentname[i],teacher])
    for i in range(len(manyround)):
        if manyround[i][1] not in nowwant:
            couple.append(manyround[i])
    return couple
def sort(x):
    return x[0]
teachername = []
studentname = []
studentdata = {}
teacherdata = {}
teachernum = 0
student = []#alldata#
teacher = []
ans = {}
first = input().split(',')#can know teacher count and name#
for i in first:
    teachername.append(i)
    teachernum += 1
student = [first]
for i in range(teachernum - 1):#student = teacher#
    data = input().split(',')
    student.append(data)
for j in range(teachernum):
    data = input().split(',')
    teacher.append(data)
for j in teacher[0]:#add stu name#
    studentname.append(j)
studentname = sorted(studentname)#sort#
teachername = sorted(teachername)#sort#
for i in range(len(studentname)):#name = alldata#
    studentdata[studentname[i]] = student[i]
for i in range(len(teachername)):
    teacherdata[teachername[i]] = teacher[i]
out = []
for i in range(0,teachernum):
    out = iwantyou(studentdata,teacherdata,studentname,i,out)
    if len(out) == teachernum:
        break
out = sorted(out,key = sort)
for i in range(len(out)):
    print(out[i][0]+'->'+out[i][1])
