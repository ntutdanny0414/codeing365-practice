import re
def user(username):
    if len(username) == 8 and len(re.sub(r'[a-zA-Z0-9]','',username)) == 0:#resub('ch','want to')#
        return True
    else:
        return False
def password(username):
    if 0 < len(username) <= 8 and len(re.sub(r'[a-zA-Z0-9@#%_-]','',username)) == 0:
        return True
    else:
        return False
def sort(x):
    return int(x[0])
userdata = []
userpassworddata = []
Candidatedata = []
Candidatevote = {}
Candidatenum = []
hasvote = []
manage= input().split(',')
if manage[0] == 'A':
    if not user(manage[1]):
        print('username error')
        print('Add user error')
    elif not password(manage[2]):#not#
        print('password error')
        print('Add user error')
    else:
        userdata.append(manage[1])
        print('Add user successful')
while True:
    data = input().split(',')
    if data[0] == 'A':
        if not user(data[1]) or (data[1] in userdata):#not#
            print('username error')
            print('Add user error')
        elif not password(data[2]):
            print('password error')
            print('Add user error')
        else:
            userdata.append(data[1])
            userpassworddata.append((data[1],data[2]))
            print('Add user successful')
    elif data[0] == 'M':
        if (data[-2],data[-1]) in Candidatedata:
            print('Candidate data error')
        elif (data[1],data[2]) != (manage[1],manage[2]):
            print('Login error')
        else:
            Candidatedata.append((data[-2],data[-1]))
            Candidatevote[data[-2]] = [data[-1],0]
            Candidatenum.append(data[-2])
            print('Add candidate successful')
    elif data[0] == 'V':
        if ((data[1],data[2]) in hasvote) or ((data[1],data[2]) == (manage[1],manage[2])):
            print('Voting error')
        elif data[-1] not in Candidatenum:
            print('Candidate error')
        elif (data[1],data[2]) not in userpassworddata:
            print('Login error')
        else:
            Candidatevote[data[-1]][1] = Candidatevote[data[-1]][1] + 1
            hasvote.append((data[1],data[2]))
            print('Voting successful')
    elif data[0] == 'Q':
        if (data[1],data[2]) not in userpassworddata:
            print('Login error')
        else:
            vote = sorted(list(Candidatevote.items()),key = sort)
            s = ''
            for i in range(len(vote)):
                s = s+'('+str(vote[i][0])+','+str(vote[i][1][0])+','+str(vote[i][1][1])+'),'#index list ##string plus ,#
            print(s.rstrip(','))#remove,#
    elif data[0] == 'E':
        print('Exit')
        break
    
