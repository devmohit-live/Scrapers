import requests as rqs,os
from bs4 import BeautifulSoup as soup
user_agent = {'User-agent': 'Mozilla/5.0'}
http_response= rqs.get("https://www.amazon.in/s?k=fossil+watches",headers=user_agent)
http_response_text=http_response.text

soup_object=soup(http_response_text,"lxml")
i=0
os.mkdir('amazon_img')
for a in soup_object.find_all("div", {"class":"a-section a-spacing-medium"}):
#print(a.prettify())
 
    i=i+1
    try:
        name=a.img["alt"]
        print(name)

        image=a.img["src"]
        print(image)

        price=a.find("span",{"class":"a-price-whole"})
        print("₹"+price.text+"\n")
        
        byte=rqs.get(image).content
        with open("amazon_img/"+str(i)+".jpg","wb+") as f:
            f.write(byte)
    except Exception as e:
        print("Not Found.",e)
    