import re

def isEmail(inp):
    return re.match(r'^[a-zA-Z0-9_]+@([a-zA-Z0-9_]+[\.]+)+[a-zA-Z]{2,4}$',inp)!=None

print isEmail('blah@hello.com')
print isEmail('sd$sd@hello.com')

def getTxts(files):
    return re.findall(r'(\w+\.txt\b)',files)

print getTxts('yo.html blah.txt woah.txt he ')

def isAwesome(inp):
    numWords= re.findall(r'\w+\b',inp)
    awesomeWords=re.findall(r'(awes[o|0]me)',inp)
    fracAwesome=(len(awesomeWords)/float(len(numWords)))*100
    return round(fracAwesome,1)
     
print isAwesome('iamawesomeblah and awes0me is as awesomeo does')
print isAwesome('hello my name is wayawesomedude') 
