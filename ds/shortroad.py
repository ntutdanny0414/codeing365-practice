data = input().split(',')
city = int(data[0])
road = int(data[1])
count = 0
get = []
citydata = [[100000]*city for i in range(city)]
for i in range (0,road):
    cityroad = input().split(',')
    citydata[int(cityroad[0])-1][int(cityroad[1])-1] = int(cityroad[2])
    citydata[int(cityroad[1])-1][int(cityroad[0])-1] = int(cityroad[2])
i = 1
while True:
    get.append(i)
    if len(get) == city:
        break
    count = count + min(citydata[i-1])
    for j in range(0,len(citydata)):
        citydata[j][i-1] = 100000
    i = citydata[i-1].index(min(citydata[i-1])) + 1
    
print(count)
