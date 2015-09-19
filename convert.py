import sys

#x = input("Enter your keyword: ")
keyword = input("Enter your keyword: ")
def search (keyword):
    for x in range (1,len(sys.argv)):
        f = open(sys.argv[x], 'r')
        text = f.read().lower().split()
        appear = False
        counter = 0
        where_appear = []
        for i in range(0, len(text)):
            if text[i] == keyword.lower():

                counter = counter + 1
                where_appear.append(i)
                appear = True
        if appear == True:
            print sys.argv[x]
            print keyword
            print counter
            print where_appear
search(keyword)
