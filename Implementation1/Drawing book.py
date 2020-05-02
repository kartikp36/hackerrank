total = int(input())
page = int(input())
pageturnsF = 0
pageturnsB = 0
if page % 2 == 0 :
    pageturnsF = page /2
else :
    pageturnsF = (page-1) /2
if total % 2 == 0 :
    pageturnsB = (total - page) /2
else :
    pageturnsB = (total - page)/2
print(int(min(pageturnsF,pageturnsB)))