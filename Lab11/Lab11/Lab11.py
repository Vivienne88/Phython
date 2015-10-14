import re
'''
pattern = re.compile("o")
result = pattern.search("dog")
print(result)
result = pattern.search("dog",2)
print(result)

result = pattern.match("dog")
print(result)
result = pattern.match("dog",1)
print(result)
'''
#import re
#str = '''sample1 
#sample2
#sample3'''

#^.* 모든문자

#p = re.compile('.*$',re.S)
#result = p.search(str);
#print(result.group())

'''
import re
pattern = re.compile("o[gh]")
result = pattern.match("dog")
print(result)
result = pattern.fullmatch("orge")
print(result)
result = pattern.match("doggie",1,3)
print(result)
'''
'''
import re
pattern = re.compile("\W+")
result = pattern.split('words,words,words')
print(result)
result = pattern.split('words,words,words',
print(result.group)

'''
'''
import re
str = '<a href="index.html">HERE</a><font size="10">'
print(str)
result = re.search(r'href="(.*?)">',str)
print(result.group(1))
'''
import re
str = input("주민번호 입력좀...")
pattern = re.compile("(\d{6})-(\d{7})")
result = pattern.fullmatch(str)
if(result) :
    print(result.group(1))
    print(result.group(2))