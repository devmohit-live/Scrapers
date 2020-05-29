import requests as rq,bs4
price=input('Enter your budget\n:')
phone_list=[]
for e in phone:
    phone_list.append(e[0].text)
print(phone_list)
# targetting ul
x=soup.select('.vFw0gD')
c=0
l1=[]
for i in x:
    l1.append(i.text)
print(l1[0])

for i,j in zip(phone_list,l1):
    print('\nPhone is :: ',i)
    print('Specifications are :: ',j)