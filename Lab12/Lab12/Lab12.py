import re
'''
str = Window
Unix
Linux
Solaris
p = re.compile('^.+',re.M)
print(p.findall(str))

str = Window
Unix
Linux
Solaris
p = re.compile('^.+',re.S)
result = p.search(str)
print(result)
'''
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.group('first_name','last_name'))
print(m.groups())

m = re.match(r"(\d+)\.?(\d+)?","24")
print(m.groups())
print(m.groups(0))

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict())

#:앞에까지만 하겠다.
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

p = re.compile("(?<=abc)def")
m = p.search("abcdef")
print(m.group())

p = re.search('(?<=-)\w+', 'spam-egg')
print(p.group())

#end 끝나고 다음 index
#start 자기 자신 index
email = "tony@tiremove_thisger.net"
m = re.search("remove_this",email)
result = email[:m.start()] + email[m.end():]
print(result)
print(m.start())
print(m.end())
print(email[m.start()])
print(email[m.end()])

text = """Ross: McFluff: 834.345.1254: 155 Elm Street
Ronald: Heathmore: 892.345.3428 436: Finley Avenue
Frank: Burger: 925.541.7625 662: South Dogwood Way
Heather: Albrecht: 548.326.4584 919: Park Place"""
entries = re.split("\n", text)
result = [re.split(":", entry, 4) for entry in entries]
print(result)
result = [re.split(":?", entry, 4) for entry in entries]
print(result)

import urllib.request

with urllib.request.urlopen('http://www.naver.com') as f:
    m = re.compile(r"<title>+.+</title>")
    print(m.findall(str(f.read())))
    #print(f.read().decode("utf-8"))