from bs4 import BeautifulSoup
'''
f = open("test.xml")
xml = f.read()
soup = BeautifulSoup(xml, "html.parser")
for node in soup.findAll("node"):
    print("Node : "+node.string)
    print("attr1 : "+node["attr1"])
'''

'''
f = open("song.xml", encoding="utf-8")
xml = f.readable()
soup = BeautifulSoup(xml,"html.parser")
for nodes in soup.test("song"):
    for node in nodes:
        print(node.string)
'''
'''
f = open("alcohol.xml",encoding="utf-8")
xml = f.read()
soup = BeautifulSoup(xml,"html.parser")
for nodes in soup.alcohol("cate1"):
    if nodes['tt'] == "안주" :
        print("Cate1 :" + nodes['tt'])
        for node in nodes("cate2"):
             print("\tCate2 :" + node["tt"])
             for item in node("item"):
                 print("\t\t" + item.string)
'''

import json
'''
data = {1:'a',2:'b'}
data2 = json.dumps(data)
data3 = json.loads(data2)
print(type(data2))
print(data2)
print(type(data3))
print(data3)

d = {1:'우리',2:'나라'}
print(d)
d2 = json.dumps(d,ensure_ascii=True)
print(d2)
'''

s = """
{
"name":"cybaek",
"detail" : {"last":"baek"},
"emails" : [ "cybaek@xxx.com", "cybaek@yyy.com" ]
}
"""
class jsonObject:
    def __init__(self,d):
        self.__dict__ = d
data = json.loads(s,object_hook=jsonObject)
print(data.name)
print(data.detail)
print(data.detail.last)
for email in data.emails:
    print(email)
