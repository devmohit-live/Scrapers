import requests as rq
from bs4 import BeautifulSoup as bs
r = rq.get('https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population')
print(r.status_code)
soup = bs(r.content, 'lxml')
table=soup.select('.wikitable td')
for it in table:
    if it.find('a'):
        m=it.text
        if m.startswith('1') or  m.startswith('2') or  m.startswith('3') or  m.startswith('4') or  m.startswith('5') or  m.startswith('6') or  m.startswith('7') or  m.startswith('8') or  m.startswith('9') or  m.startswith('0'):
            pass
        else:
#             ls.append()
            if m.__contains__('['):
                m=m[:m.index('[')]
                ls.append(m.strip())
            else:
                ls.append(m.strip())
        
fl=[]
for i in range(len(ls)):
    if i&1==0:
        fl.append(ls[i])

import json
for i in fl:
    url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=YOUR APP ID".format(i)
    data=rq.get(url)
    code=data.status_code
    json_data=json.loads(data.text)
    with open ('cities_temperature2.txt','a+') as f:
        if code==200:
            f.write(i +'\t' +str('%0.2f'%(json_data['main']['temp'] -273.15))+'°C \n')
            print(i , str(json_data['main']['temp']))
        else:
            f.write(i +'\t'+'Not Found'+'\n')
            print(i ,'Not Found')
