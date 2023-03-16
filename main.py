import webbrowser
import requests

pageurl = input("podaj adres strony: ")
date=input("podaj date: ")
url = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date)
date2=input("podaj date: ")
url2 = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date2)
date3=input("podaj date: ")
url3 = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date3)
response = requests.get(url)
response2 = requests.get(url2)
response3 = requests.get(url3)
d = response.json()
print(d)
page = d["archived_snapshots"]["closest"]["url"]

x = response2.json()
print(x)
page2 = x["archived_snapshots"]["closest"]["url"]

a = response3.json()
print(a)
page3 = a["archived_snapshots"]["closest"]["url"]

webbrowser.open(pageurl)
webbrowser.open(page)
webbrowser.open(page2)
webbrowser.open(page3)

from playsound import playsound
path = 'C:/Users/User/Downloads/03 szum-bialy.wav'
playsound(path)








