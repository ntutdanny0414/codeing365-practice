class chess:
    def __init__(self,i,j,index, name, belong):
        self.index = index
        self.i = i
        self.j = j
        self.name = name
        self.belong = belong
    def getindex(self):
        return self.index
    def geti(self):
        return self.i
    def getj(self):
        return self.j
    def getname(self):
        return self.name
    def getbelong(self):
        return self.belong 
    def getrealname(self):
        chessvalueb = {'101':'General','102':'Guard','103':'Guard','104':'Elephant','105':'Elephant','106':'Rook','107':'Rook','108':'Horse','109':'Horse','110':'Bom','111':'Bom','112':'Pawn','113':'Pawn','114':'Pawn','115':'Pawn','116':'Pawn'}
        chessvaluer = {'201':'King','202':'Assistant','203':'Assistant','204':'Bishop','205':'Bishop','206':'Chariot','207':'Chariot','208':'Knight','209':'Knight','210':'Cannon','211':'Cannon','212':'Soldier','213':'Soldier','214':'Soldier','215':'Soldier','216':'Soldier'}
        if self.belong == 1:
            return chessvalueb[self.name]
        elif self.belong == 2:
            return chessvaluer[self.name]
    def getvalue(self):
        chessvalueb = {'101':1,'102':2,'103':2,'104':3,'105':3,'106':4,'107':4,'108':5,'109':5,'110':6,'111':6,'112':7,'113':7,'114':7,'115':7,'116':7}
        chessvaluer = {'201':1,'202':2,'203':2,'204':3,'205':3,'206':4,'207':4,'208':5,'209':5,'210':6,'211':6,'212':7,'213':7,'214':7,'215':7,'216':7}
        if self.belong == 1:
            return chessvalueb[self.name]
        elif self.belong == 2:
            return chessvaluer[self.name]
def sortway(x):
    return x.getindex()
def chesscaneat(chess33,index):
    caneatlist = [[],[],[],[],[],[],[],[],[]]
    for i in range(0,2):
        for j in range(0,3):
            caneatlist[3*i+j].append(chess33[i+1][j])
            caneatlist[3*(i+1)+j].append(chess33[i][j])
    for i in range(0,3):
        for j in range(0,2):
            caneatlist[3*i+j].append(chess33[i][j+1])
            caneatlist[3*i+(j+1)].append(chess33[i][j])
    return caneatlist[index]
def bomcaneat(chess33,index):#0-2,2-0#
    caneatlist = [[],[],[],[],[],[],[],[],[]]
    for j in range(0,3):
        caneatlist[3*0+j].append(chess33[2][j])
        caneatlist[3*2+j].append(chess33[0][j])
    for i in range(0,3):
        caneatlist[3*i+0].append(chess33[i][2])
        caneatlist[3*i+2].append(chess33[i][0])
    return caneatlist[index]
chess33 = [[None,None,None],[None,None,None],[None,None,None]]
chesseat = [[],[],[]]
for i in range(9):
    data = input().split(' ')
    posr = int(data[0])
    posl = int(data[1])
    belong = int(data[2]) // 100
    chess33[posr][posl] = chess(posr,posl,3*posr+posl,data[2],belong)
for i in range(3):#append can eat#
    for j in range(3):
        if chess33[i][j].getname() == '110' or chess33[i][j].getname() == '111' or chess33[i][j].getname() == '210' or chess33[i][j].getname() == '211':
            chesseat[i].append(bomcaneat(chess33,3*i+j))
        else:
            chesseat[i].append(chesscaneat(chess33,3*i+j))
for i in range(3):#remove not#
    for j in range(3):
        for k in range(len(chesseat[i][j])):#len#
            if chess33[i][j].getbelong() == chesseat[i][j][k].getbelong():
                chesseat[i][j][k] = ''
            elif chess33[i][j].getname() == '101' or chess33[i][j].getname() == '201':
                if chesseat[i][j][k].getvalue() == 7:
                    chesseat[i][j][k] = ''
            elif chess33[i][j].getrealname() == 'Pawn' or chess33[i][j].getrealname() == 'Soldier':#soldier#
                if chesseat[i][j][k].getvalue() != 1 and chesseat[i][j][k].getvalue() != 7:#and#
                    chesseat[i][j][k] = ''
            elif chess33[i][j].getrealname() == 'Bom' or chess33[i][j].getrealname() == 'Cannon':
                pass
            else:
                if chess33[i][j].getvalue() > chesseat[i][j][k].getvalue():
                    chesseat[i][j][k] = ''
        while '' in chesseat[i][j]:#remove''#
            chesseat[i][j].remove('')
for i in range(3):#sort#
    for j in range(3):
        chesseat[i][j] = sorted(chesseat[i][j],key = sortway)
for i in range(3):#print#
    for j in range(3):
        for k in chesseat[i][j]:#len#
            who = chess33[i][j].getrealname()+'('+str(chess33[i][j].geti())+','+str(chess33[i][j].getj())+')'#j#
            eat = k.getrealname()+'('+str(k.geti())+','+str(k.getj())+')'
            print(who+'->'+eat)
#3*i+j#
    
