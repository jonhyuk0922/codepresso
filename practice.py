"""
#total 변수를 생성하는 것 (선언)
total = 0

#range(100) -> 100개의 특정 값 배열(iter)
#배열 수 만큼 
for i in range(100):
    #
    total +=i

print("최종값 :",total)
total=0

for i in range(100):
    total +=i
    print(total)
    for i in range(100):
        total+=i
        print(total)
for x in range(100):
    if x<4:
        y=x*2
        print(x)
midpoint=5

lower = [] ; upper =[]

for i in range(10):
    if (i < midpoint):
        lower.append(i)
    else:
        upper.append(i)
print("small:", lower)
print("Big:",upper)

i = 65
if i < 8:
    print("fee:", "5,000원")
if i>=8 and i <20:
    print("fee:","15,000")
if i>=20 and i < 60:
    print("fee:","20,000")
else:
    print("free")
    
if 'r' in 'letter':
    print("YES")
else:
    print("NO")
    
for i in range(0,11,2):
    print(i)
    if i == 11:
        pass 

names =("lisa","bart a","marge")

for name in names:
    
    print(f"my name is {name}")

words = ('fresh', 'out' , 'pf','ideas')
for word in words:
    print(word)

empty_tuple =()
if empty_tuple is ():
    print("empty")
else:
    print("not empty") 

nums = [1,2,3,4,3,5]
total = 0
for num in nums :
     if num==3:
        continue

     total +=num
     print(total) 

fruits=['lemon','kiwi','orange']

for i, fruit in enumerate(fruits):
    if i==1:
        continue
    print(i,fruit)"""


apps_of_ages ={'4+':4433,'9+':987,'12+':1155,'17+':622}
total_apps=7197
ratios={}
percentages={}

for apps_of_age in apps_of_ages:
    ratios[apps_of_age]=apps_of_ages[apps_of_age]/total_apps
    percentages[apps_of_age]=ratios[apps_of_age]*100

print(ratios.values())
print(percentages.values())
    
c= list(ratios.values())
