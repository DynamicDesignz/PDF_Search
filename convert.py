import sys

x = input("Enter your keyword: ")
def search (keyword):
    for x in range (1,len(sys.argv)):
        print sys.argv[x]
        f = open(sys.argv[x], 'r')
        text = f.read().lower()
        if keyword.lower() in text:
            print sys.argv[x]
            print keyword
            
            return keyword
        else:
            return False
search(x)
