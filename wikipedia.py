import requests as rq
import bs4

r = rq.get('https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population')

print(r.status_code)

soup = bs4.BeautifulSoup(r.content, 'html.parser')

table = soup.findAll('table', attrs = {'class':'wikitable'})
# print(table)
print(len(table))

tb = []
for t in table:
    x = t.findAll('tbody')
    tb.append(x)

tr = []
#trow[0] bcz it (tb) consists only one object=> [[obj]] ie  now to access a we write listname[0] returns another list=>[obj]
for trow in tb:
#     print(trow[0].findAll('tr'))
    tr.append(trow[0].findAll('tr'))
# print(tr)

print(len(cities))

print(cities)