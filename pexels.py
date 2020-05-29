import requests as rq
from bs4 import BeautifulSoup as bs

url='https://www.pexels.com/@hiteshchoudhary'

soup=bs(rq.get(url).text,'html.parser')

title=soup.find('h1')
d1=soup.find('h2',attrs={'class':'profile-header__section profile-header__section profile-header__user-info__details__bio'}).text
d1=d1.strip()
d2=soup.select('.rd__button--text-secondary')
d2=d2[0].find('span').findNext('span').text

tags,values=[],[]
tg=soup.select('.profile-header__fact__label')
for i in tg:
    tags.append(i.text)
data=soup.findAll('strong')
for i in range(len(data)-1):
    values.append(data[i].text)
    

fw=open('Profile Deatils.txt','w+')
fw.write('Name : '+title.text+'\n'+'Description:\n')
fw.write(d2)
fw.write('\n'+d1.strip()+'\n')
for i in range(len(tags)):
    fw.write(tags[i]+' :\t'+values[i]+'\n')
    
fw.close()


import os
images=[]
os.mkdir('pexels')
imglink=soup.select('.photo-item__img')
for i in range(5):
    with open ("pexels\\"+str(i+1)+'.jpg','wb+') as f:
        f.write((rq.get(imglink[i]['data-large-src'])).content)
    
print('Download done!')