import requests
import bs4

url=input("enter the url:-")
a=requests.get(url)

file="file.html"
bs=bs4.BeautifulSoup(a.text,"html.parser")
formeted_text=bs.prettify()
print(formeted_text)
with open(file,"w+")as f:
    f.write(formeted_text)
list_of_imgs=bs.find_all('img')
list_as=bs.find_all('a')

num_of_imgs=len(list_of_imgs)
num_of_as=len(list_as)

print("number of img tags",num_of_imgs)
print("number of anchor_tags",num_of_as)

