import requests as rq, bs4, os
print(10*'*'+' Welcome to image downloader '+'*'*10)
print('-----This Script only downloads images form the static website-----')
print('In case of dynamic website you may get the images or placeholders \n')
url=input('Enter the URl :: ')
r=rq.get(url)
soup=bs4.BeautifulSoup(r.text,'html.parser')
x=soup.findAll('img')
l=[]
for i in x:
    temp=i['src']
    if temp.startswith('http'):
        pass
    elif temp.startswith('/static'):
        temp=url+temp
    elif temp.startswith('/assets'):
        temp=url+temp
    elif temp.startswith('//'):
        temp='http:'+temp
    elif temp.startswith('/'):
        temp='http:/'+temp
    l.append(temp)

folder=input('Enter the name of folder in which you want to store the downloaded images :: ')
try :
    os.mkdir(folder)
except FileExistsError:
    print('Folder Already Exists, Want to download in this existing folder ?')
    print("press 'y' for Yes , other key to abort ")
    fac=input()
    if fac=='y':
        print("We are downloading the file, Don't close the program " )
        for index,img_link in enumerate(l):
            image_data=rq.get(img_link).content
            
            with open (folder+"\\"+str(index)+'.jpg','wb+') as f:
                f.write(image_data)

        print('*'*10+"\tDownload Done\t"+'*'*10)
    else:
        print('-----------Aborted!------------')
