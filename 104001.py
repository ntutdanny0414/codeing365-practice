class bank():#class銀行
    money=0
    def saveMoney(self,money):#存錢
        self.money+=money
        return self.money
    def takeMoney(self,money):#取錢
        self.money -=money
        return self.money
    def checkMoney(self):#看現在的錢 也可以直接a.money取得
        return self.money
def main():
    a = bank()
    b = bank()
    String = "A"
    while True:
        s = input()
        if(s == "a"):#切換操作帳戶 A
            temp = a # a bank 被 temp所指向
            String = "A" 
            print("Select A")
        elif(s == "b"):#切換操作帳戶 B
            temp = b
            String = "B"
            print("Select B")
        elif(s == "v"):#帳號名稱:帳號餘額
            print(String,":",temp.checkMoney(),sep="")
        elif(s == "w"):# 拿走錢
            money = int(input()) # 拿多少錢
            print(String,":Withdraw,",temp.takeMoney(money),sep="")
        elif(s == "s"):# 存錢
            money = int(input()) # 存多少錢
            print(String,":Deposit,",temp.saveMoney(money),sep="")
        elif(s == "p"):# 輸出 A帳戶 跟 B帳戶的金額
            if(a.checkMoney() <= 0 and b.checkMoney() > 0):
                print("A:0%,B:100%")
            elif(a.checkMoney() > 0 and b.checkMoney() <= 0):
                print("A:100%,B:0%")
            elif(a.checkMoney()==0 and b.checkMoney()==0):
                print("A:50%,B:50%")
            else:
                A = a.checkMoney()
                B = b.checkMoney()
                print("A:%d%%,B:%d%%"% ( round((A/(A+B))*100) , round((1-A/(A+B))*100)  ),sep="")
        else:
            exit()
main()
    
    