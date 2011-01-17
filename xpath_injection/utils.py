import libxml2
    
doc = libxml2.parseFile('credential.xml')
for e in doc.xpathEval("//Account[UserName/text()='MCotillard']"):
    print e 