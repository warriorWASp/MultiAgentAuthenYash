from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
with open('third\\home.html','r',encoding='utf-8')as f:
    content=f.read()
    
soup=BeautifulSoup(content,'lxml') 


categories=soup.find_all(itemprop="name")
categoryDescription=soup.find_all(itemprop="description")

    
links= soup.find_all('a')
name=[]
# def tabulizer():
    
#     length = min(len(categories), len(categoryDescription), len(links))
    
#     for i in range(length):
#          print("name:\t",categories[i].text ,"description:\t",categoryDescription[i].text, "URL:\t",links[i+1].get('href'))
        


# tabulizer()
name=[]
description=[]
url=[]
length = min(len(categories), len(categoryDescription), len(links))
    
for i in range(length):
          name.append(categories[i].text) ,description.append(categoryDescription[i].text), url.append(links[i+1].get('href'))
          
# table=str([name,description,url])       

# with open('third\\output.csv','w',encoding='utf-8') as f:
#     f.write(tabulate(table))
table = list(zip(name, description, url))


with open('third\\output.csv', 'w', encoding='utf-8') as f:
    f.write(tabulate(table, headers=["Name", "Description", "URL"], tablefmt="csv"))