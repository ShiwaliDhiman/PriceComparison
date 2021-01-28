import requests
from bs4 import *
print("*****MOBILE PHONE COMPARISON*****")
text=input("enter the full name of the product:")
page1=requests.get("https://www.flipkart.com/search?q="+text)
page2=requests.get("https://www.amazon.in/s?k="+text)
page3=requests.get("https://www.snapdeal.com/search?keyword="+text)
sc1=page1.status_code
sc2=page2.status_code
sc3=page3.status_code

if(sc1==200):
    try:
        soul=BeautifulSoup(page1.content,"html.parser")
        product_name=soul.find("div",class_="_4rR01T")
        price=soul.find("div",class_="_30jeq3 _1_WHN1")
        print("FLIPKART: product name=",product_name.get_text())
        print("FLIPKART: price=",price.get_text())
    except:
        print("Product Not Found")
elif(sc1==503):
    print("try again later \n server of flipkart not working")
else:
    print("Product Not Available")
    
    
if(sc2==200):
    try:
        soul=BeautifulSoup(page2.content,"html.parser")
        main=soul.find("div",class_="a-section aok-relative s-image-fixed-height")
        product_name2=main.img["alt"]
        price2=soul.find("span",class_="a-offscreen")
        print("AMAZON: product name=",product_name2)
        print("AMAZON: price=",price2.get_text())
    except:
        print("Product Not Found")
elif(sc2==503):
    print("###try again later#### \n #####server of amazon not working#####")
else:
    print("Product Not Available")


if(sc3==200):
    try:
        soul=BeautifulSoup(page3.content,"html.parser")
        main=soul.find("p",class_="product-title")
        product_name3=main.get_text()
        price3=soul.find("span",class_="lfloat product-price")
        print("SNAPDEAL: product name=",product_name3)
        print("SNAPDEAL: price=",price3.get_text())
    except:
        print("Product Not Found")
elif(sc3==503):
    print("###try again later#### \n #####server of amazon not working#####")
else:
    print("Product Not Available")

print("****if product names are not same then product you want to compare is not present in all the sites****")

