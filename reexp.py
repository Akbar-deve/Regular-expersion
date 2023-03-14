# Regular expresion is a expresion which is used to perform a search operation or pattern matching
# we have a biult-in module called 're' to deal with the regular expresion
#the search() method return a match object

#import re -->it's a module 
import re
#from this input s="" we are searching for pattern
s = "Hey beautifull did anyone told you that your smile is just nextlevel cute"

#search("pattern to search",variable or object from searching the pattern) and return a match object.

se = re.search(input( "enter pattern you want to search-->"),s)

#If se is not equals to none than pattern is found else pattern is not found.
if se!=None:
    print("pattern found")
else:
    print("pattern not found")
